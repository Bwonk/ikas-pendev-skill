---
name: ikas-pendev
description: Designs a complete, port-ready ikas e-commerce theme on the pen.dev canvas from screenshots and/or a live reference URL. Runs six gated phases — intake, design-system analysis, generated build plan, section-by-section canvas build under a fixed DS/Sub/Section/Page/Overlay/Motion contract, verification, and a port handoff package for ikas Code Components — and stops before writing ikas code. Use when the user says "ikas teması tasarla", "pen.dev'de tema", "ekran görüntüsünden tema", "bu siteden ikas teması çıkar", "referans siteyi analiz et", "tema planı üret", "bölümü pen.dev'de kur", "tasarımı doğrula", "port paketi", "$ikas-pendev", or "design an ikas theme in pen.dev", "screenshot to ikas theme" — even when they ask for only one phase (analysis, plan, one section, verify, handoff). Requires the pencil (pen.dev) MCP.
argument-hint: "[intake | analyze | plan | build <ds|subs|Section|pages|overlays|motion> | verify | handoff] [project-path]"
allowed-tools: Read, Grep, Glob, Write(docs/**), Edit(docs/**), Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/gen_plan.py *), Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/lint_plan.py *), Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/extract_targets.py *), Bash(python3 -I ${CLAUDE_SKILL_DIR}/scripts/analyze_site.py *), Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/build_manifest.py *), mcp__pencil__read_skill, mcp__pencil__get_app_state, mcp__pencil__get_style
effort: high
---

# ikas-pendev — screenshot/URL → port-ready pen.dev theme for ikas

Turns a reference (screenshots and/or a live site) into an original ikas theme design on the pen.dev canvas, built so the port to ikas Code Components is mechanical. The contract in three sentences: **a root frame is an ikas component; a layer name is a CSS class; `metadata.prop` / `metadata.anim` / `metadata.textClass` tell the port what each layer is** (a prop, an animation target, data-bound text or code-generated text).

## Rules (read these even if nothing else survives compaction)

1. **Phase gate.** Phases run 0→5. Never start phase N unless phase N−1's output file exists and its gate passed. Each phase may run in a new session, so start by reading `docs/00-brief.md` and the previous phase's file.
2. **Source of truth, in order:** the user's brief and reference → the live `.pen` file (`GetVariables()`, existing components) → `docs/` → this skill's defaults. On conflict, stop and report; do not silently pick one. The canvas is multiplayer: re-read it, never recreate from memory.
3. **Read the official pen.dev skill** at the start of every build or verify session: `mcp__pencil__read_skill()`, then `pen-schema.md` and `execute.md`; `generate.md` before any `Generate`; `guide/components.md` before `build subs`. This skill never paraphrases the pen.dev API; `references/05-pendev-pitfalls.md` only adds what the official docs do not say.
4. **The contract is fixed** (`references/02-contract.md`). No invented frame names, metadata keys, variable names or ID formats. New projects use contract 2; `contract: 1` exists only to reproduce legacy plans.
5. **Metadata at creation.** Every node gets its final `name` and flat `metadata` in the `Insert` that creates it — pen.dev does not keep metadata added later. Every text node gets `textClass` (`prop` needs `prop`+`propType`; `data` needs `source`; `code` for counters/digits). Anim IDs inside components and instances also go into `context`, because instances and overrides drop metadata. Corrections use the insert-at-index → delete → re-point recipe in 05 §2.
6. **Values only through `$variables`** (colour, font, size, spacing). The only raw values allowed are listed in 02 §3. Text always gets an explicit `fill`.
7. **ikas-portable constructs only** (`references/04-ikas-constraints.md`): the 30 prop types; Google Fonts with Turkish glyphs and weights the font ships; animations achievable with CSS, `IkasThemeSlider` or AnimeJS (no Lenis/GSAP); every Section has a `backgroundColor` COLOR prop; merchant-data props carry no default.
8. **No reference assets.** No image, copy, logo or brand name from the reference enters the design. Imagery comes from `Generate("ai"|"stock")`, logos from `Generate("svg")`. Reference imports on the canvas are look-only. Keep reference screenshots in `docs/referans/girdi/` and add that folder to the project `.gitignore`.
9. **Verify every unit.** `placeholder: true` while a root frame is being built. When a root pair is done: run `extract_targets.py --js section:<Key>`, execute the printed read-only checks, take one `TakeScreenshot`, fix in place, append to `docs/pendev/build-log.md`, then move on. Never delete-and-rebuild a frame to fix it.
10. **Language.** These instructions are English. Every generated document and every string on the canvas is Turkish (check `İ Ş Ğ Ü Ö Ç` render in the chosen fonts). Identifiers — frame, layer, prop, variable names, CHK ids — stay English. Measured values are tagged `[ölçüldü]`, estimates `[tahmini]`.

## Arguments

| `$ARGUMENTS` | Phase | Notes |
|---|---|---|
| *(none)* | resume | Read the `Durum` table in `docs/00-brief.md`; continue at the first unfinished phase. |
| `intake` | 0 | Questionnaire → `docs/00-brief.md`. |
| `analyze` | 1 | Reference → `docs/referans/globals.md` + `components.md`. |
| `plan` | 2 | `docs/pendev/plandata/` → `gen_plan.py` → `docs/pendev/plan-<P>-<slug>.md`. |
| `build <unit>` | 3 | `ds`, `subs`, a Section/Overlay key, `pages`, `overlays`, `motion`; `build` alone follows plan order. |
| `verify` | 4 | Whole-canvas checks → `docs/pendev/verify-report.md`. |
| `handoff` | 5 | `docs/port/` package. |

If the last argument is a path, it is the project root; otherwise use the working directory. The project is the ikas theme repo (or any folder with `docs/`).

## Phases

| # | Phase | Reads | Writes | Gate |
|---|---|---|---|---|
| 0 | intake | screenshots / URL / brief | `docs/00-brief.md` | user approves the brief |
| 1 | analyze | brief, inputs | `docs/referans/globals.md`, `components.md` | `lint_plan.py --globals … --components …` → `LINT OK` |
| 2 | plan | 1's outputs | `docs/pendev/plandata/`, `plan-<P>-<slug>.md` | `lint_plan.py plan.md --globals …` → `LINT OK`, contrast pass |
| 3 | build | plan, official pen.dev skill | canvas, `docs/pendev/build-log.md` | per-unit `CHK` all PASS |
| 4 | verify | canvas | `docs/pendev/verify-report.md` | `CHK` all PASS, or each FAIL has a written, user-accepted exception |
| 5 | handoff | plan, canvas dump | `docs/port/port-manifest.{json,md}`, `globals-runbook.md` | `build_manifest.py` exit 0 |

### 0 · intake
Ask in Turkish with `AskUserQuestion`, two rounds of at most four questions (details: `references/07-checklists.md` §1): inputs and the viewport width of each screenshot; brand name → slug (`^[a-z0-9-]+$`), sector, three tone adjectives; interpretation strategy (same skeleton / near clone / free interpretation) and prefix letter (check `get_app_state` for a collision with existing root frames); reference policy confirmation; pages in scope (defaults from `references/06-page-coverage.md` pre-ticked); locale, currency format, uppercase policy; palette modes (single / inverse sections / full dark); canvas and devices (1440 / 390 default); motion appetite. Fill `templates/00-brief.md`. Gate: the user says the brief is right.

### 1 · analyze
Follow `references/01-analysis.md`. URL mode: `python3 -I ${CLAUDE_SKILL_DIR}/scripts/analyze_site.py <url> --paths … --out docs/referans/analyze.md`, then read it; fall back to the Chrome snippet in 01 §3 for JS-rendered sites. Screenshot mode: vision only, every value `[tahmini]`. Hybrid: URL values win. Write `globals.md` (tokens with pen.dev variable name + ikas destination; motion catalogue) and `components.md` (page → section composition, anatomy trees with `{name:TYPE}` / `{data:}` / `{code:}`, states, mobile, prop tables) from `templates/`. Run the gate; fix every ERROR.

### 2 · plan
Write `docs/pendev/plandata/theme.json` and `sections/NN-<Key>.json` per `templates/plandata/README.md` (contract 2; the 41 core variables; every text literal in a tree line marked). Render with `python3 ${CLAUDE_SKILL_DIR}/scripts/gen_plan.py docs/pendev/plandata -o docs/pendev/`. Lint with `--globals docs/referans/globals.md`. Read the rendered §1 and §6.2 once as a designer: if a section reads as a generic template, change the data, not the prose. Show the user the §1 identity and the §6.2 section list before building.

### 3 · build
Order: `ds` → `subs` → each Section in plan §6.2 order (desktop then mobile) → `pages` → `overlays` → `motion`. Before the first `execute` of the session, read the official skill (rule 3) and `references/05-pendev-pitfalls.md`. One `execute` per root frame; build the tree in one `Insert` with all names and metadata, then `Update` for polish. After each unit: checks → screenshot → fix → build-log line (`| <root> | <nodeId> | <CHK summary> | <note> |`). `C-M`-style local recipes get their `P/Motion/…` frames in the `motion` step. The canvas is the user's file: every `mcp__pencil__execute` is a prompted action — batch sensibly, never spam.

### 4 · verify
`python3 ${CLAUDE_SKILL_DIR}/scripts/extract_targets.py <plan> --js all` → execute → paste the `CHK|…` lines into `templates/verify-report.md`. Add the two manual checks (Turkish glyph screenshot of `P/DS/Typography`; contrast pairs from 02 §10). Every FAIL either gets fixed or a one-line reasoned exception the user accepts.

### 5 · handoff
`extract_targets.py <plan> --js manifest` → execute → save the `ROOT|…` lines to `docs/port/canvas-dump.txt`. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/build_manifest.py --plandata docs/pendev/plandata --plan <plan> --dump docs/port/canvas-dump.txt -o docs/port/`. Read `references/09-handoff.md` §3 for the globals runbook the port will follow. The handoff ends with the open questions list, not with code.

## When to read which reference

| Situation | Read |
|---|---|
| Extracting tokens or inventory from a screenshot/URL | `references/01-analysis.md` |
| Naming anything, choosing variables, writing metadata, text classes, IDs | `references/02-contract.md` |
| Deciding layer structure for something that will move; writing anim-targets | `references/03-motion.md` |
| Unsure whether a construct ports (prop type, font, package, responsive) | `references/04-ikas-constraints.md` |
| About to execute on the canvas; something went wrong on the canvas | `references/05-pendev-pitfalls.md` (+ official `execute.md`) |
| Deciding which pages, overlays and states are in scope | `references/06-page-coverage.md` |
| Intake questions, per-unit loop, CHK ids, verify-report format | `references/07-checklists.md` |
| The design looks generic; writing Turkish copy; self-critique before "done" | `references/08-quality.md` |
| Producing the port package or planning theme globals | `references/09-handoff.md` |
| Writing plandata | `templates/plandata/README.md` |

## Checklist (copy into the conversation and tick)

```
ikas-pendev:
- [ ] 0 intake   docs/00-brief.md yazıldı ve onaylandı
- [ ] 1 analyze  globals.md + components.md · lint --globals/--components → LINT OK
- [ ] 2 plan     plandata/ → plan-<P>-<slug>.md · lint → LINT OK · kontrast geçti · §1 ve §6.2 kullanıcıya gösterildi
- [ ] 3 build    ds · subs · sections n/N · pages · overlays · motion  (her birim: CHK PASS + 1 ekran görüntüsü + build-log satırı)
- [ ] 4 verify   verify-report.md · CHK all PASS ya da gerekçeli istisna
- [ ] 5 handoff  port-manifest.json/.md + globals-runbook.md · açık sorular listelendi
```

## Anti-patterns (the brief always wins; see `references/08-quality.md`)

Card around everything · gradients, shadows and large radii as defaults · centred hero + three feature cards · Inter/Roboto because nothing was chosen · emoji or hand-drawn icons · English or lorem filler and fake stats · every section at the same rhythm. Spend boldness in one place per page and name it in plan §1.

## Reporting

Report in Turkish. After each phase: what was written (paths), gate result (quote the `LINT`/`SUMMARY` line), exceptions, and the next command. Never claim a check passed without its output line.
