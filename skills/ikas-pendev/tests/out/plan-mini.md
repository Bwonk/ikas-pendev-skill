# Plan K — Kaya duman testi
<!-- ikas-pendev contract:2 -->

Tema: **Kaya** (outdoor giyim) · Hedef: pen.dev canvas → ikas Code Components · Referans: https://example.com/ · Dil: tr-TR · Para birimi: TRY

Sözleşme 2 duman testi için küçük veri seti: iki bölüm, bir overlay, iki sayfa.

## 0. Bu dosya nasıl kullanılır

Bu dosya pen.dev'de tasarım üretecek ajana (ya da tasarımcıya) verilen **tek başına yeterli** brifdir. Ölçülerin kaynağı ve motion tariflerinin ayrıntısı için `docs/referans/globals.md`, prop listeleri için `docs/referans/components.md`.

**Sıra:** 3 → 6.0 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5. Her adımın sonunda o adımın kontrol listesi ve ekran görüntüsü.

**Nereye çizilir:** tercihen bu varyant için yeni bir .pen dosyası (`kaya-K.pen`). Aynı dosyada çalışılacaksa tüm kök frame adları `K/` ile başlar ve `FindEmptySpace` ile boş alana yerleştirilir.

**Ajan için hazır komutlar** (sırayla, her biri ayrı tur):
1. `docs/pendev/plan-K-kaya.md dosyasını oku. 3. bölümdeki değişkenleri tanımla ve 6.0'daki Design System frame'lerini üret.`
2. `Aynı planın 6.1 bölümündeki bileşenleri, durumlarıyla birlikte üret.`
3. `6.2'den <bölüm adı> bölümünü desktop ve mobil olarak üret; katman adları ve metadata plandaki gibi olsun.` (bölüm bölüm tekrarla)
4. `6.3'teki sayfaları section instance'larından kur.`
5. `6.4 overlay'lerini ve 6.5 Motion States karelerini üret.`
6. `9. bölümdeki bitiş kontrolünü çalıştır ve eksikleri raporla.`

## 1. Yön ve kimlik

**Konsept: "ZİRVE".** Taş grisi zemin, koyu yeşil vurgu, sakin büyük başlıklar.

- Başlık fontu `Oswald`; arayüz `Barlow`; etiketler `Space Mono`.
- Görseller `Generate("ai" | "stock")` ile üretilir; metinler Türkçe (`İ Ş Ğ Ü Ö Ç` kontrolü).

## 2. Canvas organizasyonu

Her şey **ayrı kök frame**. Kök frame adları sabit kalıpta; ikas'a aktarımda bu adlardan bileşen listesi çıkarılır.

| Sıra (yukarıdan aşağı) | Kök frame adı | İçerik | Boyut |
|---|---|---|---|
| 00 | `K/DS/Colors`, `K/DS/Typography`, `K/DS/Spacing`, `K/DS/Icons`, `K/DS/Motion`, `K/DS/Imagery` | Design system sayfaları | serbest |
| 01 | `K/Sub/<Ad>` (reusable) ve `K/Sub/<Ad> — <durum>` | Bileşenler ve durumları | içeriğe göre |
| 02 | `K/Section/<Ad>@desktop` ve `K/Section/<Ad>@mobile` (ikisi de reusable) | Bölümler | 1440 / 390 genişlik |
| 03 | `K/Page/<Ad>@desktop` ve `K/Page/<Ad>@mobile` | Sayfalar (section instance'ları) | 1440 / 390 |
| 04 | `K/Overlay/<Ad>@desktop — <durum>` ve `…@mobile — <durum>` | Menü, sepet, arama, paneller | 1440×900 / 390×844 |
| 05 | `K/Motion/<tarif> <bölüm>` | Animasyon kareleri (başlangıç / ara / bitiş) | içeriğe göre |

Yerleşim: her sıra bir yatay bant; bantlar arası 800, frame'ler arası 200 boşluk. Bir bölümün desktop ve mobil frame'i **yan yana**. Kök seviyede metin, ikon ya da serbest şekil bırakılmaz; açıklamalar `note` node'u olarak ilgili frame'in yanına konur.

Kurallar:
- Desktop kök frame'lerinde `theme: {device: "desktop"}`, mobil olanlarda `theme: {device: "mobile"}`; koyu bölümlerde ayrıca `mode: "dark"` (varsayılan `mode: "light"`). Boyut değişkenleri buna göre kendiliğinden değişir; mobil frame'de ayrıca sayı yazılmaz.
- Bölüm frame'leri `layout: "vertical"` ya da `"horizontal"`, `clip: true`. `layout: "none"` sadece gerçekten üst üste binen katmanlarda (slaytlar, görsel + gradyan + metin, hotspot).
- Tekrarlanan her şey `reusable` bileşenin `ref` instance'ıdır (ProductCard, Button, ArrowLink…). Sayfalar yalnızca section `ref`'lerinden oluşur.
- Çalışılan kök frame `placeholder: true`; bitince kaldırılır.
- Değer yazarken sayı yerine değişken: renk, font, yazı boyutu, boşluk hep `$…`.
- Görsel ve logo `Generate("ai" | "stock" | "svg")` ile üretilir; referansın görsel adresleri hiçbir `fill`'de kullanılmaz.
- Kök frame `metadata`'sı **oluşturulurken** yazılır (sonradan eklenen metadata kaybolabilir); ayrıntı 4. bölümde.

## 3. Değişkenler

İlk iş olarak tanımlanır. Adlar sözleşmede sabittir (`globals.md` ile eşleşir); değerler bu temaya özgüdür.

```js
SetVariables({
  "color-bg": {type:"color", value:[{value:"#E9E7E2", theme:{mode:"light"}}, {value:"#151614", theme:{mode:"dark"}}]},
  "color-text": {type:"color", value:[{value:"#151614", theme:{mode:"light"}}, {value:"#E9E7E2", theme:{mode:"dark"}}]},
  "color-muted": {type:"color", value:[{value:"#5E615B", theme:{mode:"light"}}, {value:"#9A9D96", theme:{mode:"dark"}}]},
  "color-line": {type:"color", value:[{value:"#151614", theme:{mode:"light"}}, {value:"#E9E7E2", theme:{mode:"dark"}}]},
  "color-surface": {type:"color", value:[{value:"#DCD9D2", theme:{mode:"light"}}, {value:"#20221F", theme:{mode:"dark"}}]},
  "color-inverse-bg": {type:"color", value:[{value:"#151614", theme:{mode:"light"}}, {value:"#E9E7E2", theme:{mode:"dark"}}]},
  "color-inverse-text": {type:"color", value:[{value:"#E9E7E2", theme:{mode:"light"}}, {value:"#151614", theme:{mode:"dark"}}]},
  "color-accent": {type:"color", value:[{value:"#1F5A3A", theme:{mode:"light"}}, {value:"#3E9B67", theme:{mode:"dark"}}]},
  "color-accent-text": {type:"color", value:[{value:"#FFFFFF", theme:{mode:"light"}}, {value:"#151614", theme:{mode:"dark"}}]},
  "color-scrim": {type:"color", value:[{value:"#15161499", theme:{mode:"light"}}, {value:"#151614B3", theme:{mode:"dark"}}]},
  "color-transparent": {type:"color", value:[{value:"#E9E7E200", theme:{mode:"light"}}, {value:"#15161400", theme:{mode:"dark"}}]},
  "color-danger": {type:"color", value:[{value:"#B3261E", theme:{mode:"light"}}, {value:"#F2B8B5", theme:{mode:"dark"}}]},
  "color-success": {type:"color", value:[{value:"#1F5A3A", theme:{mode:"light"}}, {value:"#3E9B67", theme:{mode:"dark"}}]},
  "font-display": {type:"string", value:"Oswald"},
  "font-ui": {type:"string", value:"Barlow"},
  "font-body": {type:"string", value:"Barlow"},
  "font-price": {type:"string", value:"Barlow Condensed"},
  "font-mono": {type:"string", value:"Space Mono"},
  "text-display": {type:"number", value:[{value:120, theme:{device:"desktop"}}, {value:56, theme:{device:"mobile"}}]},
  "text-h2": {type:"number", value:[{value:80, theme:{device:"desktop"}}, {value:40, theme:{device:"mobile"}}]},
  "text-h3": {type:"number", value:[{value:48, theme:{device:"desktop"}}, {value:32, theme:{device:"mobile"}}]},
  "text-h4": {type:"number", value:[{value:28, theme:{device:"desktop"}}, {value:22, theme:{device:"mobile"}}]},
  "text-title": {type:"number", value:[{value:20, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "text-ui": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:15, theme:{device:"mobile"}}]},
  "text-ui-sm": {type:"number", value:[{value:14, theme:{device:"desktop"}}, {value:13, theme:{device:"mobile"}}]},
  "text-badge": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-label": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-body": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:15, theme:{device:"mobile"}}]},
  "text-price": {type:"number", value:[{value:20, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "space-page": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-grid": {type:"number", value:[{value:8, theme:{device:"desktop"}}, {value:4, theme:{device:"mobile"}}]},
  "space-card": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:10, theme:{device:"mobile"}}]},
  "space-panel": {type:"number", value:[{value:24, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-xs": {type:"number", value:4},
  "space-sm": {type:"number", value:8},
  "space-md": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:12, theme:{device:"mobile"}}]},
  "space-section": {type:"number", value:[{value:120, theme:{device:"desktop"}}, {value:64, theme:{device:"mobile"}}]},
  "size-header": {type:"number", value:[{value:72, theme:{device:"desktop"}}, {value:60, theme:{device:"mobile"}}]},
  "size-line": {type:"number", value:1},
  "opacity-inactive": {type:"number", value:0.35},
  "size-logo": {type:"number", value:[{value:28, theme:{device:"desktop"}}, {value:22, theme:{device:"mobile"}}]},
})
```

Çekirdek set **41 değişken**dir ve adları değişmez (aktarım bu adlara güvenir). Sözleşme 2 ekleri: `color-transparent` (gradyan başlangıcı, `#RRGGBB00`), `size-logo` (logo yüksekliği, `device` ekseni), `color-danger` ve `color-success` (form ve stok durumları). Eksenler: `device: desktop | mobile`, `mode: light | dark`.

Font doğrulama: `execute` yanıtında "Font family … is invalid" uyarısı çıkarsa o değişkeni değiştir. Canvas üzerinde denenip geçerli çıkan aileler: `Barlow`, `Barlow Condensed`, `Oswald`, `Space Mono`. Geçersiz çıkanlar: `Mona Sans Condensed`, `Big Shoulders Display`. ikas yalnızca Google Fonts (latin-ext) yükler; seçilen her aile orada da bulunmalı.

Yazı stili eşlemesi: `text-display`, `text-h2`, `text-h3`, `text-h4` → `$font-display`, satır yüksekliği 1.0 · `text-title`, `text-ui`, `text-ui-sm`, `text-badge` → `$font-ui`, 600, satır 1.2 · `text-label` → `$font-mono` · `text-body` → `$font-body`, 400, satır 1.45 · `text-price` → `$font-price`, 700. Başlıklar büyük harf.

## 4. Adlandırma ve metadata sözleşmesi

Amaç: tasarımdan koda çeviri mekanik olsun.

| pen.dev | ikas / kod |
|---|---|
| Kök frame `K/Section/HeroSlider@desktop` | section bileşeni **HeroSlider** (`src/components/HeroSlider/`) |
| Kök frame `K/Sub/ProductCard` | sub-component **ProductCard** (`src/sub-components/ProductCard/`) |
| Kök frame `K/Overlay/CartDrawer…` | ilgili section'ın alt bileşeni |
| Katman adı `hero-title` (kebab-case) | CSS sınıfı `.hero-title` |
| `ref` instance adı = bileşen adı (`ProductCard`) | JSX `<ProductCard />` |
| Metin katmanı + `metadata.prop` | TEXT prop (JSX'te sabit metin olmaz) |
| Görsel dolgulu frame + `metadata.prop` | IMAGE / PRODUCT / CATEGORY prop |
| Tekrarlanan çocuk grubu + `metadata.prop` | COMPONENT_LIST ya da *_LIST prop |
| Metin katmanı + `metadata.textClass: "data"` + `source` | mağaza verisi (ör. `product.name`); prop değil, JSX'te veri bağlamasıdır |
| Metin katmanı + `metadata.textClass: "code"` | kodda üretilen metin (sayaç, biçimli tutar, durum etiketi) |
| Section kök frame'i + `prop: "backgroundColor"` | her section'da zorunlu `backgroundColor` COLOR prop'u |
| `metadata.anim` | 7. bölümdeki animasyon hedefi |

Katman ağaçlarındaki `{ad:TİP}` notasyonu o katmanın `metadata.prop` ve `metadata.propType` değeridir. `{data:kaynak}` metnin mağaza verisinden geldiğini (`textClass: "data"`, `source: "kaynak"`), `{code:ad}` metnin kodda üretildiğini (`textClass: "code"`) gösterir. Ağaçta tırnak içinde yazılan her örnek metin bu üç işaretten birini taşır; işaretsiz sabit metin yoktur.

**Metadata (düz anahtarlar; iç içe nesne kullanma):**

```js
// kök frame
metadata: {type:"kaya", role:"section", ikas:"HeroSlider", device:"desktop", variant:"K", contract:2, prop:"backgroundColor", propType:"COLOR"}
// role: "ds" | "sub" | "section" | "overlay" | "page" | "motion"

// prop'a bağlı katman
metadata: {type:"kaya", role:"prop", prop:"title", propType:"TEXT", textClass:"prop"}

// mağaza verisi gösteren metin (prop değil)
metadata: {type:"kaya", textClass:"data", source:"product.name"}

// kodda üretilen metin
metadata: {type:"kaya", textClass:"code"}

// animasyonlu katman (prop'a da bağlıysa aynı nesnede)
metadata: {type:"kaya", role:"anim", anim:"K-HERO-02", recipe:"M-07", trigger:"state-change", prop:"title", propType:"TEXT", textClass:"prop"}
context: "K-HERO-02 · M-07 · başlık slaytla birlikte değişir"
```

- Bir katmanda birden çok hedef varsa `anim` virgülle ayrılır: `"K-HERO-01,K-HERO-07"`.
- `context` hem insan için kısa açıklamadır hem de katmandaki **tüm** anim id'lerini içermek zorundadır. pen.dev instance ve override'larda `metadata` saklamaz; makine `metadata.anim` ∪ `context` okur.
- Metadata yalnızca node **oluşturulurken** güvenle yazılır. Sonradan değişecekse yeni node eklenir, eskisi silinir.
- Her metin node'unda `textClass` zorunludur: `"prop"` → `prop` + `propType`; `"data"` → `source`; `"code"` → ek alan yok.
- Section kök frame'leri `prop: "backgroundColor"`, `propType: "COLOR"` taşır; kök `contract: 2` yazar.

## 5. Animasyona hazır tasarım kuralları

pen.dev hareket göstermez. Aşağıdaki yapılar çizilmezse aktarımda katmanları yeniden kurmak gerekir.

1. **Bitiş hali çizilir.** Bölüm ve sayfa frame'leri animasyon bittikten sonraki görünümü gösterir. Başlangıç ve ara haller sadece `K/Motion/…` frame'lerinde.
2. **Maske = `clip: true` frame.** Kayarak giren her metin satırı kendi `…-mask` frame'inin içindedir; maske metinle aynı boyutta. Çok satırlı başlıkta her satır ayrı metin node'u ve ayrı maske.
3. **Roll eden öğeler çift kopyadır.** Buton, nav linki ve ok ikonunda `top` (görünen) ve `bottom` (maske dışında bekleyen) kopyaları birlikte çizilir; kap `clip: true`.
4. **Sonsuz kayanlar track + kopya.** `marquee` / `ticker` kabı `clip: true`; içindeki `…-track` içerik setini en az iki kez barındırır ve kabın dışına taşar.
5. **Yer değiştirenler kardeş frame.** Slaytlar, sekme içerikleri, ön/arka ürün görseli aynı ebeveynde üst üste (`layout: "none"`); görünmeyenler `opacity: 0` ile durur, silinmez.
6. **İlerleme göstergesi ayrı katman.** `progress-bar` dolgusu ebeveyninden ayrı bir dikdörtgen; yarı dolu çizilir.
7. **Sticky alanlar gerçek yükseklikte.** Sabit kalan öğenin kabı, kaydırma boyunca kat edeceği yükseklikte çizilir (ör. 4 görsellik galeri yanında tek detay sütunu).
8. **Overlay ayrı frame.** Menü, çekmece, arama: `scrim` + panel, sayfa frame'inin kopyası üzerinde değil, kendi kök frame'inde; açık ve boş/dolu halleri ayrı.
9. **Kaydırmaya bağlı öğeler serbest katman.** Dönen/kayan görsel ya da parallax arka plan, akıştan bağımsız (`layoutPosition: "absolute"`) ve kabından büyük çizilir.
10. **Hover hali ayrı frame.** Her etkileşimli bileşenin hover hali `K/Sub/<Ad> — hover` olarak çizilir; bölüm içinde tekrar çizilmez.
11. **Her hedef işaretli.** 6. bölümde `anim-targets` bloğunda geçen her `layer`, tasarımda aynı adla bulunur ve `metadata.anim` taşır; id'ler `context` alanında da yazılıdır.
12. **Mobil hali kararlaştırılmış.** Hedefin `mobile` alanı "kapalı" ya da farklıysa mobil frame o hale göre çizilir (ör. sticky yok → normal akış).

### 5.1 Bu plana özgü motion tarifleri

`globals.md` kataloğuna ek olarak (M-xx tarifleri orada):

| ID | Ad | Hareket | Zorunlu katman yapısı | Uygulama | Mobil | Azaltılmış hareket |
|---|---|---|---|---|---|---|
| **K-M-01** | Katman kayması | Görsel katmanları kaydırmayla farklı hızda kayar. `{ layer.y: 0 } → { layer.y: -60 }`, `{ scrub: true }` | her katman ayrı node; `layoutPosition: "absolute"` | scroll-scrub | kapalı | kapalı |

## 6. Yapım sırası

### 6.0 Design System frame'leri

| Kök frame | İçerik |
|---|---|
| `K/DS/Colors` | Her renk değişkeni için örnek kare + ad + hex; metin/zemin kontrast çiftleri (metin, muted, vurgu üzerinde metin) |
| `K/DS/Typography` | 11 yazı stili, her biri desktop ve mobil boyutunda örnek satırla (Türkçe karakterli: "ZİRVEDE ŞIK ÇÖZÜM 2.450 TL") |
| `K/DS/Spacing` | Boşluk ölçeği çubukları; 1440 ve 390 için ızgara şeması (kenar boşluğu, sütunlar, aralık); çizgi kalınlığı |
| `K/DS/Icons` | Kullanılan tüm ikonlar 20×20 (arama, hesap, sepet, menü, kapat, filtre, ok ↗, artı, eksi) + logo ve işaret |
| `K/DS/Motion` | Kullanılan tarif ID'leri, kısa açıklama ve tetikleyici simgeleri; `note` node'ları ile. Bu frame animasyon "lejantı"dır |
| `K/DS/Imagery` | Görsel dili: `Generate("ai" | "stock")` ile üretilmiş 3–4 örnek kare (kadraj, ışık, renk notu `note` ile); logo ve işaret `Generate("svg")` ile. Referans görseli kullanılmaz |

### 6.1 Bileşenler (`K/Sub/…`)

Her bileşen `reusable` kök frame; durumlar yanında ayrı frame. Önce bunlar, çünkü bölümler bunların instance'larını kullanır.

| Bileşen | Yapı | Durumlar (ayrı frame) |
|---|---|---|
| `Button` | `button` (clip) içinde `top` + `bottom` kopya; yükseklik 48; text-ui | varsayılan · hover · pasif · yükleniyor · eklendi · stok yok |
| `ArrowLink` | `link`: etiket text-ui + `link-line` + `link-arrow` (clip: `arrow-top` + `arrow-bottom`) | varsayılan · hover |
| `ProductCard` | `card-images` (clip, 3:4): `image-front` + `image-back` · `card-info`: `card-title` · `price` | varsayılan · hover · stok yok |

Sözleşme 2 zorunlu ekleri (lint ve `pendev_checks.js` arar):
- `Button` durumları arasında `eklendi` ve `stok yok` var (sepete ekle akışı; ProductDetail ve hızlı ekle bunları kullanır).
- `K/Overlay/FilterDrawer@mobile` (mobil filtre çekmecesi) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili.
- `K/Overlay/QuickBuy@desktop` ve `@mobile` (hızlı al penceresi: açık · seçim eksik · ekleniyor) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili; ProductCard'ın sepet düğmesi açar.
- Ürün detayda ikas mağaza blokları (`pdp-rating`, `pdp-campaign`, `pdp-offers`, `pdp-pay`, `pdp-bundle`, `pdp-tiers`, `pdp-options`, `pdp-group`, `pdp-back-in-stock`), ayrı `ProductReviews` section'ı; sepet sayfası ve çekmecede kampanya satırları, uygulanan kupon, öneri şeridi; `OfferCard`, `BundleItem`, `RatingStars`, `ReviewCard` Sub'ları ve CartLineItem'ın indirimli · hediye · set · kişiselleştirilmiş halleri (06-page-coverage §3b).
- Mağaza tamamlama (06-page-coverage §3c): Toast, CookieBar, ImagePreview, LocaleSwitcher, AccountMenu overlay'leri (özel hesapta AddressModal + ConfirmModal); RichText ve OrderTracking section'ları; filtre tipleri, varyant swatch'ları, galeride video, sosyal/SMS giriş, sipariş detayı ve hesap ayarları katmanları; VariantSwatch, PriceRange, SocialLoginButton, Skeleton Sub'ları.
- Her section kök frame'i `backgroundColor` COLOR prop'unu taşır; her metin node'u `textClass` taşır.

Bileşen animasyon hedefleri (bölümlerde `via` ile anılır, kodu bileşenin içinde yazılır):

<!-- anim-targets:start -->
```yaml
- id: K-CMP-01
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
- id: K-CMP-02
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
```
<!-- anim-targets:end -->

### 6.2 Bölümler ve overlay'ler

Her başlık bir kök frame çiftidir (`@desktop` + `@mobile`). "ikas" satırı aktarımda başlanacak şablonu gösterir.

#### Section/HeroBanner
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** hero-slider-section (uyarlanır)
- **Prop'lar:** `title`, `buttonText` TEXT · `image` IMAGE · `link` LINK · `backgroundColor` COLOR
- **Desktop:** 1440 × 760; tam kaplama görsel, sol altta başlık ve buton.
- **Mobil:** 390 × 520; başlık text-display (mobil).

```
hero-banner
├─ hero-image                        {image:IMAGE}, kabından %15 yüksek
├─ hero-title-mask (clip) → hero-title   {title:TEXT} text-display "ZİRVEYE ÇIK"
├─ hero-counter                      {code:slideCounter} font-mono "01 / 03"
└─ hero-button (clip)                {buttonText:TEXT}; top + bottom kopya
```

Kontrol: başlık kendi clip maskesinde

<!-- anim-targets:start -->
```yaml
- id: K-HERO-01
  section: HeroBanner
  layer: hero-image
  recipe: K-M-01
  trigger: scroll-scrub
  what: "Görsel \"katman\" hızıyla kayar"
  from: { layer.y: 0 }
  to: { layer.y: -60 }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: K-HERO-02
  section: HeroBanner
  layer: hero-title
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
- id: K-HERO-03
  section: HeroBanner
  layer: hero-button
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

#### Section/ProductGrid
- **Kullanıldığı yer:** Ana sayfa, kategori
- **ikas:** category-list-section
- **Prop'lar:** `title` TEXT · `productList` PRODUCT_LIST · `filterButtonText` TEXT · `backgroundColor` COLOR
- **Mod:** `mode: "dark"`
- **Desktop:** 1440; başlık satırı + 4 sütun ızgara (kart 344×460), aralık $space-grid.
- **Mobil:** 2 sütun; "FİLTRE" butonu FilterDrawer'ı açar.

```
product-grid-section
├─ grid-header
│   ├─ grid-title                    {title:TEXT} text-h2
│   ├─ grid-count                    {data:category.productCount} font-mono
│   └─ filter-button                 {filterButtonText:TEXT}
└─ product-grid
    └─ ProductCard ×8                {productList:PRODUCT_LIST}; card-images → image-front + image-back
        ├─ card-title                {data:product.name}
        └─ price                     {data:product.price}
```

Kontrol: en az 8 kart

<!-- anim-targets:start -->
```yaml
- id: K-GRID-01
  section: ProductGrid
  layer: product-grid
  recipe: M-01
  trigger: inview
  what: "Kartlar sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.05 }
  impl: animejs + io-hook
  mobile: aynı
  reducedMotion: anında
  done: false
- id: K-GRID-02
  section: ProductGrid
  layer: image-back
  via: ProductCard
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
```
<!-- anim-targets:end -->

#### Overlay/FilterDrawer
- **Kullanıldığı yer:** ProductGrid (mobil)
- **ikas:** ProductGrid sub-component
- **Desktop:** Desktop karşılığı yok (filtreler satır içinde).
- **Mobil:** Alttan açılan tam genişlik çekmece; arkada `scrim`.

```
filter-overlay
├─ scrim
└─ filter-drawer
    ├─ filter-header                 {filterTitle:TEXT} + close-button
    ├─ filter-group ×3               {data:category.filterName} + filter-option ×N
    └─ apply-button (clip)           {applyText:TEXT}; top + bottom kopya
```

Kontrol: açık ve seçimli halleri ayrı frame

<!-- anim-targets:start -->
```yaml
- id: K-FILT-01
  section: FilterDrawer
  layer: filter-drawer
  recipe: M-20
  trigger: click
  what: "Çekmece alttan kayar, scrim belirir"
  from: { y: 100%, scrim.opacity: 0 }
  to: { y: 0, scrim.opacity: 1 }
  timing: { spring: spring-drawer, scrim.duration: 0.4, rows.stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: css-transition + animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
- id: K-FILT-02
  section: FilterDrawer
  layer: filter-group
  recipe: M-22
  trigger: click
  what: "Filtre grubu akordeon olarak açılır"
  from: { height: 0, icon.rotate: 0 }
  to: { height: auto, icon.rotate: 45 }
  timing: { spring: "bounce 0, 0.5s" }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/QuickBuy
- **Kullanıldığı yer:** Header (ProductCard sepet düğmesi açar)
- **ikas:** Header sub-component (variant-selection + add-to-cart + PayWithIkas)
- **Desktop:** Ortada pencere; solda görsel, sağda ad, fiyat, varyant çipleri, adet + Sepete ekle, Hızlı Öde yuvası.
- **Mobil:** Alttan açılan alt sayfa; küçük görsel + ad + fiyat, altında çipler ve eylemler.

```
quickbuy-overlay
├─ scrim
└─ quickbuy-panel
    ├─ qb-media                      {data:product.image}
    └─ qb-details
        ├─ qb-head                   {data:product.name} + close-button {closeAriaLabel:TEXT}
        ├─ qb-variant-group ×2       {data:variant.name} + variant-chip ×N
        ├─ qb-variant-error          {chooseOptionText:TEXT}
        └─ qb-actions                add-to-cart-button {addText:TEXT} / {addingText:TEXT}
```

Kontrol: açık · seçim eksik · ekleniyor halleri ayrı frame

<!-- anim-targets:start -->
```yaml
- id: K-QB-01
  section: QuickBuy
  layer: quickbuy-panel
  recipe: M-20
  trigger: click
  what: "Pencere açılır, scrim belirir"
  from: { opacity: 0, scale: 0.96 }
  to: { opacity: 1, scale: 1 }
  timing: { spring: spring-drawer, scrim.duration: 0.4, rows.stagger: [0.2, 0.3, 0.4, 0.5] }
  impl: css-transition + animejs
  mobile: tam genişlik
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

### 6.3 Sayfalar

Her sayfa için `K/Page/<Ad>@desktop` ve `@mobile`: dikey layout, `clip: true`, çocukları yalnızca section instance'ları.

| Sayfa | Bölümler (sırayla) | ikas sayfa tipi |
|---|---|---|
| `Home` | HeroBanner · ProductGrid | `INDEX` |
| `Category` | ProductGrid (filtreli) | `CATEGORY` |

### 6.4 Overlay frame'leri

6.2'de "Overlay" başlıklı her öğe için, yarı saydam bir sayfa görüntüsü yerine düz `$color-scrim` zemin üzerinde panel çizilir. Her biri desktop (1440×900) ve mobil (390×844), belirtilen durumlarıyla ayrı kök frame.

Çizilecek overlay kök frame'leri (her durum ayrı frame, ad sonuna ` — <durum>`):
- `K/Overlay/FilterDrawer@mobile — <durum>`
- `K/Overlay/QuickBuy@desktop — <durum>`
- `K/Overlay/QuickBuy@mobile — <durum>`

### 6.5 Motion States

Aşağıdaki tariflerin her biri için **bir** örnek üzerinde 2–3 kare çizilir (kök frame `K/Motion/<tarif> <bölüm>`; kareler soldan sağa, altlarında `note` ile yüzde/an bilgisi). Diğer kullanım yerleri aynı mantığı izler.

| Tarif | Örnek bölüm | Çizilecek kareler |
|---|---|---|
| M-03 | HeroBanner (`hero-title`) | başlık: kelimeler maske altında (görünmez) → yarısı girmiş → hepsi yerinde |
| M-09 | ProductGrid (`image-back`) | ürün kartı: ön görsel → arka görsel + dönmüş ok |
| M-11 | HeroBanner (`hero-button`) | buton: varsayılan → dolgu yarı yolda → ters dolgu |
| M-20 | FilterDrawer (`filter-drawer`) | çekmece: kapalı (sayfa) → yarı açık + scrim → açık |
| M-22 | FilterDrawer (`filter-group`) | akordeon: kapalı → açık |
| K-M-01 | HeroBanner (`hero-image`) | katmanlar: üst üste → ayrışmış → en uçta |

## 7. Animasyon hedefleri özeti

Toplam **10 hedef**. Ayrıntılar 6.1 ve 6.2'deki `anim-targets` bloklarında.

| Bölüm | Hedef | Tarifler | ID aralığı |
|---|---|---|---|
| HeroBanner | 3 | M-03, M-11, K-M-01 | `K-HERO-01` … `K-HERO-03` |
| ProductGrid | 2 | M-01, M-09 | `K-GRID-01` … `K-GRID-02` |
| FilterDrawer | 2 | M-20, M-22 | `K-FILT-01` … `K-FILT-02` |
| QuickBuy | 1 | M-20 | `K-QB-01` … `K-QB-01` |
| Sub/Button | 1 | M-11 | `K-CMP-01` … `K-CMP-01` |
| Sub/ArrowLink | 1 | M-10 | `K-CMP-02` … `K-CMP-02` |

| Tarif | Kullanım | Uygulama yolu |
|---|---|---|
| M-01 | 1 | css-keyframes |
| M-03 | 1 | animejs + io-hook |
| M-09 | 1 | css-transition |
| M-10 | 1 | css-transition |
| M-11 | 2 | css-transition |
| M-20 | 2 | css-transition + animejs |
| M-22 | 1 | css-transition |
| K-M-01 | 1 | scroll-scrub |

## 8. Aktarım sonrası: animasyon üretimi

Tasarım ikas'a aktarıldıktan (statik hali çalışır olduktan) sonra bu bölüm uygulanır.

**1) Hedefleri topla.** Bu dosyadaki tüm `anim-targets` bloklarını tek listeye çıkar:

```bash
python3 - <<'EOF'
import re, sys
src = open("docs/pendev/plan-K-kaya.md", encoding="utf-8").read()
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

pen.dev, bileşen instance'larında ve override'larında `metadata` saklamaz; bu hedeflerin `id`'si katmanın `context` alanında durur. Sadece `metadata.anim` okunursa instance hedefleri listeden düşer, o yüzden `context` da taranır:

```js
Get(n => n.context && /K-[A-Z]{2,}-\d\d/.test(n.context) ? Print(n.context.match(/K-[A-Z]{2,}-\d\d/g).join(","), "|", n.name, "| context") : undefined)
```

İki çıktının birleşimi 7. bölümdeki listeyle karşılaştırılır.

**3) Ortak parçaları bir kez yaz** (`kaya/src/` altında):

| Parça | Yer | Hangi hedefler |
|---|---|---|
| Motion custom property'leri (`--ease-*`, `--dur-*`) | `src/global.css` | hepsi |
| `useInView(ref, {threshold, once})` | `src/utils/motion/useInView.ts` | `impl` içinde `io-hook` |
| `useScrollProgress(ref)` → CSS değişkeni | `src/utils/motion/useScrollProgress.ts` | `impl` içinde `scroll-scrub` |
| `splitWords(el)` + AnimeJS stagger | `src/utils/motion/revealWords.ts` | M-03 |
| `Button`, `ArrowLink`, `Drawer` | `src/sub-components/<Ad>/` | `via` alanı dolu olan hedefler (animasyon bileşenin içinde, bölümde tekrar yazılmaz) |

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

Tasarım tarafı (pen.dev). Her madde `pendev_checks.js` içindeki bir CHK id'sidir (`extract_targets.py --js all` → `execute`; çıktı `CHK|<id>|PASS|FAIL|WARN|…`):
- [ ] `CHK vars`: `GetVariables()` 3. bölümdeki 41 çekirdek değişkeni ve eksenleri (`device`, `mode`) içeriyor.
- [ ] `CHK hardcoded`: tasarımda sabit hex dolgu, sabit yazı boyutu ya da sabit font ailesi yok; hepsi `$…`.
- [ ] `CHK sections`: 6.2'deki her bölümün `@desktop` ve `@mobile` kök frame'i var, ikisi de `reusable`.
- [ ] `CHK pages`: 6.3'teki her sayfa yalnızca section instance'larından oluşuyor; cihaz ekleri eşleşiyor.
- [ ] `CHK overlays`: 6.4'teki her overlay kök frame'i durumlarıyla birlikte var.
- [ ] `CHK anim`: `metadata.anim` ∪ `context` taramasındaki (8. bölüm, 2. adım) `id`'ler 7. bölümdeki listeyle birebir aynı.
- [ ] `CHK textclass`: her metin node'unda `textClass` var (`prop` → `prop` + `propType`; `data` → `source`).
- [ ] `CHK clip`: kırpılmış ("clipped") içerik yok; mask, track, marquee, ticker, pin, stage ve curtain kapları bilinçli olarak hariç.
- [ ] `CHK rootmeta`: her kök frame'de `type`, `role`, `ikas`, `device`, `variant`, `contract: 2` metadata'sı var.
- [ ] `CHK bgprop`: her section kök frame'i `prop: "backgroundColor"`, `propType: "COLOR"` taşıyor.
- [ ] `CHK placeholder`: hiçbir kök frame `placeholder: true` olarak kalmadı.
- [ ] `CHK refassets`: referansın görselleri, metinleri ve logosu kullanılmadı (referans sadece ilham; görsel, metin ve logo kullanılmaz); hiçbir `fill` referans alan adını içermiyor.
- [ ] `CHK ds`: `K/DS/Colors`, `Typography`, `Spacing`, `Icons`, `Motion`, `Imagery` frame'leri var.
- [ ] Türkçe karakterler (`İ Ş Ğ Ü Ö Ç`) seçilen fontlarda doğru görünüyor (ekran görüntüsüyle).

Aktarım tarafı (ikas):
- [ ] Tema global'leri (renk, tipografi, kırılım) açıldı; `list_theme_globals` ile doğrulandı.
- [ ] Her section `check` ve `build` adımından hatasız geçti.
- [ ] 7. bölümdeki tüm hedefler `done: true`.

