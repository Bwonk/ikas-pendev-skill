// pendev_checks.js — read-only verification snippet for the pen.dev `execute` tool.
// Template: extract_targets.py --js <mode> fills the five placeholders and strips these
// whole-line comments (the official execute.md asks for comment-free snippets).
// Uses only Get / GetVariables / Print. Never mutates the document.
//
// Modes (__MODE__):
//   all              every CHK over every root frame whose name starts with "<P>/"
//   section:<Key>    one build unit: a Section/Overlay key, or DS | Sub | Page | Overlays | Motion
//   manifest         one ROOT line per root frame (port dump, docs/port/canvas-dump.txt)
//
// Output: CHK|<id>|PASS|FAIL|WARN|<n>|<detail<=200>  ...  SUMMARY|pass=..|fail=..|warn=..|mode=..
// CHK ids: vars ds sections overlays pages anim hardcoded textclass clip rootmeta bgprop
//          parity placeholder refassets
// parity: every kebab-case layer name of the @desktop component also exists in @mobile, and every
// "@desktop — <state>" root has its "@mobile — <state>" twin. Exempt: wrappers named *-row,
// *-column, *-wrap, *-body, *-main; states containing "hover"; the plan's "Yalnız masaüstü" lists
// (EXP.parity[<Key>] = {layers, states}; a listed layer exempts its whole subtree).
// textclass skips text inside <P>/DS/* and <P>/Motion/* roots (legend/specimen text).
// One execute call = one scope: the whole file is a single snippet; nothing persists.
// anim scans Section/Sub component roots and every Overlay root (Section state frames only hold refs);
// the resolveInstances pass runs only when ids are still missing.
// Large canvases: EXP.only (list of CHK ids) runs a subset; EXP.part = [k, n] limits the node walk
// of hardcoded/textclass/clip/refassets to every n-th root starting at k (counts add up over parts);
// in manifest mode it prints ROOT lines for that slice only (concatenate the parts).
const P = "__PREFIX__", SLUG = "__SLUG__", CONTRACT = __CONTRACT__, EXP = __EXP__, MODE = "__MODE__";
let pass = 0, fail = 0, warn = 0;
const cut = s => { s = String(s).replace(/[|\n]/g, "/"); return s.length > 200 ? s.slice(0, 197) + "..." : s; };
const chk = (id, st, n, d) => { if (st === "PASS") pass++; else if (st === "FAIL") fail++; else warn++; Print("CHK|" + id + "|" + st + "|" + n + "|" + cut(d || "")); };
const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const idRe = new RegExp(esc(P) + "-(?:CMP|[A-Z]{2,5})-\\d\\d", "g");
const lite = n => ({ id: n.id, name: n.name || "", type: n.type, reusable: !!n.reusable, placeholder: !!n.placeholder, metadata: n.metadata || null, theme: n.theme || null, ref: n.ref || null });
let top = Get((n, c) => { c.skipChildren(); return lite(n); });
if (top.length <= 1 && !top.some(r => r.name.indexOf(P + "/") === 0)) {
  const d = Get(document, { depth: 1 });
  top = (d && Array.isArray(d.children) ? d.children : []).filter(x => x && typeof x === "object").map(lite);
}
const roots = top.filter(r => r.name.indexOf(P + "/") === 0);
const byId = {}; top.forEach(r => { byId[r.id] = r; });
const rest = r => r.name.slice(P.length + 1);
const band = r => rest(r).split("/")[0];
const devOf = s => { const m = /@(desktop|mobile)\b/.exec(s); return m ? m[1] : "-"; };
const keyOf = r => { const m = /^[A-Za-z]+\/([A-Za-z0-9]+)/.exec(rest(r)); return m ? m[1] : ""; };
const ROLE = { DS: "ds", Sub: "sub", Section: "section", Overlay: "overlay", Page: "page", Motion: "motion" };
const ALIAS = { ds: "DS", subs: "Sub", sub: "Sub", pages: "Page", page: "Page", overlays: "Overlays", motion: "Motion" };
const anims = (m, ctx) => { const s = new Set(); if (m && typeof m.anim === "string") m.anim.split(",").forEach(x => { x = x.trim(); if (x) s.add(x); }); if (typeof ctx === "string") (ctx.match(idRe) || []).forEach(x => s.add(x)); return s; };
const scanNode = (n, into) => { anims(n.metadata, n.context).forEach(x => into.add(x)); const d = n.descendants; if (d && typeof d === "object") Object.keys(d).forEach(k => { const o = d[k] || {}; anims(o.metadata, o.context).forEach(x => into.add(x)); }); };

if (MODE === "manifest") {
  roots.filter((r, i) => !EXP.part || i % EXP.part[1] === EXP.part[0] - 1).forEach(r => {
    const props = [], data = [], code = [], ids = new Set();
    const add = (a, v) => { if (a.indexOf(v) < 0) a.push(v); };
    Get(r.id, n => {
      const m = n.metadata || {};
      if (m.prop) add(props, m.prop + ":" + (m.propType || "?"));
      if (m.textClass === "data") add(data, (n.name || "?") + "=" + (m.source || "?"));
      if (m.textClass === "code") add(code, n.name || "?");
      scanNode(n, ids);
      return undefined;
    });
    if (band(r) !== "Page") Get(r.id, n => { scanNode(n, ids); return undefined; }, { resolveInstances: true });
    const dev = devOf(r.name) !== "-" ? devOf(r.name) : ((r.metadata && r.metadata.device) || "-");
    Print(["ROOT", r.name.replace(/\|/g, "/"), r.id, "device=" + dev, "props=" + props.join(";"), "data=" + data.join(";"), "code=" + code.join(";"), "anims=" + Array.from(ids).sort().join(";")].join("|"));
  });
  Print("SUMMARY|roots=" + roots.length + "|mode=manifest" + (EXP.part ? "|part=" + EXP.part.join("/") : ""));
} else {
  let unit = MODE.indexOf("section:") === 0 ? MODE.slice(8) : null;
  if (unit && ALIAS[unit]) unit = ALIAS[unit];
  const isBand = unit === "DS" || unit === "Sub" || unit === "Page" || unit === "Motion" || unit === "Overlays";
  const inUnit = r => {
    if (!unit) return true;
    const b = band(r);
    if (unit === "Overlays") return b === "Overlay";
    if (isBand) return b === unit;
    return (b === "Section" || b === "Overlay") && keyOf(r) === unit;
  };
  const U = roots.filter(inUnit);
  if (unit && !isBand && (EXP.sections || []).indexOf(unit) < 0 && (EXP.overlays || []).indexOf(unit) < 0) chk("sections", "FAIL", 0, "unknown unit key " + unit + " (not a plan Section/Overlay)");
  const run = id => { if (EXP.only && EXP.only.indexOf(id) < 0) return false; if (!unit) return true; if (unit === "DS") return ["vars", "ds", "hardcoded", "textclass", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Page") return ["pages", "rootmeta", "placeholder"].indexOf(id) >= 0; if (unit === "Motion") return ["hardcoded", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Sub") return ["anim", "hardcoded", "textclass", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Overlays") return ["overlays", "anim", "hardcoded", "textclass", "clip", "rootmeta", "parity", "placeholder", "refassets"].indexOf(id) >= 0; return ["sections", "overlays", "anim", "hardcoded", "textclass", "clip", "rootmeta", "bgprop", "parity", "placeholder", "refassets"].indexOf(id) >= 0; };
  const find = nm => roots.find(r => r.name === nm);
  const findPre = pre => roots.filter(r => r.name === pre || r.name.indexOf(pre + " ") === 0);

  if (run("vars")) {
    const gv = GetVariables(), have = Object.keys((gv && gv.variables) || {});
    const miss = (EXP.vars || []).filter(v => have.indexOf(v) < 0), extra = have.filter(v => (EXP.vars || []).indexOf(v) < 0);
    chk("vars", miss.length ? "FAIL" : "PASS", (EXP.vars || []).length - miss.length, (EXP.vars || []).length - miss.length + "/" + (EXP.vars || []).length + (miss.length ? " missing:" + miss.join(",") : "") + (extra.length ? " extra:" + extra.join(",") : ""));
  }
  if (run("ds")) {
    const want = EXP.ds || [], got = want.filter(d => roots.some(r => rest(r) === "DS/" + d));
    const miss = want.filter(d => got.indexOf(d) < 0);
    chk("ds", miss.length ? "FAIL" : "PASS", got.length, got.length + "/" + want.length + (miss.length ? " missing:" + miss.join(",") : ""));
  }
  if (run("sections")) {
    const keys = unit && !isBand ? (EXP.sections || []).filter(k => k === unit) : (EXP.sections || []);
    if (keys.length || !unit) {
      const bad = [];
      keys.forEach(k => ["desktop", "mobile"].forEach(d => { const r = find(P + "/Section/" + k + "@" + d); if (!r) bad.push(k + "@" + d + ":missing"); else if (!r.reusable) bad.push(k + "@" + d + ":not-reusable"); }));
      const ok = keys.filter(k => !bad.some(b => b.indexOf(k + "@") === 0)).length;
      chk("sections", bad.length ? "FAIL" : "PASS", ok, ok + "/" + keys.length + (bad.length ? " " + bad.join(",") : ""));
    }
  }
  if (run("overlays")) {
    const keys = unit && !isBand ? (EXP.overlays || []).filter(k => k === unit) : (EXP.overlays || []);
    if (keys.length || !unit || unit === "Overlays") {
      const bad = [];
      keys.forEach(k => ((EXP.overlayDevices || {})[k] || ["desktop", "mobile"]).forEach(d => { if (!findPre(P + "/Overlay/" + k + "@" + d).length) bad.push(k + "@" + d); }));
      const ok = keys.filter(k => !bad.some(b => b.indexOf(k + "@") === 0)).length;
      chk("overlays", bad.length ? "FAIL" : "PASS", ok, ok + "/" + keys.length + (bad.length ? " missing:" + bad.join(",") : ""));
    }
  }
  if (run("pages")) {
    const pages = EXP.pages || {}, names = Object.keys(pages), bad = [], diff = [];
    const expand = EXP.pageExpand || {};
    names.forEach(pg => ["desktop", "mobile"].forEach(d => {
      const cands = U.filter(r => rest(r) === "Page/" + pg + "@" + d || (rest(r).indexOf("Page/" + pg + " \u2014 ") === 0 && rest(r).slice(-("@" + d).length) === "@" + d));
      if (!cands.length) { bad.push(pg + "@" + d + ":missing"); return; }
      if (cands.length < (expand[pg] || 1)) diff.push(pg + "@" + d + ":variants " + cands.length + "/" + expand[pg]);
      cands.forEach(r => {
      const node = Get(r.id, { depth: 1 }), kids = (node && Array.isArray(node.children)) ? node.children : [];
      const seq = [];
      kids.forEach(k => {
        const t = k && k.ref ? byId[k.ref] : null;
        if (!k || k.type !== "ref" || !t || rest(t).indexOf("Section/") !== 0) bad.push(pg + "@" + d + ":non-section:" + ((k && k.name) || "?"));
        else { if (devOf(t.name) !== d) bad.push(pg + "@" + d + ":device:" + keyOf(t)); seq.push(keyOf(t)); }
      });
      if (seq.join(",") !== (pages[pg] || []).join(",")) diff.push(pg + "@" + d);
      });
    }));
    const ok = names.filter(pg => !bad.some(b => b.indexOf(pg + "@") === 0)).length;
    chk("pages", bad.length ? "FAIL" : (diff.length ? "WARN" : "PASS"), ok, ok + "/" + names.length + (bad.length ? " " + bad.join(",") : "") + (diff.length ? " order/composition differs:" + diff.join(",") : ""));
  }
  if (run("anim")) {
    const want = unit ? ((EXP.unit && EXP.unit.ids) || []) : (EXP.ids || []);
    const found = new Set();
    const scope = U.filter(r => ["Section", "Overlay", "Sub"].indexOf(band(r)) >= 0 && !(band(r) === "Section" && r.name.indexOf(" \u2014 ") >= 0));
    scope.forEach(r => { Get(r.id, n => { scanNode(n, found); return undefined; }); });
    if (want.some(x => !found.has(x))) scope.filter(r => r.name.indexOf(" \u2014 ") < 0).forEach(r => { Get(r.id, n => { scanNode(n, found); return undefined; }, { resolveInstances: true }); });
    const miss = want.filter(x => !found.has(x)), extra = Array.from(found).filter(x => want.indexOf(x) < 0);
    const ok = want.length - miss.length;
    chk("anim", miss.length ? "FAIL" : (extra.length && !unit ? "WARN" : "PASS"), ok, ok + "/" + want.length + (miss.length ? " missing:" + miss.join(",") : "") + (extra.length ? " extra:" + extra.join(",") : ""));
  }
  const W = { hc: { fill: 0, stroke: 0, fontSize: 0, fontFamily: 0 }, hcx: [], texts: 0, tcMiss: 0, tcBad: 0, tcx: [], noProp: 0, clip: 0, clipx: [], ref: 0, refx: [] };
  const lit = f => { if (typeof f === "string") return f[0] === "#"; if (Array.isArray(f)) return f.some(lit); if (f && typeof f === "object") { if (f.type === "color") return typeof f.color === "string" && f.color[0] === "#"; if (f.type === "gradient") return (f.colors || []).some(x => x && typeof x.color === "string" && x.color[0] === "#"); if (f.type === "mesh_gradient") return (f.colors || []).some(x => typeof x === "string" && x[0] === "#"); } return false; };
  const imgs = f => Array.isArray(f) ? f.reduce((a, x) => a.concat(imgs(x)), []) : (f && typeof f === "object" && f.type === "image" && typeof f.url === "string" ? [f.url] : []);
  const host = EXP.referenceHost || "";
  const excl = /mask|track|marquee|ticker|pin|stage|curtain|hover|scroll|(^|-)(top|bottom|next|prev)$/i;
  if (["hardcoded", "textclass", "clip", "refassets"].some(run)) {
    U.filter((r, i) => !EXP.part || i % EXP.part[1] === EXP.part[0] - 1).forEach(r => Get(r.id, (n, c) => {
      const k = [];
      if (lit(n.fill)) k.push("fill");
      if (lit(n.stroke)) k.push("stroke");
      if (n.type === "text") {
        if (typeof n.fontSize === "number") k.push("fontSize");
        if (typeof n.fontFamily === "string" && n.fontFamily[0] !== "$") k.push("fontFamily");
        const m = n.metadata || {};
        if (band(r) !== "DS" && band(r) !== "Motion") {
          W.texts++;
          if (!m.prop) W.noProp++;
          if (!m.textClass) { W.tcMiss++; if (W.tcx.length < 6) W.tcx.push(n.name); }
          else if ((m.textClass === "prop" && !(m.prop && m.propType)) || (m.textClass === "data" && !m.source) || ["prop", "data", "code"].indexOf(m.textClass) < 0) { W.tcBad++; if (W.tcx.length < 6) W.tcx.push(n.name + ":" + m.textClass); }
        }
      }
      k.forEach(x => { W.hc[x]++; });
      if (k.length && W.hcx.length < 6) W.hcx.push((n.name || n.id) + ":" + k.join("+"));
      if (c.problems) {
        let e = false, p = c;
        while (p && !e) { if (excl.test((p.node && p.node.name) || "")) e = true; p = p.parentCtx; }
        if (!e) { W.clip++; if (W.clipx.length < 6) W.clipx.push(keyOf(r) + ">" + (n.name || n.id)); }
      }
      imgs(n.fill).forEach(u => { if ((host && u.indexOf(host) >= 0) || /framerusercontent\.com/.test(u)) { W.ref++; if (W.refx.length < 4) W.refx.push(n.name || n.id); } });
      return undefined;
    }));
  }
  if (run("hardcoded")) {
    const t = W.hc.fill + W.hc.stroke + W.hc.fontSize + W.hc.fontFamily;
    chk("hardcoded", t ? (CONTRACT < 2 ? "WARN" : "FAIL") : "PASS", t, "fill=" + W.hc.fill + " stroke=" + W.hc.stroke + " fontSize=" + W.hc.fontSize + " fontFamily=" + W.hc.fontFamily + (W.hcx.length ? " e.g. " + W.hcx.join(",") : ""));
  }
  if (run("textclass")) {
    if (CONTRACT >= 2) chk("textclass", W.tcMiss + W.tcBad ? "FAIL" : "PASS", W.tcMiss + W.tcBad, "texts=" + W.texts + " none=" + W.tcMiss + " invalid=" + W.tcBad + (W.tcx.length ? " e.g. " + W.tcx.join(",") : ""));
    else chk("textclass", W.noProp ? "WARN" : "PASS", W.noProp, "contract 1 baseline: texts=" + W.texts + " without metadata.prop=" + W.noProp);
  }
  if (run("clip")) chk("clip", W.clip ? "WARN" : "PASS", W.clip, W.clip ? "clipped (excl. mask/track/marquee/ticker/pin/stage/curtain): " + W.clipx.join(",") : "no clipped content");
  if (run("rootmeta")) {
    const bad = [];
    U.forEach(r => {
      const m = r.metadata || {}, b = band(r), why = [];
      const isState = r.name.indexOf(" \u2014 ") >= 0;
      if (isState && CONTRACT < 2) return;
      if (m.type !== SLUG) why.push("type");
      if (m.role !== ROLE[b]) why.push("role");
      if (isState) { if (why.length) bad.push(rest(r) + ":" + why.join("+")); return; }
      if (m.variant !== P) why.push("variant");
      const d = devOf(r.name);
      if (d !== "-" && m.device !== d) why.push("device");
      if (d !== "-" && (!r.theme || r.theme.device !== d)) why.push("theme");
      if ((b === "Section" || b === "Sub" || b === "Overlay") && !m.ikas) why.push("ikas");
      if (CONTRACT >= 2 && m.contract !== CONTRACT && String(m.contract) !== String(CONTRACT)) why.push("contract");
      if (why.length) bad.push(rest(r) + ":" + why.join("+"));
    });
    chk("rootmeta", bad.length ? "FAIL" : "PASS", U.length - bad.length, (U.length - bad.length) + "/" + U.length + (bad.length ? " " + bad.join(",") : ""));
  }
  if (run("bgprop")) {
    const secs = U.filter(r => band(r) === "Section");
    if (CONTRACT < 2) chk("bgprop", "PASS", 0, "skip: contract 1 roots carry no backgroundColor");
    else {
      const bad = secs.filter(r => !(r.metadata && r.metadata.prop === "backgroundColor" && r.metadata.propType === "COLOR")).map(rest);
      chk("bgprop", bad.length ? "FAIL" : "PASS", secs.length - bad.length, (secs.length - bad.length) + "/" + secs.length + (bad.length ? " missing:" + bad.join(",") : ""));
    }
  }
  if (run("parity")) {
    const PAR = EXP.parity || {}, kebab = /^[a-z][a-z0-9-]*$/, STRUCT = /-(row|column|wrap|body|main)$/;
    const keys = unit === "Overlays" ? (EXP.overlays || []) : (unit && !isBand ? [unit] : (EXP.sections || []).concat(EXP.overlays || []));
    const names = (id, allow) => { const s = new Set(); Get(id, (n, c) => { const nm = n.name || ""; if (n.id !== id && kebab.test(nm)) { if (allow.indexOf(nm) >= 0) { c.skipChildren(); return undefined; } if (!STRUCT.test(nm)) s.add(nm); } return undefined; }); return s; };
    const badL = [], badS = [], badK = new Set(); let checked = 0;
    keys.forEach(k => {
      const kind = (EXP.sections || []).indexOf(k) >= 0 ? "Section" : "Overlay";
      if (kind === "Overlay" && ((EXP.overlayDevices || {})[k] || ["desktop", "mobile"]).length < 2) return;
      const al = (PAR[k] && PAR[k].layers) || [], as = (PAR[k] && PAR[k].states) || [];
      const pre = P + "/" + kind + "/" + k + "@", dsk = roots.filter(r => r.name.indexOf(pre + "desktop \u2014 ") === 0);
      let d = find(pre + "desktop"), m = find(pre + "mobile");
      if (!(d && m)) { const tw = dsk.map(r => [r, find(r.name.replace("@desktop \u2014 ", "@mobile \u2014 "))]).find(x => x[1]); if (tw) { d = tw[0]; m = tw[1]; } }
      if (!(d && m)) return;
      checked++;
      const M = names(m.id, []);
      names(d.id, al).forEach(x => { if (!M.has(x)) { badK.add(k); badL.push(k + ">" + x); } });
      dsk.forEach(r => { const st = r.name.slice((pre + "desktop \u2014 ").length); if (/hover/i.test(st) || as.indexOf(st) >= 0) return; if (!find(pre + "mobile \u2014 " + st)) { badK.add(k); badS.push(k + " \u2014 " + st); } });
    });
    const okK = checked - badK.size;
    chk("parity", badK.size ? "FAIL" : "PASS", okK, okK + "/" + checked + (badS.length ? " mobile state missing:" + badS.join(",") : "") + (badL.length ? " desktop-only layers:" + badL.join(",") : ""));
  }
  if (run("placeholder")) {
    const ph = U.filter(r => r.placeholder).map(rest);
    chk("placeholder", ph.length ? "FAIL" : "PASS", ph.length, ph.length ? "still placeholder:" + ph.join(",") : "none");
  }
  if (run("refassets")) chk("refassets", W.ref ? "FAIL" : "PASS", W.ref, W.ref ? "reference-host image fills: " + W.refx.join(",") : "no reference-host image fills" + (host ? " (" + host + ")" : ""));
  Print("SUMMARY|pass=" + pass + "|fail=" + fail + "|warn=" + warn + "|mode=" + MODE + "|roots=" + U.length + (EXP.only ? "|only=" + EXP.only.join(",") : "") + (EXP.part ? "|part=" + EXP.part.join("/") : ""));
}
