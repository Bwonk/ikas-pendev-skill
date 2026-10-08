#!/usr/bin/env bash
# Regression tests for the ikas-pendev skill scripts. Stdlib Python only.
# Usage: bash tests/run.sh [--gizem /path/to/gizem-theme/docs]
#   Without --gizem, the byte-exact plan regression is checked against tests/expected/plan-C.sha256.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SK="$(cd "$HERE/.." && pwd)"
S="$SK/scripts"; EX="$SK/examples/gizem"; FX="$HERE/fixtures"; EXP="$HERE/expected"
OUT="$HERE/out"; mkdir -p "$OUT"
GIZEM=""
[ "${1:-}" = "--gizem" ] && GIZEM="$2"
pass=0; fail=0
ok()   { pass=$((pass+1)); echo "PASS  $1"; }
bad()  { fail=$((fail+1)); echo "FAIL  $1"; [ -n "${2:-}" ] && echo "      $2"; }

# 1. gen_plan: contract-1 reproduction of plan-C (byte-exact)
python3 "$S/gen_plan.py" "$EX/plandata.json" --stdout > "$OUT/plan-C.md" 2>"$OUT/gen-C.log" || bad "gen_plan C renders" "$(cat "$OUT/gen-C.log")"
if [ -n "$GIZEM" ]; then
  if diff -q "$OUT/plan-C.md" "$GIZEM/pendev/plan-C-serbest-yorum.md" >/dev/null; then ok "gen_plan C byte-exact vs gizem"; else bad "gen_plan C byte-exact vs gizem" "$(diff "$OUT/plan-C.md" "$GIZEM/pendev/plan-C-serbest-yorum.md" | head -5)"; fi
else
  want="$(cat "$EXP/plan-C.sha256" | cut -d' ' -f1)"; got="$(shasum -a 256 "$OUT/plan-C.md" | cut -d' ' -f1)"
  [ "$want" = "$got" ] && ok "gen_plan C sha256" || bad "gen_plan C sha256" "want $want got $got"
fi
grep -q "ikas-pendev contract" "$OUT/plan-C.md" && bad "contract-1 output has no marker" || ok "contract-1 output has no marker"

# 2. gen_plan: contract-1 reproduction of plan-A (only with --gizem)
if [ -n "$GIZEM" ] && [ -f "$FX/gizem-A.plandata.json" ]; then
  python3 "$S/gen_plan.py" "$FX/gizem-A.plandata.json" --stdout > "$OUT/plan-A.md" 2>/dev/null
  diff -q "$OUT/plan-A.md" "$GIZEM/pendev/plan-A-ayni-iskelet-yeni-kimlik.md" >/dev/null && ok "gen_plan A byte-exact vs gizem" || bad "gen_plan A byte-exact vs gizem"
fi

# 3. gen_plan: contract-2 mini dataset renders with marker
python3 "$S/gen_plan.py" "$FX/mini-plandata" --stdout > "$OUT/plan-mini.md" 2>"$OUT/gen-mini.log" && ok "gen_plan mini renders" || bad "gen_plan mini renders" "$(cat "$OUT/gen-mini.log")"
sed -n 2p "$OUT/plan-mini.md" | grep -q "ikas-pendev contract:2" && ok "mini has contract-2 marker on line 2" || bad "mini has contract-2 marker on line 2"

# 4. lint: plan-C passes with globals; mini passes; broken fails with snapshot
python3 "$S/lint_plan.py" "$OUT/plan-C.md" --globals "$EX/globals.md" > "$OUT/lint-C.txt" 2>&1 && ok "lint plan-C OK" || bad "lint plan-C OK" "$(tail -3 "$OUT/lint-C.txt")"
grep -q "LINT OK (115 targets)" "$OUT/lint-C.txt" && ok "lint plan-C counts 115 targets" || bad "lint plan-C counts 115 targets" "$(tail -1 "$OUT/lint-C.txt")"
python3 "$S/lint_plan.py" "$OUT/plan-mini.md" > "$OUT/lint-mini.txt" 2>&1 && ok "lint mini OK" || bad "lint mini OK" "$(grep ERROR "$OUT/lint-mini.txt" | head -5)"
python3 "$S/lint_plan.py" "$FX/broken-plan.md" > "$OUT/lint-broken.txt" 2>&1 && bad "lint broken-plan fails" || ok "lint broken-plan fails"
if [ -f "$EXP/lint-broken.txt" ]; then diff -q "$OUT/lint-broken.txt" "$EXP/lint-broken.txt" >/dev/null && ok "lint broken snapshot" || bad "lint broken snapshot" "$(diff "$OUT/lint-broken.txt" "$EXP/lint-broken.txt" | head -5)"; fi
python3 "$S/lint_plan.py" --globals "$EX/globals.md" --components "$EX/components.md" > "$OUT/lint-phase1.txt" 2>&1 && ok "lint phase-1 gate on gizem docs" || bad "lint phase-1 gate on gizem docs" "$(grep ERROR "$OUT/lint-phase1.txt" | head -5)"
python3 "$S/lint_plan.py" --globals "$FX/broken-globals.md" --components "$FX/broken-components.md" > "$OUT/lint-broken-phase1.txt" 2>&1 && bad "lint broken phase-1 fails" || ok "lint broken phase-1 fails"
if [ -f "$EXP/lint-broken-phase1.txt" ]; then diff -q "$OUT/lint-broken-phase1.txt" "$EXP/lint-broken-phase1.txt" >/dev/null && ok "lint broken phase-1 snapshot" || bad "lint broken phase-1 snapshot" "$(diff "$OUT/lint-broken-phase1.txt" "$EXP/lint-broken-phase1.txt" | head -5)"; fi

# 5. extract_targets
n="$(python3 "$S/extract_targets.py" "$OUT/plan-C.md" --format ids | sort -u | wc -l | tr -d ' ')"
[ "$n" = "115" ] && ok "extract ids = 115" || bad "extract ids = 115" "got $n"
python3 "$S/extract_targets.py" "$OUT/plan-C.md" --format tsv > "$OUT/targets-C.tsv"
diff -q "$OUT/targets-C.tsv" "$EXP/targets-C.tsv" >/dev/null && ok "extract tsv snapshot" || bad "extract tsv snapshot"
python3 "$S/extract_targets.py" "$OUT/plan-C.md" --js all > "$OUT/checks-all.js" && ok "extract --js all renders" || bad "extract --js all renders"
grep -q "__" "$OUT/checks-all.js" && bad "checks js has no unfilled placeholders" "$(grep -o '__[A-Z]*__' "$OUT/checks-all.js" | sort -u | tr '\n' ' ')" || ok "checks js has no unfilled placeholders"
if command -v node >/dev/null; then node --check "$OUT/checks-all.js" 2>"$OUT/node.log" && ok "checks js parses (node --check)" || bad "checks js parses (node --check)" "$(head -3 "$OUT/node.log")"; fi

# 6. analyze_site on offline fixture
if [ -d "$FX/site" ]; then
  python3 -I "$S/analyze_site.py" --fixture "$FX/site" > "$OUT/analyze-axm.txt" 2>"$OUT/analyze.log" && ok "analyze_site fixture runs" || bad "analyze_site fixture runs" "$(tail -3 "$OUT/analyze.log")"
  for v in "#7A7A7A" "#1C1C1C"; do grep -qi "$v" "$OUT/analyze-axm.txt" && ok "analyze finds $v" || bad "analyze finds $v"; done
  diff -q "$OUT/analyze-axm.txt" "$EXP/analyze-axm.txt" >/dev/null && ok "analyze snapshot" || bad "analyze snapshot" "$(diff "$OUT/analyze-axm.txt" "$EXP/analyze-axm.txt" | head -5)"
else
  echo "SKIP  analyze_site fixture (tests/fixtures/site missing; run tests/tools/fetch_fixture.sh)"
fi

# 7. build_manifest on the synthetic gizem canvas dump
python3 "$S/build_manifest.py" --plandata "$EX/plandata.json" --plan "$OUT/plan-C.md" --dump "$FX/gizem-canvas-dump.txt" -o "$OUT/port" > "$OUT/manifest.log" 2>&1 && ok "build_manifest gizem exit 0" || bad "build_manifest gizem exit 0" "$(tail -3 "$OUT/manifest.log")"
tail -1 "$OUT/manifest.log" | diff -q - "$EXP/manifest-gizem.txt" >/dev/null && ok "build_manifest summary snapshot" || bad "build_manifest summary snapshot" "$(tail -1 "$OUT/manifest.log")"
grep -v '^ROOT|C/Section/Timeline@' "$FX/gizem-canvas-dump.txt" | sed -E 's/C-PDP-03;?//' > "$OUT/gizem-canvas-dump-broken.txt"
python3 "$S/build_manifest.py" --plandata "$EX/plandata.json" --plan "$OUT/plan-C.md" --dump "$OUT/gizem-canvas-dump-broken.txt" -o "$OUT/port-broken" > "$OUT/manifest-broken.log" 2>&1 && bad "build_manifest broken dump exits 1" || ok "build_manifest broken dump exits 1"
nb="$(grep -c '|BLOCKING$' "$OUT/manifest-broken.log" | tr -d ' ')"; [ "$nb" = "2" ] && ok "build_manifest broken dump has 2 blocking" || bad "build_manifest broken dump has 2 blocking" "got $nb"

echo "----"; echo "passed=$pass failed=$fail"
[ "$fail" = "0" ]
