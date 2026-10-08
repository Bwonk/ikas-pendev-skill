#!/usr/bin/env python3
"""analyze_site.py - measure design tokens of a reference website (text-only).

Fetches the HTML of one or more pages, their stylesheets (external, @import,
inline <style>, style="" attributes) and, optionally, a bounded number of JS
modules, and parses everything AS TEXT. Nothing fetched is ever executed or
interpreted as instructions; it is untrusted data.

Output: a Turkish markdown report (stdout or --out) whose table rows are all
tagged `[ölçüldü]` with a source, plus an optional --json dump of the same data.

Usage:
  python3 -I analyze_site.py <url> [--paths /,/shop,/about] [--json out.json]
                             [--max-css 25] [--max-js 40] [--timeout 20]
                             [--top 30] [--out report.md]
  python3 -I analyze_site.py --fixture <dir> [<label-url>] ...   (offline)
  python3 -I analyze_site.py file:///abs/path/to/dir-or-page.html ...

Fixture mode reads <dir>/*.html as pages, <dir>/*.css as stylesheets and
<dir>/*.js|*.mjs as script text; it never touches the network.

Stdlib only, Python 3.9+.
"""

import argparse
import colorsys
import hashlib
import ipaddress
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, OrderedDict, defaultdict
from html.parser import HTMLParser

CAP_BYTES = 5 * 1024 * 1024
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
TAG = "[ölçüldü]"

# Representative viewport widths for the four buckets (desktop >=1200,
# laptop 992-1199, tablet 768-991, mobile <768).
BUCKETS = OrderedDict([("desktop", 1440), ("laptop", 1100), ("tablet", 880), ("mobile", 390)])
BUCKET_HDR = {"desktop": "desktop ≥1200", "laptop": "laptop 992–1199",
              "tablet": "tablet 768–991", "mobile": "mobile <768"}

GENERIC_FAMILIES = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui",
                    "ui-sans-serif", "ui-serif", "ui-monospace", "ui-rounded", "emoji", "math",
                    "fangsong", "inherit", "initial", "unset", "revert", "-apple-system",
                    "blinkmacsystemfont", "segoe ui", "roboto", "helvetica neue", "arial",
                    "noto sans", "apple color emoji", "segoe ui emoji", "segoe ui symbol",
                    "noto color emoji", "helvetica", "var"}

# Vendor/library bundles whose easing defaults are noise, and third-party hosts.
JS_SKIP_NAME = re.compile(r"^(react|react-dom|motion|framer|rolldown-runtime|jquery|lenis|gsap|"
                          r"scrolltrigger|polyfills?|vendors?|runtime|webpack-runtime|swiper|"
                          r"lodash|three)([.\-_]|$)", re.I)
JS_SKIP_HOST = re.compile(r"(googletagmanager|google-analytics|doubleclick|facebook|hotjar|"
                          r"clarity\.ms|events\.framer\.com|segment|intercom|hubspot|tiktok|"
                          r"klaviyo|cloudflareinsights|sentry)", re.I)

NAME_ATTRS = ("data-framer-name", "data-name", "data-layer", "data-section", "data-section-type",
              "data-component", "data-block")
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
             "param", "source", "track", "wbr"}
LANDMARK_TAGS = {"header", "nav", "main", "section", "footer", "aside", "article"}

# Framer (and similar builders) express typography via custom properties.
TYPO_ALIASES = {
    "font-size": "size", "--framer-font-size": "size",
    "line-height": "lh", "--framer-line-height": "lh",
    "font-weight": "weight", "--framer-font-weight": "weight",
    "letter-spacing": "ls", "--framer-letter-spacing": "ls",
    "text-transform": "transform", "--framer-text-transform": "transform",
    "font-family": "family", "--framer-font-family": "family",
    "font-variation-settings": "axes", "--framer-font-variation-axes": "axes",
}

NAMED_COLORS = {"white": (255, 255, 255, 1.0), "black": (0, 0, 0, 1.0)}


# --------------------------------------------------------------------------- fetch

class _SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).scheme not in ("http", "https"):
            return None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_SafeRedirect())


def host_is_private(url):
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    if not host or host == "localhost" or host.endswith(".local") or host.endswith(".internal"):
        return True
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False
    return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved


def fetch(url, timeout, warnings, accept="*/*"):
    """Return decoded text or None. Never raises."""
    if urllib.parse.urlsplit(url).scheme not in ("http", "https"):
        warnings.append("şema desteklenmiyor, atlandı: %s" % url)
        return None
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept,
                                               "Accept-Language": "en,tr;q=0.8"})
    try:
        with _OPENER.open(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "") or ""
            if re.match(r"\s*(image|font|video|audio)/", ctype):
                warnings.append("metin değil (%s), atlandı: %s" % (ctype.split(";")[0], url))
                return None
            data = resp.read(CAP_BYTES + 1)
            charset = resp.headers.get_content_charset() or "utf-8"
    except urllib.error.HTTPError as exc:
        warnings.append("indirilemedi (HTTP %s): %s" % (exc.code, url))
        return None
    except (urllib.error.URLError, OSError, ValueError) as exc:
        warnings.append("indirilemedi (%s): %s" % (exc.__class__.__name__, url))
        return None
    if len(data) > CAP_BYTES:
        data = data[:CAP_BYTES]
        warnings.append("5 MB sınırında kesildi: %s" % url)
    try:
        return data.decode(charset, errors="replace")
    except LookupError:
        return data.decode("utf-8", errors="replace")


def read_local(path, warnings):
    try:
        with open(path, "rb") as fh:
            data = fh.read(CAP_BYTES + 1)
    except OSError as exc:
        warnings.append("okunamadı (%s): %s" % (exc.__class__.__name__, os.path.basename(path)))
        return None
    if len(data) > CAP_BYTES:
        data = data[:CAP_BYTES]
        warnings.append("5 MB sınırında kesildi: %s" % os.path.basename(path))
    return data.decode("utf-8", errors="replace")


# --------------------------------------------------------------------------- HTML

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stylesheets = []      # hrefs
        self.js = []               # hrefs (script src + modulepreload)
        self.font_links = []       # Google Fonts css hrefs
        self.styles = []           # inline <style> texts
        self.data_scripts = []     # inline <script> texts (scanned for motion objects only)
        self.style_attrs = []      # (tag, style text)
        self.generator = []
        self.title = ""
        self.canonical = ""
        self.class_counts = Counter()
        self.layers = []           # (name, tag, depth, named_depth, attr, order, region)
        self.landmarks = []        # (tag, label, depth)
        self._stack = []           # (tag, named)
        self._in = None            # "style" | "script" | "title"
        self._buf = []
        self._order = 0
        self._seen_main = False

    def _depth(self):
        return len(self._stack)

    def _region(self, tag):
        """'pre' before <main>, 'main' inside it, 'post' after it."""
        if tag == "main" or any(t == "main" for t, _ in self._stack):
            self._seen_main = True
            return "main"
        return "post" if self._seen_main else "pre"

    def _named_depth(self):
        return sum(1 for _, named in self._stack if named)

    def handle_starttag(self, tag, attrs):
        a = {}
        for k, v in attrs:
            a[k.lower()] = v if v is not None else ""
        tag = tag.lower()
        if tag == "link":
            rel = a.get("rel", "").lower().split()
            href = a.get("href", "")
            if "stylesheet" in rel and href:
                if "fonts.googleapis.com" in href:
                    self.font_links.append(href)
                self.stylesheets.append(href)
            elif "modulepreload" in rel and href:
                self.js.append(href)
            elif "canonical" in rel and href:
                self.canonical = href
        elif tag == "meta" and a.get("name", "").lower() == "generator":
            self.generator.append(a.get("content", ""))
        elif tag == "script" and a.get("src"):
            self.js.append(a["src"])
        cls = a.get("class", "")
        if cls:
            self.class_counts.update(cls.split())
        if a.get("style"):
            self.style_attrs.append((tag, a["style"]))
        named = False
        for attr in NAME_ATTRS:
            if a.get(attr):
                self._order += 1
                self.layers.append((a[attr].strip(), tag, self._depth(), self._named_depth(),
                                    attr, self._order, self._region(tag)))
                named = True
                break
        if tag in LANDMARK_TAGS:
            label = a.get("id") or a.get("aria-label") or a.get("data-framer-name") or \
                (cls.split()[0] if cls else "")
            self.landmarks.append((tag, label, self._depth()))
        if tag in ("style", "script", "title"):
            self._in = tag
            self._buf = []
        if tag not in VOID_TAGS:
            self._stack.append((tag, named))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_TAGS and self._stack:
            self._stack.pop()

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self._in == tag:
            text = "".join(self._buf)
            if tag == "style":
                self.styles.append(text)
            elif tag == "script":
                if text.strip():
                    self.data_scripts.append(text)
            elif tag == "title":
                self.title = text.strip()
            self._in = None
            self._buf = []
        if tag in VOID_TAGS:
            return
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                del self._stack[i:]
                break

    def handle_data(self, data):
        if self._in:
            self._buf.append(data)


# --------------------------------------------------------------------------- CSS

def _scan_until(css, i, stops):
    n = len(css)
    quote = None
    depth = 0
    while i < n:
        ch = css[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0 and ch in stops:
            return i
        i += 1
    return n


def _match_brace(css, i):
    """css[i] == '{' -> index of matching '}' (or len)."""
    n = len(css)
    depth = 0
    quote = None
    while i < n:
        ch = css[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return n


def split_top(text, sep=","):
    parts, depth, quote, cur = [], 0, None, []
    for ch in text:
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
            continue
        cur.append(ch)
    parts.append("".join(cur))
    return [p.strip() for p in parts if p.strip()]


def parse_decls(body):
    # drop nested blocks (CSS nesting) - only top-level declarations are kept
    out = []
    flat = []
    i, n = 0, len(body)
    while i < n:
        j = _scan_until(body, i, "{")
        flat.append(body[i:j])
        if j >= n:
            break
        k = _match_brace(body, j)
        # discard the nested rule's prelude (text after the last ';')
        if flat:
            last = flat[-1]
            cut = last.rfind(";")
            flat[-1] = last[:cut + 1] if cut >= 0 else ""
        i = k + 1
    for part in split_top("".join(flat), ";"):
        if ":" not in part:
            continue
        prop, _, value = part.partition(":")
        prop = prop.strip().lower()
        value = value.strip()
        if not prop or not value:
            continue
        value = re.sub(r"\s*!important\s*$", "", value, flags=re.I)
        out.append((prop, value))
    return out


class CSSData:
    def __init__(self):
        self.decls = []        # dict(src, sel, cond, prop, value, order)
        self.fontfaces = []    # dict(src, decls)
        self.keyframes = []    # (name, steps, src)
        self.media = []        # (cond, src)
        self.imports = []      # (href, src)
        self._order = 0

    def add_rule(self, sel, cond, decls, src):
        for prop, value in decls:
            self._order += 1
            self.decls.append({"src": src, "sel": sel, "cond": cond, "prop": prop,
                               "value": value, "order": self._order})


def parse_css(css, data, src, cond=(), depth=0):
    if depth == 0:
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    if depth > 20:
        return
    i, n = 0, len(css)
    while i < n:
        j = _scan_until(css, i, "{;}")
        if j >= n:
            break
        prelude = css[i:j].strip()
        ch = css[j]
        if ch == "}":
            i = j + 1
            continue
        if ch == ";":
            if prelude.lower().startswith("@import"):
                m = re.search(r"url\(\s*['\"]?([^'\")]+)|['\"]([^'\"]+)['\"]", prelude)
                if m:
                    data.imports.append((m.group(1) or m.group(2), src))
            i = j + 1
            continue
        end = _match_brace(css, j)
        body = css[j + 1:end]
        i = end + 1
        low = prelude.lower()
        if low.startswith("@media"):
            mc = prelude[6:].strip()
            data.media.append((mc, src))
            parse_css(body, data, src, cond + (mc,), depth + 1)
        elif low.startswith(("@supports", "@layer", "@container", "@document", "@scope",
                             "@-moz-document", "@starting-style")):
            parse_css(body, data, src, cond, depth + 1)
        elif low.startswith("@font-face"):
            data.fontfaces.append({"src": src, "decls": dict(parse_decls(body))})
        elif re.match(r"@(-\w+-)?keyframes\b", low):
            name = re.sub(r"^@(-\w+-)?keyframes\s*", "", prelude, flags=re.I).strip().strip("\"'")
            steps = len(re.findall(r"[^{}]+\{", body))
            data.keyframes.append((name, steps, src))
        elif low.startswith("@"):
            continue
        elif prelude:
            data.add_rule(prelude, cond, parse_decls(body), src)


# --------------------------------------------------------------------------- media

def _px(num, unit):
    v = float(num)
    unit = (unit or "px").lower()
    return v * 16 if unit in ("em", "rem") else v


def media_widths(cond):
    """List of (kind, value_px) found in a media condition."""
    out = []
    for m in re.finditer(r"\(\s*(min|max)-width\s*:\s*([\d.]+)\s*(px|em|rem)?\s*\)", cond, re.I):
        out.append((m.group(1).lower(), _px(m.group(2), m.group(3))))
    for m in re.finditer(r"\(\s*width\s*(>=|<=|>|<)\s*([\d.]+)\s*(px|em|rem)?\s*\)", cond, re.I):
        op, v = m.group(1), _px(m.group(2), m.group(3))
        out.append(("min" if ">" in op else "max", v + (0.02 if op == ">" else 0) - (0.02 if op == "<" else 0)))
    return out


def _cond_part_matches(part, width):
    p = part.lower()
    if re.search(r"\bprint\b", p) and not re.search(r"\b(screen|all)\b", p):
        return False
    if re.match(r"\s*not\b", p):
        return False
    if re.search(r"prefers-reduced-motion\s*:\s*reduce", p):
        return False
    if re.search(r"prefers-color-scheme\s*:\s*dark", p):
        return False
    if re.search(r"forced-colors\s*:\s*active|prefers-contrast", p):
        return False
    for kind, v in media_widths(part):
        if kind == "min" and width < v:
            return False
        if kind == "max" and width > v:
            return False
    return True


def cond_matches(cond, width):
    for c in cond:
        if not any(_cond_part_matches(p, width) for p in (split_top(c, ",") or [c])):
            return False
    return True


def cond_buckets(cond):
    if not cond:
        return ["base"]
    hit = [b for b, w in BUCKETS.items() if cond_matches(cond, w)]
    if len(hit) == len(BUCKETS):
        return ["base"]
    return hit


# --------------------------------------------------------------------------- values

def fmt_num(x, lead_zero=True):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    s = ("%.3f" % x).rstrip("0").rstrip(".")
    if not lead_zero:
        if s.startswith("0."):
            s = s[1:]
        elif s.startswith("-0."):
            s = "-" + s[2:]
    return s


def fmt_bezier(nums):
    return "cubic-bezier(%s)" % ", ".join(fmt_num(v, lead_zero=False) for v in nums)


def _hex(r, g, b, a=1.0):
    r, g, b = [max(0, min(255, int(round(c)))) for c in (r, g, b)]
    s = "#%02X%02X%02X" % (r, g, b)
    if a < 0.999:
        s += "%02X" % max(0, min(255, int(round(a * 255))))
    return s


def _num_or_pct(tok, scale):
    tok = tok.strip()
    if tok.endswith("%"):
        return float(tok[:-1]) / 100.0 * scale
    return float(tok)


COLOR_RE = re.compile(
    r"(?<![\w\-#(])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![\w\-])"
    r"|\b(rgba?|hsla?)\(\s*([^()]*?)\s*\)"
    r"|(?<![\w\-])(white|black)(?![\w\-])", re.I)


def find_colors(value, allow_named=False):
    out = []
    for m in COLOR_RE.finditer(value):
        if m.group(1):
            h = m.group(1)
            if len(h) in (3, 4):
                h = "".join(c * 2 for c in h)
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            a = int(h[6:8], 16) / 255.0 if len(h) == 8 else 1.0
            out.append(_hex(r, g, b, a))
        elif m.group(2):
            fn = m.group(2).lower()
            args = m.group(3)
            if "var(" in args or "calc(" in args or "from " in args:
                continue
            toks = [t for t in re.split(r"[\s,/]+", args) if t]
            if len(toks) < 3:
                continue
            try:
                if fn.startswith("rgb"):
                    r, g, b = (_num_or_pct(t, 255) for t in toks[:3])
                else:
                    hue = float(re.sub(r"deg$", "", toks[0])) / 360.0
                    s_ = _num_or_pct(toks[1], 1) if toks[1].endswith("%") else float(toks[1]) / 100
                    l_ = _num_or_pct(toks[2], 1) if toks[2].endswith("%") else float(toks[2]) / 100
                    rr, gg, bb = colorsys.hls_to_rgb(hue % 1.0, l_, s_)
                    r, g, b = rr * 255, gg * 255, bb * 255
                a = _num_or_pct(toks[3], 1) if len(toks) > 3 else 1.0
            except ValueError:
                continue
            out.append(_hex(r, g, b, a))
        elif m.group(4) and allow_named:
            r, g, b, a = NAMED_COLORS[m.group(4).lower()]
            out.append(_hex(r, g, b, a))
    return out


def color_category(prop):
    if prop in ("color", "-webkit-text-fill-color", "caret-color", "text-decoration-color",
                "--framer-text-color", "--framer-link-text-color", "--framer-link-hover-text-color",
                "--framer-link-current-text-color", "--framer-text-decoration-color"):
        return "metin"
    if "background" in prop:
        return "zemin"
    if "border" in prop or prop.startswith("outline") or "column-rule" in prop or "divider" in prop:
        return "çizgi"
    if "shadow" in prop or prop == "filter":
        return "gölge"
    if prop in ("fill", "stroke", "stop-color"):
        return "svg"
    if prop.startswith("--"):
        return "değişken"
    return "diğer"


TIME_RE = re.compile(r"(?<![\w.\-])(-?[\d.]+)(ms|s)(?![\w\-])", re.I)


def to_ms(num, unit):
    v = float(num)
    return int(round(v if unit.lower() == "ms" else v * 1000))


EASE_KEYWORDS = ("ease-in-out", "ease-in", "ease-out", "ease", "linear", "step-start", "step-end")


def parse_bezier_args(txt):
    try:
        nums = [float(x) for x in re.split(r"[\s,]+", txt.strip()) if x]
    except ValueError:
        return None
    return nums if len(nums) == 4 else None


FONT_SHORT_RE = re.compile(
    r"^\s*((?:(?:italic|oblique|normal|small-caps|bold|bolder|lighter|[1-9]00|ultra-condensed|"
    r"condensed|semi-condensed|expanded)\s+)*)"
    r"([\d.]+(?:px|r?em|%)|(?:x{1,2}-)?small|medium|(?:x{1,2}-)?large)"
    r"(?:\s*/\s*([^\s]+))?\s+(.+)$", re.I)


def typo_items(prop, value):
    """(attr, value) pairs for a declaration; expands the `font` shorthand."""
    attr = TYPO_ALIASES.get(prop)
    if attr:
        return [(attr, value)]
    if prop != "font":
        return []
    m = FONT_SHORT_RE.match(value)
    if not m:
        return []
    out = [("size", m.group(2)), ("family", m.group(4))]
    if m.group(3):
        out.append(("lh", m.group(3)))
    w = re.search(r"\b([1-9]00|bold)\b", m.group(1) or "", re.I)
    if w:
        out.append(("weight", "700" if w.group(1).lower() == "bold" else w.group(1)))
    return out


def first_family(value):
    for fam in split_top(value, ","):
        f = fam.strip().strip("\"'").strip()
        if not f or f.lower() in GENERIC_FAMILIES or f.lower().startswith("var("):
            continue
        if f.endswith(" Placeholder"):
            continue
        return f
    return None


def short(text, n=70):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[:n - 1] + "…"


def px_tokens(value):
    return [float(m.group(1)) for m in re.finditer(r"(?<![\w.\-])(-?[\d.]+)px\b", value)]


# --------------------------------------------------------------------------- JS motion

OBJ_RE = re.compile(r"\{[^{}]{0,600}\}")
KV_RE = re.compile(r"[\"']?([A-Za-z_]\w*)[\"']?\s*:\s*(\[[^\]]*\]|`[^`]*`|\"[^\"]*\"|'[^']*'|[^,}]+)")


def scan_motion_text(text, src, motion):
    for m in OBJ_RE.finditer(text):
        body = m.group(0)
        if not re.search(r"\b(ease|stiffness|bounce|type)[\"']?\s*:", body):
            continue
        kv = {}
        for k, v in KV_RE.findall(body[1:-1]):
            kv[k] = v.strip().strip("`\"'")
        is_spring = kv.get("type") == "spring"
        ease = kv.get("ease", "")
        bez = None
        if ease.startswith("["):
            bez = parse_bezier_args(ease.strip("[]"))
        if not (is_spring or bez):
            continue
        motion["objects"].append({"src": src, "text": body})
        try:
            if bez and kv.get("type", "tween") != "spring":
                motion["bezier"][fmt_bezier(bez)]["js"] += 1
                motion["bezier_src"].setdefault(fmt_bezier(bez), src)
                if "duration" in kv:
                    motion["dur"][to_ms(kv["duration"], "s")]["js"] += 1
                    motion["dur_src"].setdefault(to_ms(kv["duration"], "s"), src)
            if is_spring:
                if "bounce" in kv or kv.get("durationBasedSpring") in ("!0", "true"):
                    sig = "spring bounce %s, %ss" % (fmt_num(float(kv.get("bounce", "0") or 0)),
                                                    fmt_num(float(kv.get("duration", "0") or 0)))
                else:
                    sig = "spring stiffness %s, damping %s, mass %s" % (
                        fmt_num(float(kv.get("stiffness", "100"))),
                        fmt_num(float(kv.get("damping", "10"))),
                        fmt_num(float(kv.get("mass", "1"))))
                motion["spring"][sig] += 1
                motion["spring_src"].setdefault(sig, src)
        except ValueError:
            continue


# --------------------------------------------------------------------------- analysis

def analyze(pages, css, js_texts, top):
    """pages: list of dict(label, parser). css: CSSData. js_texts: list of (src, text)."""
    res = OrderedDict()

    class_counts = Counter()
    for p in pages:
        class_counts.update(p["parser"].class_counts)

    # inline style attributes are treated as rules with selector "[style]"
    for p in pages:
        for tag, style in p["parser"].style_attrs:
            css.add_rule("%s[style]" % tag, (), parse_decls(style), "%s [style]" % p["label"])

    decls = css.decls

    # ---- root custom properties per bucket (for var() resolution) and rem base
    vmaps = OrderedDict((b, {}) for b in BUCKETS)
    vbase = {}
    ROOT["px"] = 16.0
    for d in decls:
        sels = [x.strip() for x in split_top(d["sel"], ",")]
        if not any(x in (":root", "html", "body", ":host") for x in sels):
            continue
        if d["prop"].startswith("--"):
            for b, wpx in BUCKETS.items():
                if cond_matches(d["cond"], wpx):
                    vmaps[b][d["prop"]] = d["value"]
            if not d["cond"]:
                vbase[d["prop"]] = d["value"]
    for d in decls:
        if d["prop"] == "font-size" and not d["cond"] and \
                any(x.strip() in (":root", "html") for x in split_top(d["sel"], ",")):
            v, _fb = resolve_vars(d["value"], vbase)
            v = v.strip()
            m = re.fullmatch(r"([\d.]+)(px|%)", v)
            if m:
                ROOT["px"] = float(m.group(1)) * (0.16 if m.group(2) == "%" else 1)
            elif v.lower().startswith("calc("):
                x = eval_calc(v[5:-1], pct_px=0.16)
                if x:
                    ROOT["px"] = x
    res["rem_px"] = ROOT["px"]

    # ---- fonts
    fam_count, fam_src = Counter(), {}
    for d in decls:
        prop = d["prop"]
        val = None
        if prop in ("font-family", "--framer-font-family"):
            val = d["value"]
        elif prop == "font":
            val = dict(typo_items(prop, d["value"])).get("family")
        if val:
            f = first_family(val)
            if f:
                fam_count[f] += 1
                fam_src.setdefault(f, "%s `%s`" % (d["src"], short(d["sel"], 50)))
    faces = OrderedDict()
    for ff in css.fontfaces:
        dd = ff["decls"]
        fam = (dd.get("font-family", "") or "").strip().strip("\"'")
        if not fam:
            continue
        e = faces.setdefault(fam, {"weights": set(), "styles": set(), "formats": set(),
                                   "subsets": 0, "hosts": set(), "src": ff["src"]})
        e["weights"].add(dd.get("font-weight", "400").strip())
        e["styles"].add(dd.get("font-style", "normal").strip())
        e["subsets"] += 1
        srcv = dd.get("src", "")
        for fm in re.findall(r"format\(\s*['\"]?([\w-]+)", srcv):
            e["formats"].add(fm)
        for u in re.findall(r"url\(\s*['\"]?(https?://[^/'\")]+)", srcv):
            e["hosts"].add(urllib.parse.urlsplit(u).hostname or "")
        if not re.findall(r"format\(", srcv):
            for ext in re.findall(r"\.(woff2|woff|ttf|otf)\b", srcv):
                e["formats"].add(ext)
    gfonts = []
    for p in pages:
        for href in p["parser"].font_links:
            gfonts.append((href, p["label"]))
    for href, src in css.imports:
        if "fonts.googleapis.com" in href:
            gfonts.append((href, src))
    gf_rows = []
    for href, src in gfonts:
        q = urllib.parse.parse_qs(urllib.parse.urlsplit(href).query)
        for fam in q.get("family", []):
            for one in fam.split("|"):
                name, _, spec = one.partition(":")
                gf_rows.append({"family": name.replace("+", " "), "spec": spec, "src": src})
    res["fonts"] = {
        "usage": [{"family": f, "count": c, "src": fam_src[f]}
                  for f, c in sorted(fam_count.items(), key=lambda x: (-x[1], x[0]))],
        "fontfaces": [{"family": f, "weights": sorted(e["weights"], key=_weight_key),
                       "styles": sorted(e["styles"]), "formats": sorted(e["formats"]),
                       "subsets": e["subsets"], "hosts": sorted(h for h in e["hosts"] if h),
                       "src": e["src"]} for f, e in faces.items()],
        "google_fonts": gf_rows,
    }

    # ---- colours + colour tokens
    col_total, col_cat, col_src = Counter(), defaultdict(Counter), {}
    token_val, token_src = {}, {}
    for d in decls:
        prop, val = d["prop"], d["value"]
        if prop.startswith("--") and prop not in TYPO_ALIASES:
            cols = find_colors(val, allow_named=True)
            if len(cols) == 1 and re.fullmatch(r"\s*(#[0-9a-fA-F]{3,8}|(rgba?|hsla?)\([^()]*\)|white|black)\s*", val, re.I):
                token_val.setdefault(prop, cols[0])
                token_src.setdefault(prop, "%s `%s`" % (d["src"], short(d["sel"], 40)))
        allow_named = prop in ("color", "background", "background-color", "border", "border-color",
                               "fill", "stroke", "outline", "outline-color") or "color" in prop
        cat = color_category(prop)
        for c in find_colors(val, allow_named=allow_named):
            col_total[c] += 1
            col_cat[c][cat] += 1
            col_src.setdefault(c, "%s `%s` (%s)" % (d["src"], short(d["sel"], 40), prop))
    var_refs = Counter()
    all_vals = "\n".join(d["value"] for d in decls)
    for m in re.finditer(r"var\(\s*(--[\w-]+)", all_vals):
        var_refs[m.group(1)] += 1
    res["colors"] = [{"hex": c, "count": n, "where": dict(col_cat[c]), "src": col_src[c]}
                     for c, n in sorted(col_total.items(), key=lambda x: (-x[1], x[0]))]
    res["color_tokens"] = [{"name": t, "value": v, "refs": var_refs.get(t, 0), "src": token_src[t]}
                           for t, v in sorted(token_val.items(),
                                              key=lambda x: (-var_refs.get(x[0], 0), x[0]))]

    # ---- typography presets (cascade per bucket, document order wins)
    groups = OrderedDict()
    for d in decls:
        items = typo_items(d["prop"], d["value"])
        if not items:
            continue
        for sel in split_top(d["sel"], ","):
            key = selector_key(sel)
            if not key:
                continue
            for key_attr, value in items:
                groups.setdefault(key, []).append((d["cond"], key_attr, value, d["src"], d["order"]))
    presets = []
    for key, recs in groups.items():
        recs.sort(key=lambda r: r[4])
        per = OrderedDict()
        for b, w in BUCKETS.items():
            vals = {}
            for cond, attr, value, _src, _o in recs:
                if cond_matches(cond, w):
                    vals[attr] = value
            per[b] = vals
        sizes = OrderedDict()
        for b in BUCKETS:
            raw = per[b].get("size")
            if raw and "var(" in raw:
                rv, fb = resolve_vars(raw, vmaps[b])
                raw = raw if fb else rv
            sizes[b] = norm_size(raw)
        for b in BUCKETS:
            for attr in ("lh", "weight", "ls", "family", "transform"):
                raw = per[b].get(attr)
                if raw and "var(" in raw:
                    rv, fb = resolve_vars(raw, vmaps[b])
                    if not fb:
                        per[b][attr] = rv
        if not any(_size_sort(v) > 0 for v in sizes.values()):
            continue
        dv = per["desktop"] if per["desktop"] else per["mobile"]
        cls = key[1:] if key.startswith(".") else None
        presets.append({
            "selector": key,
            "sizes": sizes,
            "weight": norm_weight(dv.get("weight"), dv.get("axes")),
            "line_height": norm_lh(dv.get("lh")),
            "letter_spacing": norm_ls(dv.get("ls")),
            "transform": (dv.get("transform") or "").strip(),
            "family": first_family(dv.get("family") or "") or "",
            "usage": class_counts.get(cls, 0) if cls else 0,
            "src": recs[0][3],
        })
    presets.sort(key=lambda p: (-_size_sort(p["sizes"]["desktop"]), -p["usage"], p["selector"]))
    merged, seen = [], {}
    for p in presets:
        sig = (tuple(p["sizes"].values()), p["weight"], p["line_height"], p["letter_spacing"],
               p["transform"], p["family"])
        if sig in seen:
            seen[sig]["also"].append(p["selector"])
            seen[sig]["usage"] += p["usage"]
            continue
        p["also"] = []
        seen[sig] = p
        merged.append(p)
    res["presets"] = merged

    size_freq = defaultdict(Counter)
    size_src = {}
    for d in decls:
        sz = dict(typo_items(d["prop"], d["value"])).get("size")
        if not sz:
            continue
        if "var(" in sz:
            rv, fb = resolve_vars(sz, vbase)
            sz = sz if fb else rv
        s = norm_size(sz)
        if not s:
            continue
        for b in cond_buckets(d["cond"]):
            size_freq[s][b] += 1
        size_src.setdefault(s, "%s `%s`" % (d["src"], short(d["sel"], 40)))
    res["font_sizes"] = [{"size": s, "buckets": dict(c), "total": sum(c.values()), "src": size_src[s]}
                         for s, c in sorted(size_freq.items(), key=lambda x: (-_size_sort(x[0]), x[0]))]

    # ---- breakpoints
    bp = defaultdict(lambda: {"raw": Counter(), "count": 0, "src": ""})
    for cond, src in css.media:
        for kind, v in media_widths(cond):
            if v <= 0:
                continue
            if kind == "min":
                boundary = int(round(v))
            else:
                boundary = int(math.ceil(v)) if abs(v - round(v)) > 1e-9 else int(round(v)) + 1
            e = bp[boundary]
            e["raw"]["%s-width:%s" % (kind, fmt_num(v))] += 1
            e["count"] += 1
            e["src"] = e["src"] or "%s @media %s" % (src, short(cond, 50))
    res["breakpoints"] = [{"boundary": b, "count": e["count"],
                           "raw": dict(e["raw"].most_common()), "band": _band(b), "src": e["src"]}
                          for b, e in sorted(bp.items(), key=lambda x: -x[0])]

    # ---- motion
    motion = {"bezier": defaultdict(Counter), "bezier_src": {}, "keyword": Counter(),
              "dur": defaultdict(Counter), "dur_src": {}, "delay": Counter(),
              "spring": Counter(), "spring_src": {}, "props": Counter(),
              "anim_names": Counter(), "objects": []}
    for d in decls:
        prop, val = d["prop"], d["value"]
        kind = None
        if prop.startswith("transition") or prop.startswith("-webkit-transition"):
            kind = "css_transition"
        elif prop.startswith("animation") or prop.startswith("-webkit-animation"):
            kind = "css_animation"
        if not kind:
            continue
        src = "%s `%s`" % (d["src"], short(d["sel"], 40))
        for m in re.finditer(r"cubic-bezier\(([^)]*)\)", val):
            nums = parse_bezier_args(m.group(1))
            if nums:
                motion["bezier"][fmt_bezier(nums)][kind] += 1
                motion["bezier_src"].setdefault(fmt_bezier(nums), src)
        stripped = re.sub(r"cubic-bezier\([^)]*\)|steps\([^)]*\)", " ", val)
        for kw in re.findall(r"(?<![\w-])(ease-in-out|ease-in|ease-out|ease|linear|step-start|step-end)(?![\w-])", stripped):
            motion["keyword"][kw] += 1
        if prop.endswith(("-delay",)):
            for m in TIME_RE.finditer(stripped):
                motion["delay"][to_ms(m.group(1), m.group(2))] += 1
            continue
        if prop.endswith(("-property",)):
            for p_ in split_top(val, ","):
                motion["props"][p_] += 1
            continue
        if prop.endswith("-name"):
            for p_ in split_top(val, ","):
                if p_ != "none":
                    motion["anim_names"][p_] += 1
            continue
        parts = split_top(stripped, ",") if prop in ("transition", "animation", "-webkit-transition",
                                                     "-webkit-animation") else [stripped]
        for part in parts:
            times = [to_ms(m.group(1), m.group(2)) for m in TIME_RE.finditer(part)]
            if prop.endswith("-duration"):
                for t in times:
                    motion["dur"][t][kind] += 1
                    motion["dur_src"].setdefault(t, src)
                continue
            if times:
                motion["dur"][times[0]][kind] += 1
                motion["dur_src"].setdefault(times[0], src)
                if len(times) > 1:
                    motion["delay"][times[1]] += 1
            words = [w for w in re.split(r"\s+", TIME_RE.sub(" ", part)) if w]
            if prop in ("transition", "-webkit-transition") and words:
                if words[0] not in EASE_KEYWORDS:
                    motion["props"][words[0]] += 1
            if prop in ("animation", "-webkit-animation"):
                for w in words:
                    if w not in EASE_KEYWORDS and not re.match(r"^(infinite|alternate|reverse|normal|forwards|backwards|both|none|running|paused|alternate-reverse|[\d.]+)$", w):
                        motion["anim_names"][w] += 1
                        break
    for src, text in js_texts:
        scan_motion_text(text, src, motion)
    res["motion"] = {
        "beziers": [{"curve": c, "css_transition": n.get("css_transition", 0),
                     "css_animation": n.get("css_animation", 0), "js": n.get("js", 0),
                     "total": sum(n.values()), "src": motion["bezier_src"][c]}
                    for c, n in sorted(motion["bezier"].items(), key=lambda x: (-sum(x[1].values()), x[0]))],
        "keywords": dict(motion["keyword"].most_common()),
        "durations": [{"ms": t, "css_transition": n.get("css_transition", 0),
                       "css_animation": n.get("css_animation", 0), "js": n.get("js", 0),
                       "total": sum(n.values()), "src": motion["dur_src"][t]}
                      for t, n in sorted(motion["dur"].items(), key=lambda x: (-sum(x[1].values()), x[0]))],
        "delays": dict(sorted(motion["delay"].items(), key=lambda x: (-x[1], x[0]))),
        "springs": [{"signature": s, "count": n, "src": motion["spring_src"][s]}
                    for s, n in sorted(motion["spring"].items(), key=lambda x: (-x[1], x[0]))],
        "properties": dict(motion["props"].most_common()),
        "objects": motion["objects"],
    }
    kf = OrderedDict()
    for name, steps, src in css.keyframes:
        e = kf.setdefault(name, {"name": name, "defs": 0, "steps": steps, "src": src})
        e["defs"] += 1
    res["keyframes"] = [dict(e, used=motion["anim_names"].get(n, 0)) for n, e in kf.items()]

    # ---- borders + radius
    bw, bw_style, bw_src = Counter(), defaultdict(Counter), {}
    rad, rad_src = Counter(), {}
    for d in decls:
        prop, val = d["prop"], d["value"]
        src = "%s `%s`" % (d["src"], short(d["sel"], 40))
        if re.fullmatch(r"(border|border-(top|right|bottom|left|block|inline)(-(start|end))?|outline)", prop):
            if val.strip().lower() in ("none", "0", "unset", "initial", "inherit"):
                continue
            ws = px_tokens(val)
            style = re.search(r"\b(solid|dashed|dotted|double)\b", val)
            if ws:
                w = fmt_num(ws[0]) + "px"
                bw[w] += 1
                bw_style[w][style.group(1) if style else "?"] += 1
                bw_src.setdefault(w, src)
        elif re.fullmatch(r"(border(-(top|right|bottom|left))?-width|--border-(top|right|bottom|left)-width|outline-width)", prop):
            for v in px_tokens(val):
                if v > 0:
                    w = fmt_num(v) + "px"
                    bw[w] += 1
                    bw_style[w]["(width)"] += 1
                    bw_src.setdefault(w, src)
        elif re.fullmatch(r"border(-(top|bottom)-(left|right))?-radius|--border-radius|--framer-border-radius", prop):
            v = re.sub(r"\s+", " ", val.strip())
            if "var(" in v or not re.search(r"\d", v):
                continue
            rad[v] += 1
            rad_src.setdefault(v, src)
    res["borders"] = [{"width": w, "count": n, "styles": dict(bw_style[w]), "src": bw_src[w]}
                      for w, n in sorted(bw.items(), key=lambda x: (-x[1], x[0]))]
    res["radius"] = [{"value": v, "count": n, "src": rad_src[v]}
                     for v, n in sorted(rad.items(), key=lambda x: (-x[1], x[0]))]

    # ---- spacing
    sp, sp_src = defaultdict(Counter), {}
    for d in decls:
        prop = d["prop"]
        grp = None
        if prop in ("gap", "row-gap", "column-gap", "grid-gap"):
            grp = "gap"
        elif prop == "padding" or prop.startswith("padding-"):
            grp = "padding"
        if not grp:
            continue
        for v in px_tokens(d["value"]):
            if v <= 0:
                continue
            k = fmt_num(v)
            sp[k][grp] += 1
            sp_src.setdefault(k, "%s `%s` (%s)" % (d["src"], short(d["sel"], 40), prop))
    res["spacing"] = [{"px": k, "gap": c.get("gap", 0), "padding": c.get("padding", 0),
                       "total": sum(c.values()), "src": sp_src[k]}
                      for k, c in sorted(sp.items(), key=lambda x: (-sum(x[1].values()), float(x[0])))]

    # ---- layers
    freq, first, depth_min, tags, attr_of, lsrc = Counter(), {}, {}, defaultdict(Counter), {}, {}
    shallow = []
    for p in pages:
        for name, tag, depth, nd, attr, order, _region in p["parser"].layers:
            if not name:
                continue
            freq[name] += 1
            first.setdefault(name, (p["label"], order))
            depth_min[name] = min(depth_min.get(name, 10 ** 6), nd)
            tags[name][tag] += 1
            attr_of.setdefault(name, attr)
            lsrc.setdefault(name, "%s [%s]" % (p["label"], attr))
    for p in pages:
        lay = [x for x in p["parser"].layers if x[0]]
        if not lay:
            continue
        # section hints: shallowest named layers before <main>, inside it (excluding the
        # <main> element itself) and after it, in document order
        groups_ = OrderedDict((r, [x for x in lay if x[6] == r and x[1] != "main"])
                              for r in ("pre", "main", "post"))
        for region, items in groups_.items():
            if not items:
                continue
            target = min(x[3] for x in items)
            prev = None
            for name, tag, depth, nd, attr, order, _r in items:
                if nd == target and name != prev:
                    shallow.append({"page": p["label"], "region": region, "name": name,
                                    "tag": tag, "depth": depth})
                    prev = name
    bem = Counter()
    for cls, n in class_counts.items():
        block = cls.split("__")[0]
        if "__" in cls and re.match(r"^[a-z][a-z0-9-]*$", block) and not block.startswith(("framer", "hidden")):
            bem[block] += n
    landmarks = OrderedDict()
    for p in pages:
        for tag, label, depth in p["parser"].landmarks:
            k = (p["label"], tag, label.strip())
            e = landmarks.setdefault(k, {"page": p["label"], "tag": tag, "label": label.strip(),
                                         "depth": depth, "count": 0})
            e["count"] += 1
            e["depth"] = min(e["depth"], depth)
    landmarks = list(landmarks.values())
    res["layers"] = {
        "sections": shallow,
        "frequency": [{"name": n, "count": c, "min_named_depth": depth_min[n],
                       "tags": dict(tags[n]), "src": lsrc[n]}
                      for n, c in sorted(freq.items(), key=lambda x: (-x[1], x[0]))],
        "bem_blocks": dict(sorted(bem.items(), key=lambda x: (-x[1], x[0]))),
        "landmarks": landmarks,
    }
    return res


def _weight_key(w):
    m = re.match(r"\d+", w)
    return (int(m.group(0)) if m else 0, w)


def selector_key(sel):
    sel = sel.strip()
    if not sel or sel.startswith("@"):
        return None
    m = re.search(r"(\.framer-styles-preset-[\w-]+)", sel)
    if m:
        return m.group(1)
    sel = re.sub(r":not\([^()]*\)", "", sel)
    parts = re.split(r"\s*[>+~]\s*|\s+", sel.strip())
    last = parts[-1] if parts else sel
    return last or None


ROOT = {"px": 16.0}   # rem base, set per analysis from html/:root font-size


def norm_size(v):
    if not v:
        return ""
    v = v.strip()
    m = re.fullmatch(r"([\d.]+)(px|rem|em)", v)
    if m:
        x = float(m.group(1))
        return fmt_num(x * ROOT["px"] if m.group(2) == "rem" else x * 16 if m.group(2) == "em" else x)
    if v.lower().startswith("calc("):
        x = eval_calc(v[5:-1] if v.endswith(")") else v[5:])
        if x is not None:
            return fmt_num(round(x, 3))
    return short(v, 40)


VAR_RE = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*))?\)")


def resolve_vars(value, vmap):
    """Substitute var() from vmap. Returns (value, used_fallback)."""
    used_fb = [False]

    def sub(m):
        v = vmap.get(m.group(1))
        if v is None:
            if m.group(2) is None:
                return m.group(0)
            used_fb[0] = True
            return m.group(2).strip()
        return v.strip()

    for _ in range(8):
        if "var(" not in value:
            break
        new = VAR_RE.sub(sub, value)
        if new == value:
            break
        value = new
    return value, used_fb[0]


_CALC_TOK = re.compile(r"\s*(?:(\d*\.?\d+)(px|rem|em|%)?|([()*/+-]))")


def eval_calc(expr, pct_px=None):
    """Evaluate a simple calc() body to px (lengths) or a scalar. None if unsupported."""
    r = _eval_calc(expr, pct_px)
    return None if r is None else r[0]


def _eval_calc(expr, pct_px=None):
    expr = re.sub(r"\bcalc\(", "(", expr.strip())
    for _ in range(8):
        m = re.search(r"\b(min|max|clamp)\(([^()]*)\)", expr)
        if not m:
            break
        vals = [_eval_calc(a, pct_px) for a in m.group(2).split(",")]
        if not vals or any(v is None for v in vals):
            return None
        nums = [v for v, _ln in vals]
        fn = m.group(1)
        if fn == "clamp":
            if len(nums) != 3:
                return None
            r = max(nums[0], min(nums[1], nums[2]))
        else:
            r = min(nums) if fn == "min" else max(nums)
        unit = "px" if any(ln for _v, ln in vals) else ""
        expr = expr[:m.start()] + "(" + repr(float(r)) + unit + ")" + expr[m.end():]
    toks, i = [], 0
    while i < len(expr):
        m = _CALC_TOK.match(expr, i)
        if not m or m.end() == i:
            return None
        i = m.end()
        if m.group(1) is not None:
            unit = m.group(2)
            v = float(m.group(1))
            if unit == "%":
                if pct_px is None:
                    return None
                toks.append((v * pct_px, True))
            elif unit:
                toks.append((v * (ROOT["px"] if unit == "rem" else 16 if unit == "em" else 1), True))
            else:
                toks.append((v, False))
        else:
            toks.append(m.group(3))
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def atom():
        t = peek()
        pos[0] += 1
        if t == "(":
            r = expr_()
            if peek() != ")":
                raise ValueError
            pos[0] += 1
            return r
        if t == "-":
            v, ln = atom()
            return (-v, ln)
        if isinstance(t, tuple):
            return t
        raise ValueError

    def term():
        v, ln = atom()
        while peek() in ("*", "/"):
            op = toks[pos[0]]
            pos[0] += 1
            w, ln2 = atom()
            if op == "*":
                if ln and ln2:
                    raise ValueError
                v, ln = v * w, ln or ln2
            else:
                if ln2 or w == 0:
                    raise ValueError
                v = v / w
        return v, ln

    def expr_():
        v, ln = term()
        while peek() in ("+", "-"):
            op = toks[pos[0]]
            pos[0] += 1
            w, ln2 = term()
            if ln != ln2:
                raise ValueError
            v = v + w if op == "+" else v - w
        return v, ln

    try:
        v, ln = expr_()
        if pos[0] != len(toks):
            return None
    except (ValueError, IndexError, TypeError, RecursionError):
        return None
    return v, ln


def _size_sort(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return -1.0


def norm_weight(w, axes):
    if axes:
        m = re.search(r"[\"']wght[\"']\s+([\d.]+)", axes)
        if m:
            wd = re.search(r"[\"']wdth[\"']\s+([\d.]+)", axes)
            return fmt_num(float(m.group(1))) + (" (wdth %s)" % fmt_num(float(wd.group(1))) if wd else "")
    return (w or "").strip()


def norm_lh(v):
    if not v:
        return ""
    v = v.strip()
    m = re.fullmatch(r"([\d.]+)(em|%)?", v)
    if m:
        x = float(m.group(1))
        if m.group(2) == "%":
            x /= 100.0
        return fmt_num(x)
    if v.lower().startswith("calc("):
        x = eval_calc(v[5:-1])
        if x is not None:
            return fmt_num(round(x, 3)) + ("px" if re.search(r"\d(px|r?em)\b", v) else "")
    return v


def norm_ls(v):
    if not v:
        return ""
    v = v.strip()
    m = re.fullmatch(r"(-?)([\d.]+)(px|em|rem)", v)
    if m:
        return "%s%s%s" % (m.group(1), fmt_num(float(m.group(2))), m.group(3))
    if v.lower().startswith("calc("):
        x = eval_calc(v[5:-1])
        if x is not None:
            return fmt_num(round(x, 3)) + ("px" if re.search(r"\d(px|r?em)\b", v) else "")
    return v


def _band(b):
    if b >= 1200:
        return "desktop alt sınırı" if b == 1200 else "desktop içi"
    if b >= 992:
        return "laptop alt sınırı" if b == 992 else "laptop bandı"
    if b >= 768:
        return "tablet alt sınırı (mobil < %d)" % b if b == 768 else "tablet bandı"
    return "mobil içi"


# --------------------------------------------------------------------------- collection

def collect_live(url, paths, args, warnings):
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        raise SystemExit("error: url must be http(s)://host/... (or use --fixture)")
    origin = "%s://%s" % (parts.scheme, parts.netloc)
    page_urls = []
    if paths:
        for p in paths:
            u = urllib.parse.urljoin(origin + "/", p.strip())
            if urllib.parse.urlsplit(u).netloc != parts.netloc:
                warnings.append("farklı origin, atlandı: %s" % p)
                continue
            page_urls.append(u)
    else:
        page_urls.append(url)
    pages, css, js_texts = [], CSSData(), []
    seen_css, seen_js, seen_inline = set(), set(), set()
    css_budget, js_budget = args.max_css, args.max_js
    queue_css = []
    skipped = Counter()
    for pu in page_urls:
        html = fetch(pu, args.timeout, warnings, accept="text/html,*/*;q=0.8")
        if html is None:
            continue
        label = urllib.parse.urlsplit(pu).path or "/"
        pp = PageParser()
        pp.feed(html)
        pp.close()
        pages.append({"label": label, "url": pu, "parser": pp})
        for k, text in enumerate(pp.styles, 1):
            h = hashlib.sha1(text.encode("utf-8", "replace")).hexdigest()
            if h in seen_inline:
                continue
            seen_inline.add(h)
            parse_css(text, css, "%s <style#%d>" % (label, k))
        for k, text in enumerate(pp.data_scripts, 1):
            h = hashlib.sha1(text.encode("utf-8", "replace")).hexdigest()
            if h in seen_inline:
                continue
            seen_inline.add(h)
            js_texts.append(("%s <script#%d>" % (label, k), text))
        for href in pp.stylesheets:
            queue_css.append(urllib.parse.urljoin(pu, href))
        for href in pp.js:
            ju = urllib.parse.urljoin(pu, href)
            if ju in seen_js:
                continue
            seen_js.add(ju)
            name = os.path.basename(urllib.parse.urlsplit(ju).path)
            if JS_SKIP_HOST.search(urllib.parse.urlsplit(ju).netloc) or JS_SKIP_NAME.match(name):
                continue
            if js_budget <= 0:
                skipped["js"] += 1
                continue
            if host_is_private(ju):
                warnings.append("özel/yerel adres, atlandı: %s" % ju)
                continue
            js_budget -= 1
            text = fetch(ju, args.timeout, warnings)
            if text is not None:
                js_texts.append((ju, text))
    i = 0
    while i < len(queue_css):
        cu = queue_css[i]
        i += 1
        if cu in seen_css:
            continue
        seen_css.add(cu)
        if css_budget <= 0:
            skipped["css"] += 1
            continue
        if host_is_private(cu):
            warnings.append("özel/yerel adres, atlandı: %s" % cu)
            continue
        css_budget -= 1
        text = fetch(cu, args.timeout, warnings, accept="text/css,*/*;q=0.1")
        if text is None:
            continue
        n_imp = len(css.imports)
        parse_css(text, css, cu)
        for href, _src in css.imports[n_imp:]:
            queue_css.append(urllib.parse.urljoin(cu, href))
    if skipped["css"]:
        warnings.append("--max-css sınırı: %d stil dosyası atlandı" % skipped["css"])
    if skipped["js"]:
        warnings.append("--max-js sınırı: %d JS dosyası atlandı" % skipped["js"])
    meta = {"origin": origin, "pages": [p["url"] for p in pages],
            "external_css": sorted(seen_css), "js_scanned": [s for s, _ in js_texts]}
    return pages, css, js_texts, meta


def collect_fixture(path, label_url, warnings):
    if os.path.isfile(path):
        files = [path]
        root = os.path.dirname(path)
    else:
        root = path
        files = sorted(os.path.join(root, f) for f in os.listdir(root))
    pages, css, js_texts = [], CSSData(), []
    seen_inline = set()
    html_files = [f for f in files if f.lower().endswith((".html", ".htm"))]
    css_files = [f for f in files if f.lower().endswith(".css")] if os.path.isdir(path) else []
    js_files = [f for f in files if f.lower().endswith((".js", ".mjs"))] if os.path.isdir(path) else []
    external = 0
    for f in html_files:
        text = read_local(f, warnings)
        if text is None:
            continue
        label = "fixture:" + os.path.basename(f)
        pp = PageParser()
        pp.feed(text)
        pp.close()
        pages.append({"label": label, "url": label, "parser": pp})
        for k, t in enumerate(pp.styles, 1):
            h = hashlib.sha1(t.encode("utf-8", "replace")).hexdigest()
            if h not in seen_inline:
                seen_inline.add(h)
                parse_css(t, css, "%s <style#%d>" % (label, k))
        for k, t in enumerate(pp.data_scripts, 1):
            js_texts.append(("%s <script#%d>" % (label, k), t))
        external += len(pp.stylesheets)
    for f in css_files:
        t = read_local(f, warnings)
        if t is not None:
            parse_css(t, css, "fixture:" + os.path.basename(f))
    for f in js_files:
        t = read_local(f, warnings)
        if t is not None:
            js_texts.append(("fixture:" + os.path.basename(f), t))
    if external:
        warnings.append("fixture modu: HTML'deki %d harici stil bağlantısı çekilmedi" % external)
    origin = label_url
    if not origin:
        for p in pages:
            if p["parser"].canonical:
                origin = p["parser"].canonical
                break
    meta = {"origin": origin or "fixture", "pages": [p["url"] for p in pages],
            "external_css": ["fixture:" + os.path.basename(f) for f in css_files],
            "js_scanned": [s for s, _ in js_texts]}
    return pages, css, js_texts, meta


# --------------------------------------------------------------------------- report

def cell(x):
    return str(x).replace("|", "\\|").replace("\n", " ")


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(cell(c) for c in r) + " |")
    return out


def render(res, meta, warnings, top):
    L = []
    w = L.append
    w("# Site analizi — %s" % meta["origin"])
    w("")
    w("Üretici: `analyze_site.py` (metin olarak ayrıştırma; hiçbir şey çalıştırılmadı). "
      "`%s` = kaynaktan okunan değer; her satırda kaynak (URL/dosya + seçici) verilir." % TAG)
    w("")
    w("## 0. Kaynaklar")
    w("")
    rows = []
    for p in meta["pages"]:
        rows.append(["Sayfa", p, TAG])
    for g in meta.get("generator", []):
        rows.append(["meta generator", g, TAG])
    rows.append(["Satır içi <style> blokları", meta["inline_styles"], TAG])
    rows.append(["Harici CSS", len(meta["external_css"]), TAG])
    for c in meta["external_css"]:
        rows.append(["CSS", c, TAG])
    inline_js = [s for s in meta["js_scanned"] if "<script#" in s]
    rows.append(["Taranan satır içi <script> metni", len(inline_js), TAG])
    for s in meta["js_scanned"]:
        if s not in inline_js:
            rows.append(["JS (metin)", s, TAG])
    rows.append(["CSS bildirimi", meta["decl_count"], TAG])
    rows.append(["rem tabanı (html/:root font-size)", "%spx" % fmt_num(res["rem_px"]), TAG])
    L += table(["Öğe", "Değer", "Etiket"], rows)
    w("")

    w("## 1. Fontlar")
    w("")
    w("### 1.1 Kullanım sıklığı (ilk aile)")
    w("")
    L += table(["Aile", "Kullanım", "Kaynak", "Etiket"],
               [[f["family"], f["count"], f["src"], TAG] for f in res["fonts"]["usage"][:top]])
    w("")
    w("### 1.2 @font-face")
    w("")
    L += table(["Aile", "Ağırlıklar", "Stiller", "Biçim", "Alt küme", "Barındırma", "Kaynak", "Etiket"],
               [[f["family"], ", ".join(f["weights"]), ", ".join(f["styles"]), ", ".join(f["formats"]),
                 f["subsets"], ", ".join(f["hosts"]) or "—", f["src"], TAG]
                for f in res["fonts"]["fontfaces"][:top]])
    w("")
    if res["fonts"]["google_fonts"]:
        w("### 1.3 Google Fonts bağlantıları")
        w("")
        L += table(["Aile", "Eksen/ağırlık", "Kaynak", "Etiket"],
                   [[g["family"], g["spec"] or "—", g["src"], TAG] for g in res["fonts"]["google_fonts"]])
        w("")

    w("## 2. Renkler")
    w("")
    w("### 2.1 Sıklık")
    w("")
    rows = []
    for c in res["colors"][:top]:
        where = " · ".join("%s %d" % (k, v) for k, v in sorted(c["where"].items(), key=lambda x: (-x[1], x[0])))
        rows.append(["`%s`" % c["hex"], c["count"], where, c["src"], TAG])
    L += table(["Renk", "Toplam", "Kullanım yeri", "Örnek kaynak", "Etiket"], rows)
    w("")
    if res["color_tokens"]:
        w("### 2.2 Renk değişkenleri")
        w("")
        L += table(["Değişken", "Değer", "var() referansı", "Kaynak", "Etiket"],
                   [["`%s`" % t["name"], "`%s`" % t["value"], t["refs"], t["src"], TAG]
                    for t in res["color_tokens"][:top]])
        w("")

    w("## 3. Tipografi")
    w("")
    w("### 3.1 Preset adayları (kademeli çözümleme: 1440 / 1100 / 880 / 390 px)")
    w("")
    rows = []
    for p in res["presets"][:top]:
        sel = "`%s`" % p["selector"] + (" (+%d)" % len(p["also"]) if p["also"] else "")
        rows.append([sel] + [p["sizes"][b] or "—" for b in BUCKETS] +
                    [short(x, 40) or "—" for x in (p["weight"], p["line_height"], p["letter_spacing"],
                                                   p["transform"], p["family"])] +
                    [p["usage"], p["src"], TAG])
    L += table(["Seçici"] + [BUCKET_HDR[b] for b in BUCKETS] +
               ["Ağırlık", "Satır", "Harf aralığı", "Dönüşüm", "Aile", "Kullanım", "Kaynak", "Etiket"], rows)
    w("")
    w("### 3.2 font-size sıklığı (medya bandına göre)")
    w("")
    rows = []
    for s in res["font_sizes"][:top]:
        b = s["buckets"]
        rows.append([s["size"], s["total"], b.get("base", 0)] + [b.get(k, 0) for k in BUCKETS] +
                    [s["src"], TAG])
    L += table(["Boyut (px)", "Toplam", "medyasız"] + [BUCKET_HDR[b] for b in BUCKETS] +
               ["Örnek kaynak", "Etiket"], rows)
    w("")

    w("## 4. Kırılım adayları")
    w("")
    L += table(["Sınır (px)", "Sorgu", "Ham değerler", "Yorum", "Örnek kaynak", "Etiket"],
               [[b["boundary"], b["count"], ", ".join("%s ×%d" % kv for kv in b["raw"].items()),
                 b["band"], b["src"], TAG] for b in res["breakpoints"][:top]])
    w("")

    m = res["motion"]
    w("## 5. Hareket")
    w("")
    w("### 5.1 Easing eğrileri")
    w("")
    L += table(["Eğri", "CSS transition", "CSS animation", "JS", "Toplam", "Örnek kaynak", "Etiket"],
               [["`%s`" % b["curve"], b["css_transition"], b["css_animation"], b["js"], b["total"],
                 b["src"], TAG] for b in m["beziers"][:top]])
    if m["keywords"]:
        w("")
        L += table(["Anahtar kelime", "Sayı", "Kaynak", "Etiket"],
                   [[k, v, "CSS transition/animation", TAG] for k, v in m["keywords"].items()])
    w("")
    w("### 5.2 Süreler")
    w("")
    L += table(["Süre", "CSS transition", "CSS animation", "JS tween", "Toplam", "Örnek kaynak", "Etiket"],
               [["%dms" % d["ms"], d["css_transition"], d["css_animation"], d["js"], d["total"],
                 d["src"], TAG] for d in m["durations"][:top]])
    w("")
    if m["springs"]:
        w("### 5.3 Spring parametreleri (JS)")
        w("")
        L += table(["İmza", "Sayı", "Örnek kaynak", "Etiket"],
                   [[s["signature"], s["count"], s["src"], TAG] for s in m["springs"][:top]])
        w("")
    w("### 5.4 @keyframes")
    w("")
    if res["keyframes"]:
        L += table(["Ad", "Tanım", "Adım", "animation kullanımı", "Kaynak", "Etiket"],
                   [["`%s`" % k["name"], k["defs"], k["steps"], k["used"], k["src"], TAG]
                    for k in res["keyframes"][:top]])
    else:
        w("Bulunamadı.")
    w("")
    if m["properties"]:
        w("### 5.5 Geçiş yapılan özellikler")
        w("")
        L += table(["Özellik", "Sayı", "Kaynak", "Etiket"],
                   [[k, v, "CSS transition", TAG] for k, v in list(m["properties"].items())[:top]])
        w("")

    w("## 6. Çizgi ve köşe")
    w("")
    w("### 6.1 Çizgi kalınlıkları")
    w("")
    L += table(["Kalınlık", "Sayı", "Stil", "Örnek kaynak", "Etiket"],
               [[b["width"], b["count"], ", ".join("%s ×%d" % kv for kv in sorted(b["styles"].items())),
                 b["src"], TAG] for b in res["borders"][:top]])
    w("")
    w("### 6.2 Köşe yarıçapı")
    w("")
    L += table(["Değer", "Sayı", "Örnek kaynak", "Etiket"],
               [["`%s`" % r["value"], r["count"], r["src"], TAG] for r in res["radius"][:top]])
    w("")

    w("## 7. Boşluk (gap / padding)")
    w("")
    L += table(["px", "gap", "padding", "Toplam", "Örnek kaynak", "Etiket"],
               [[s["px"], s["gap"], s["padding"], s["total"], s["src"], TAG] for s in res["spacing"][:top]])
    w("")

    lay = res["layers"]
    w("## 8. Katman adları (bölüm ipuçları)")
    w("")
    if lay["sections"]:
        w("### 8.1 Sığ katmanlar (belge sırası)")
        w("")
        region_tr = {"pre": "main öncesi", "main": "main içi", "post": "main sonrası"}
        L += table(["#", "Ad", "Bölge", "HTML", "Kaynak", "Etiket"],
                   [[i + 1, s["name"], region_tr[s["region"]], s["tag"],
                     "%s [data-*-name]" % s["page"], TAG]
                    for i, s in enumerate(lay["sections"][:top * 2])])
        w("")
    w("### 8.2 Sıklık")
    w("")
    if lay["frequency"]:
        L += table(["Ad", "Sayı", "Adlı derinlik", "HTML", "Kaynak", "Etiket"],
                   [[f["name"], f["count"], f["min_named_depth"],
                     ", ".join("%s ×%d" % kv for kv in sorted(f["tags"].items())), f["src"], TAG]
                    for f in lay["frequency"][:top]])
    else:
        w("data-*-name katmanı bulunamadı.")
    w("")
    if lay["bem_blocks"]:
        w("### 8.3 BEM blokları (class)")
        w("")
        L += table(["Blok", "Sınıf kullanımı", "Kaynak", "Etiket"],
                   [[k, v, "class=\"%s__…\"" % k, TAG] for k, v in list(lay["bem_blocks"].items())[:top]])
        w("")
    if lay["landmarks"]:
        w("### 8.4 HTML landmark'ları")
        w("")
        L += table(["HTML", "Ad/id", "Sayı", "Derinlik", "Kaynak", "Etiket"],
                   [[l["tag"], l["label"] or "—", l["count"], l["depth"], "%s <%s>" % (l["page"], l["tag"]), TAG]
                    for l in lay["landmarks"][:top]])
        w("")

    w("## 9. Ölçülemeyenler ve notlar")
    w("")
    notes = []
    if not res["presets"]:
        notes.append("Tipografi preset'i bulunamadı (boyutlar JS ile atanıyor olabilir).")
    if not m["beziers"] and not m["springs"]:
        notes.append("Easing/spring bulunamadı; hareket JS'te çalışma anında üretiliyor olabilir (`--max-js` artırılabilir).")
    if not res["breakpoints"]:
        notes.append("Medya sorgusu yok; kırılımlar JS ile yönetiliyor olabilir.")
    notes.append("Render edilmiş ölçüler (bölüm yükseklikleri, grid sütun genişlikleri, görsel oranları), hover/aktif durum görünümleri ve kaydırmaya bağlı davranışlar metinden ölçülemez; tarayıcıda (Chrome) ölçülüp `[ölçüldü]` ya da gözlemle `[tahmini]` etiketlenmelidir.")
    notes.append("Değişken font eksenleri (`wdth`, `wght`) pen.dev'de ayarlanamaz; dar aile karşılığı seçilmelidir.")
    for n_ in notes:
        w("- " + n_)
    for wn in warnings:
        w("- Uyarı: " + wn)
    w("")
    return "\n".join(L)


# --------------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Measure fonts, colours, type presets, breakpoints, motion, borders, spacing "
                    "and layer names of a reference site. Text-only parsing; nothing is executed.")
    ap.add_argument("url", nargs="?", help="page URL (http/https or file:// to a fixture dir/page); "
                    "in --fixture mode an optional label")
    ap.add_argument("--paths", help="comma-separated paths relative to the URL origin, e.g. /,/shop,/about")
    ap.add_argument("--fixture", metavar="DIR", help="offline mode: read DIR/*.html, *.css, *.js|*.mjs")
    ap.add_argument("--json", metavar="FILE", help="also dump structured data as JSON")
    ap.add_argument("--out", metavar="FILE", help="write the markdown report here instead of stdout")
    ap.add_argument("--max-css", type=int, default=25, help="max external stylesheets (default 25)")
    ap.add_argument("--max-js", type=int, default=40,
                    help="max JS files scanned as text for easing/spring objects (default 40; 0 = off)")
    ap.add_argument("--timeout", type=float, default=20, help="per-request timeout in seconds (default 20)")
    ap.add_argument("--top", type=int, default=30, help="rows per table (default 30)")
    args = ap.parse_args(argv)

    warnings = []
    fixture = args.fixture
    label = args.url
    if not fixture and args.url and args.url.startswith("file://"):
        fixture = urllib.parse.unquote(urllib.parse.urlsplit(args.url).path)
        label = None
    if fixture:
        if not os.path.exists(fixture):
            ap.error("fixture not found: %s" % fixture)
        pages, css, js_texts, meta = collect_fixture(fixture, label, warnings)
    else:
        if not args.url:
            ap.error("url or --fixture is required")
        paths = [p for p in (args.paths or "").split(",") if p.strip()]
        pages, css, js_texts, meta = collect_live(args.url, paths, args, warnings)
    if not pages:
        print("error: no page could be read", file=sys.stderr)
        for wn in warnings:
            print("  " + wn, file=sys.stderr)
        return 1
    meta["generator"] = sorted(set(g for p in pages for g in p["parser"].generator if g))
    meta["inline_styles"] = len(set(s for p in pages for s in p["parser"].styles))
    res = analyze(pages, css, js_texts, args.top)
    meta["decl_count"] = len(css.decls)
    report = render(res, meta, warnings, args.top)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")
    else:
        sys.stdout.write(report + "\n")
    if args.json:
        out = OrderedDict([("meta", meta), ("warnings", warnings)])
        out.update(res)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
