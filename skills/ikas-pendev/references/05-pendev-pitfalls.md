# 05 · pen.dev pitfalls — symptom → cause → fix

This file only adds what the official pen.dev skill does not say, or says in a place that is easy to miss. It never restates the API: read the official files first (`mcp__pencil__read_skill()` → `SKILL.md`, `pen-schema.md`, `execute.md`; `generate.md` before any `Generate`; `guide/components.md` before building Subs). "Official" lines point to the file and section to open. Items marked *observed* were found on real canvases and are not in the official docs.

## Contents
1. Metadata is only kept at creation · 2. `Replace` on a normal layer · 3. Instances drop metadata · 4. Invalid fonts · 5. Translucent colours · 6. `Generate` is async · 7. No wrap · 8. Invisible text · 9. One scope per call · 10. Placement · 11. Failed `execute` · 12. Multiplayer · 13. `fit_content` / `fill_container` loop · 14. Screenshot discipline

## 1. Metadata is only kept at creation *(observed)*
- **Symptom:** `Update(id, {metadata:{…}})` returns without error, but a later `Get` shows the old or no metadata; CHK `rootmeta`, `anim` or `textclass` fails on a layer you "fixed".
- **Cause:** pen.dev keeps `metadata` from the `Insert`/`Copy` that created the node; later writes are not persisted.
- **Fix:** write the final `name`, flat `metadata` and `context` in the creating `Insert` (build each root frame's tree with all metadata in one call). To correct metadata on an existing layer, recreate that layer with the §2 recipe.
- **Official:** `pen-schema.md` (`Entity.metadata`, `Entity.context`) defines the fields; persistence is not documented.

## 2. `Replace` on a normal layer throws "reading 'type'" *(observed)*
- **Symptom:** `Replace(layerId, {...})` on a layer that is *not* inside an instance fails with `Cannot read properties of undefined (reading 'type')`.
- **Cause:** `Replace` is meant for instance descendants (`instanceId/childId`). On regular frames the official guidance is to `Insert`.
- **Fix — insert at index → Move → Delete → re-point overrides:**
  1. Read where the old layer sits and which instances override it (read-only call; persist with bare assignment):
     ```js
     Get((n,c)=>{ if(n.id===OLD){ at={parent:c.parentCtx.node.id,index:c.index}; c.skipChildren() } })
     Get(n => n.type==="ref" && n.ref===COMP ? Print(n.id, n.name, JSON.stringify(Object.keys(n.descendants||{}).filter(k=>k.includes(OLD)))) : undefined)
     ```
     `COMP` is the id of the reusable root that contains `OLD` (for a section: the `P/Section/<Key>@device` frame). `n.type==="ref" && n.ref===COMP` lists every instance of that component (page frames, other sections).
  2. `newId = Insert(at.parent, {…full node with final name + metadata…})`, then `Move(newId, at.parent, at.index)` (Insert appends at the end). If the old layer had children you keep, `Move(childId, newId)` each.
  3. `Delete(OLD)`.
  4. Re-point overrides: for each instance printed in step 1, re-apply the same override values on the new id: `Update(instId + "/" + newId, {…})`. Overrides keyed by the deleted id are dead — they silently stop applying.
  5. Run the unit's checks again (CHK `anim`, `textclass`, `pages`).
- **Official:** `execute.md` §Replace and §Move; `guide/components.md` "When modifying component instance descendants" (use `Insert` when the parent is a regular frame).

## 3. Instances and overrides drop metadata → put IDs in `context` *(observed)*
- **Symptom:** a `Get(n => n.metadata?.anim …)` scan of a page returns fewer anim ids than the plan; instance layers show no `metadata`.
- **Cause:** metadata lives on the component's own nodes; `ref` instances and their overrides do not carry it.
- **Fix:** every animated layer inside a reusable root also writes its ids in `context` (`"P-HERO-02 · M-07 · …"`). Verification scans the union of `metadata.anim` and the `context` regex, with `resolveInstances: true` (CHK `anim`). Never re-add metadata per instance.
- **Official:** `guide/components.md` (instances have no children of their own; overrides via `descendants`).

## 4. Invalid fonts *(observed)*
- **Symptom:** `execute` warns "Font family … is invalid"; text renders in a fallback face.
- **Cause:** not every Google family name is accepted, despite "All Google fonts are available".
- **Fix:** change the `font-*` variable value, not individual nodes. Known invalid: `Mona Sans Condensed`, `Big Shoulders Display`. Tested valid: `Anton`, `Antonio`, `Archivo Narrow`, `Barlow`, `Barlow Condensed`, `Bebas Neue`, `JetBrains Mono`, `Mona Sans`, `Oswald`, `Sofia Sans Extra Condensed`, `Space Mono`. Variable-font axes cannot be set; pick a family that is already condensed. Re-check Turkish glyphs (`04-ikas-constraints.md` §4).
- **Official:** `SKILL.md` §Style ("All Google fonts are available"); `execute.md` top (fix warnings in the next call).

## 5. Translucent colours need their own variable
- **Symptom:** you want `$color-text` at 60% (scrim, gradient start, overlay) and there is no property for it.
- **Cause:** colour-fill opacity exists only as the hex alpha channel; a `$variable` reference cannot take an extra alpha.
- **Fix:** define a dedicated themed colour variable whose value is `#RRGGBBAA`: `color-scrim` (`#0D0D0D99`), `color-transparent` (`#RRGGBB00`, the gradient start that matches the section background). Never hardcode the hex on the node (CHK `hardcoded`).
- **Official:** `pen-schema.md` `Color` and `Fill` ("Fill opacity can only be set via the hex alpha channel").

## 6. `Generate` is async
- **Symptom:** the screenshot right after `Generate` shows an empty frame; a second `Generate` doubles the cost.
- **Fix:** keep building; check later with a cheap `Get` (fill `url` no longer `pencil:pending-image-…`, or SVG frame `placeholder` cleared), screenshot only after it landed. Never re-generate pending work. Logos once, as a reusable `P/Sub/Logo`.
- **Official:** `generate.md` §Waiting for a result.

## 7. Flex layout never wraps
- **Symptom:** a chip row, 4-column grid or tag cloud runs off the frame.
- **Fix:** build rows explicitly (one horizontal frame per row inside a vertical frame). On `@mobile`, a horizontally scrolling rail is drawn as one row that overflows a `clip: true` container (name it `…-track`, so CHK `clip` exempts it).
- **Official:** `SKILL.md` §Flexbox Layout ("single-axis only with no item wrapping").

## 8. Text is invisible without `fill`
- **Fix:** every text node gets `fill: "$color-…"`. Put `fill` in the shared text style object you spread.
- **Official:** `SKILL.md` §Objects ("Text has no `fill` by default").

## 9. One scope per `execute` call
- **Symptom:** `ReferenceError` for a helper or id from the previous call.
- **Fix:** persist ids with bare assignment (`heroId = Insert(…)`), redefine helpers in each call, keep `Get` results out of globals. The build log records root ids so a new session can resume.
- **Official:** `execute.md` intro ("Each `execute` is executed in its own scope").

## 10. Placement: `FindEmptySpace`, `placeholder`, bands
- **Fix:** every new root frame is placed with `FindEmptySpace` (chain with `nodeId` = previous root) and created with `placeholder: true`; clear it when that unit's checks pass (CHK `placeholder`). Respect the contract's bands (DS → Sub → Section → Page → Overlay → Motion, top to bottom; desktop and mobile of one unit side by side — `02-contract.md`). Never place loose text or shapes at the document root; notes are `note` nodes beside the frame.
- **Official:** `execute.md` §FindEmptySpace; `SKILL.md` §Using placeholders and §General instructions (clean document root).

## 11. A failed `execute` must be patched, not resent
- **Fix:** all changes of a failed call are rolled back. Patch the same snippet with `edits` + the `editId` from the error; on a second failure keep patching under the same `editId` (the `find` must match the already-patched text). Resending the snippet creates divergent code and loses the edit history.
- **Official:** `execute.md` intro (error handling).

## 12. Multiplayer: the canvas changes under you
- **Fix:** before editing a unit from an earlier session, re-read it (`Get(rootId, {depth: 2})` or a visitor). If a node is missing or different, re-read instead of recreating, and never undo the user's edits. Resume from `docs/pendev/build-log.md` node ids, then verify they still exist.
- **Official:** `SKILL.md` §General instructions (collaborative multiplayer).

## 13. `fit_content` parent with only `fill_container` children
- **Symptom:** a frame collapses to 0 (or to its fallback size) and its text disappears.
- **Fix:** at least one axis must be defined from outside: give the parent a fixed or `fill_container` width, or give one child an intrinsic size. Typical case: a text with `textGrowth: "fixed-width"` + `width: "fill_container"` inside a `fit_content` card.
- **Official:** `SKILL.md` §Flexbox Layout (circular dependency, antipattern block).

## 14. Screenshot discipline
- **Rule:** one `TakeScreenshot` per finished unit (a root pair or a Sub with its states), of the smallest meaningful node, at the end of the call that finished it. Structure, sizing and clipping are checked with `Get` visitors (`ctx.bounds`, `ctx.problems`) and the CHK snippet, not with screenshots. Note the screenshot in the build-log line.
- **Official:** `execute.md` §TakeScreenshot.
