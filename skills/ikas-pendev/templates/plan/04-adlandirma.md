
## 4. Adlandırma ve metadata sözleşmesi

Amaç: tasarımdan koda çeviri mekanik olsun.

| pen.dev | ikas / kod |
|---|---|
| Kök frame `{{prefix}}/Section/HeroSlider@desktop` | section bileşeni **HeroSlider** (`src/components/HeroSlider/`) |
| Kök frame `{{prefix}}/Sub/ProductCard` | sub-component **ProductCard** (`src/sub-components/ProductCard/`) |
| Kök frame `{{prefix}}/Overlay/CartDrawer…` | ilgili section'ın alt bileşeni |
| Katman adı `hero-title` (kebab-case) | CSS sınıfı `.hero-title` |
| `ref` instance adı = bileşen adı (`ProductCard`) | JSX `<ProductCard />` |
| Metin katmanı + `metadata.prop` | TEXT prop (JSX'te sabit metin olmaz) |
| Görsel dolgulu frame + `metadata.prop` | IMAGE / PRODUCT / CATEGORY prop |
| Tekrarlanan çocuk grubu + `metadata.prop` | COMPONENT_LIST ya da *_LIST prop |
{{#c2}}
| Metin katmanı + `metadata.textClass: "data"` + `source` | mağaza verisi (ör. `product.name`); prop değil, JSX'te veri bağlamasıdır |
| Metin katmanı + `metadata.textClass: "code"` | kodda üretilen metin (sayaç, biçimli tutar, durum etiketi) |
| Section kök frame'i + `prop: "backgroundColor"` | her section'da zorunlu `backgroundColor` COLOR prop'u |
{{/c2}}
| `metadata.anim` | 7. bölümdeki animasyon hedefi |

Katman ağaçlarındaki `{ad:TİP}` notasyonu o katmanın `metadata.prop` ve `metadata.propType` değeridir.{{#c2}} `{data:kaynak}` metnin mağaza verisinden geldiğini (`textClass: "data"`, `source: "kaynak"`), `{code:ad}` metnin kodda üretildiğini (`textClass: "code"`) gösterir. Ağaçta tırnak içinde yazılan her örnek metin bu üç işaretten birini taşır; işaretsiz sabit metin yoktur.{{/c2}}

**Metadata (düz anahtarlar; iç içe nesne kullanma):**

```js
// kök frame
metadata: {type:"{{slug}}", role:"section", ikas:"HeroSlider", device:"desktop", variant:"{{prefix}}"{{#c2}}, contract:2, prop:"backgroundColor", propType:"COLOR"{{/c2}}}
// role: "ds" | "sub" | "section" | "overlay" | "page" | "motion"

// prop'a bağlı katman
metadata: {type:"{{slug}}", role:"prop", prop:"title", propType:"TEXT"{{#c2}}, textClass:"prop"{{/c2}}}
{{#c2}}

// mağaza verisi gösteren metin (prop değil)
metadata: {type:"{{slug}}", textClass:"data", source:"product.name"}

// kodda üretilen metin
metadata: {type:"{{slug}}", textClass:"code"}
{{/c2}}

// animasyonlu katman (prop'a da bağlıysa aynı nesnede)
metadata: {type:"{{slug}}", role:"anim", anim:"{{prefix}}-HERO-02", recipe:"M-07", trigger:"state-change", prop:"title", propType:"TEXT"{{#c2}}, textClass:"prop"{{/c2}}}
context: "{{prefix}}-HERO-02 · M-07 · başlık slaytla birlikte değişir"
```

- Bir katmanda birden çok hedef varsa `anim` virgülle ayrılır: `"{{prefix}}-HERO-01,{{prefix}}-HERO-07"`.
{{^c2}}
- `context` insan için kısa açıklamadır; makine `metadata` okur.
- Bileşenin içindeki katmana verilen metadata instance'lara taşınır; her instance'a yeniden yazılmaz.
{{/c2}}
{{#c2}}
- `context` hem insan için kısa açıklamadır hem de katmandaki **tüm** anim id'lerini içermek zorundadır. pen.dev instance ve override'larda `metadata` saklamaz; makine `metadata.anim` ∪ `context` okur.
- Metadata yalnızca node **oluşturulurken** güvenle yazılır. Sonradan değişecekse yeni node eklenir, eskisi silinir.
- Her metin node'unda `textClass` zorunludur: `"prop"` → `prop` + `propType`; `"data"` → `source`; `"code"` → ek alan yok.
- Section kök frame'leri `prop: "backgroundColor"`, `propType: "COLOR"` taşır; kök `contract: 2` yazar.
{{/c2}}

