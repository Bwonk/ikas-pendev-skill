# Plan A — Aynı iskelet, yeni kimlik

Tema: **Gizem** (streetwear) · Hedef: pen.dev canvas → ikas Code Components · Referans: https://axm.framer.website/

Referansın grid sistemi, bölüm sırası ve hareket dili korunur; renk, tipografi, görsel dili ve metinler Gizem'e özgüdür.

## 0. Bu dosya nasıl kullanılır

Bu dosya pen.dev'de tasarım üretecek ajana (ya da tasarımcıya) verilen **tek başına yeterli** brifdir. Ölçülerin kaynağı ve motion tariflerinin ayrıntısı için `docs/referans/globals.md`, prop listeleri için `docs/referans/components.md`.

**Sıra:** 3 → 6.0 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5. Her adımın sonunda o adımın kontrol listesi ve ekran görüntüsü.

**Nereye çizilir:** tercihen bu varyant için yeni bir .pen dosyası (`gizem-A.pen`). Aynı dosyada çalışılacaksa tüm kök frame adları `A/` ile başlar ve `FindEmptySpace` ile boş alana yerleştirilir. Dosyadaki `axm.framer.website` adlı 8 frame referansın ham import'udur: **sadece bakmak için**; içinden katman kopyalanmaz, silinmez, değiştirilmez.

**Ajan için hazır komutlar** (sırayla, her biri ayrı tur):
1. `docs/pendev/plan-A-ayni-iskelet-yeni-kimlik.md dosyasını oku. 3. bölümdeki değişkenleri tanımla ve 6.0'daki Design System frame'lerini üret.`
2. `Aynı planın 6.1 bölümündeki bileşenleri, durumlarıyla birlikte üret.`
3. `6.2'den <bölüm adı> bölümünü desktop ve mobil olarak üret; katman adları ve metadata plandaki gibi olsun.` (bölüm bölüm tekrarla)
4. `6.3'teki sayfaları section instance'larından kur.`
5. `6.4 overlay'lerini ve 6.5 Motion States karelerini üret.`
6. `9. bölümdeki bitiş kontrolünü çalıştır ve eksikleri raporla.`

## 1. Yön ve kimlik

**Marka:** GİZEM — streetwear. Ton: gece, beton, sessiz özgüven; az söz, büyük harf.
**Wordmark:** `GİZEM` (font-display); kısa işaret `GZM`. Logo `Generate("svg")` ile üretilir, elle çizilmez.

**Referanstan farklar (iskelet aynı, yüz farklı):**
- Zemin saf siyah değil, sıcak mürekkep siyahı; metin kemik beyazı. Çizgiler referanstaki açık gri yerine koyu (`$color-line`), ızgara daha sakin.
- Tek vurgu rengi: **volt** `$color-accent`. Sadece şuralarda: SALE rozeti, hotspot iç noktası, `progress-bar`, aktif sekme altındaki 2px çizgi, sepet sayısı kutusu, odak (focus) çerçevesi. Buton dolgusunda **kullanılmaz** (butonlar kemik beyazı kalır).
- Başlıklar `Anton` (ağır, dar); arayüz `Barlow Condensed`; kategori etiketi, tarih, breadcrumb ve ürün kodu gibi küçük bilgiler `JetBrains Mono` (teknik etiket hissi).
- Görsel dili: sert flaş, düşük doygunluk, beton / otopark / gece sokağı; ürün çekimleri koyu zeminde; her sahnede en fazla bir renkli obje. Referansın görselleri **kullanılmaz**; `Generate("ai" | "stock")` ile özgün üretilir.
- Metinler Türkçe, büyük harf. Font seçerken `İ Ş Ğ Ü Ö Ç` karakterlerini kontrol et.

**Örnek içerik:** nav `MAĞAZA · HAKKINDA · JOURNAL · İLETİŞİM` · duyurular `750 TL ÜZERİ ÜCRETSİZ KARGO` / `30 GÜN İÇİNDE ÜCRETSİZ İADE` / `İLK SİPARİŞE %10` · hero `GECE VARDİYASI`, `SOKAĞIN SESİ`, `İKİ MEVSİM ARASI` · bölümler `YENİ GELENLER`, `ÇOK SATANLAR`, `KOLEKSİYONLARI KEŞFET`, `GİZEM'İ TAKİP ET`, `JOURNAL'DAN` · butonlar `ALIŞVERİŞE BAŞLA ↗`, `SEPETE EKLE`, `HEPSİNİ GÖR ↗`, `YAZIYI OKU ↗` · footer `KENDİ YOLUNDA YÜRÜ.` · ürünler `GECE OVERSIZE HOODIE — 1.850 TL`, `ASFALT GRAFİK TİŞÖRT — 850 TL`, `SİS KARGO PANTOLON — 1.650 TL`, `SİNYAL RÜZGARLIK — 2.250 TL`.

## 2. Canvas organizasyonu

Her şey **ayrı kök frame**. Kök frame adları sabit kalıpta; ikas'a aktarımda bu adlardan bileşen listesi çıkarılır.

| Sıra (yukarıdan aşağı) | Kök frame adı | İçerik | Boyut |
|---|---|---|---|
| 00 | `A/DS/Colors`, `A/DS/Typography`, `A/DS/Spacing`, `A/DS/Icons`, `A/DS/Motion` | Design system sayfaları | serbest |
| 01 | `A/Sub/<Ad>` (reusable) ve `A/Sub/<Ad> — <durum>` | Bileşenler ve durumları | içeriğe göre |
| 02 | `A/Section/<Ad>@desktop` ve `A/Section/<Ad>@mobile` (ikisi de reusable) | Bölümler | 1440 / 390 genişlik |
| 03 | `A/Page/<Ad>@desktop` ve `A/Page/<Ad>@mobile` | Sayfalar (section instance'ları) | 1440 / 390 |
| 04 | `A/Overlay/<Ad>@desktop — <durum>` ve `…@mobile — <durum>` | Menü, sepet, arama, paneller | 1440×900 / 390×844 |
| 05 | `A/Motion/<tarif> <bölüm>` | Animasyon kareleri (başlangıç / ara / bitiş) | içeriğe göre |

Yerleşim: her sıra bir yatay bant; bantlar arası 800, frame'ler arası 200 boşluk. Bir bölümün desktop ve mobil frame'i **yan yana**. Kök seviyede metin, ikon ya da serbest şekil bırakılmaz; açıklamalar `note` node'u olarak ilgili frame'in yanına konur.

Kurallar:
- Desktop kök frame'lerinde `theme: {device: "desktop"}`, mobil olanlarda `theme: {device: "mobile"}`. Boyut değişkenleri buna göre kendiliğinden değişir; mobil frame'de ayrıca sayı yazılmaz.
- Bölüm frame'leri `layout: "vertical"` ya da `"horizontal"`, `clip: true`. `layout: "none"` sadece gerçekten üst üste binen katmanlarda (slaytlar, görsel + gradyan + metin, hotspot).
- Tekrarlanan her şey `reusable` bileşenin `ref` instance'ıdır (ProductCard, Button, ArrowLink…). Sayfalar yalnızca section `ref`'lerinden oluşur.
- Çalışılan kök frame `placeholder: true`; bitince kaldırılır.
- Değer yazarken sayı yerine değişken: renk, font, yazı boyutu, boşluk hep `$…`.

## 3. Değişkenler

İlk iş olarak tanımlanır. Adlar üç planda aynıdır (`globals.md` ile eşleşir); değerler bu varyanta özgüdür.

```js
SetVariables({
  "color-bg": {type:"color", value:"#0A0A0B"},
  "color-text": {type:"color", value:"#F2EFE9"},
  "color-muted": {type:"color", value:"#8C8A85"},
  "color-line": {type:"color", value:"#3A3A3C"},
  "color-surface": {type:"color", value:"#161617"},
  "color-inverse-bg": {type:"color", value:"#F2EFE9"},
  "color-inverse-text": {type:"color", value:"#0A0A0B"},
  "color-accent": {type:"color", value:"#C8FF2E"},
  "color-accent-text": {type:"color", value:"#0A0A0B"},
  "color-scrim": {type:"color", value:"#0A0A0BB3"},
  "font-display": {type:"string", value:"Anton"},
  "font-ui": {type:"string", value:"Barlow Condensed"},
  "font-body": {type:"string", value:"Barlow"},
  "font-price": {type:"string", value:"Barlow Condensed"},
  "font-mono": {type:"string", value:"JetBrains Mono"},
  "text-display": {type:"number", value:[{value:104, theme:{device:"desktop"}}, {value:44, theme:{device:"mobile"}}]},
  "text-h2": {type:"number", value:[{value:84, theme:{device:"desktop"}}, {value:36, theme:{device:"mobile"}}]},
  "text-h3": {type:"number", value:[{value:56, theme:{device:"desktop"}}, {value:32, theme:{device:"mobile"}}]},
  "text-h4": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:24, theme:{device:"mobile"}}]},
  "text-title": {type:"number", value:[{value:24, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "text-ui": {type:"number", value:[{value:20, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "text-ui-sm": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:14, theme:{device:"mobile"}}]},
  "text-badge": {type:"number", value:[{value:14, theme:{device:"desktop"}}, {value:12, theme:{device:"mobile"}}]},
  "text-label": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-body": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:15, theme:{device:"mobile"}}]},
  "text-price": {type:"number", value:[{value:24, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "space-page": {type:"number", value:[{value:20, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-grid": {type:"number", value:[{value:5, theme:{device:"desktop"}}, {value:4, theme:{device:"mobile"}}]},
  "space-card": {type:"number", value:10},
  "space-panel": {type:"number", value:[{value:20, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-xs": {type:"number", value:5},
  "space-sm": {type:"number", value:10},
  "space-md": {type:"number", value:[{value:15, theme:{device:"desktop"}}, {value:12, theme:{device:"mobile"}}]},
  "space-section": {type:"number", value:[{value:100, theme:{device:"desktop"}}, {value:60, theme:{device:"mobile"}}]},
  "size-header": {type:"number", value:[{value:60, theme:{device:"desktop"}}, {value:56, theme:{device:"mobile"}}]},
  "size-line": {type:"number", value:1},
  "opacity-inactive": {type:"number", value:0.3},
})
```

Font doğrulama: `execute` yanıtında "Font family … is invalid" uyarısı çıkarsa o değişkeni değiştir. Canvas üzerinde denenip geçerli çıkan aileler: `Anton`, `Antonio`, `Archivo Narrow`, `Barlow`, `Barlow Condensed`, `Bebas Neue`, `JetBrains Mono`, `Mona Sans`, `Oswald`, `Sofia Sans Extra Condensed`, `Space Mono`. Geçersiz çıkanlar: `Mona Sans Condensed`, `Big Shoulders Display`.

Yazı stili eşlemesi: `text-display`, `text-h2`, `text-h3`, `text-h4` → `$font-display`, satır yüksekliği 0.9–1.0 · `text-title`, `text-ui`, `text-ui-sm`, `text-badge` → `$font-ui`, 700, satır 1.1 · `text-label` → `$font-mono` · `text-body` → `$font-body`, 500, satır 1.35 · `text-price` → `$font-price`, 700. Hepsi büyük harf (gövde metni hariç).

## 4. Adlandırma ve metadata sözleşmesi

Amaç: tasarımdan koda çeviri mekanik olsun.

| pen.dev | ikas / kod |
|---|---|
| Kök frame `A/Section/HeroSlider@desktop` | section bileşeni **HeroSlider** (`src/components/HeroSlider/`) |
| Kök frame `A/Sub/ProductCard` | sub-component **ProductCard** (`src/sub-components/ProductCard/`) |
| Kök frame `A/Overlay/CartDrawer…` | ilgili section'ın alt bileşeni |
| Katman adı `hero-title` (kebab-case) | CSS sınıfı `.hero-title` |
| `ref` instance adı = bileşen adı (`ProductCard`) | JSX `<ProductCard />` |
| Metin katmanı + `metadata.prop` | TEXT prop (JSX'te sabit metin olmaz) |
| Görsel dolgulu frame + `metadata.prop` | IMAGE / PRODUCT / CATEGORY prop |
| Tekrarlanan çocuk grubu + `metadata.prop` | COMPONENT_LIST ya da *_LIST prop |
| `metadata.anim` | 7. bölümdeki animasyon hedefi |

Katman ağaçlarındaki `{ad:TİP}` notasyonu o katmanın `metadata.prop` ve `metadata.propType` değeridir.

**Metadata (düz anahtarlar; iç içe nesne kullanma):**

```js
// kök frame
metadata: {type:"gizem", role:"section", ikas:"HeroSlider", device:"desktop", variant:"A"}
// role: "ds" | "sub" | "section" | "overlay" | "page" | "motion"

// prop'a bağlı katman
metadata: {type:"gizem", role:"prop", prop:"title", propType:"TEXT"}

// animasyonlu katman (prop'a da bağlıysa aynı nesnede)
metadata: {type:"gizem", role:"anim", anim:"A-HERO-02", recipe:"M-07", trigger:"state-change", prop:"title", propType:"TEXT"}
context: "A-HERO-02 · M-07 · başlık slaytla birlikte değişir"
```

- Bir katmanda birden çok hedef varsa `anim` virgülle ayrılır: `"A-HERO-01,A-HERO-07"`.
- `context` insan için kısa açıklamadır; makine `metadata` okur.
- Bileşenin içindeki katmana verilen metadata instance'lara taşınır; her instance'a yeniden yazılmaz.

## 5. Animasyona hazır tasarım kuralları

pen.dev hareket göstermez. Aşağıdaki yapılar çizilmezse aktarımda katmanları yeniden kurmak gerekir.

1. **Bitiş hali çizilir.** Bölüm ve sayfa frame'leri animasyon bittikten sonraki görünümü gösterir. Başlangıç ve ara haller sadece `A/Motion/…` frame'lerinde.
2. **Maske = `clip: true` frame.** Kayarak giren her metin satırı kendi `…-mask` frame'inin içindedir; maske metinle aynı boyutta. Çok satırlı başlıkta her satır ayrı metin node'u ve ayrı maske.
3. **Roll eden öğeler çift kopyadır.** Buton, nav linki ve ok ikonunda `top` (görünen) ve `bottom` (maske dışında bekleyen) kopyaları birlikte çizilir; kap `clip: true`.
4. **Sonsuz kayanlar track + kopya.** `marquee` / `ticker` kabı `clip: true`; içindeki `…-track` içerik setini en az iki kez barındırır ve kabın dışına taşar.
5. **Yer değiştirenler kardeş frame.** Slaytlar, sekme içerikleri, ön/arka ürün görseli aynı ebeveynde üst üste (`layout: "none"`); görünmeyenler `opacity: 0` ile durur, silinmez.
6. **İlerleme göstergesi ayrı katman.** `progress-bar` dolgusu ebeveyninden ayrı bir dikdörtgen; yarı dolu çizilir.
7. **Sticky alanlar gerçek yükseklikte.** Sabit kalan öğenin kabı, kaydırma boyunca kat edeceği yükseklikte çizilir (ör. 4 görsellik galeri yanında tek detay sütunu).
8. **Overlay ayrı frame.** Menü, çekmece, arama: `scrim` + panel, sayfa frame'inin kopyası üzerinde değil, kendi kök frame'inde; açık ve boş/dolu halleri ayrı.
9. **Kaydırmaya bağlı öğeler serbest katman.** Dönen/kayan görsel ya da parallax arka plan, akıştan bağımsız (`layoutPosition: "absolute"`) ve kabından büyük çizilir.
10. **Hover hali ayrı frame.** Her etkileşimli bileşenin hover hali `A/Sub/<Ad> — hover` olarak çizilir; bölüm içinde tekrar çizilmez.
11. **Her hedef işaretli.** 6. bölümde `anim-targets` bloğunda geçen her `layer`, tasarımda aynı adla bulunur ve `metadata.anim` taşır.
12. **Mobil hali kararlaştırılmış.** Hedefin `mobile` alanı "kapalı" ya da farklıysa mobil frame o hale göre çizilir (ör. sticky yok → normal akış).

## 6. Yapım sırası

### 6.0 Design System frame'leri

| Kök frame | İçerik |
|---|---|
| `A/DS/Colors` | Her renk değişkeni için örnek kare + ad + hex; metin/zemin kontrast çiftleri (metin, muted, vurgu üzerinde metin) |
| `A/DS/Typography` | 11 yazı stili, her biri desktop ve mobil boyutunda örnek satırla (Türkçe karakterli: "GÖLGE İÇİNDE ŞIK ÇÖZÜM 1.850 TL") |
| `A/DS/Spacing` | Boşluk ölçeği çubukları; 1440 ve 390 için ızgara şeması (kenar boşluğu, sütunlar, aralık); çizgi kalınlığı |
| `A/DS/Icons` | Kullanılan tüm ikonlar 20×20 (arama, hesap, sepet, menü, kapat, ok ↗, caret, artı, eksi, onay) + logo ve işaret |
| `A/DS/Motion` | Kullanılan tarif ID'leri, kısa açıklama ve tetikleyici simgeleri; `note` node'ları ile. Bu frame animasyon "lejantı"dır |

### 6.1 Bileşenler (`A/Sub/…`)

Her bileşen `reusable` kök frame; durumlar yanında ayrı frame. Önce bunlar, çünkü bölümler bunların instance'larını kullanır.

| Bileşen | Yapı | Durumlar (ayrı frame) |
|---|---|---|
| `ProductCard` | çerçeveli; `card-badges` (sol üst, boşluk $space-card) · `card-images` (clip, 4:3): `image-front` + `image-back` üst üste · `card-info` (boşluk $space-card): `card-category` text-label muted · `card-title` text-title · `card-price-row`: `price` + `price-compare` (üstü çizili, muted) + `card-arrow` (clip: `arrow-top` + `arrow-bottom`) | varsayılan · hover (arka görsel + ok dönmüş) · stok yok · indirimli · 3 genişlik: 429 / 478 / 370 (mobil) |
| `ProductCardSmall` | çerçeveli satır: görsel 100×110 (sağ çizgi) · `card-category` · `card-title` (text-ui) · `price` · `card-arrow` | varsayılan · hover |
| `BlogCard` | çerçeveli: `blog-card-image` (16:9, clip) · `blog-card-info` (boşluk $space-panel): `journal-date` text-label muted · `blog-card-title` text-h4 · `link` | varsayılan · hover |
| `Button` | `button` (clip) içinde `top` + `bottom` kopya; yükseklik 44 / 48; text-ui; türler: dolu (ters zemin), çerçeveli | varsayılan · hover · pasif · yükleniyor (spinner) |
| `ArrowLink` | `link`: etiket text-ui + `link-line` (1px, tam genişlik) + `link-arrow` (clip 20×20: `arrow-top` + `arrow-bottom`) | varsayılan · hover |
| `Badge` | zeminsiz text-badge; yan yana birden çok olabilir, aralık 10 | NEW · SALE · BEST SELLER |
| `Hotspot` | 48×48 dokunma alanı: `hotspot-outer` (halka) + `hotspot-inner` (nokta) + `hotspot-card` (ProductCardSmall, kapalıyken gizli) | kapalı · açık |
| `Marquee` | `marquee` (clip) → `marquee-track` → metin ×≥3 kopya | — |
| `Breadcrumbs` | text-label; linkler altı çizili, ayırıcı "/", son öğe muted | — |
| `Tabs` | `filter-tab` / `info-tab` / `anchor-link` ortak stili | aktif · pasif · hover |
| `VariantChip` | `variant-chip`: yükseklik 28, 1px çerçeve, yatay boşluk 20, normal genişlikte 13px yazı | seçili · pasif · hover · stok yok (üstü çizili) |
| `FormField` | `form-field`: yükseklik 48, 1px çerçeve, placeholder text-ui-sm muted; `form-textarea` 160 | boş · dolu · odak · hata (+ mesaj) · pasif |
| `Checkbox` | 12×12 kutu + text-label | işaretli · boş |
| `AccordionItem` | `faq-item`: `faq-question` satırı (yükseklik 44, alt çizgi) + `faq-icon` + `faq-answer` | açık · kapalı |
| `QuantitySelector` | eksi · adet · artı; çerçeveli, yükseklik 32 | varsayılan · alt sınır (eksi pasif) |
| `SectionHeading` | `section-heading`: `section-title-mask` → `section-title` (text-h2) + `section-description` + `link` (sağda) | açıklamalı · açıklamasız |
| `IconButton` | ikon 20, dokunma alanı 40×60; sol çizgi | varsayılan · hover |
| `Spinner` | 16 / 20 halka | — |

Bileşen animasyon hedefleri (bölümlerde `via` ile anılır, kodu bileşenin içinde yazılır):

<!-- anim-targets:start -->
```yaml
- id: A-CMP-01
  section: Sub/ProductCard
  layer: image-back
  recipe: M-09
  trigger: hover
  what: "Ön görsel arka görsele geçer"
  from: { front.opacity: 1, back.opacity: 0 }
  to: { front.opacity: 0, back.opacity: 1 }
  timing: { duration: 0.4, ease: ease-standard, arrow.spring: spring-soft }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
- id: A-CMP-02
  section: Sub/ProductCard
  layer: card-arrow
  recipe: M-10
  trigger: hover
  what: "Ok çapraz döner"
  from: { arrow: top }
  to: { arrow: bottom }
  timing: { spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
- id: A-CMP-03
  section: Sub/ProductCardSmall
  layer: card-arrow
  recipe: M-10
  trigger: hover
  what: "Ok çapraz döner"
  from: { arrow: top }
  to: { arrow: bottom }
  timing: { spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
- id: A-CMP-04
  section: Sub/BlogCard
  layer: blog-card-image
  recipe: M-09
  trigger: hover
  what: "Görsel hafif büyür"
  from: { scale: 1 }
  to: { scale: 1.04 }
  timing: { spring: spring-card }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
- id: A-CMP-05
  section: Sub/Button
  layer: button
  recipe: M-11
  trigger: hover
  what: "Dolgu alttan kayar, etiket yukarı çıkar"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-CMP-06
  section: Sub/ArrowLink
  layer: link
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
- id: A-CMP-07
  section: Sub/Hotspot
  layer: hotspot-outer
  recipe: M-12
  trigger: auto-loop
  what: "Halka nabız gibi atar"
  from: { outer.scale: 1, outer.opacity: 1 }
  to: { outer.scale: 2.2, outer.opacity: 0 }
  timing: { duration: 1.5, loop: true, card.spring: spring-soft }
  impl: css-keyframes + css-transition
  mobile: dokunmayla açılır
  reducedMotion: pulse durur
  done: false
- id: A-CMP-08
  section: Sub/Marquee
  layer: marquee-track
  recipe: M-14
  trigger: auto-loop
  what: "Metin kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: A-CMP-09
  section: Sub/Tabs
  layer: filter-tab
  recipe: M-28
  trigger: hover
  what: "Renk parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-CMP-10
  section: Sub/VariantChip
  layer: variant-chip
  recipe: M-28
  trigger: hover
  what: "Çerçeve ve metin parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-CMP-11
  section: Sub/AccordionItem
  layer: faq-answer
  recipe: M-22
  trigger: click
  what: "Cevap açılır, ikon döner"
  from: { height: 0, icon.rotate: 0 }
  to: { height: auto, icon.rotate: 45 }
  timing: { spring: "bounce 0, 0.5s" }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-CMP-12
  section: Sub/SectionHeading
  layer: section-title
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

### 6.2 Bölümler ve overlay'ler

Her başlık bir kök frame çiftidir (`@desktop` + `@mobile`). "ikas" satırı aktarımda başlanacak şablonu gösterir.

#### Section/Header
- **Kullanıldığı yer:** tüm sayfalar
- **ikas:** header-section (--isHeader)
- **Desktop:** Tam genişlik × 60; üst + alt çizgi; zemin `$color-bg`; sayfada en üstte sabit. Hücreler arası dikey çizgi.
- **Mobil:** Ayrı frame: `menu-button` (hamburger, 54×60, sağ çizgi) · `header-logo` ortada · `header-actions` sağda. `announcement-mask` ve `header-nav` yok (MobileMenu içinde).

```
header
├─ header-logo                       {logo:SVG}  yatay boşluk $space-page
├─ announcement-mask                 clip, esner
│   ├─ announcement-text             {text:TEXT}  görünen
│   └─ announcement-text (×2)        maske dışında, alt alta
├─ header-nav
│   ├─ nav-link (clip)  ×4           genişlik 132, sol çizgi
│   │   ├─ top                       etiket {label:LINK}, + caret (sadece Shop)
│   │   └─ bottom                    ters zemin + ters metin, maske dışında altta
│   └─ header-actions
│       ├─ search-button             ikon 20
│       ├─ account-button            ikon 20
│       └─ cart-button               ikon 20 + cart-count (ters zeminli sayı kutusu)
```

Kontrol: nav-link içinde top ve bottom kopyaları var · duyuru metinlerinin hepsi maske içinde çizili · ikon dokunma alanı ≥ 40×60

<!-- anim-targets:start -->
```yaml
- id: A-HDR-01
  section: Header
  layer: announcement-mask
  recipe: M-04
  trigger: auto-loop
  what: "Duyuru metinleri dikey kayarak döner"
  from: { y: 100% }
  to: { y: 0 }
  timing: { interval: 3, spring: spring-hover }
  impl: css-keyframes
  mobile: mobil menü içinde
  reducedMotion: ilk metin sabit
  done: false
- id: A-HDR-02
  section: Header
  layer: nav-link
  recipe: M-05
  trigger: hover
  what: "Ters dolgu alttan kayar, etiket yukarı çıkar"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: spring-hover }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-HDR-03
  section: Header
  layer: cart-count
  recipe: M-01
  trigger: state-change
  what: "Sepet sayısı değişince kısa zıplama"
  from: { scale: 1.4 }
  to: { scale: 1 }
  timing: { spring: spring-soft }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/Megamenu
- **Kullanıldığı yer:** Header (desktop)
- **ikas:** Header sub-component
- **Desktop:** Header altında tam genişlik × 354; alt çizgi; 3 eşit sütun, aralarında dikey çizgi. Arkadaki sayfa görünür kalır.
- **Mobil:** Mobilde yok; yerine MobileMenu içindeki akordeon.

```
megamenu
├─ megamenu-links                    boşluk $space-page, 2 kolon
│   └─ megamenu-column ×2
│       ├─ megamenu-column-title     {title:TEXT}  text-ui-sm muted
│       └─ megamenu-link ×N          {links:LIST_OF_LINK}  text-ui, satır aralığı 37
└─ megamenu-card ×2
    ├─ megamenu-card-image           {image:IMAGE}
    ├─ gradient-mask                 alttan siyah gradyan
    └─ megamenu-card-text            {title:TEXT} text-h4 + {subtitle:TEXT} text-ui-sm muted
```

Kontrol: açık hali ayrı overlay frame olarak çizildi · Shop nav-link açık durumda ters dolgulu

<!-- anim-targets:start -->
```yaml
- id: A-MEGA-01
  section: Megamenu
  layer: megamenu
  recipe: M-06
  trigger: hover | click
  what: "Panel header altından açılır; Shop caret döner"
  from: { clipHeight: 0, caret.rotate: 0 }
  to: { clipHeight: 100%, caret.rotate: 180 }
  timing: { spring: spring-soft, ease: ease-nav, duration: 0.4 }
  impl: css-transition
  mobile: akordeon
  reducedMotion: anında
  done: false
- id: A-MEGA-02
  section: Megamenu
  layer: megamenu-card-image
  recipe: M-09
  trigger: hover
  what: "Kart görseli hafif büyür"
  from: { scale: 1 }
  to: { scale: 1.05 }
  timing: { spring: spring-smooth }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
- id: A-MEGA-03
  section: Megamenu
  layer: megamenu-link
  recipe: M-28
  trigger: hover
  what: "Diğer linkler soluklaşır, üzerindeki parlak kalır"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/MobileMenu
- **Kullanıldığı yer:** Header (mobil)
- **ikas:** Header sub-component
- **Desktop:** Desktop karşılığı yok.
- **Mobil:** 390 × tam ekran, header altında. Hamburger çarpıya döner.

```
mobile-menu
├─ mobile-announcement               {text:TEXT} ortalı, alt çizgi, yükseklik 60
├─ mobile-nav-item ×4                text-h3, alt çizgi; Shop satırında caret
│   └─ mobile-submenu                (Shop açıkken) megamenu-link listesi
└─ mobile-secondary-links            text-ui muted
```

Kontrol: kapalı ve Shop-açık halleri ayrı çizildi

<!-- anim-targets:start -->
```yaml
- id: A-MMENU-01
  section: MobileMenu
  layer: mobile-menu
  recipe: M-20
  trigger: click
  what: "Menü yukarıdan/yandan açılır, satırlar sırayla girer"
  from: { y: -100%, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { spring: spring-drawer, scrim.duration: 0.4, rows.stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: css-transition + animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
- id: A-MMENU-02
  section: MobileMenu
  layer: mobile-submenu
  recipe: M-22
  trigger: click
  what: "Shop alt menüsü akordeon olarak açılır"
  from: { height: 0, icon.rotate: 0 }
  to: { height: auto, icon.rotate: 45 }
  timing: { spring: "bounce 0, 0.5s" }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/CartDrawer
- **Kullanıldığı yer:** Header
- **ikas:** Header sub-component (cart-patterns rehberi)
- **Desktop:** Sağdan 500 × tam yükseklik; sol çizgi; arkada `scrim` (koyu + blur).
- **Mobil:** 390 tam genişlik çekmece.

```
cart-overlay
├─ scrim
└─ cart-drawer
    ├─ cart-header                   {cartTitleText:TEXT} + close-button, alt çizgi, yükseklik 85
    ├─ cart-body
    │   ├─ cart-empty                {cartEmptyTitle:TEXT} text-h4 + {cartEmptyText:TEXT} text-label
    │   └─ cart-line-item ×N         görsel · ad · varyant · quantity-selector · fiyat · remove-button
    └─ cart-footer                   üst çizgi, boşluk $space-panel
        ├─ cart-shipping-row         {cartShippingLabel:TEXT} + {cartShippingNote:TEXT}  text-label muted
        ├─ cart-subtotal-row         {cartSubtotalLabel:TEXT} text-h4 + tutar text-price
        └─ checkout-button           {checkoutButtonText:TEXT}
```

Kontrol: boş ve dolu (2 ürün) halleri ayrı frame · checkout butonu boşken soluk

<!-- anim-targets:start -->
```yaml
- id: A-CART-01
  section: CartDrawer
  layer: cart-drawer
  recipe: M-20
  trigger: click
  what: "Çekmece sağdan kayar, scrim belirir"
  from: { x: 100%, scrim.opacity: 0 }
  to: { x: 0, scrim.opacity: 1 }
  timing: { spring: spring-drawer, scrim.duration: 0.4, rows.stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: css-transition + animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
- id: A-CART-02
  section: CartDrawer
  layer: cart-line-item
  recipe: M-20
  trigger: state-change
  what: "Satırlar gecikmeli girer"
  from: { opacity: 0, y: 20 }
  to: { opacity: 1, y: 0 }
  timing: { spring: spring-smooth, stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
- id: A-CART-03
  section: CartDrawer
  layer: checkout-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
```
<!-- anim-targets:end -->

#### Overlay/SearchOverlay
- **Kullanıldığı yer:** Header
- **ikas:** Header sub-component
- **Desktop:** Header altında tam genişlik panel; alt çizgi; arkada `scrim`.
- **Mobil:** Tam ekran; sonuçlar tek sütun liste (ProductCardSmall).

```
search-overlay
├─ scrim
└─ search-panel
    ├─ search-field                  {searchPlaceholder:TEXT} text-h3 boyutunda giriş + close-button
    ├─ search-results                ProductCard ×3–4 (yatay)
    └─ search-empty                  {searchEmptyText:TEXT}
```

Kontrol: boş, sonuçlu ve sonuçsuz halleri ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-SRCH-01
  section: SearchOverlay
  layer: search-panel
  recipe: M-21
  trigger: click
  what: "Panel header altından açılır"
  from: { y: -100%, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { spring: spring-search }
  impl: css-transition
  mobile: tam ekran
  reducedMotion: anında
  done: false
- id: A-SRCH-02
  section: SearchOverlay
  layer: search-results
  recipe: M-01
  trigger: state-change
  what: "Sonuç kartları sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.4, ease: ease-standard, stagger: 0.05 }
  impl: animejs
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/Footer
- **Kullanıldığı yer:** tüm sayfalar
- **ikas:** footer-section (--isFooter)
- **Desktop:** Tam genişlik × ~725. Üstte görselli banner 280, ortada 4 sütun, altta çizgili form satırı.
- **Mobil:** Banner 180; sütunlar 2×2; form tam genişlik alt alta; yasal linkler en altta.

```
footer
├─ footer-banner (clip)
│   ├─ footer-banner-image           {bannerImage:IMAGE}
│   ├─ footer-wordmark               {wordmarkText:TEXT} dev boyut, yarı saydam, banner genişliğinde
│   ├─ footer-banner-title           {bannerTitle:TEXT} text-h2, sol üst
│   └─ footer-logomark               {logoMark:SVG} 48, sağ alt
├─ footer-columns                    4 sütun, boşluk $space-page
│   └─ footer-column ×4
│       ├─ footer-column-title       {title:TEXT} text-ui
│       └─ footer-link ×N            {links:LIST_OF_LINK} text-ui-sm muted
└─ footer-bottom                     üst çizgi
    ├─ newsletter-form               newsletter-input (337×48) + newsletter-button (222×48) + newsletter-consent
    └─ footer-legal                  footer-link ×2 + {copyrightText:TEXT}
```

Kontrol: footer-wordmark ayrı katman · input: boş, odak ve hata halleri Components sayfasında

<!-- anim-targets:start -->
```yaml
- id: A-FTR-01
  section: Footer
  layer: footer
  recipe: M-16
  trigger: scroll-scrub
  what: "Footer içeriğin altından ortaya çıkar (sticky)"
  from: {}
  to: { position: sticky, bottom: 0 }
  timing: {}
  impl: layout
  mobile: normal akış
  reducedMotion: normal akış
  done: false
- id: A-FTR-02
  section: Footer
  layer: footer-wordmark
  recipe: M-16
  trigger: scroll-scrub
  what: "Dev yazı kaydırmayla hafifçe kayar"
  from: { wordmark.y: -80 }
  to: { wordmark.y: 0 }
  timing: { scrub: true }
  impl: layout + scroll-scrub
  mobile: normal akış
  reducedMotion: normal akış
  done: false
- id: A-FTR-03
  section: Footer
  layer: footer-link
  recipe: M-28
  trigger: hover
  what: "Link rengi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-FTR-04
  section: Footer
  layer: newsletter-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
```
<!-- anim-targets:end -->

#### Section/HeroSlider
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** hero-slider-section
- **Desktop:** 1440 × 720 (viewport − header). Tam kaplama görsel, alttan gradyan. Metin sol altta, thumbnail sağ altta; kenar boşluğu $space-page.
- **Mobil:** 390 × 420. `hero-description` ve `hero-thumbs` yok; alt kenarda tam genişlik 2px `progress-bar`. Başlık text-display (mobil değer).

```
hero-slider
├─ hero-slides                       layout none, tüm slaytlar üst üste
│   └─ hero-slide ×3
│       └─ hero-slide-mask (clip)
│           ├─ hero-slide-image      {image:IMAGE}
│           └─ gradient-mask
├─ hero-text
│   ├─ hero-badge (clip)             {badgeText:TEXT} çerçeveli; top + bottom kopya
│   ├─ hero-title-mask (clip)
│   │   └─ hero-title                {title:TEXT} text-display
│   └─ hero-description              {description:TEXT} text-ui muted, genişlik 500
├─ hero-thumbs                       aralık $space-grid
│   └─ hero-thumb ×3                 151×105, çerçeveli; pasif olanlar $opacity-inactive
│       ├─ hero-thumb-image
│       └─ progress-bar              aktif thumb üzerinde yarı saydam dolgu (genişlik %50 çiz)
└─ hero-click-left / hero-click-right   görünmez, yarı genişlik
```

Kontrol: 3 slaytın hepsi kardeş frame, sadece biri görünür · başlık kendi clip maskesinde · Motion States: slayt geçişi %0 / %50 / %100

<!-- anim-targets:start -->
```yaml
- id: A-HERO-01
  section: HeroSlider
  layer: hero-slide-mask
  recipe: M-07
  trigger: auto | click
  what: "Yeni slayt soldan maske ile açılır, görsel küçülerek oturur"
  from: { mask.width: 0%, image.scale: 1.2 }
  to: { mask.width: 100%, image.scale: 1 }
  timing: { spring: spring-hero, text.delay: 1, text.spring: "bounce 0, 1.2s" }
  impl: animejs
  mobile: çapraz geçiş 0.6s
  reducedMotion: anında değişim
  done: false
- id: A-HERO-02
  section: HeroSlider
  layer: hero-title
  recipe: M-07
  trigger: state-change
  what: "Başlık slaytla birlikte değişir"
  from: { y: 100% }
  to: { y: 0 }
  timing: { spring: "bounce 0, 1.2s", delay: 1 }
  impl: animejs
  mobile: çapraz geçiş 0.6s
  reducedMotion: anında değişim
  done: false
- id: A-HERO-03
  section: HeroSlider
  layer: hero-description
  recipe: M-01
  trigger: state-change
  what: "Açıklama başlıktan sonra girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 1.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-HERO-04
  section: HeroSlider
  layer: progress-bar
  recipe: M-08
  trigger: auto
  what: "Aktif thumbnail çubuğu slayt süresince dolar"
  from: { width: 0% }
  to: { width: 100% }
  timing: { duration: 4, ease: ease-inout, reset: 0.6 }
  impl: css-transition
  mobile: tek ince çizgi
  reducedMotion: çubuk gizli
  done: false
- id: A-HERO-05
  section: HeroSlider
  layer: hero-thumb
  recipe: M-28
  trigger: hover
  what: "Pasif thumbnail parlar"
  from: { opacity: 0.3 }
  to: { opacity: 1 }
  timing: { spring: spring-smooth }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-HERO-06
  section: HeroSlider
  layer: hero-badge
  recipe: M-11
  trigger: hover
  what: "Etiket butonu dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-HERO-07
  section: HeroSlider
  layer: hero-slides
  recipe: M-02
  trigger: load
  what: "İlk yüklemede görsel yumuşak belirir"
  from: { opacity: 0 }
  to: { opacity: 1 }
  timing: { spring: "bounce 0, 1.2s", delay: 0.3 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-HERO-08
  section: HeroSlider
  layer: hero-text
  recipe: M-01
  trigger: load
  what: "İlk yüklemede metin bloğu aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/FeaturedCollection
- **Kullanıldığı yer:** Ana sayfa (2 kez: promo solda / sağda)
- **ikas:** product-slider-section
- **Desktop:** 1440 × ~835. Promo panel 576×432 (sticky) + ürün ızgarası 2 sütun × 2 satır (kart 429×415), aralık $space-grid. İkinci örnekte panel sağda.
- **Mobil:** Panel tam genişlik (390×420) üstte; altında ürünler yatay kaydırmalı (kart 370, sonraki kart 15px görünür).

```
featured-collection
├─ promo-panel                       çerçeveli; sticky
│   ├─ promo-image                   {promoImage:IMAGE}
│   ├─ hotspot                       {hotspotProduct:PRODUCT}
│   │   ├─ hotspot-outer
│   │   └─ hotspot-inner
│   └─ promo-header                  boşluk $space-panel
│       ├─ link                      {linkText:TEXT} + link-line + link-arrow (clip: arrow-top + arrow-bottom)
│       └─ promo-title-mask (clip)
│           └─ promo-title           {title:TEXT} text-h2
└─ product-grid
    └─ ProductCard ×4                {productList:PRODUCT_LIST}
```

Kontrol: kap yüksekliği iki ürün satırı kadar (sticky aralığı görünür) · promo solda ve sağda iki örnek çizildi · hotspot açık hali Motion States içinde

<!-- anim-targets:start -->
```yaml
- id: A-FEAT-01
  section: FeaturedCollection
  layer: promo-panel
  recipe: M-13
  trigger: sticky
  what: "Panel, yanındaki ürünler kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-FEAT-02
  section: FeaturedCollection
  layer: promo-title
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-FEAT-03
  section: FeaturedCollection
  layer: hotspot-outer
  via: Hotspot
  recipe: M-12
  trigger: auto-loop
  what: "Hotspot halkası nabız gibi atar"
  from: { outer.scale: 1, outer.opacity: 1 }
  to: { outer.scale: 2.2, outer.opacity: 0 }
  timing: { duration: 1.5, loop: true, card.spring: spring-soft }
  impl: css-keyframes + css-transition
  mobile: dokunmayla açılır
  reducedMotion: pulse durur
  done: false
- id: A-FEAT-04
  section: FeaturedCollection
  layer: hotspot
  via: Hotspot
  recipe: M-12
  trigger: hover | click
  what: "Hotspot ürün mini kartını açar"
  from: { card.opacity: 0, card.scale: 0.9 }
  to: { card.opacity: 1, card.scale: 1 }
  timing: { spring: spring-soft }
  impl: css-transition
  mobile: dokunmayla açılır
  reducedMotion: pulse durur
  done: false
- id: A-FEAT-05
  section: FeaturedCollection
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/ShoppableImages
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** category-images-section (uyarlanır)
- **Desktop:** 1440 × 540; 2 eşit görsel (720), aralık $space-grid, çerçeveli; her birinde bir hotspot.
- **Mobil:** Alt alta, her biri 390×390.

```
shoppable-images
└─ shoppable-image ×2
    ├─ shoppable-image-media         {image:IMAGE}
    └─ hotspot                       {product:PRODUCT}
        ├─ hotspot-outer
        └─ hotspot-inner
```

Kontrol: hotspot konumu ürünün üzerinde

<!-- anim-targets:start -->
```yaml
- id: A-SHOP-01
  section: ShoppableImages
  layer: hotspot-outer
  via: Hotspot
  recipe: M-12
  trigger: auto-loop
  what: "Hotspot halkası nabız gibi atar"
  from: { outer.scale: 1, outer.opacity: 1 }
  to: { outer.scale: 2.2, outer.opacity: 0 }
  timing: { duration: 1.5, loop: true, card.spring: spring-soft }
  impl: css-keyframes + css-transition
  mobile: dokunmayla açılır
  reducedMotion: pulse durur
  done: false
- id: A-SHOP-02
  section: ShoppableImages
  layer: hotspot
  via: Hotspot
  recipe: M-12
  trigger: hover | click
  what: "Hotspot ürün mini kartını açar"
  from: { card.opacity: 0, card.scale: 0.9 }
  to: { card.opacity: 1, card.scale: 1 }
  timing: { spring: spring-soft }
  impl: css-transition
  mobile: dokunmayla açılır
  reducedMotion: pulse durur
  done: false
```
<!-- anim-targets:end -->

#### Section/CategoryCards
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** category-images-section
- **Desktop:** 1440 × 362; 4 eşit kart (357), aralık $space-grid, çerçeveli.
- **Mobil:** Yatay kaydırmalı; kart 370×420, sonraki kart kenardan görünür.

```
category-cards
└─ category-card ×4 (clip)
    ├─ marquee (clip)
    │   └─ marquee-track             {label:TEXT} ×3 kopya, text-h2 muted, kart dışına taşar
    ├─ category-image                {image:IMAGE} ortada, zeminsiz ürün görseli
    └─ category-footer               boşluk $space-panel, iki uca yaslı
        ├─ category-label            {label:TEXT} text-ui
        └─ link                      {linkText:TEXT} + link-line + link-arrow
```

Kontrol: marquee-track içinde en az 3 kopya · hover hali Components sayfasında

<!-- anim-targets:start -->
```yaml
- id: A-CAT-01
  section: CategoryCards
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Kategori adı kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: A-CAT-02
  section: CategoryCards
  layer: category-card
  recipe: M-28
  trigger: hover
  what: "Marquee parlar, etiket soluklaşır"
  from: { marquee.color: color-muted, label.opacity: 1 }
  to: { marquee.color: color-text, label.opacity: 0.4 }
  timing: { spring: spring-card }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-CAT-03
  section: CategoryCards
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/SplitBanners
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** hero-slider-section (uyarlanır)
- **Desktop:** 1440 × 780; 2 eşit banner (720), aralık $space-grid, çerçeveli; tam kaplama görsel; metin sol altta.
- **Mobil:** Alt alta, her biri 390×380.

```
split-banners
└─ split-banner ×2
    ├─ split-banner-image            {image:IMAGE}
    ├─ gradient-mask
    └─ split-banner-text             boşluk $space-panel
        ├─ link                      {linkText:TEXT} + link-line + link-arrow
        └─ split-banner-title        her satır ayrı clip maskede
            └─ title-line-mask ×3 → title-line   {title:TEXT} text-h2
```

Kontrol: her başlık satırı ayrı maskede

<!-- anim-targets:start -->
```yaml
- id: A-SPLIT-01
  section: SplitBanners
  layer: title-line
  recipe: M-03
  trigger: inview
  what: "Başlık satırları sırayla açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-SPLIT-02
  section: SplitBanners
  layer: split-banner-image
  recipe: M-09
  trigger: hover
  what: "Görsel hafif büyür"
  from: { scale: 1 }
  to: { scale: 1.04 }
  timing: { spring: spring-card }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
- id: A-SPLIT-03
  section: SplitBanners
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/SocialFeed
- **Kullanıldığı yer:** Ana sayfa, ürün detay
- **ikas:** (özel)
- **Desktop:** 1440 × ~713; üst boşluk $space-section. Başlık satırı + altında 5 görsel görünen kesintisiz şerit (görsel 300×428, aralık $space-grid).
- **Mobil:** Başlık alt alta; görsel 220×314.

```
social-feed
├─ section-heading                   boşluk $space-page
│   ├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
│   ├─ section-description           {description:TEXT} text-ui muted
│   └─ link                          {linkText:TEXT} + link-line + link-arrow, sağda
└─ ticker (clip)
    └─ ticker-track                  {images:IMAGE_LIST} iki set, frame dışına taşar
        └─ ticker-item ×10           çerçeveli
```

Kontrol: ticker-track iki set görsel içeriyor

<!-- anim-targets:start -->
```yaml
- id: A-SOC-01
  section: SocialFeed
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-SOC-02
  section: SocialFeed
  layer: ticker-track
  recipe: M-15
  trigger: auto-loop
  what: "Görseller kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "40px/s", ease: linear, loop: true, hoverSlow: true }
  impl: css-keyframes
  mobile: yatay kaydırma
  reducedMotion: durur
  done: false
- id: A-SOC-03
  section: SocialFeed
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/JournalFeatured
- **Kullanıldığı yer:** Ana sayfa, ürün detay, journal yazı
- **ikas:** blog-home-section (uyarlanır)
- **Desktop:** 1440 × ~1244; üst boşluk $space-section. Başlık satırı; öne çıkan yazı (818 görsel + 626 metin, çerçeveli, yükseklik 541); altında 3 BlogCard (478).
- **Mobil:** Öne çıkan alt alta (görsel 390×260); kartlar yatay kaydırmalı.

```
journal-featured
├─ section-heading
│   ├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
│   ├─ section-description           {description:TEXT} text-ui muted
│   └─ link                          {viewAllText:TEXT} + link-line + link-arrow
├─ journal-feature                   çerçeveli
│   ├─ journal-feature-image         {blogList:BLOG_LIST}[0]
│   └─ journal-feature-text          boşluk 40
│       ├─ journal-date              text-label muted
│       ├─ journal-feature-title     text-h3
│       ├─ journal-excerpt           text-body
│       └─ link                      {readMoreText:TEXT} + link-line + link-arrow
└─ journal-cards
    └─ BlogCard ×3
```

Kontrol: BlogCard bileşen instance'ı

<!-- anim-targets:start -->
```yaml
- id: A-JRNF-01
  section: JournalFeatured
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-JRNF-02
  section: JournalFeatured
  layer: journal-feature-image
  recipe: M-09
  trigger: hover
  what: "Görsel hafif büyür"
  from: { scale: 1 }
  to: { scale: 1.04 }
  timing: { spring: spring-card }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
- id: A-JRNF-03
  section: JournalFeatured
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/ProductList
- **Kullanıldığı yer:** Kategori, koleksiyon, arama, favoriler
- **ikas:** category-list-section
- **Desktop:** 1440; başlık alanı 126 (alt çizgi), sticky filtre barı 72 (alt çizgi), 3 sütun ızgara (kart 478×451), aralık $space-grid.
- **Mobil:** Tek sütun (kart 390×~380); filter-bar yatay kaydırmalı; başlık text-display (mobil değer).

```
product-list
├─ list-header                       boşluk $space-page
│   └─ list-title                    {title:TEXT} text-display
├─ filter-bar                        sticky; boşluk $space-page; aralık 15
│   └─ filter-tab ×8                 {filterLinks:LIST_OF_LINK} text-h4; aktif $color-text, pasif $color-muted
├─ product-grid
│   └─ ProductCard ×9+
└─ list-footer
    ├─ load-more-button              {loadMoreText:TEXT}
    └─ list-empty                    {emptyTitle:TEXT} + {emptyText:TEXT}
```

Kontrol: en az 9 kart; rozet çeşitleri (NEW, SALE, BEST SELLER, rozetsiz) görünür · boş durum ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-PLP-01
  section: ProductList
  layer: filter-bar
  recipe: M-18
  trigger: sticky
  what: "Filtre barı header altında sabit kalır"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: layout + css-transition
  mobile: yatay kaydırma
  reducedMotion: anında
  done: false
- id: A-PLP-02
  section: ProductList
  layer: filter-tab
  via: Tabs
  recipe: M-28
  trigger: hover | click
  what: "Sekme rengi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PLP-03
  section: ProductList
  layer: product-grid
  recipe: M-01
  trigger: state-change
  what: "Filtre değişince kartlar sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.4, ease: ease-standard, stagger: 0.04 }
  impl: animejs
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PLP-04
  section: ProductList
  layer: list-title
  recipe: M-01
  trigger: load
  what: "Sayfa başlığı aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/CollectionHero
- **Kullanıldığı yer:** Koleksiyon
- **ikas:** (özel)
- **Desktop:** 1440 × 720; arka plan görseli + gradyan; sol altta koleksiyon adı ve slogan; altında açıklama satırı ve iki yardımcı görsel.
- **Mobil:** 390 × 480; collection-info alt alta.

```
collection-hero
├─ collection-hero-bg                {backgroundImage:IMAGE}, kabından %15 yüksek
├─ gradient-mask
├─ collection-hero-text
│   ├─ collection-tagline            {tagline:TEXT} text-ui muted
│   └─ collection-title-mask (clip) → collection-title   {title:TEXT} text-display
└─ collection-info                   boşluk $space-page, 3 hücre
    ├─ collection-image-a            {imageA:IMAGE} 3:4
    ├─ collection-description        {description:TEXT} text-ui
    └─ collection-image-b            {imageB:IMAGE} 4:3
```

<!-- anim-targets:start -->
```yaml
- id: A-COLL-01
  section: CollectionHero
  layer: collection-hero-bg
  recipe: M-27
  trigger: scroll-scrub
  what: "Arka plan içerikten yavaş kayar"
  from: { bg.y: 0 }
  to: { bg.y: 20% }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: A-COLL-02
  section: CollectionHero
  layer: collection-title
  recipe: M-03
  trigger: load
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-COLL-03
  section: CollectionHero
  layer: collection-info
  recipe: M-01
  trigger: inview
  what: "Bilgi hücreleri sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.1 }
  impl: animejs + io-hook
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/ProductDetail
- **Kullanıldığı yer:** Ürün detay
- **ikas:** product-detail-section
- **Desktop:** 1440; solda 500 sticky detay sütunu (viewport yüksekliği, sağ çizgi), sağda 940 galeri (4 görsel, her biri 720 yükseklik, alt çizgi), sağ üstte dikey thumbnail şeridi (60×75, aralık 5, çerçeveli).
- **Mobil:** Sıra: yatay galeri (390×490, altında noktalar) → pdp-top → variant-chips → pdp-buy-row. Sticky yok; `mini-buy-bar` alt kenarda tam genişlik.

```
product-detail
├─ pdp-details                       sticky; dikey, iki uca yaslı
│   ├─ pdp-top                       boşluk $space-page, aralık 20
│   │   ├─ breadcrumbs               text-label
│   │   ├─ pdp-title                 text-h3
│   │   ├─ pdp-description           text-ui
│   │   └─ info-tabs                 info-tab ×3 {infoTabs:COMPONENT_LIST} text-ui-sm muted
│   └─ pdp-bottom
│       ├─ variant-chips             variant-chip ×N (seçili / pasif / stok yok)
│       ├─ link                      {sizeGuideText:TEXT} + link-line + link-arrow, sağda
│       └─ pdp-buy-row               üst çizgi, boşluk $space-page
│           ├─ pdp-price             text-price (+ eski fiyat) + {shippingNoteText:TEXT} text-label
│           └─ add-to-cart-button    {addToCartText:TEXT} dolu buton 225×44
├─ pdp-gallery
│   └─ pdp-image ×4
├─ pdp-thumbs
│   └─ pdp-thumb ×4                  aktif olan $color-text çerçeveli
└─ mini-buy-bar                      sağ altta 350×72 çerçeveli: küçük görsel + ad + fiyat + buton
```

Kontrol: galeri gerçek yükseklikte (4 görsel alt alta) · buton halleri: varsayılan, yükleniyor, eklendi, stok yok · mini-buy-bar ayrı overlay frame

<!-- anim-targets:start -->
```yaml
- id: A-PDP-01
  section: ProductDetail
  layer: pdp-details
  recipe: M-13
  trigger: sticky
  what: "Detay sütunu galeri kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-PDP-02
  section: ProductDetail
  layer: pdp-thumb
  recipe: M-19
  trigger: scroll-scrub
  what: "Görünen görselin thumbnail çerçevesi yanar"
  from: { thumb.border: none, bar.y: 100% }
  to: { thumb.border: color-text, bar.y: 0 }
  timing: { duration: 0.3, bar.spring: spring-soft }
  impl: layout + io-hook
  mobile: yatay galeri + noktalar
  reducedMotion: anında
  done: false
- id: A-PDP-03
  section: ProductDetail
  layer: mini-buy-bar
  recipe: M-19
  trigger: inview
  what: "Galeri bitince mini satın alma çubuğu alttan girer"
  from: { thumb.border: none, bar.y: 100% }
  to: { thumb.border: color-text, bar.y: 0 }
  timing: { duration: 0.3, bar.spring: spring-soft }
  impl: layout + io-hook
  mobile: yatay galeri + noktalar
  reducedMotion: anında
  done: false
- id: A-PDP-04
  section: ProductDetail
  layer: add-to-cart-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-PDP-05
  section: ProductDetail
  layer: variant-chip
  via: VariantChip
  recipe: M-28
  trigger: hover | click
  what: "Çip çerçevesi ve metni parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PDP-06
  section: ProductDetail
  layer: info-tab
  recipe: M-28
  trigger: hover
  what: "Sekme rengi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PDP-07
  section: ProductDetail
  layer: pdp-title
  recipe: M-01
  trigger: load
  what: "Başlık ve açıklama aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PDP-08
  section: ProductDetail
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/InfoDrawer
- **Kullanıldığı yer:** Ürün detay (Materials / Care / Shipping / Size guide)
- **ikas:** ProductDetail sub-component
- **Desktop:** Soldan 460 × tam yükseklik; sağ çizgi; arkada `scrim` (koyu + blur).
- **Mobil:** 390 tam genişlik.

```
info-overlay
├─ scrim
└─ info-drawer
    ├─ info-media (clip)             yükseklik 300, alt çizgi
    │   ├─ info-image                {image:IMAGE}
    │   ├─ marquee (clip) → marquee-track   sekme adı ×3, text-h2 muted, görselin üst kenarında
    │   └─ close-button              sağ üst
    ├─ info-tabs-row                 info-tab ×3 text-h4; aktif $color-text
    └─ info-content                  {content:RICH_TEXT} text-body, madde listesi
```

Kontrol: beden rehberi (tablo) hali ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-INFO-01
  section: InfoDrawer
  layer: info-drawer
  recipe: M-20
  trigger: click
  what: "Çekmece soldan kayar, scrim belirir"
  from: { x: -100%, scrim.opacity: 0 }
  to: { x: 0, scrim.opacity: 1 }
  timing: { spring: spring-drawer, scrim.duration: 0.4, rows.stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: css-transition + animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
- id: A-INFO-02
  section: InfoDrawer
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Sekme adı görselin üstünde kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: A-INFO-03
  section: InfoDrawer
  layer: info-content
  recipe: M-01
  trigger: state-change
  what: "Sekme değişince içerik yumuşak değişir"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.3, ease: ease-standard }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/ProductCarousel
- **Kullanıldığı yer:** Ürün detay (2 kez), iletişim
- **ikas:** product-slider-section
- **Desktop:** 1440 × ~664; üst boşluk $space-section. Başlık satırı (başlık + sağda link); altında yatay ProductCard şeridi (kart 478, 3 görünür, devamı taşar).
- **Mobil:** Kart 370; yatay kaydırmalı.

```
product-carousel
├─ section-heading
│   ├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
│   └─ link                          {linkText:TEXT} + link-line + link-arrow
└─ carousel (clip)
    └─ carousel-track
        └─ ProductCard ×6            {productList:PRODUCT_LIST}
```

<!-- anim-targets:start -->
```yaml
- id: A-CRSL-01
  section: ProductCarousel
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-CRSL-02
  section: ProductCarousel
  layer: carousel-track
  recipe: M-15
  trigger: drag
  what: "Şerit sürüklenir / kaydırılır"
  from: {}
  to: {}
  timing: { snap: true }
  impl: css scroll-snap
  mobile: yatay kaydırma
  reducedMotion: aynı
  done: false
- id: A-CRSL-03
  section: ProductCarousel
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/AboutHero
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × 780; tam kaplama görsel; sol altta 3 satır başlık; sağda 300 genişlik misyon bloğu.
- **Mobil:** 390 × 620; misyon bloğu başlığın altında tam genişlik.

```
about-hero
├─ about-hero-bg                     {backgroundImage:IMAGE}, kabından %15 yüksek
├─ about-hero-title
│   └─ title-line-mask ×3 → title-line   {title:TEXT} text-display
└─ about-mission                     genişlik 300
    ├─ about-mission-label           {missionLabel:TEXT} text-ui-sm muted
    └─ about-mission-text            {missionText:TEXT} text-ui
```

<!-- anim-targets:start -->
```yaml
- id: A-ABH-01
  section: AboutHero
  layer: about-hero-bg
  recipe: M-27
  trigger: scroll-scrub
  what: "Arka plan içerikten yavaş kayar"
  from: { bg.y: 0 }
  to: { bg.y: 20% }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: A-ABH-02
  section: AboutHero
  layer: title-line
  recipe: M-03
  trigger: load
  what: "Başlık satırları sırayla açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-ABH-03
  section: AboutHero
  layer: about-mission
  recipe: M-01
  trigger: load
  what: "Misyon bloğu aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.6 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/PressSlider
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × 410; üst + alt çizgi; ortada 600 genişlik alıntı, solda ve sağda soluk komşu alıntılar (kısmen görünür).
- **Mobil:** Tek alıntı görünür (350); yatay kaydırmalı.

```
press-slider
└─ press-track                       yatay, aralık 120, ortalı
    └─ press-quote ×5                genişlik 600, ortalı metin; ortadaki tam opak, diğerleri 0.4
        ├─ press-logo                {logo:SVG} yükseklik 34
        └─ press-text                {quote:TEXT} text-title
```

<!-- anim-targets:start -->
```yaml
- id: A-PRS-01
  section: PressSlider
  layer: press-track
  recipe: M-26
  trigger: auto | drag
  what: "Alıntılar 3 saniyede bir kayar; ortadaki parlar"
  from: { side.opacity: 0.4 }
  to: { center.opacity: 1 }
  timing: { interval: 3, spring: spring-smooth, drag: true }
  impl: animejs
  mobile: scroll-snap
  reducedMotion: otomatik durur
  done: false
```
<!-- anim-targets:end -->

#### Section/ValuesStack
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × 3120 (4 panel × 780). Her panel tam viewport ve sticky; ortada 800 genişlik metin; kenarda döndürülmüş görsel (4:3 = 527×411 solda / 3:4 = 587×753 sağda, sırayla).
- **Mobil:** Normal akış (sticky yok); her panel: görsel üstte tam genişlik + metin altında; rotasyon yok.

```
values-stack
├─ value-panel (giriş)
│   ├─ value-image                   {image:IMAGE} mutlak konum, sol kenar
│   └─ value-text
│       ├─ value-title               {introTitle:TEXT} text-h2
│       └─ value-paragraph           {introText:TEXT} text-ui
└─ value-panel ×3
    ├─ value-image                   {image:IMAGE} mutlak konum; sağ / sol / sağ
    └─ value-text
        ├─ value-title               {title:TEXT} text-h3
        └─ value-paragraph           {text:TEXT} text-ui
```

Kontrol: görseller bitiş (0°) halinde çizildi · Motion States: bir panelin %0 (10° dönük) / %50 / %100 hali

<!-- anim-targets:start -->
```yaml
- id: A-VAL-01
  section: ValuesStack
  layer: value-panel
  recipe: M-13
  trigger: sticky
  what: "Paneller üst üste biner"
  from: {}
  to: { position: sticky, top: 0 }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-VAL-02
  section: ValuesStack
  layer: value-image
  recipe: M-23
  trigger: scroll-scrub
  what: "Görsel dönerek düzelir ve yukarı kayar"
  from: { rotate: 10, y: 0 }
  to: { rotate: 0, y: -1200 }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı, normal akış
  reducedMotion: kapalı
  done: false
- id: A-VAL-03
  section: ValuesStack
  layer: value-title
  recipe: M-24
  trigger: scroll-scrub
  what: "Başlık kaydırdıkça büyüyerek kaybolur"
  from: { opacity: 1, scale: 1, text.y: 0 }
  to: { opacity: 0, scale: 1.2, text.y: -200 }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: A-VAL-04
  section: ValuesStack
  layer: value-paragraph
  recipe: M-24
  trigger: scroll-scrub
  what: "Paragraf yukarı kayar"
  from: { y: 0 }
  to: { y: -200 }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
```
<!-- anim-targets:end -->

#### Section/ProcessSteps
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × ~1275; üst boşluk $space-section; 1200 genişlik kap: başlık + paragraf, altında 3 sütun adım; en altta tam genişlik görsel (788).
- **Mobil:** Adımlar alt alta; görsel 390×300.

```
process-steps
├─ process-container                 genişlik 1200
│   ├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
│   ├─ process-text                  {text:TEXT} text-ui
│   └─ process-grid                  3 sütun, aralık 40
│       └─ process-step ×3
│           ├─ process-step-title    {title:TEXT} text-ui
│           └─ process-step-text     {text:TEXT} text-body
└─ process-image                     {image:IMAGE}
```

<!-- anim-targets:start -->
```yaml
- id: A-PRC-01
  section: ProcessSteps
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-PRC-02
  section: ProcessSteps
  layer: process-step
  recipe: M-01
  trigger: inview
  what: "Adımlar sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.1 }
  impl: animejs + io-hook
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-PRC-03
  section: ProcessSteps
  layer: process-image
  recipe: M-27
  trigger: scroll-scrub
  what: "Görsel hafif parallax yapar"
  from: { bg.y: 0 }
  to: { bg.y: 20% }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
```
<!-- anim-targets:end -->

#### Section/TeamGrid
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × ~811; üst boşluk $space-section; 1200 kap: başlık + paragraf; altında tam genişlik 4 sütun üye kartı (çerçeveli, aralık $space-grid).
- **Mobil:** Kartlar yatay kaydırmalı (kart 300).

```
team-grid
├─ team-container
│   ├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
│   └─ team-text                     {text:TEXT} text-ui
└─ team-members
    └─ team-member ×4
        ├─ team-member-image         {image:IMAGE} 357×380
        └─ team-member-info          boşluk $space-card: {role:TEXT} text-label muted + {name:TEXT} text-title
```

<!-- anim-targets:start -->
```yaml
- id: A-TEAM-01
  section: TeamGrid
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-TEAM-02
  section: TeamGrid
  layer: team-member
  recipe: M-01
  trigger: inview
  what: "Kartlar sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/Timeline
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440; üst boşluk $space-section; başlık + 5 satır; her satır alt çizgili: solda yıl, ortada başlık, sağda paragraf.
- **Mobil:** Satır içi alt alta: yıl → başlık → paragraf.

```
timeline
├─ section-title-mask (clip) → section-title   {title:TEXT} text-h2
└─ timeline-row ×5                   boşluk 40 $space-page, alt çizgi
    ├─ timeline-year                 {year:TEXT} text-h2
    ├─ timeline-title                {title:TEXT} text-ui
    └─ timeline-text                 {text:TEXT} text-body, genişlik 480
```

<!-- anim-targets:start -->
```yaml
- id: A-TML-01
  section: Timeline
  layer: section-title
  via: SectionHeading
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-TML-02
  section: Timeline
  layer: timeline-row
  recipe: M-01
  trigger: inview
  what: "Satırlar görünürlüğe girince tek tek belirir"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/CtaBanner
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** 1440 × 600; tam kaplama görsel + gradyan; ortada başlık ve buton.
- **Mobil:** 390 × 420.

```
cta-banner
├─ cta-image                         {image:IMAGE}
├─ gradient-mask
├─ cta-title-mask (clip) → cta-title {title:TEXT} text-h2
└─ cta-button (clip)                 {buttonText:TEXT}; top + bottom kopya
```

<!-- anim-targets:start -->
```yaml
- id: A-CTA-01
  section: CtaBanner
  layer: cta-title
  recipe: M-03
  trigger: inview
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-CTA-02
  section: CtaBanner
  layer: cta-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
```
<!-- anim-targets:end -->

#### Section/AnchorNav
- **Kullanıldığı yer:** Hakkında
- **ikas:** (özel)
- **Desktop:** Alt kenarda sabit çubuk: tam genişlik × 72, üst çizgi, zemin $color-bg; ortalı sekmeler, aralık 20.
- **Mobil:** Yükseklik 56; yatay kaydırmalı; sol hizalı.

```
anchor-nav
└─ anchor-link ×6                    {items:LIST_OF_LINK} text-h4; aktif $color-text, pasif $color-muted
```

Kontrol: sayfa frame'inde alt kenara mutlak konumla yerleştirildi

<!-- anim-targets:start -->
```yaml
- id: A-ANC-01
  section: AnchorNav
  layer: anchor-link
  recipe: M-25
  trigger: scroll-scrub
  what: "Görünen bölümün sekmesi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: io-hook + css-transition
  mobile: yatay kaydırma
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/BlogList
- **Kullanıldığı yer:** Journal liste
- **ikas:** blog-home-section
- **Desktop:** 1440; öne çıkan yazı (818 görsel + 626 metin, yükseklik 541, çerçeveli); altında 2 sütun BlogCard ızgarası (kart 720), aralık $space-grid.
- **Mobil:** Tek sütun.

```
blog-list
├─ journal-feature
│   ├─ journal-feature-image
│   └─ journal-feature-text          journal-date · journal-feature-title (text-h3) · journal-excerpt · link
├─ blog-grid
│   └─ BlogCard ×4+                  {blogList:BLOG_LIST}
└─ load-more-button                  {loadMoreText:TEXT}
```

<!-- anim-targets:start -->
```yaml
- id: A-BLG-01
  section: BlogList
  layer: journal-feature
  recipe: M-01
  trigger: load
  what: "Öne çıkan yazı aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-BLG-02
  section: BlogList
  layer: blog-grid
  recipe: M-01
  trigger: inview
  what: "Kartlar sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-BLG-03
  section: BlogList
  layer: link
  via: ArrowLink
  recipe: M-10
  trigger: hover
  what: "Ok döner, alt çizgi uzar"
  from: { line.width: 0%, arrow: top }
  to: { line.width: 100%, arrow: bottom }
  timing: { duration: 0.4, spring: spring-soft }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/BlogPost
- **Kullanıldığı yer:** Journal yazı
- **ikas:** blog-post-section
- **Desktop:** 1440; hero 720 (görsel + tarih + başlık + özet, sol hizalı, genişlik 600); altında 1200 genişlik gövde (sol + sağ çizgi): içerik 826 + yan sütun 372 (sol çizgi, sticky).
- **Mobil:** Hero 390×520; gövde tek sütun; yan sütun içeriğin altında.

```
blog-post
├─ post-hero
│   ├─ post-hero-bg                  görsel, kabından %15 yüksek
│   └─ post-hero-text                journal-date · post-title (text-h2) · post-excerpt (text-body)
└─ post-body
    ├─ post-content                  boşluk 40
    │   ├─ breadcrumbs
    │   ├─ post-heading              text-h3
    │   ├─ post-paragraph            text-body
    │   ├─ post-quote                text-h4
    │   └─ post-image                640×360
    └─ post-sidebar                  sticky
        ├─ post-next (clip)          {nextText:TEXT} ortalı, alt çizgi; top + bottom kopya
        ├─ post-sidebar-title        {relatedProductsTitle:TEXT} text-h4
        └─ ProductCardSmall ×3       {relatedProducts:PRODUCT_LIST}
```

<!-- anim-targets:start -->
```yaml
- id: A-BLP-01
  section: BlogPost
  layer: post-hero-bg
  recipe: M-27
  trigger: scroll-scrub
  what: "Hero görseli içerikten yavaş kayar"
  from: { bg.y: 0 }
  to: { bg.y: 20% }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: A-BLP-02
  section: BlogPost
  layer: post-title
  recipe: M-03
  trigger: load
  what: "Başlık kelime kelime açılır"
  from: { opacity: 0, y: 50, rotateX: 20, skewX: 10, skewY: 5 }
  to: { opacity: 1, y: 0, rotateX: 0, skewX: 0, skewY: 0 }
  timing: { spring: spring-text, stagger: 0.05, threshold: 0.5, once: true }
  impl: animejs + io-hook
  mobile: sadece y + opacity
  reducedMotion: anında
  done: false
- id: A-BLP-03
  section: BlogPost
  layer: post-sidebar
  recipe: M-13
  trigger: sticky
  what: "Yan sütun içerik kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-BLP-04
  section: BlogPost
  layer: post-next
  recipe: M-11
  trigger: hover
  what: "NEXT hücresi ters dolguya döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
```
<!-- anim-targets:end -->

#### Section/MarqueeTitle
- **Kullanıldığı yer:** İletişim
- **ikas:** (özel)
- **Desktop:** 1440 × 120; alt çizgi; sayfa adı kesintisiz kayar.
- **Mobil:** Yükseklik 70.

```
marquee-title
└─ marquee (clip)
    └─ marquee-track                 {text:TEXT} ×6 kopya, text-display, aralık 40
```

<!-- anim-targets:start -->
```yaml
- id: A-MQT-01
  section: MarqueeTitle
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Sayfa başlığı kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "90px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
```
<!-- anim-targets:end -->

#### Section/Contact
- **Kullanıldığı yer:** İletişim
- **ikas:** (özel; form-handling rehberi)
- **Desktop:** 1440; iki eşit sütun, ortada dikey çizgi. Sütun başlıkları 85 yüksekliğinde alt çizgili satırlar.
- **Mobil:** Tek sütun: önce form, sonra bilgiler ve FAQ.

```
contact
├─ contact-left
│   ├─ contact-heading               {infoTitle:TEXT} text-h3, alt çizgi
│   ├─ contact-info                  2 kolon: (e-posta, telefon, adres) | sosyal linkler
│   │   ├─ contact-item ×3           etiket text-ui-sm + değer text-label altı çizili
│   │   └─ contact-socials           {socialLinks:LIST_OF_LINK} text-label muted
│   ├─ faq-heading                   {faqTitle:TEXT} text-h3
│   └─ faq-list                      çerçeveli
│       └─ faq-item ×5               {faqItems:COMPONENT_LIST}
│           ├─ faq-question          text-ui-sm + faq-icon (artı / eksi)
│           └─ faq-answer            text-body
└─ contact-right
    ├─ contact-heading               {formTitle:TEXT} text-h3, alt çizgi
    └─ contact-form                  bitişik çerçeveli hücreler
        ├─ form-row                  form-field ×1–3 (yükseklik 48)
        ├─ form-textarea             yükseklik 160
        └─ submit-button (clip)      {submitText:TEXT} tam genişlik; top + bottom kopya
```

Kontrol: faq-item açık ve kapalı halleri · form: boş, hata, gönderiliyor, başarılı halleri ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-CNT-01
  section: Contact
  layer: faq-answer
  via: AccordionItem
  recipe: M-22
  trigger: click
  what: "Cevap açılır, ikon döner"
  from: { height: 0, icon.rotate: 0 }
  to: { height: auto, icon.rotate: 45 }
  timing: { spring: "bounce 0, 0.5s" }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: A-CNT-02
  section: Contact
  layer: submit-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-CNT-03
  section: Contact
  layer: contact-heading
  recipe: M-01
  trigger: load
  what: "Sütun başlıkları aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/SupportContent
- **Kullanıldığı yer:** Destek / politika sayfaları
- **ikas:** rich-text-section
- **Desktop:** 1440; 1200 genişlik kap: solda 300 yan menü (sticky), sağda içerik.
- **Mobil:** Yan menü üstte yatay kaydırmalı sekmeler; içerik altında.

```
support-content
├─ support-nav                       sticky
│   ├─ support-link ×6               {navLinks:LIST_OF_LINK} text-ui-sm; aktif $color-text
│   └─ support-contact               çerçeveli kutu: {contactTitle:TEXT} + {contactText:TEXT} + link
└─ support-body
    ├─ support-title                 {title:TEXT} text-h3
    └─ support-rich-text             {content:RICH_TEXT}: ara başlık text-h4 + paragraf text-body
```

<!-- anim-targets:start -->
```yaml
- id: A-SUP-01
  section: SupportContent
  layer: support-nav
  recipe: M-13
  trigger: sticky
  what: "Yan menü içerik kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-SUP-02
  section: SupportContent
  layer: support-link
  recipe: M-28
  trigger: hover
  what: "Link rengi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/CartPage
- **Kullanıldığı yer:** Sepet (referansta yok, ikas için gerekli)
- **ikas:** cart-section
- **Desktop:** 1440; başlık alanı (text-display); solda ürün satırları (alt çizgili), sağda 480 genişlik sticky özet kutusu (çerçeveli).
- **Mobil:** Tek sütun; özet altta; checkout butonu alt kenarda sabit.

```
cart-page
├─ list-header → list-title          {title:TEXT} text-display
├─ cart-lines
│   └─ cart-line-item ×N             görsel 120×150 · ad · varyant · quantity-selector · fiyat · remove-button
├─ cart-summary                      sticky
│   ├─ cart-coupon                   giriş + buton
│   ├─ cart-summary-row ×3           ara toplam · kargo · indirim
│   ├─ cart-total-row                text-h4 + text-price
│   └─ checkout-button (clip)        top + bottom kopya
└─ cart-empty                        {emptyTitle:TEXT} + {emptyText:TEXT} + buton
```

Kontrol: dolu ve boş halleri ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-CRTP-01
  section: CartPage
  layer: cart-summary
  recipe: M-13
  trigger: sticky
  what: "Özet kutusu satırlar kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: A-CRTP-02
  section: CartPage
  layer: checkout-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-CRTP-03
  section: CartPage
  layer: cart-line-item
  recipe: M-01
  trigger: state-change
  what: "Satır silinince/eklenince yumuşak geçiş"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.3, ease: ease-standard }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/AuthForms
- **Kullanıldığı yer:** Giriş, kayıt, şifremi unuttum, şifre yenile (referansta yok)
- **ikas:** login-section / register-section / forgot-password-section / recover-password-section
- **Desktop:** 1440 × 720; iki eşit sütun: solda tam kaplama görsel + başlık, sağda ortalı 420 genişlik form.
- **Mobil:** Görsel üstte 390×200; form altında tam genişlik.

```
auth
├─ auth-media
│   ├─ auth-image                    {image:IMAGE}
│   └─ auth-title                    {title:TEXT} text-h2
└─ auth-form                         genişlik 420
    ├─ form-field ×2–4               bitişik çerçeveli
    ├─ auth-helper-link              text-label altı çizili
    ├─ submit-button (clip)          {submitButtonText:TEXT}; top + bottom kopya
    └─ auth-switch                   {switchText:TEXT} + link
```

Kontrol: 4 sayfa ayrı frame: giriş, kayıt, şifremi unuttum, şifre yenile · hata ve yükleniyor halleri

<!-- anim-targets:start -->
```yaml
- id: A-AUTH-01
  section: AuthForms
  layer: submit-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: A-AUTH-02
  section: AuthForms
  layer: auth-form
  recipe: M-01
  trigger: load
  what: "Form aşağıdan girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, delay: 0.2 }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/Account
- **Kullanıldığı yer:** Hesabım (referansta yok)
- **ikas:** account-info-section
- **Desktop:** 1440; başlık alanı; sticky sekme barı (PLP filter-bar ile aynı); altında sekme içeriği.
- **Mobil:** Sekmeler yatay kaydırmalı; içerik tek sütun.

```
account
├─ list-header → list-title          {title:TEXT} text-display
├─ filter-bar                        sticky
│   └─ filter-tab ×5                 Bilgilerim · Siparişler · Adresler · Favoriler · Çıkış
└─ account-content
    ├─ account-info-form             form-field ızgarası + submit-button
    ├─ order-row ×N                  alt çizgili: sipariş no · tarih · durum · tutar · link
    ├─ address-card ×N               çerçeveli kart
    └─ order-detail                  ürün satırları + özet
```

Kontrol: her sekme içeriği ayrı frame

<!-- anim-targets:start -->
```yaml
- id: A-ACC-01
  section: Account
  layer: filter-bar
  recipe: M-18
  trigger: sticky
  what: "Sekme barı header altında sabit kalır"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: layout + css-transition
  mobile: yatay kaydırma
  reducedMotion: anında
  done: false
- id: A-ACC-02
  section: Account
  layer: filter-tab
  via: Tabs
  recipe: M-28
  trigger: hover | click
  what: "Sekme rengi parlar"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/NotFound
- **Kullanıldığı yer:** 404 ve e-posta doğrulama (referansta ölçülmedi)
- **ikas:** not-found-section / email-verification-section
- **Desktop:** 1440 × 720; kayan dev "404" şeridi + ortada mesaj ve buton.
- **Mobil:** 390 × 560.

```
not-found
├─ marquee (clip)
│   └─ marquee-track                 {code:TEXT} ×6 kopya, text-display muted
├─ not-found-title                   {title:TEXT} text-h3
├─ not-found-text                    {text:TEXT} text-ui muted
└─ not-found-button (clip)           {buttonText:TEXT}; top + bottom kopya
```

<!-- anim-targets:start -->
```yaml
- id: A-NF-01
  section: NotFound
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "404 yazısı kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: A-NF-02
  section: NotFound
  layer: not-found-button
  via: Button
  recipe: M-11
  trigger: hover
  what: "Buton dolgusu ters döner"
  from: { bottom.y: 100% }
  to: { bottom.y: 0, top.y: -100% }
  timing: { spring: "bounce 0.3, 0.4s" }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
```
<!-- anim-targets:end -->

### 6.3 Sayfalar

Her sayfa için `A/Page/<Ad>@desktop` ve `@mobile`: dikey layout, `clip: true`, çocukları yalnızca section instance'ları.

| Sayfa | Bölümler (sırayla) |
|---|---|
| `Home` | Header · HeroSlider · FeaturedCollection (promo solda) · FeaturedCollection (promo sağda) · ShoppableImages · CategoryCards · SplitBanners · SocialFeed · JournalFeatured · Footer |
| `Category` | Header · ProductList · Footer |
| `Collection` | Header · CollectionHero · ProductList · Footer |
| `Product` | Header · ProductDetail · ProductCarousel · ProductCarousel · JournalFeatured · SocialFeed · Footer |
| `About` | Header · AboutHero · PressSlider · ValuesStack · ProcessSteps · TeamGrid · Timeline · CtaBanner · Footer (+ AnchorNav sabit) |
| `Journal` | Header · BlogList · Footer |
| `JournalPost` | Header · BlogPost · JournalFeatured · Footer |
| `Contact` | Header · MarqueeTitle · Contact · ProductCarousel · Footer |
| `Support` | Header · SupportContent · Footer |
| `Cart` | Header · CartPage · Footer |
| `Auth (×4)` | Header · AuthForms · Footer |
| `Account` | Header · Account · Footer |
| `NotFound` | Header · NotFound · Footer |

### 6.4 Overlay frame'leri

6.2'de "Overlay" başlıklı her öğe için, yarı saydam bir sayfa görüntüsü yerine düz `$color-scrim` zemin üzerinde panel çizilir. Her biri desktop (1440×900) ve mobil (390×844), belirtilen durumlarıyla ayrı kök frame.

### 6.5 Motion States

Aşağıdaki tariflerin her biri için **bir** örnek üzerinde 2–3 kare çizilir (kök frame `A/Motion/<tarif> <bölüm>`; kareler soldan sağa, altlarında `note` ile yüzde/an bilgisi). Diğer kullanım yerleri aynı mantığı izler.

| Tarif | Örnek bölüm | Çizilecek kareler |
|---|---|---|
| M-03 | FeaturedCollection (`promo-title`) | başlık: kelimeler maske altında (görünmez) → yarısı girmiş → hepsi yerinde |
| M-05 | Header (`nav-link`) | nav-link: varsayılan → dolgu yarı yolda → tam ters dolgu |
| M-06 | Megamenu (`megamenu`) | megamenu: kapalı → yarı açık → açık |
| M-07 | HeroSlider (`hero-slide-mask`) | slayt geçişi: eski slayt → maske %50 (iki görsel yan yana) → yeni slayt |
| M-09 | Megamenu (`megamenu-card-image`) | ürün kartı: ön görsel → arka görsel + dönmüş ok |
| M-11 | CartDrawer (`checkout-button`) | buton: varsayılan → dolgu yarı yolda → ters dolgu |
| M-12 | FeaturedCollection (`hotspot-outer`) | hotspot: halka küçük → halka büyük ve soluk; ayrıca mini kart açık |
| M-20 | CartDrawer (`cart-drawer`) | çekmece: kapalı (sayfa) → yarı açık + scrim → açık |
| M-21 | SearchOverlay (`search-panel`) | arama: kapalı → açık boş → açık sonuçlu |
| M-22 | MobileMenu (`mobile-submenu`) | akordeon: kapalı → açık |
| M-23 | ValuesStack (`value-image`) | değer paneli: görsel 10° dönük ve aşağıda → 5° → 0° ve yerinde |
| M-24 | ValuesStack (`value-title`) | değer başlığı: tam opak → büyümüş ve yarı saydam → görünmez |

## 7. Animasyon hedefleri özeti

Toplam **117 hedef**. Ayrıntılar 6.1 ve 6.2'deki `anim-targets` bloklarında.

| Bölüm | Hedef | Tarifler | ID aralığı |
|---|---|---|---|
| Header | 3 | M-01, M-04, M-05 | `A-HDR-01` … `A-HDR-03` |
| Megamenu | 3 | M-06, M-09, M-28 | `A-MEGA-01` … `A-MEGA-03` |
| MobileMenu | 2 | M-20, M-22 | `A-MMENU-01` … `A-MMENU-02` |
| CartDrawer | 3 | M-11, M-20 | `A-CART-01` … `A-CART-03` |
| SearchOverlay | 2 | M-01, M-21 | `A-SRCH-01` … `A-SRCH-02` |
| Footer | 4 | M-11, M-16, M-28 | `A-FTR-01` … `A-FTR-04` |
| HeroSlider | 8 | M-01, M-02, M-07, M-08, M-11, M-28 | `A-HERO-01` … `A-HERO-08` |
| FeaturedCollection | 5 | M-03, M-10, M-12, M-13 | `A-FEAT-01` … `A-FEAT-05` |
| ShoppableImages | 2 | M-12 | `A-SHOP-01` … `A-SHOP-02` |
| CategoryCards | 3 | M-10, M-14, M-28 | `A-CAT-01` … `A-CAT-03` |
| SplitBanners | 3 | M-03, M-09, M-10 | `A-SPLIT-01` … `A-SPLIT-03` |
| SocialFeed | 3 | M-03, M-10, M-15 | `A-SOC-01` … `A-SOC-03` |
| JournalFeatured | 3 | M-03, M-09, M-10 | `A-JRNF-01` … `A-JRNF-03` |
| ProductList | 4 | M-01, M-18, M-28 | `A-PLP-01` … `A-PLP-04` |
| CollectionHero | 3 | M-01, M-03, M-27 | `A-COLL-01` … `A-COLL-03` |
| ProductDetail | 8 | M-01, M-10, M-11, M-13, M-19, M-28 | `A-PDP-01` … `A-PDP-08` |
| InfoDrawer | 3 | M-01, M-14, M-20 | `A-INFO-01` … `A-INFO-03` |
| ProductCarousel | 3 | M-03, M-10, M-15 | `A-CRSL-01` … `A-CRSL-03` |
| AboutHero | 3 | M-01, M-03, M-27 | `A-ABH-01` … `A-ABH-03` |
| PressSlider | 1 | M-26 | `A-PRS-01` … `A-PRS-01` |
| ValuesStack | 4 | M-13, M-23, M-24 | `A-VAL-01` … `A-VAL-04` |
| ProcessSteps | 3 | M-01, M-03, M-27 | `A-PRC-01` … `A-PRC-03` |
| TeamGrid | 2 | M-01, M-03 | `A-TEAM-01` … `A-TEAM-02` |
| Timeline | 2 | M-01, M-03 | `A-TML-01` … `A-TML-02` |
| CtaBanner | 2 | M-03, M-11 | `A-CTA-01` … `A-CTA-02` |
| AnchorNav | 1 | M-25 | `A-ANC-01` … `A-ANC-01` |
| BlogList | 3 | M-01, M-10 | `A-BLG-01` … `A-BLG-03` |
| BlogPost | 4 | M-03, M-11, M-13, M-27 | `A-BLP-01` … `A-BLP-04` |
| MarqueeTitle | 1 | M-14 | `A-MQT-01` … `A-MQT-01` |
| Contact | 3 | M-01, M-11, M-22 | `A-CNT-01` … `A-CNT-03` |
| SupportContent | 2 | M-13, M-28 | `A-SUP-01` … `A-SUP-02` |
| CartPage | 3 | M-01, M-11, M-13 | `A-CRTP-01` … `A-CRTP-03` |
| AuthForms | 2 | M-01, M-11 | `A-AUTH-01` … `A-AUTH-02` |
| Account | 2 | M-18, M-28 | `A-ACC-01` … `A-ACC-02` |
| NotFound | 2 | M-11, M-14 | `A-NF-01` … `A-NF-02` |
| Sub/ProductCard | 2 | M-09, M-10 | `A-CMP-01` … `A-CMP-02` |
| Sub/ProductCardSmall | 1 | M-10 | `A-CMP-03` … `A-CMP-03` |
| Sub/BlogCard | 1 | M-09 | `A-CMP-04` … `A-CMP-04` |
| Sub/Button | 1 | M-11 | `A-CMP-05` … `A-CMP-05` |
| Sub/ArrowLink | 1 | M-10 | `A-CMP-06` … `A-CMP-06` |
| Sub/Hotspot | 1 | M-12 | `A-CMP-07` … `A-CMP-07` |
| Sub/Marquee | 1 | M-14 | `A-CMP-08` … `A-CMP-08` |
| Sub/Tabs | 1 | M-28 | `A-CMP-09` … `A-CMP-09` |
| Sub/VariantChip | 1 | M-28 | `A-CMP-10` … `A-CMP-10` |
| Sub/AccordionItem | 1 | M-22 | `A-CMP-11` … `A-CMP-11` |
| Sub/SectionHeading | 1 | M-03 | `A-CMP-12` … `A-CMP-12` |

| Tarif | Kullanım | Uygulama yolu |
|---|---|---|
| M-01 | 18 | css-keyframes |
| M-02 | 1 | css-keyframes |
| M-03 | 13 | animejs + io-hook |
| M-04 | 1 | css-keyframes |
| M-05 | 1 | css-transition |
| M-06 | 1 | css-transition |
| M-07 | 2 | animejs |
| M-08 | 1 | css-transition |
| M-09 | 5 | css-transition |
| M-10 | 11 | css-transition |
| M-11 | 11 | css-transition |
| M-12 | 5 | css-keyframes + css-transition |
| M-13 | 6 | layout |
| M-14 | 5 | css-keyframes |
| M-15 | 2 | css-keyframes |
| M-16 | 2 | layout + scroll-scrub |
| M-18 | 2 | layout + css-transition |
| M-19 | 2 | layout + io-hook |
| M-20 | 4 | css-transition + animejs |
| M-21 | 1 | css-transition |
| M-22 | 3 | css-transition |
| M-23 | 1 | scroll-scrub |
| M-24 | 2 | scroll-scrub |
| M-25 | 1 | io-hook + css-transition |
| M-26 | 1 | animejs |
| M-27 | 4 | scroll-scrub |
| M-28 | 11 | css-transition |

## 8. Aktarım sonrası: animasyon üretimi

Tasarım ikas'a aktarıldıktan (statik hali çalışır olduktan) sonra bu bölüm uygulanır.

**1) Hedefleri topla.** Bu dosyadaki tüm `anim-targets` bloklarını tek listeye çıkar:

```bash
python3 - <<'EOF'
import re, sys
src = open("docs/pendev/plan-A-ayni-iskelet-yeni-kimlik.md", encoding="utf-8").read()
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

**3) Ortak parçaları bir kez yaz** (`gizem/src/` altında):

| Parça | Yer | Hangi hedefler |
|---|---|---|
| Motion custom property'leri (`--ease-*`, `--dur-*`) | `src/global.css` | hepsi |
| `useInView(ref, {threshold, once})` | `src/utils/motion/useInView.ts` | `impl` içinde `io-hook` |
| `useScrollProgress(ref)` → CSS değişkeni | `src/utils/motion/useScrollProgress.ts` | `impl` içinde `scroll-scrub` |
| `splitWords(el)` + AnimeJS stagger | `src/utils/motion/revealWords.ts` | M-03 |
| `Marquee`, `Button`, `ArrowLink`, `Hotspot`, `AccordionItem`, `Drawer` | `src/sub-components/<Ad>/` | `via` alanı dolu olan hedefler (animasyon bileşenin içinde, bölümde tekrar yazılmaz) |

**4) Bölüm bölüm uygula.** Her bölüm için sıra: `layout` (sticky) → `css-transition` → `css-keyframes` → `io-hook` → `animejs` → `scroll-scrub`. Her hedefte:
- `layer` = CSS sınıfı; durum sınıfları `is-inview`, `is-active`, `is-open`, `is-loading`.
- `from` / `to` / `timing` değerleri doğrudan kullanılır; token adları (`spring-soft`, `ease-inout`…) `globals.md` §7.1'den.
- `mobile` alanı medya sorgusuna (`@media (max-width: bp(<mobileId>))`), `reducedMotion` alanı `@media (prefers-reduced-motion: reduce)` bloğuna çevrilir.
- SSR çıktısı bitiş halini gösterir; başlangıç hali JS yüklenince eklenen sınıfla verilir.
- Tarayıcı API'leri sadece `useEffect` içinde. AnimeJS: `import { AnimeJS } from "@ikas/bp-storefront"`.
- Bileşen `styles.css` içindeki `@keyframes` adı o bileşene özeldir; birden çok bileşen aynı keyframe'i kullanacaksa `create_theme_global` (kind `keyframe`) ile tema keyframe'i aç.

**5) Doğrula ve işaretle.** `npx ikas-component check --json` → `npx ikas-component build` → editörde 1440 ve 390 genişlikte, ayrıca "hareketi azalt" açıkken kontrol. Tamamlanan hedefte `done: false` → `done: true`.

**Önerilen sıra (etki / emek):** `via` bileşenleri (her yerde görünür) → Header → ana sayfa bölümleri → ProductList / ProductDetail → overlay'ler → içerik sayfaları → scroll-scrub olanlar.

## 9. Bitiş kontrol listesi

Tasarım tarafı (pen.dev):
- [ ] `GetVariables()` 3. bölümdeki tüm değişkenleri içeriyor; tasarımda sabit hex / sabit yazı boyutu yok.
- [ ] 6.2'deki her bölümün `@desktop` ve `@mobile` kök frame'i var, ikisi de `reusable`.
- [ ] 6.3'teki her sayfa yalnızca section instance'larından oluşuyor.
- [ ] `Get(n => n.metadata?.anim …)` çıktısındaki `id`'ler 7. bölümdeki listeyle birebir aynı.
- [ ] Her metin katmanında ya `metadata.prop` var ya da katman bir bileşen instance'ının parçası.
- [ ] Hiçbir frame'de kırpılmış ("clipped") içerik uyarısı yok (maske ve track'ler hariç; onlar bilinçli).
- [ ] Türkçe karakterler (`İ Ş Ğ Ü Ö Ç`) seçilen fontlarda doğru görünüyor.
- [ ] Referansın görselleri, metinleri ve logosu kullanılmadı.

Aktarım tarafı (ikas):
- [ ] Tema global'leri (renk, tipografi, kırılım) açıldı; `list_theme_globals` ile doğrulandı.
- [ ] Her section `check` ve `build` adımından hatasız geçti.
- [ ] 7. bölümdeki tüm hedefler `done: true`.

