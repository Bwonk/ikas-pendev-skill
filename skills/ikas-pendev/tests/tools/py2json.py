#!/usr/bin/env python3
"""Dev-only: convert the recovered Gizem generator data (genplans.py +
plandata_base.py + plandata_c.py) into plandata JSON for gen_plan.py.

Writes:
  examples/gizem/plandata.json            contract 1, variant C (+ hand edits)
  tests/fixtures/gizem-A.plandata.json     contract 1, variant A
  scripts/data/motion-catalogue.json       M-01..M-28 defaults (single source)

Usage:
  python3 tests/tools/py2json.py --recover <dir with genplans.py> \
      [--globals <gizem docs/referans/globals.md>] [--skill <skill dir>]

The recovered sources are executed (trusted, local scratch copies only).
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.abspath(os.path.join(HERE, '..', '..'))

TYPE_STYLE_MAP = [
    {"styles": ["text-display", "text-h2", "text-h3", "text-h4"], "spec": "`$font-display`, satır yüksekliği 0.9–1.0"},
    {"styles": ["text-title", "text-ui", "text-ui-sm", "text-badge"], "spec": "`$font-ui`, 700, satır 1.1"},
    {"styles": ["text-label"], "spec": "`$font-mono`"},
    {"styles": ["text-body"], "spec": "`$font-body`, 500, satır 1.35"},
    {"styles": ["text-price"], "spec": "`$font-price`, 700"},
]

DARK_C = {"MenuOverlay", "Footer", "Manifesto", "TickerStrip"}

PAGE_TYPES = {
    "Home": "INDEX", "Category": "CATEGORY", "Collection": "COLLECTION", "Product": "PRODUCT_DETAIL",
    "About": "CUSTOM", "Journal": "BLOG", "JournalPost": "BLOG_POST", "Contact": "CUSTOM",
    "Support": "CUSTOM", "Cart": "CART", "Account": "ACCOUNT", "NotFound": "NOT_FOUND",
}
AUTH_EXPAND = [
    {"name": "Login", "pageType": "LOGIN"},
    {"name": "Register", "pageType": "REGISTER"},
    {"name": "ForgotPassword", "pageType": "FORGOT_PASSWORD"},
    {"name": "RecoverPassword", "pageType": "RECOVER_PASSWORD"},
]

EXTRA_UTILS_C = [
    {"part": "`scrambleText(el, opts)`", "path": "`src/utils/motion/scramble.ts`", "targets": "C-M-01"},
    {"part": "`useCursorFollow(ref)`", "path": "`src/utils/motion/useCursorFollow.ts`", "targets": "C-M-03"},
    {"part": "`usePinnedHorizontal(ref)`", "path": "`src/utils/motion/usePinnedHorizontal.ts`", "targets": "C-M-04"},
    {"part": "`Sticker`, `Countdown`", "path": "`src/sub-components/<Ad>/`", "targets": "C-M-07, C-M-08"},
]


def load_recovered(rdir):
    sys.path.insert(0, rdir)
    src = open(os.path.join(rdir, 'genplans.py'), encoding='utf-8').read()
    head = src.split('os.makedirs(OUT')[0].replace('OUT = sys.argv[1]', 'OUT = None')
    ns = {'__name__': 'genplans_recovered'}
    exec(compile(head, 'genplans.py', 'exec'), ns)
    return ns


def anim(a):
    o = {"layer": a[0], "recipe": a[1], "trigger": a[2], "what": a[3]}
    if len(a) > 4 and a[4]:
        o.update(a[4])
    return o


def section(s, dark=()):
    o = {"key": s['key'], "code": s['code'], "kind": s['kind'], "pages": s['pages'], "ikas": s['ikas']}
    if s.get('props'):
        o['props'] = s['props']
    if s['key'] in dark:
        o['mode'] = 'dark'
    o['desktop'] = s['d']
    o['mobile'] = s['m']
    o['tree'] = s['tree'].split('\n')
    o['checks'] = list(s['checks'])
    o['anims'] = [anim(a) for a in s['anims']]
    return o


def component(c):
    name, struct, states, anims = c
    return {"name": name, "structure": struct, "states": states, "anims": [anim(a) for a in anims]}


def page(p):
    name, comp = p
    o = {"name": name, "sections": comp}
    if name.startswith('Auth'):
        o['pageType'] = 'LOGIN'
        o['expand'] = AUTH_EXPAND
    else:
        o['pageType'] = PAGE_TYPES[name]
    return o


def variables(cfg, muted_fix=False):
    colors = {}
    for c in cfg['colors']:
        v = list(c[1:]) if cfg['modes'] else c[1]
        colors[c[0]] = v
    if muted_fix:
        assert colors['color-muted'][0] == '#77736A'
        colors['color-muted'][0] = '#6B675F'
    d, m = cfg['sizes']
    return {
        "intro": "Adlar üç planda aynıdır (`globals.md` ile eşleşir); değerler bu varyanta özgüdür.",
        "colors": colors,
        "fonts": {k: v for k, v in cfg['fonts']},
        "type": {k: [d[k], m[k]] for k in d},
        "numbers": {k: (dv if dv == mv else [dv, mv]) for k, dv, mv in cfg['nums']},
    }


def plandata(ns, V, file_slug_hint, muted_fix, context_scan):
    cfg = ns['VARIANTS'][V]
    rec_local = {}
    if cfg['extra']:
        recs, docs = cfg['extra']
        for rid, name, what, struct in docs:
            r = recs[rid]
            rec_local[rid] = {"name": name, "what": what, "struct": struct, "frm": r['frm'], "to": r['to'],
                              "timing": r['timing'], "impl": r['impl'], "mobile": r['mobile'], "rm": r['rm']}
            if rid in ns['STATE_HINT']:
                rec_local[rid]['stateHint'] = ns['STATE_HINT'][rid]
    dark = DARK_C if V == 'C' else ()
    return {
        "schema": 1,
        "contract": 1,
        "contextScan": context_scan,
        "theme": {
            "slug": "gizem",
            "name": "Gizem",
            "sector": "streetwear",
            "prefix": V,
            "file": cfg['file'],
            "title": cfg['title'],
            "lead": cfg['lead'],
            "reference": {
                "url": "https://axm.framer.website/",
                "canvasImportNote": "Dosyadaki `axm.framer.website` adlı 8 frame referansın ham import'udur: **sadece bakmak için**; içinden katman kopyalanmaz, silinmez, değiştirilmez.",
                "policy": "Referans (ücretli Framer şablonu) sadece ilham; görselleri, metinleri, logosu ve adı kullanılmaz.",
            },
            "penFile": "gizem-%s.pen" % V,
            "codeDir": "gizem/src/",
            "locale": "tr-TR",
            "currency": "TRY",
        },
        "identity_md": cfg['identity'].strip('\n').split('\n'),
        "modes": list(cfg['modes']) if cfg['modes'] else None,
        "devices": {"desktop": {"width": 1440, "height": 900}, "mobile": {"width": 390, "height": 844}},
        "variables": variables(cfg, muted_fix),
        "typeStyles": {"map": TYPE_STYLE_MAP, "note": "Hepsi büyük harf (gövde metni hariç)."},
        "fontCheck": {
            "valid": ["Anton", "Antonio", "Archivo Narrow", "Barlow", "Barlow Condensed", "Bebas Neue", "JetBrains Mono",
                      "Mona Sans", "Oswald", "Sofia Sans Extra Condensed", "Space Mono"],
            "invalid": ["Mona Sans Condensed", "Big Shoulders Display"],
        },
        "ds": {
            "sampleText": "GÖLGE İÇİNDE ŞIK ÇÖZÜM 1.850 TL",
            "icons": "arama, hesap, sepet, menü, kapat, ok ↗, caret, artı, eksi, onay",
        },
        "recipes": {"local": rec_local},
        "via": dict(ns['VIA']),
        "viaRules": [{"recipe": "M-11", "layerContains": "button", "via": "Button"}],
        "utils": {
            "viaComponents": ["Marquee", "Button", "ArrowLink", "Hotspot", "AccordionItem", "Drawer"],
            "extra": EXTRA_UTILS_C if V == 'C' else [],
        },
        "components": [component(c) for c in cfg['components']],
        "sections": [section(s, dark) for s in cfg['sections']],
        "pages": [page(p) for p in cfg['pages']],
    }


def catalogue(ns, globals_md):
    names = {}
    if globals_md and os.path.exists(globals_md):
        for m in re.finditer(r'^\| \*\*(M-\d\d)\*\* \| ([^|]+?) \|', open(globals_md, encoding='utf-8').read(), re.M):
            names[m.group(1)] = m.group(2).strip()
    out = {}
    ids = sorted(set(ns['RECIPES']) | {'M-17'})
    for rid in ids:
        if rid == 'M-17':
            out[rid] = {"name": names.get(rid, "Yumuşak kaydırma"), "forbidden": True,
                        "reason": "Lenis ikas'ta kullanılamaz (paket izni yok)."}
            continue
        r = ns['RECIPES'][rid]
        o = {"name": names.get(rid, "")}
        o.update({k: r[k] for k in ('frm', 'to', 'timing', 'impl', 'mobile', 'rm')})
        if rid in ns['STATE_HINT']:
            o['stateHint'] = ns['STATE_HINT'][rid]
        out[rid] = o
    return {"schema": 1, "note": "Motion recipe catalogue M-01..M-28 (default from/to/timing/impl/mobile/reducedMotion). "
                                 "Single source for gen_plan.py, lint_plan.py and references/03-motion.md. M-17 is forbidden.",
            "recipes": out}


def dump(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote', os.path.relpath(path, SKILL))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--recover', required=True, help='directory with genplans.py, plandata_base.py, plandata_c.py')
    ap.add_argument('--globals', default=None, help='gizem docs/referans/globals.md (catalogue names)')
    ap.add_argument('--skill', default=SKILL)
    a = ap.parse_args()
    ns = load_recovered(os.path.abspath(a.recover))
    dump(plandata(ns, 'C', 'serbest-yorum', True, True), os.path.join(a.skill, 'examples/gizem/plandata.json'))
    dump(plandata(ns, 'A', 'ayni-iskelet-yeni-kimlik', False, False), os.path.join(a.skill, 'tests/fixtures/gizem-A.plandata.json'))
    dump(catalogue(ns, a.globals), os.path.join(a.skill, 'scripts/data/motion-catalogue.json'))


if __name__ == '__main__':
    main()
