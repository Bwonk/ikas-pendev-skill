
## 8. Aktarım sonrası: animasyon üretimi

Tasarım ikas'a aktarıldıktan (statik hali çalışır olduktan) sonra bu bölüm uygulanır.

**1) Hedefleri topla.** Bu dosyadaki tüm `anim-targets` bloklarını tek listeye çıkar:

```bash
python3 - <<'EOF'
import re, sys
src = open("docs/pendev/{{file}}", encoding="utf-8").read()
blocks = re.findall(r"<!-- anim-targets:start -->\s*```yaml\n(.*?)```", src, re.S)
items = re.split(r"\n(?=- id: )", "\n".join(blocks).strip())
for it in items:
    get = lambda k: (re.search(r"^\s*-?\s*%s: (.*)$" % k, it, re.M) or [None, ""])[1]
    print(get("id"), get("section"), get("layer"), get("recipe"), get("impl"), sep=" | ")
EOF
```

**2) Tasarımla karşılaştır.** pen.dev'de işaretli katmanları listele; iki liste aynı `id`'leri içermeli:

```js
Get(n => n.metadata && n.metadata.anim ? Print(n.metadata.anim, "|", n.name, "|", n.metadata.recipe) : undefined)
```
{{#contextScan}}

pen.dev, bileşen instance'larında ve override'larında `metadata` saklamaz; bu hedeflerin `id`'si katmanın `context` alanında durur. Sadece `metadata.anim` okunursa instance hedefleri listeden düşer, o yüzden `context` da taranır:

```js
Get(n => n.context && /{{prefix}}-[A-Z]{2,}-\d\d/.test(n.context) ? Print(n.context.match(/{{prefix}}-[A-Z]{2,}-\d\d/g).join(","), "|", n.name, "| context") : undefined)
```

İki çıktının birleşimi 7. bölümdeki listeyle karşılaştırılır.
{{/contextScan}}

**3) Ortak parçaları bir kez yaz** (`{{codeDir}}` altında):

| Parça | Yer | Hangi hedefler |
|---|---|---|
| Motion custom property'leri (`--ease-*`, `--dur-*`) | `src/global.css` | hepsi |
| `useInView(ref, {threshold, once})` | `src/utils/motion/useInView.ts` | `impl` içinde `io-hook` |
| `useScrollProgress(ref)` → CSS değişkeni | `src/utils/motion/useScrollProgress.ts` | `impl` içinde `scroll-scrub` |
| `splitWords(el)` + AnimeJS stagger | `src/utils/motion/revealWords.ts` | M-03 |
| {{via_components}} | `src/sub-components/<Ad>/` | `via` alanı dolu olan hedefler (animasyon bileşenin içinde, bölümde tekrar yazılmaz) |
{{utils_rows}}
**4) Bölüm bölüm uygula.** Her bölüm için sıra: `layout` (sticky) → `css-transition` → `css-keyframes` → `io-hook` → `animejs` → `scroll-scrub`. Her hedefte:
- `layer` = CSS sınıfı; durum sınıfları `is-inview`, `is-active`, `is-open`, `is-loading`.
- `from` / `to` / `timing` değerleri doğrudan kullanılır; token adları (`spring-soft`, `ease-inout`…) `globals.md` §7.1'den.
- `mobile` alanı medya sorgusuna (`@media (max-width: bp(<mobileId>))`), `reducedMotion` alanı `@media (prefers-reduced-motion: reduce)` bloğuna çevrilir.
- SSR çıktısı bitiş halini gösterir; başlangıç hali JS yüklenince eklenen sınıfla verilir.
- Tarayıcı API'leri sadece `useEffect` içinde. AnimeJS: `import { AnimeJS } from "@ikas/bp-storefront"`.
- Bileşen `styles.css` içindeki `@keyframes` adı o bileşene özeldir; birden çok bileşen aynı keyframe'i kullanacaksa `create_theme_global` (kind `keyframe`) ile tema keyframe'i aç.

**5) Doğrula ve işaretle.** `npx ikas-component check --json` → `npx ikas-component build` → editörde 1440 ve 390 genişlikte, ayrıca "hareketi azalt" açıkken kontrol. Tamamlanan hedefte `done: false` → `done: true`.

**Önerilen sıra (etki / emek):** `via` bileşenleri (her yerde görünür) → Header → ana sayfa bölümleri → ProductList / ProductDetail → overlay'ler → içerik sayfaları → scroll-scrub olanlar.

