const P = "C", SLUG = "gizem", CONTRACT = 1, EXP = {"prefix":"C","slug":"gizem","contract":1,"referenceHost":"axm.framer.website","vars":["color-bg","color-text","color-muted","color-line","color-surface","color-inverse-bg","color-inverse-text","color-accent","color-accent-text","color-scrim","font-display","font-ui","font-body","font-price","font-mono","text-display","text-h2","text-h3","text-h4","text-title","text-ui","text-ui-sm","text-badge","text-label","text-body","text-price","space-page","space-grid","space-card","space-panel","space-xs","space-sm","space-md","space-section","size-header","size-line","opacity-inactive"],"ds":["Colors","Typography","Spacing","Icons","Motion"],"sections":["Header","Footer","HeroSplit","TickerStrip","ProductIndex","LookbookScroll","CategoryMosaic","DropGrid","Manifesto","StickerWall","JournalRows","ProductList","CollectionHero","ProductDetail","ProductCarousel","AboutHero","PressSlider","ValuesStack","ProcessSteps","TeamGrid","Timeline","CtaBanner","AnchorNav","BlogPost","MarqueeTitle","Contact","SupportContent","CartPage","AuthForms","Account","NotFound"],"overlays":["MenuOverlay","CartDrawer","SearchOverlay"],"overlayDevices":{"MenuOverlay":["desktop","mobile"],"CartDrawer":["desktop","mobile"],"SearchOverlay":["desktop","mobile"]},"pages":{"Home":["Header","HeroSplit","TickerStrip","ProductIndex","LookbookScroll","CategoryMosaic","DropGrid","Manifesto","StickerWall","JournalRows","TickerStrip","Footer"],"Category":["Header","ProductList","Footer"],"Collection":["Header","CollectionHero","ProductList","Footer"],"Product":["Header","ProductDetail","ProductCarousel","ProductCarousel","StickerWall","Footer"],"About":["Header","AboutHero","Manifesto","PressSlider","ValuesStack","ProcessSteps","TeamGrid","Timeline","CtaBanner","Footer","AnchorNav"],"Journal":["Header","MarqueeTitle","JournalRows","Footer"],"JournalPost":["Header","BlogPost","JournalRows","Footer"],"Contact":["Header","MarqueeTitle","Contact","ProductCarousel","Footer"],"Support":["Header","SupportContent","Footer"],"Cart":["Header","CartPage","Footer"],"Auth":["Header","AuthForms","Footer"],"Account":["Header","Account","Footer"],"NotFound":["Header","NotFound","Footer"]},"pageExpand":{"Home":1,"Category":1,"Collection":1,"Product":1,"About":1,"Journal":1,"JournalPost":1,"Contact":1,"Support":1,"Cart":1,"Auth":4,"Account":1,"NotFound":1},"ids":["C-CMP-01","C-CMP-02","C-CMP-03","C-CMP-04","C-CMP-05","C-CMP-06","C-CMP-07","C-CMP-08","C-CMP-09","C-CMP-10","C-CMP-11","C-CMP-12","C-CMP-13","C-CMP-14","C-HDR-01","C-HDR-02","C-HDR-03","C-MENU-01","C-MENU-02","C-MENU-03","C-MENU-04","C-CART-01","C-CART-02","C-CART-03","C-SRCH-01","C-SRCH-02","C-FTR-01","C-FTR-02","C-FTR-03","C-HERO-01","C-HERO-02","C-HERO-03","C-HERO-04","C-HERO-05","C-HERO-06","C-TICK-01","C-IDX-01","C-IDX-02","C-IDX-03","C-IDX-04","C-LOOK-01","C-LOOK-02","C-LOOK-03","C-LOOK-04","C-MOS-01","C-MOS-02","C-MOS-03","C-DROP-01","C-DROP-02","C-DROP-03","C-DROP-04","C-MANI-01","C-MANI-02","C-WALL-01","C-WALL-02","C-WALL-03","C-WALL-04","C-JROW-01","C-JROW-02","C-JROW-03","C-PLP-01","C-PLP-02","C-PLP-03","C-PLP-04","C-PLP-05","C-PLP-06","C-COLL-01","C-COLL-02","C-COLL-03","C-PDP-01","C-PDP-02","C-PDP-03","C-PDP-04","C-PDP-05","C-PDP-06","C-CRSL-01","C-CRSL-02","C-CRSL-03","C-ABH-01","C-ABH-02","C-ABH-03","C-PRS-01","C-VAL-01","C-VAL-02","C-VAL-03","C-VAL-04","C-PRC-01","C-PRC-02","C-PRC-03","C-TEAM-01","C-TEAM-02","C-TML-01","C-TML-02","C-CTA-01","C-CTA-02","C-ANC-01","C-BLP-01","C-BLP-02","C-BLP-03","C-BLP-04","C-MQT-01","C-CNT-01","C-CNT-02","C-CNT-03","C-SUP-01","C-SUP-02","C-CRTP-01","C-CRTP-02","C-CRTP-03","C-AUTH-01","C-AUTH-02","C-ACC-01","C-ACC-02","C-NF-01","C-NF-02"]}, MODE = "all";
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
roots.forEach(r => {
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
Print("SUMMARY|roots=" + roots.length + "|mode=manifest");
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
const run = id => { if (!unit) return true; if (unit === "DS") return ["vars", "ds", "hardcoded", "textclass", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Page") return ["pages", "rootmeta", "placeholder"].indexOf(id) >= 0; if (unit === "Motion") return ["hardcoded", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Sub") return ["anim", "hardcoded", "textclass", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; if (unit === "Overlays") return ["overlays", "anim", "hardcoded", "textclass", "clip", "rootmeta", "placeholder", "refassets"].indexOf(id) >= 0; return ["sections", "overlays", "anim", "hardcoded", "textclass", "clip", "rootmeta", "bgprop", "placeholder", "refassets"].indexOf(id) >= 0; };
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
U.filter(r => ["Section", "Overlay", "Sub"].indexOf(band(r)) >= 0).forEach(r => {
Get(r.id, n => { scanNode(n, found); return undefined; });
Get(r.id, n => { scanNode(n, found); return undefined; }, { resolveInstances: true });
});
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
U.forEach(r => Get(r.id, (n, c) => {
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
if (run("placeholder")) {
const ph = U.filter(r => r.placeholder).map(rest);
chk("placeholder", ph.length ? "FAIL" : "PASS", ph.length, ph.length ? "still placeholder:" + ph.join(",") : "none");
}
if (run("refassets")) chk("refassets", W.ref ? "FAIL" : "PASS", W.ref, W.ref ? "reference-host image fills: " + W.refx.join(",") : "no reference-host image fills" + (host ? " (" + host + ")" : ""));
Print("SUMMARY|pass=" + pass + "|fail=" + fail + "|warn=" + warn + "|mode=" + MODE + "|roots=" + U.length);
}
