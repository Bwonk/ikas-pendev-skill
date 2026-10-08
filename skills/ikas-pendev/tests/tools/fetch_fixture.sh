#!/usr/bin/env bash
# Regenerates the offline analyze_site fixture. The snapshot is a third-party page and is NOT committed;
# run this once locally before `tests/run.sh` if you want the analyze_site regression.
set -eu
HERE="$(cd "$(dirname "$0")" && pwd)"; FX="$HERE/../fixtures/site"; mkdir -p "$FX"
URL="${1:-https://axm.framer.website/}"
python3 - "$URL" "$FX/axm-snapshot.html" <<'PY'
import sys,re,urllib.request
url,out=sys.argv[1],sys.argv[2]
req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
html=urllib.request.urlopen(req,timeout=30).read(5_000_000).decode("utf-8","replace")
html=re.sub(r"<script\b[^>]*>.*?</script>","",html,flags=re.S|re.I)
open(out,"w",encoding="utf-8").write(html); print("wrote",out,len(html))
PY
echo "Note: axm-motion.excerpt.js (JS-only easing/spring excerpts) is kept in git; regenerate by hand if the site changes."
