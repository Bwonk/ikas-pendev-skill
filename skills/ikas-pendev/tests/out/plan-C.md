# Plan C — Serbest yorum

Tema: **Gizem** (streetwear) · Hedef: pen.dev canvas → ikas Code Components · Referans: https://axm.framer.website/

Referans sadece ilham: kalite çıtası ve "ızgara + büyük tipografi + hareket" fikri alınır; bölüm kurgusu, palet ve imza animasyonları yeniden tasarlanır.

## 0. Bu dosya nasıl kullanılır

Bu dosya pen.dev'de tasarım üretecek ajana (ya da tasarımcıya) verilen **tek başına yeterli** brifdir. Ölçülerin kaynağı ve motion tariflerinin ayrıntısı için `docs/referans/globals.md`, prop listeleri için `docs/referans/components.md`.

**Sıra:** 3 → 6.0 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5. Her adımın sonunda o adımın kontrol listesi ve ekran görüntüsü.

**Nereye çizilir:** tercihen bu varyant için yeni bir .pen dosyası (`gizem-C.pen`). Aynı dosyada çalışılacaksa tüm kök frame adları `C/` ile başlar ve `FindEmptySpace` ile boş alana yerleştirilir. Dosyadaki `axm.framer.website` adlı 8 frame referansın ham import'udur: **sadece bakmak için**; içinden katman kopyalanmaz, silinmez, değiştirilmez.

**Ajan için hazır komutlar** (sırayla, her biri ayrı tur):
1. `docs/pendev/plan-C-serbest-yorum.md dosyasını oku. 3. bölümdeki değişkenleri tanımla ve 6.0'daki Design System frame'lerini üret.`
2. `Aynı planın 6.1 bölümündeki bileşenleri, durumlarıyla birlikte üret.`
3. `6.2'den <bölüm adı> bölümünü desktop ve mobil olarak üret; katman adları ve metadata plandaki gibi olsun.` (bölüm bölüm tekrarla)
4. `6.3'teki sayfaları section instance'larından kur.`
5. `6.4 overlay'lerini ve 6.5 Motion States karelerini üret.`
6. `9. bölümdeki bitiş kontrolünü çalıştır ve eksikleri raporla.`

## 1. Yön ve kimlik

**Konsept: "ŞİFRE".** Gizem = çözülmeyi bekleyen şey. Tema bir sokak fanzini gibi: kağıt zemin, sert siyah çizgiler, dev dar başlıklar, daktilo/mono etiketler, bant ve sticker'lar. İmza hareketi **şifre çözme** (C-M-01): başlıklar ve linkler karışık karakterlerden çözülerek belirir.

**Referanstan farklar:**
- **Açık zemin** (kağıt) varsayılan; Manifesto, Footer, MenuOverlay ve TickerStrip **ters palette** (koyu). pen.dev'de `mode: light | dark` tema ekseni; ikas'ta iki paletli color scheme (`Paper`, `Ink`).
- Çizgiler 2px ve tam siyah; kartlar **bitişik** (ızgara aralığı 0). Referanstaki 5px aralıklı ince gri ızgaranın tersi.
- Vurgu: sıcak kırmızı-turuncu `$color-accent`; sticker, rozet, ticker şeridi ve hover vurgularında.
- Başlık fontu `Sofia Sans Extra Condensed` (çok dar, çok uzun); arayüz `Archivo Narrow`; etiketler `Space Mono`.
- Megamenu yok → tam ekran numaralı menü. Ürün sunumu tablo-liste (ProductIndex) + yatay sabitlenmiş lookbook + bitişik 4 sütun ızgara. Instagram şeridi yerine sticker duvarı. PDP'de çekmece yerine akordeon ve 2 sütun görsel mozaiği.
- Görsel dili: flaşlı sokak çekimi, grenli, hafif sıcak; fotoğraflar beyaz çerçeveli (polaroid) ya da tam kesim. `Generate("ai" | "stock")` ile özgün üretilir.
- Metinler Türkçe, büyük harf (`İ Ş Ğ Ü Ö Ç` kontrolü). Mono metinlerde kod hissi: `DROP 07 / KIŞ 26`, `001`, `[ MAĞAZA ]`.

**Örnek içerik:** ticker `ÜCRETSİZ KARGO 750 TL+ ✳ YENİ DROP CUMA 20:00 ✳ 30 GÜN İADE` · hero `SOKAK KONUŞUR.` / `ŞİFREYİ ÇÖZ.` / `GECE BİZİM.` · sticker `SINIRLI ÜRETİM`, `YENİ`, `SON 12 ADET` · manifesto `BİZ GÜRÜLTÜ YAPMAYIZ. KUMAŞ KONUŞUR, KESİM ANLATIR, SOKAK DİNLER.` · butonlar `[ DROP'A GİT ]`, `[ SEPETE EKLE ]`.

## 2. Canvas organizasyonu

Her şey **ayrı kök frame**. Kök frame adları sabit kalıpta; ikas'a aktarımda bu adlardan bileşen listesi çıkarılır.

| Sıra (yukarıdan aşağı) | Kök frame adı | İçerik | Boyut |
|---|---|---|---|
| 00 | `C/DS/Colors`, `C/DS/Typography`, `C/DS/Spacing`, `C/DS/Icons`, `C/DS/Motion` | Design system sayfaları | serbest |
| 01 | `C/Sub/<Ad>` (reusable) ve `C/Sub/<Ad> — <durum>` | Bileşenler ve durumları | içeriğe göre |
| 02 | `C/Section/<Ad>@desktop` ve `C/Section/<Ad>@mobile` (ikisi de reusable) | Bölümler | 1440 / 390 genişlik |
| 03 | `C/Page/<Ad>@desktop` ve `C/Page/<Ad>@mobile` | Sayfalar (section instance'ları) | 1440 / 390 |
| 04 | `C/Overlay/<Ad>@desktop — <durum>` ve `…@mobile — <durum>` | Menü, sepet, arama, paneller | 1440×900 / 390×844 |
| 05 | `C/Motion/<tarif> <bölüm>` | Animasyon kareleri (başlangıç / ara / bitiş) | içeriğe göre |

Yerleşim: her sıra bir yatay bant; bantlar arası 800, frame'ler arası 200 boşluk. Bir bölümün desktop ve mobil frame'i **yan yana**. Kök seviyede metin, ikon ya da serbest şekil bırakılmaz; açıklamalar `note` node'u olarak ilgili frame'in yanına konur.

Kurallar:
- Desktop kök frame'lerinde `theme: {device: "desktop"}`, mobil olanlarda `theme: {device: "mobile"}`; koyu bölümlerde ayrıca `mode: "dark"` (varsayılan `mode: "light"`). Boyut değişkenleri buna göre kendiliğinden değişir; mobil frame'de ayrıca sayı yazılmaz.
- Bölüm frame'leri `layout: "vertical"` ya da `"horizontal"`, `clip: true`. `layout: "none"` sadece gerçekten üst üste binen katmanlarda (slaytlar, görsel + gradyan + metin, hotspot).
- Tekrarlanan her şey `reusable` bileşenin `ref` instance'ıdır (ProductCard, Button, ArrowLink…). Sayfalar yalnızca section `ref`'lerinden oluşur.
- Çalışılan kök frame `placeholder: true`; bitince kaldırılır.
- Değer yazarken sayı yerine değişken: renk, font, yazı boyutu, boşluk hep `$…`.

## 3. Değişkenler

İlk iş olarak tanımlanır. Adlar üç planda aynıdır (`globals.md` ile eşleşir); değerler bu varyanta özgüdür.

```js
SetVariables({
  "color-bg": {type:"color", value:[{value:"#EFEBE2", theme:{mode:"light"}}, {value:"#0D0D0D", theme:{mode:"dark"}}]},
  "color-text": {type:"color", value:[{value:"#0D0D0D", theme:{mode:"light"}}, {value:"#EFEBE2", theme:{mode:"dark"}}]},
  "color-muted": {type:"color", value:[{value:"#6B675F", theme:{mode:"light"}}, {value:"#8F8B82", theme:{mode:"dark"}}]},
  "color-line": {type:"color", value:[{value:"#0D0D0D", theme:{mode:"light"}}, {value:"#EFEBE2", theme:{mode:"dark"}}]},
  "color-surface": {type:"color", value:[{value:"#E3DED2", theme:{mode:"light"}}, {value:"#1A1A1A", theme:{mode:"dark"}}]},
  "color-inverse-bg": {type:"color", value:[{value:"#0D0D0D", theme:{mode:"light"}}, {value:"#EFEBE2", theme:{mode:"dark"}}]},
  "color-inverse-text": {type:"color", value:[{value:"#EFEBE2", theme:{mode:"light"}}, {value:"#0D0D0D", theme:{mode:"dark"}}]},
  "color-accent": {type:"color", value:[{value:"#FF3B1F", theme:{mode:"light"}}, {value:"#FF3B1F", theme:{mode:"dark"}}]},
  "color-accent-text": {type:"color", value:[{value:"#0D0D0D", theme:{mode:"light"}}, {value:"#0D0D0D", theme:{mode:"dark"}}]},
  "color-scrim": {type:"color", value:[{value:"#0D0D0D99", theme:{mode:"light"}}, {value:"#0D0D0DB3", theme:{mode:"dark"}}]},
  "font-display": {type:"string", value:"Sofia Sans Extra Condensed"},
  "font-ui": {type:"string", value:"Archivo Narrow"},
  "font-body": {type:"string", value:"Archivo Narrow"},
  "font-price": {type:"string", value:"Archivo Narrow"},
  "font-mono": {type:"string", value:"Space Mono"},
  "text-display": {type:"number", value:[{value:168, theme:{device:"desktop"}}, {value:72, theme:{device:"mobile"}}]},
  "text-h2": {type:"number", value:[{value:112, theme:{device:"desktop"}}, {value:52, theme:{device:"mobile"}}]},
  "text-h3": {type:"number", value:[{value:64, theme:{device:"desktop"}}, {value:40, theme:{device:"mobile"}}]},
  "text-h4": {type:"number", value:[{value:36, theme:{device:"desktop"}}, {value:26, theme:{device:"mobile"}}]},
  "text-title": {type:"number", value:[{value:22, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "text-ui": {type:"number", value:[{value:18, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "text-ui-sm": {type:"number", value:[{value:15, theme:{device:"desktop"}}, {value:14, theme:{device:"mobile"}}]},
  "text-badge": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-label": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-body": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:15, theme:{device:"mobile"}}]},
  "text-price": {type:"number", value:[{value:22, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "space-page": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-grid": {type:"number", value:0},
  "space-card": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:10, theme:{device:"mobile"}}]},
  "space-panel": {type:"number", value:[{value:24, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-xs": {type:"number", value:[{value:6, theme:{device:"desktop"}}, {value:4, theme:{device:"mobile"}}]},
  "space-sm": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:10, theme:{device:"mobile"}}]},
  "space-md": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:12, theme:{device:"mobile"}}]},
  "space-section": {type:"number", value:[{value:120, theme:{device:"desktop"}}, {value:64, theme:{device:"mobile"}}]},
  "size-header": {type:"number", value:[{value:96, theme:{device:"desktop"}}, {value:88, theme:{device:"mobile"}}]},
  "size-line": {type:"number", value:2},
  "opacity-inactive": {type:"number", value:0.3},
})
```

Font doğrulama: `execute` yanıtında "Font family … is invalid" uyarısı çıkarsa o değişkeni değiştir. Canvas üzerinde denenip geçerli çıkan aileler: `Anton`, `Antonio`, `Archivo Narrow`, `Barlow`, `Barlow Condensed`, `Bebas Neue`, `JetBrains Mono`, `Mona Sans`, `Oswald`, `Sofia Sans Extra Condensed`, `Space Mono`. Geçersiz çıkanlar: `Mona Sans Condensed`, `Big Shoulders Display`.

Yazı stili eşlemesi: `text-display`, `text-h2`, `text-h3`, `text-h4` → `$font-display`, satır yüksekliği 0.9–1.0 · `text-title`, `text-ui`, `text-ui-sm`, `text-badge` → `$font-ui`, 700, satır 1.1 · `text-label` → `$font-mono` · `text-body` → `$font-body`, 500, satır 1.35 · `text-price` → `$font-price`, 700. Hepsi büyük harf (gövde metni hariç).

## 4. Adlandırma ve metadata sözleşmesi

Amaç: tasarımdan koda çeviri mekanik olsun.

| pen.dev | ikas / kod |
|---|---|
| Kök frame `C/Section/HeroSlider@desktop` | section bileşeni **HeroSlider** (`src/components/HeroSlider/`) |
| Kök frame `C/Sub/ProductCard` | sub-component **ProductCard** (`src/sub-components/ProductCard/`) |
| Kök frame `C/Overlay/CartDrawer…` | ilgili section'ın alt bileşeni |
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
metadata: {type:"gizem", role:"section", ikas:"HeroSlider", device:"desktop", variant:"C"}
// role: "ds" | "sub" | "section" | "overlay" | "page" | "motion"

// prop'a bağlı katman
metadata: {type:"gizem", role:"prop", prop:"title", propType:"TEXT"}

// animasyonlu katman (prop'a da bağlıysa aynı nesnede)
metadata: {type:"gizem", role:"anim", anim:"C-HERO-02", recipe:"M-07", trigger:"state-change", prop:"title", propType:"TEXT"}
context: "C-HERO-02 · M-07 · başlık slaytla birlikte değişir"
```

- Bir katmanda birden çok hedef varsa `anim` virgülle ayrılır: `"C-HERO-01,C-HERO-07"`.
- `context` insan için kısa açıklamadır; makine `metadata` okur.
- Bileşenin içindeki katmana verilen metadata instance'lara taşınır; her instance'a yeniden yazılmaz.

## 5. Animasyona hazır tasarım kuralları

pen.dev hareket göstermez. Aşağıdaki yapılar çizilmezse aktarımda katmanları yeniden kurmak gerekir.

1. **Bitiş hali çizilir.** Bölüm ve sayfa frame'leri animasyon bittikten sonraki görünümü gösterir. Başlangıç ve ara haller sadece `C/Motion/…` frame'lerinde.
2. **Maske = `clip: true` frame.** Kayarak giren her metin satırı kendi `…-mask` frame'inin içindedir; maske metinle aynı boyutta. Çok satırlı başlıkta her satır ayrı metin node'u ve ayrı maske.
3. **Roll eden öğeler çift kopyadır.** Buton, nav linki ve ok ikonunda `top` (görünen) ve `bottom` (maske dışında bekleyen) kopyaları birlikte çizilir; kap `clip: true`.
4. **Sonsuz kayanlar track + kopya.** `marquee` / `ticker` kabı `clip: true`; içindeki `…-track` içerik setini en az iki kez barındırır ve kabın dışına taşar.
5. **Yer değiştirenler kardeş frame.** Slaytlar, sekme içerikleri, ön/arka ürün görseli aynı ebeveynde üst üste (`layout: "none"`); görünmeyenler `opacity: 0` ile durur, silinmez.
6. **İlerleme göstergesi ayrı katman.** `progress-bar` dolgusu ebeveyninden ayrı bir dikdörtgen; yarı dolu çizilir.
7. **Sticky alanlar gerçek yükseklikte.** Sabit kalan öğenin kabı, kaydırma boyunca kat edeceği yükseklikte çizilir (ör. 4 görsellik galeri yanında tek detay sütunu).
8. **Overlay ayrı frame.** Menü, çekmece, arama: `scrim` + panel, sayfa frame'inin kopyası üzerinde değil, kendi kök frame'inde; açık ve boş/dolu halleri ayrı.
9. **Kaydırmaya bağlı öğeler serbest katman.** Dönen/kayan görsel ya da parallax arka plan, akıştan bağımsız (`layoutPosition: "absolute"`) ve kabından büyük çizilir.
10. **Hover hali ayrı frame.** Her etkileşimli bileşenin hover hali `C/Sub/<Ad> — hover` olarak çizilir; bölüm içinde tekrar çizilmez.
11. **Her hedef işaretli.** 6. bölümde `anim-targets` bloğunda geçen her `layer`, tasarımda aynı adla bulunur ve `metadata.anim` taşır.
12. **Mobil hali kararlaştırılmış.** Hedefin `mobile` alanı "kapalı" ya da farklıysa mobil frame o hale göre çizilir (ör. sticky yok → normal akış).

### 5.1 Bu plana özgü motion tarifleri

`globals.md` kataloğuna ek olarak (M-xx tarifleri orada):

| ID | Ad | Hareket | Zorunlu katman yapısı | Uygulama | Mobil | Azaltılmış hareket |
|---|---|---|---|---|---|---|
| **C-M-01** | Şifre çözme (scramble) | Metin önce rastgele karakterlerle görünür, soldan sağa gerçek harflere çözülür. Markanın imza hareketi ("gizem"). Hover ve görünürlükte. `{ chars: rastgele } → { chars: gerçek metin }`, `{ duration: 0.7, perChar: 0.03, direction: soldan-sağa }` | tek metin node'u; **sabit genişlikli** kap içinde (çözülürken satır kaymasın); mono ya da tabular font | animejs (ya da setInterval) | sadece inview, hover yok | kapalı (metin sabit) |
| **C-M-02** | Dikey perde | Yeni görsel alttan yukarı açılan bir perdeyle gelir; görsel hafifçe yukarı kayar. `{ clip: "inset(100% 0 0 0)", image.y: 10% } → { clip: "inset(0)", image.y: 0 }`, `{ duration: 1.0, ease: ease-inout }` | `hero-stage` (clip) içinde tüm görseller kardeş; her biri kendi `curtain` (clip) frame'inde | animejs | çapraz geçiş 0.5s | anında değişim |
| **C-M-03** | İmleç takipli önizleme | Liste satırının üzerine gelince ürün görseli imleci gecikmeli takip eder, hafif eğik durur. `{ preview.opacity: 0, preview.scale: 0.9 } → { preview.opacity: 1, preview.scale: 1, preview.rotate: "±4" }`, `{ follow: "lerp 0.15", fade: 0.25 }` | `index-preview` ayrı katman (mutlak konum, satırların üstünde); her satır için bir görsel; Motion States'te bir satır hover hali | scroll-scrub benzeri (pointermove + rAF) | kapalı; satırda küçük görsel sabit | takip yok, görsel satır yanında sabit |
| **C-M-04** | Sabitlenmiş yatay kaydırma | Bölüm ekranda sabitlenir, dikey kaydırma içeriği yatay hareket ettirir. `{ track.x: 0 } → { track.x: "-(trackWidth - viewport)" }`, `{ scrub: true, pin: true }` | `lookbook-pin` (viewport yüksekliği, clip) içinde `lookbook-track` tüm kareleriyle **tam genişlikte** çizilir (frame dışına taşar) | layout + scroll-scrub | pin yok; yatay scroll-snap | pin yok; yatay kaydırma |
| **C-M-05** | Spec-sheet hover | Kartın altından beden seçimi ve hızlı ekle paneli kayarak çıkar. `{ overlay.y: 100% } → { overlay.y: 0 }`, `{ duration: 0.4, ease: ease-standard }` | `card-images` (clip) içinde en üstte `card-spec` katmanı (bedenler + buton); varsayılan halde maske dışında altta | css-transition | kapalı; hızlı ekle butonu hep görünür | anında |
| **C-M-06** | Kaydırmayla kelime vurgusu | Büyük metnin kelimeleri kaydırdıkça sırayla soluktan tam renge geçer. `{ word.opacity: 0.2 } → { word.opacity: 1 }`, `{ scrub: true, sequential: true }` | metin tek node; Motion States'te %0 / %50 / %100 kareleri (soluk kelimeler ayrı renkle) | scroll-scrub | aynı | tüm kelimeler tam opak |
| **C-M-07** | Sticker düşüşü | Görseller/etiketler büyükten küçülerek ve dönerek yerine "yapışır". `{ scale: 1.4, rotate: "son açı ± 12", opacity: 0 } → { scale: 1, rotate: son açı, opacity: 1 }`, `{ spring: "bounce 0.4, 0.6s", stagger: 0.08 }` | her sticker ayrı katman, **son açısıyla** (rotation) çizilir | animejs + io-hook | aynı, daha az sticker | anında |
| **C-M-08** | Geri sayım | Rakamlar saniyede bir dikey kayarak değişir. `{ digit.y: 0 } → { digit.y: -100% }`, `{ duration: 0.3, every: 1 }` | her hane kendi `digit-mask` (clip) frame'inde; içinde iki rakam alt alta | css-transition + setInterval | aynı | rakam anında değişir |

## 6. Yapım sırası

### 6.0 Design System frame'leri

| Kök frame | İçerik |
|---|---|
| `C/DS/Colors` | Her renk değişkeni için örnek kare + ad + hex; metin/zemin kontrast çiftleri (metin, muted, vurgu üzerinde metin) |
| `C/DS/Typography` | 11 yazı stili, her biri desktop ve mobil boyutunda örnek satırla (Türkçe karakterli: "GÖLGE İÇİNDE ŞIK ÇÖZÜM 1.850 TL") |
| `C/DS/Spacing` | Boşluk ölçeği çubukları; 1440 ve 390 için ızgara şeması (kenar boşluğu, sütunlar, aralık); çizgi kalınlığı |
| `C/DS/Icons` | Kullanılan tüm ikonlar 20×20 (arama, hesap, sepet, menü, kapat, ok ↗, caret, artı, eksi, onay) + logo ve işaret |
| `C/DS/Motion` | Kullanılan tarif ID'leri, kısa açıklama ve tetikleyici simgeleri; `note` node'ları ile. Bu frame animasyon "lejantı"dır |

### 6.1 Bileşenler (`C/Sub/…`)

Her bileşen `reusable` kök frame; durumlar yanında ayrı frame. Önce bunlar, çünkü bölümler bunların instance'larını kullanır.

| Bileşen | Yapı | Durumlar (ayrı frame) |
|---|---|---|
| `ProductCard` | bitişik hücre, 2px çizgi; `card-images` (clip, 3:4): `image-front` + `image-back` + `card-spec` (alttan çıkan panel: beden çipleri + hızlı ekle) · `card-badges` (vurgu zeminli etiket, sol üst) · `card-info`: `card-title` (font-ui) · `card-category` (font-mono, muted) · `price` + `price-compare` | varsayılan · hover (card-spec açık) · stok yok · indirimli · genişlikler: 356 / 290 / 195 (mobil) |
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
| `Sticker` | `wall-sticker`: vurgu zeminli, font-mono metinli etiket; kendi açısıyla (−12° … +12°) | düz · dönük |
| `ScrambleText` | `scramble-text`: sabit genişlikli kap içinde tek metin; C-M-01 uygulanan her başlık/link bu yapıyı kullanır | çözülmüş · karışık (Motion States) |

Bileşen animasyon hedefleri (bölümlerde `via` ile anılır, kodu bileşenin içinde yazılır):

<!-- anim-targets:start -->
```yaml
- id: C-CMP-01
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
- id: C-CMP-02
  section: Sub/ProductCard
  layer: card-spec
  recipe: C-M-05
  trigger: hover
  what: "Beden ve hızlı ekle paneli alttan çıkar"
  from: { overlay.y: 100% }
  to: { overlay.y: 0 }
  timing: { duration: 0.4, ease: ease-standard }
  impl: css-transition
  mobile: kapalı; hızlı ekle butonu hep görünür
  reducedMotion: anında
  done: false
- id: C-CMP-03
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
- id: C-CMP-04
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
- id: C-CMP-05
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
- id: C-CMP-06
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
- id: C-CMP-07
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
- id: C-CMP-08
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
- id: C-CMP-09
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
- id: C-CMP-10
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
- id: C-CMP-11
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
- id: C-CMP-12
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
- id: C-CMP-13
  section: Sub/Sticker
  layer: wall-sticker
  recipe: C-M-07
  trigger: inview
  what: "Etiket dönerek yapışır"
  from: { scale: 1.4, rotate: "son açı ± 12", opacity: 0 }
  to: { scale: 1, rotate: son açı, opacity: 1 }
  timing: { spring: "bounce 0.4, 0.6s", stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı, daha az sticker
  reducedMotion: anında
  done: false
- id: C-CMP-14
  section: Sub/ScrambleText
  layer: scramble-text
  recipe: C-M-01
  trigger: hover | inview
  what: "Metin şifre çözülür gibi yenilenir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
```
<!-- anim-targets:end -->

### 6.2 Bölümler ve overlay'ler

Her başlık bir kök frame çiftidir (`@desktop` + `@mobile`). "ikas" satırı aktarımda başlanacak şablonu gösterir.

#### Section/Header
- **Kullanıldığı yer:** tüm sayfalar
- **ikas:** header-section (--isHeader)
- **Prop'lar:** `logo` SVG · `announcements` COMPONENT_LIST (AnnouncementItem) · `navLinks` LIST_OF_LINK · `searchText`, `accountText`, `cartText`, `menuText` TEXT · sepet/arama metinleri (components.md Header ile aynı) · `backgroundColor` COLOR
- **Desktop:** İki satır. Üstte vurgu renkli kayan şerit (yükseklik 32). Altında 64 yüksekliğinde ana satır: solda wordmark, ortada köşeli parantezli linkler, sağda metin tabanlı eylemler. Alt çizgi 2px.
- **Mobil:** ticker-strip aynı; header-row: `menu-button` ("MENU" metni) solda, logo ortada, `cart-button` sağda.

```
header
├─ ticker-strip (clip)               zemin $color-accent
│   └─ marquee-track                 {text:TEXT} ×6 kopya, font-mono 12
└─ header-row
    ├─ header-logo                   {logo:SVG} wordmark
    ├─ header-nav
    │   └─ nav-link ×4               "[ SHOP ]" biçiminde; sabit genişlikli kap
    └─ header-actions                metin: search-button "SEARCH" · account-button "ACCOUNT" · cart-button "BAG (0)"
```

Kontrol: nav-link kapları sabit genişlikte

<!-- anim-targets:start -->
```yaml
- id: C-HDR-01
  section: Header
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Duyuru şeridi kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: C-HDR-02
  section: Header
  layer: nav-link
  recipe: C-M-01
  trigger: hover
  what: "Link metni şifre çözülür gibi yenilenir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-HDR-03
  section: Header
  layer: cart-button
  recipe: C-M-01
  trigger: state-change
  what: "Sepet sayısı değişince metin yeniden çözülür"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
```
<!-- anim-targets:end -->

#### Overlay/MenuOverlay
- **Kullanıldığı yer:** Header (desktop + mobil; megamenu yerine)
- **ikas:** Header sub-component
- **Desktop:** Tam ekran, ters palet (koyu). Solda numaralı dev link listesi, sağda üzerine gelinen linkin görseli; altta kategori sütunları.
- **Mobil:** Tek sütun; menu-preview yok; menu-item-label text-h2.

```
menu-overlay
├─ menu-index
│   └─ menu-item ×5                  menu-item-number (font-mono) + menu-item-label (text-display) ; alt çizgi
├─ menu-preview (clip)               üzerine gelinen öğenin görseli, 520×680
└─ menu-footer                       megamenu-column ×2 + sosyal linkler
```

Kontrol: açık hali ayrı overlay frame · koyu palet (mode: dark)

<!-- anim-targets:start -->
```yaml
- id: C-MENU-01
  section: MenuOverlay
  layer: menu-overlay
  recipe: C-M-02
  trigger: click
  what: "Menü perdeyle açılır"
  from: { clip: "inset(0 0 100% 0)" }
  to: { clip: "inset(0)" }
  timing: { duration: 0.7, ease: ease-inout }
  impl: animejs
  mobile: çapraz geçiş 0.5s
  reducedMotion: anında değişim
  done: false
- id: C-MENU-02
  section: MenuOverlay
  layer: menu-item
  recipe: M-01
  trigger: state-change
  what: "Öğeler sırayla girer"
  from: { y: 40, opacity: 0 }
  to: { y: 0, opacity: 1 }
  timing: { duration: 0.5, ease: ease-standard, stagger: 0.06 }
  impl: animejs
  mobile: aynı
  reducedMotion: anında
  done: false
- id: C-MENU-03
  section: MenuOverlay
  layer: menu-item-label
  recipe: C-M-01
  trigger: hover
  what: "Etiket şifre çözülür gibi yenilenir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-MENU-04
  section: MenuOverlay
  layer: menu-preview
  recipe: C-M-02
  trigger: hover
  what: "Önizleme görseli perdeyle değişir"
  from: { clip: "inset(100% 0 0 0)", image.y: 10% }
  to: { clip: "inset(0)", image.y: 0 }
  timing: { duration: 0.5, ease: ease-inout }
  impl: animejs
  mobile: çapraz geçiş 0.5s
  reducedMotion: anında değişim
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
- id: C-CART-01
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
- id: C-CART-02
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
- id: C-CART-03
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
- id: C-SRCH-01
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
- id: C-SRCH-02
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
- **Prop'lar:** components.md Footer + `newsletterTitle` TEXT; `bannerImage` yok
- **Desktop:** Ters palet (koyu). Üstte bülten satırı (dev başlık + tek satır form), ortada 4 sütun, altta frame genişliğinde dev wordmark.
- **Mobil:** Sütunlar 2×2; wordmark 2 satıra bölünmez, küçülür.

```
footer
├─ footer-newsletter                 alt çizgi
│   ├─ footer-newsletter-title       {newsletterTitle:TEXT} text-h2
│   └─ newsletter-form               newsletter-input (alt çizgili) + newsletter-button
├─ footer-columns
│   └─ footer-column ×4              footer-column-title (font-mono) + footer-link ×N
├─ footer-wordmark                   {wordmarkText:TEXT} frame genişliğinde tek satır
└─ footer-legal                      font-mono 11: footer-link ×2 + {copyrightText:TEXT}
```

<!-- anim-targets:start -->
```yaml
- id: C-FTR-01
  section: Footer
  layer: footer-wordmark
  recipe: C-M-01
  trigger: inview
  what: "Wordmark şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-FTR-02
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
- id: C-FTR-03
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

#### Section/HeroSplit
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** hero-slider-section (uyarlanır)
- **Prop'lar:** `slides` COMPONENT_LIST (HeroSplitSlide: image IMAGE, title TEXT, link LINK) · `dropLabel`, `season`, `buttonText`, `stickerText` TEXT · `countdownDate` DATE · `autoplayDelay` NUMBER · `backgroundColor` COLOR
- **Desktop:** 1440 × 760, iki sütun. Sol 640: kağıt zemin, üstte drop bilgisi, ortada dev başlık, altta geri sayım + buton. Sağ 800: görsel sahnesi, köşede "01 / 03" sayacı ve döndürülmüş sticker.
- **Mobil:** Alt alta: önce hero-stage (390×460), sonra hero-info; başlık text-display (mobil).

```
hero-split
├─ hero-info                         boşluk 32, dikey, iki uca yaslı
│   ├─ hero-meta                     {dropLabel:TEXT} font-mono + {season:TEXT}
│   ├─ hero-title                    {title:TEXT} text-display, sabit genişlikli kap
│   └─ hero-bottom
│       ├─ countdown                 digit-mask ×8 (clip; içinde digit ×2) + ayırıcılar
│       └─ hero-button (clip)        {buttonText:TEXT}; top + bottom kopya
└─ hero-stage (clip)
    ├─ curtain ×3 (clip)             → hero-image {image:IMAGE}
    ├─ hero-counter                  font-mono "01 / 03"
    └─ hero-sticker                  {stickerText:TEXT} vurgu zeminli, -8° dönük
```

Kontrol: 3 görselin hepsi kardeş curtain frame · başlık kabı sabit genişlikte

<!-- anim-targets:start -->
```yaml
- id: C-HERO-01
  section: HeroSplit
  layer: curtain
  recipe: C-M-02
  trigger: auto | click
  what: "Yeni görsel alttan perdeyle açılır"
  from: { clip: "inset(100% 0 0 0)", image.y: 10% }
  to: { clip: "inset(0)", image.y: 0 }
  timing: { duration: 1.0, ease: ease-inout, interval: 5 }
  impl: animejs
  mobile: çapraz geçiş 0.5s
  reducedMotion: anında değişim
  done: false
- id: C-HERO-02
  section: HeroSplit
  layer: hero-title
  recipe: C-M-01
  trigger: load | state-change
  what: "Başlık şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-HERO-03
  section: HeroSplit
  layer: digit-mask
  recipe: C-M-08
  trigger: auto-loop
  what: "Geri sayım rakamları saniyede bir kayar"
  from: { digit.y: 0 }
  to: { digit.y: -100% }
  timing: { duration: 0.3, every: 1 }
  impl: css-transition + setInterval
  mobile: aynı
  reducedMotion: rakam anında değişir
  done: false
- id: C-HERO-04
  section: HeroSplit
  layer: hero-sticker
  recipe: C-M-07
  trigger: load
  what: "Sticker dönerek yerine yapışır"
  from: { scale: 1.4, rotate: "son açı ± 12", opacity: 0 }
  to: { scale: 1, rotate: son açı, opacity: 1 }
  timing: { spring: "bounce 0.4, 0.6s", stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı, daha az sticker
  reducedMotion: anında
  done: false
- id: C-HERO-05
  section: HeroSplit
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
- id: C-HERO-06
  section: HeroSplit
  layer: hero-counter
  recipe: C-M-01
  trigger: state-change
  what: "Sayaç slaytla birlikte yenilenir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
```
<!-- anim-targets:end -->

#### Section/TickerStrip
- **Kullanıldığı yer:** Ana sayfa (bölümler arasında 2 kez)
- **ikas:** (özel)
- **Prop'lar:** `text` TEXT · `speed` NUMBER · `direction` ENUM · `backgroundColor` COLOR
- **Desktop:** 1440 × 96; ters palet ya da vurgu zemini; üst + alt çizgi 2px; dev kayan metin ve aralarında ikon.
- **Mobil:** Yükseklik 56.

```
ticker-band
└─ marquee (clip)
    └─ marquee-track                 ({text:TEXT} text-h2 + ticker-icon) ×6
```

<!-- anim-targets:start -->
```yaml
- id: C-TICK-01
  section: TickerStrip
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Şerit kesintisiz kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "100px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
```
<!-- anim-targets:end -->

#### Section/ProductIndex
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** product-slider-section (uyarlanır)
- **Prop'lar:** `title`, `linkText` TEXT · `link` LINK · `productList` PRODUCT_LIST · `backgroundColor` COLOR
- **Desktop:** 1440; başlık satırı + tablo gibi ürün listesi: her satır 88 yükseklik, alt çizgi; sütunlar: no · ad · kategori · beden aralığı · fiyat · ok. Üzerine gelinen satır ters renge döner ve görseli imleci takip eder.
- **Mobil:** Liste yerine yatay kaydırmalı ProductCard şeridi (kart 300).

```
product-index
├─ section-heading                   section-title (text-h2) + link
├─ index-list
│   └─ index-row ×6                  {productList:PRODUCT_LIST}
│       ├─ index-number              font-mono "001"
│       ├─ index-name                text-h4
│       ├─ index-category            font-mono muted
│       ├─ index-sizes               font-mono muted
│       ├─ index-price               text-price
│       └─ index-arrow (clip)        arrow-top + arrow-bottom
└─ index-preview                     mutlak konum, 280×360, -4° dönük, çerçeveli
```

Kontrol: bir satır hover halinde çizildi (ters renk + index-preview görünür)

<!-- anim-targets:start -->
```yaml
- id: C-IDX-01
  section: ProductIndex
  layer: index-preview
  recipe: C-M-03
  trigger: hover
  what: "Ürün görseli imleci takip eder"
  from: { preview.opacity: 0, preview.scale: 0.9 }
  to: { preview.opacity: 1, preview.scale: 1, preview.rotate: "±4" }
  timing: { follow: "lerp 0.15", fade: 0.25 }
  impl: scroll-scrub benzeri (pointermove + rAF)
  mobile: kapalı; satırda küçük görsel sabit
  reducedMotion: takip yok, görsel satır yanında sabit
  done: false
- id: C-IDX-02
  section: ProductIndex
  layer: index-row
  recipe: M-11
  trigger: hover
  what: "Satır ters renge döner"
  from: { bg: transparent, color: color-text }
  to: { bg: color-inverse-bg, color: color-inverse-text }
  timing: { duration: 0.2 }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında renk değişimi
  done: false
- id: C-IDX-03
  section: ProductIndex
  layer: index-name
  recipe: C-M-01
  trigger: inview
  what: "Ürün adları sırayla çözülür"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.6, perChar: 0.02, stagger: 0.08 }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-IDX-04
  section: ProductIndex
  layer: index-arrow
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
```
<!-- anim-targets:end -->

#### Section/LookbookScroll
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** (özel)
- **Prop'lar:** `title` TEXT · `frames` COMPONENT_LIST (LookbookFrame: image IMAGE, note TEXT, product PRODUCT) · `backgroundColor` COLOR
- **Desktop:** Viewport yüksekliğinde sabitlenen bölüm (1440 × 760); içinde 5 kare yatay dizili (her kare 560×640, aralık 32), aralarında dev numaralar ve kısa notlar. Toplam şerit genişliği ~3200.
- **Mobil:** Sabitleme yok; kareler yatay scroll-snap (kare 320×420); numara küçülür.

```
lookbook
└─ lookbook-pin (clip)               viewport yüksekliği
    ├─ lookbook-title                {title:TEXT} text-h2, sol üstte sabit
    ├─ lookbook-progress             alt kenarda ince çizgi (genişlik %40 çiz)
    └─ lookbook-track                yatay, frame dışına taşar
        └─ lookbook-frame ×5
            ├─ lookbook-image        {image:IMAGE}
            ├─ lookbook-number       font-display dev "01"
            ├─ lookbook-note         {note:TEXT} font-mono
            └─ lookbook-tag          {product:PRODUCT} ürün etiketi (ad + fiyat), vurgu zeminli
```

Kontrol: lookbook-track tam genişlikte çizildi · Motion States: şeridin baş / orta / son konumu

<!-- anim-targets:start -->
```yaml
- id: C-LOOK-01
  section: LookbookScroll
  layer: lookbook-track
  recipe: C-M-04
  trigger: scroll-scrub
  what: "Dikey kaydırma şeridi yatay hareket ettirir"
  from: { track.x: 0 }
  to: { track.x: "-(trackWidth - viewport)" }
  timing: { scrub: true, pin: true }
  impl: layout + scroll-scrub
  mobile: pin yok; yatay scroll-snap
  reducedMotion: pin yok; yatay kaydırma
  done: false
- id: C-LOOK-02
  section: LookbookScroll
  layer: lookbook-progress
  recipe: M-08
  trigger: scroll-scrub
  what: "İlerleme çizgisi kaydırmayla dolar"
  from: { width: 0% }
  to: { width: 100% }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: tek ince çizgi
  reducedMotion: çubuk gizli
  done: false
- id: C-LOOK-03
  section: LookbookScroll
  layer: lookbook-number
  recipe: M-27
  trigger: scroll-scrub
  what: "Numaralar görsellerden farklı hızda kayar"
  from: { x: 0 }
  to: { x: -80 }
  timing: { scrub: true }
  impl: scroll-scrub
  mobile: kapalı
  reducedMotion: kapalı
  done: false
- id: C-LOOK-04
  section: LookbookScroll
  layer: lookbook-tag
  recipe: C-M-07
  trigger: inview
  what: "Ürün etiketi dönerek yapışır"
  from: { scale: 1.4, rotate: "son açı ± 12", opacity: 0 }
  to: { scale: 1, rotate: son açı, opacity: 1 }
  timing: { spring: "bounce 0.4, 0.6s", stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı, daha az sticker
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/CategoryMosaic
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** category-images-section (uyarlanır)
- **Prop'lar:** `cells` COMPONENT_LIST (MosaicCell: category CATEGORY, image IMAGE, label TEXT, link LINK) · `countSuffixText` TEXT · `backgroundColor` COLOR
- **Desktop:** 1440 × 760; asimetrik ızgara: solda 1 büyük hücre (712×760), sağda 2×2 küçük hücre (356×376); çizgi 2px, aralık yok (hücreler bitişik).
- **Mobil:** Büyük hücre tam genişlik (390×420); küçükler 2 sütun (195×220).

```
category-mosaic
└─ mosaic-cell ×5 (clip)
    ├─ mosaic-image                  {image:IMAGE}
    ├─ mosaic-label                  {label:TEXT} text-h3 (büyük hücrede text-h2), sol alt
    ├─ mosaic-count                  font-mono "24 ÜRÜN", sağ üst
    └─ mosaic-hover                  ters zeminli katman: marquee → marquee-track (etiket ×3)
```

Kontrol: bir hücre hover halinde

<!-- anim-targets:start -->
```yaml
- id: C-MOS-01
  section: CategoryMosaic
  layer: mosaic-hover
  recipe: C-M-05
  trigger: hover
  what: "Ters zeminli şerit alttan kayar"
  from: { overlay.y: 100% }
  to: { overlay.y: 0 }
  timing: { duration: 0.35, ease: ease-standard }
  impl: css-transition
  mobile: kapalı; hızlı ekle butonu hep görünür
  reducedMotion: anında
  done: false
- id: C-MOS-02
  section: CategoryMosaic
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Hover şeridindeki etiket kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s", ease: linear, loop: true }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: C-MOS-03
  section: CategoryMosaic
  layer: mosaic-image
  recipe: M-09
  trigger: hover
  what: "Görsel hafif büyür"
  from: { scale: 1 }
  to: { scale: 1.05 }
  timing: { spring: spring-card }
  impl: css-transition
  mobile: kapalı (dokunmatik)
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Section/DropGrid
- **Kullanıldığı yer:** Ana sayfa
- **ikas:** product-slider-section
- **Prop'lar:** `title`, `metaText`, `linkText`, `quickAddText` TEXT · `link` LINK · `productList` PRODUCT_LIST · `backgroundColor` COLOR
- **Desktop:** 1440; başlık satırı + 4 sütun ızgara (kart 356×520, hücreler bitişik, 2px çizgi). Kart: görsel 3:4, altında mono bilgi satırı.
- **Mobil:** 2 sütun (kart 195×300); card-spec yerine görselin köşesinde sabit "+" butonu.

```
drop-grid
├─ section-heading                   section-title (text-h2) + drop-meta (font-mono) + link
└─ product-grid
    └─ ProductCard ×8                C kartı: card-images (clip) → image-front + image-back + card-spec; card-info
```

Kontrol: bir kart hover halinde (card-spec açık)

<!-- anim-targets:start -->
```yaml
- id: C-DROP-01
  section: DropGrid
  layer: card-spec
  via: ProductCard
  recipe: C-M-05
  trigger: hover
  what: "Beden seçimi ve hızlı ekle paneli alttan çıkar"
  from: { overlay.y: 100% }
  to: { overlay.y: 0 }
  timing: { duration: 0.4, ease: ease-standard }
  impl: css-transition
  mobile: kapalı; hızlı ekle butonu hep görünür
  reducedMotion: anında
  done: false
- id: C-DROP-02
  section: DropGrid
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
- id: C-DROP-03
  section: DropGrid
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
- id: C-DROP-04
  section: DropGrid
  layer: section-title
  via: SectionHeading
  recipe: C-M-01
  trigger: inview
  what: "Başlık şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
```
<!-- anim-targets:end -->

#### Section/Manifesto
- **Kullanıldığı yer:** Ana sayfa, hakkında
- **ikas:** (özel)
- **Prop'lar:** `label`, `text`, `signature`, `buttonText` TEXT · `link` LINK · `backgroundColor` COLOR
- **Desktop:** 1440 × ~900; ters palet (koyu); ortada 1100 genişlik dev paragraf (text-h2), altında imza satırı ve buton.
- **Mobil:** Metin text-h3 (mobil değer); tam genişlik.

```
manifesto
├─ manifesto-label                   {label:TEXT} font-mono
├─ manifesto-text                    {text:TEXT} text-h2, tek metin node
└─ manifesto-footer                  {signature:TEXT} font-mono + manifesto-button (clip; top + bottom)
```

Kontrol: Motion States: %0 / %50 / %100

<!-- anim-targets:start -->
```yaml
- id: C-MANI-01
  section: Manifesto
  layer: manifesto-text
  recipe: C-M-06
  trigger: scroll-scrub
  what: "Kelimeler kaydırdıkça sırayla belirginleşir"
  from: { word.opacity: 0.2 }
  to: { word.opacity: 1 }
  timing: { scrub: true, sequential: true }
  impl: scroll-scrub
  mobile: aynı
  reducedMotion: tüm kelimeler tam opak
  done: false
- id: C-MANI-02
  section: Manifesto
  layer: manifesto-button
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

#### Section/StickerWall
- **Kullanıldığı yer:** Ana sayfa, ürün detay
- **ikas:** (özel; SocialFeed yerine)
- **Prop'lar:** `title`, `linkText` TEXT · `link` LINK · `images` IMAGE_LIST · `stickers` COMPONENT_LIST (WallSticker: text TEXT) · `backgroundColor` COLOR
- **Desktop:** 1440 × 820; kağıt zemin; 8 polaroid görsel serbest yerleşimli ve farklı açılarda (−12° … +12°), üst üste binen; ortada başlık ve link; birkaç bant/etiket.
- **Mobil:** 5 görsel; daha küçük; başlık üstte.

```
sticker-wall
├─ wall-title                        {title:TEXT} text-h2, ortada
├─ link                              {linkText:TEXT} + link-line + link-arrow
├─ wall-photo ×8                     beyaz çerçeveli görsel {images:IMAGE_LIST}; her biri kendi açısıyla
└─ wall-sticker ×3                   vurgu renkli etiket/bant, font-mono
```

Kontrol: her wall-photo son açısıyla çizildi

<!-- anim-targets:start -->
```yaml
- id: C-WALL-01
  section: StickerWall
  layer: wall-photo
  recipe: C-M-07
  trigger: inview
  what: "Fotoğraflar sırayla dönerek yapışır"
  from: { scale: 1.4, rotate: "son açı ± 12", opacity: 0 }
  to: { scale: 1, rotate: son açı, opacity: 1 }
  timing: { spring: "bounce 0.4, 0.6s", stagger: 0.08 }
  impl: animejs + io-hook
  mobile: aynı, daha az sticker
  reducedMotion: anında
  done: false
- id: C-WALL-02
  section: StickerWall
  layer: wall-sticker
  recipe: C-M-07
  trigger: inview
  what: "Etiketler fotoğraflardan sonra yapışır"
  from: { scale: 1.4, rotate: "son açı ± 12", opacity: 0 }
  to: { scale: 1, rotate: son açı, opacity: 1 }
  timing: { spring: "bounce 0.4, 0.6s", stagger: 0.08, delay: 0.5 }
  impl: animejs + io-hook
  mobile: aynı, daha az sticker
  reducedMotion: anında
  done: false
- id: C-WALL-03
  section: StickerWall
  layer: wall-title
  recipe: C-M-01
  trigger: inview
  what: "Başlık şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-WALL-04
  section: StickerWall
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

#### Section/JournalRows
- **Kullanıldığı yer:** Ana sayfa, journal liste
- **ikas:** blog-home-section (uyarlanır)
- **Prop'lar:** `title`, `linkText` TEXT · `link` LINK · `blogList` BLOG_LIST · `backgroundColor` COLOR
- **Desktop:** 1440; başlık satırı + 4 yazı satırı; her satır 160 yükseklik, alt çizgi: tarih (mono) · başlık (text-h3) · küçük görsel (240×140, sağda) · ok.
- **Mobil:** Satır: görsel üstte tam genişlik, altında tarih + başlık.

```
journal-rows
├─ section-heading                   section-title (text-h2) + link
└─ journal-row ×4                    {blogList:BLOG_LIST}
    ├─ journal-date                  font-mono
    ├─ journal-row-title             text-h3
    ├─ journal-row-image (clip)      görsel
    └─ index-arrow (clip)            arrow-top + arrow-bottom
```

<!-- anim-targets:start -->
```yaml
- id: C-JROW-01
  section: JournalRows
  layer: journal-row-image
  recipe: C-M-02
  trigger: inview
  what: "Satır görseli perdeyle açılır"
  from: { clip: "inset(100% 0 0 0)", image.y: 10% }
  to: { clip: "inset(0)", image.y: 0 }
  timing: { duration: 0.8, ease: ease-inout }
  impl: animejs + io-hook
  mobile: çapraz geçiş 0.5s
  reducedMotion: anında değişim
  done: false
- id: C-JROW-02
  section: JournalRows
  layer: journal-row-title
  recipe: M-01
  trigger: hover
  what: "Başlık sağa kayar"
  from: { x: 0 }
  to: { x: 16 }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: C-JROW-03
  section: JournalRows
  layer: index-arrow
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
```
<!-- anim-targets:end -->

#### Section/ProductList
- **Kullanıldığı yer:** Kategori, koleksiyon, arama, favoriler
- **ikas:** category-list-section
- **Prop'lar:** components.md ProductList + `countSuffixText`, `viewToggleAriaLabel`, `applyFiltersText`, `clearFiltersText` TEXT
- **Desktop:** 1440; üstte dev başlık + ürün sayısı (mono); solda 280 genişlik sticky filtre sütunu (akordeon gruplar), sağda 4 sütun ızgara (kart 290×430, bitişik hücreler, 2px çizgi); üstte sıralama ve görünüm (2/4 sütun) seçici.
- **Mobil:** filter-sidebar alttan açılan çekmece olur ("FİLTRE" butonu toolbar'da); ızgara 2 sütun.

```
product-list
├─ list-header
│   ├─ list-title                    {title:TEXT} text-display, sabit genişlikli kap
│   └─ list-count                    font-mono "48 ÜRÜN"
├─ list-toolbar                      sticky; sort-select + view-toggle
├─ filter-sidebar                    sticky
│   └─ filter-group ×4               faq-question benzeri başlık + filter-option ×N (checkbox)
├─ product-grid
│   └─ ProductCard ×12               C kartı (card-spec dahil)
└─ load-more-button (clip)           top + bottom kopya
```

Kontrol: mobil filtre çekmecesi ayrı overlay frame

<!-- anim-targets:start -->
```yaml
- id: C-PLP-01
  section: ProductList
  layer: list-title
  recipe: C-M-01
  trigger: load
  what: "Başlık şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-PLP-02
  section: ProductList
  layer: filter-sidebar
  recipe: M-13
  trigger: sticky
  what: "Filtre sütunu ızgara kayarken sabit kalır"
  from: {}
  to: { position: sticky, top: size-header }
  timing: {}
  impl: layout
  mobile: sticky yok
  reducedMotion: aynı
  done: false
- id: C-PLP-03
  section: ProductList
  layer: list-toolbar
  recipe: M-18
  trigger: sticky
  what: "Araç çubuğu header altında sabit kalır"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: layout + css-transition
  mobile: yatay kaydırma
  reducedMotion: anında
  done: false
- id: C-PLP-04
  section: ProductList
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
- id: C-PLP-05
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
- id: C-PLP-06
  section: ProductList
  layer: card-spec
  via: ProductCard
  recipe: C-M-05
  trigger: hover
  what: "Beden seçimi ve hızlı ekle paneli alttan çıkar"
  from: { overlay.y: 100% }
  to: { overlay.y: 0 }
  timing: { duration: 0.4, ease: ease-standard }
  impl: css-transition
  mobile: kapalı; hızlı ekle butonu hep görünür
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
- id: C-COLL-01
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
- id: C-COLL-02
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
- id: C-COLL-03
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
- **Prop'lar:** components.md ProductDetail; `infoTabs` akordeon olarak render edilir
- **Desktop:** 1440; solda 880 görsel mozaiği (2 sütun, 440×560 hücreler, bitişik, 2px çizgi), sağda 560 sticky detay sütunu. Bilgiler çekmece yerine akordeon.
- **Mobil:** Galeri yatay (390×490) + sayaç "01 / 06"; detaylar altında; add-to-cart alt kenarda sabit.

```
product-detail
├─ pdp-gallery
│   └─ pdp-image ×6                  2 sütun mozaik
└─ pdp-details                       sticky; boşluk 32
    ├─ breadcrumbs                   font-mono
    ├─ pdp-title                     text-h2, sabit genişlikli kap
    ├─ pdp-price                     text-price (+ eski fiyat)
    ├─ pdp-description               text-body
    ├─ variant-chips                 variant-chip ×N (kare, 48×48)
    ├─ link                          {sizeGuideText:TEXT} + link-line + link-arrow
    ├─ add-to-cart-button (clip)     tam genişlik, yükseklik 64; top + bottom kopya
    └─ pdp-accordion
        └─ faq-item ×3               faq-question + faq-icon + faq-answer (Materials / Care / Shipping)
```

Kontrol: buton halleri: varsayılan, yükleniyor, eklendi, stok yok

<!-- anim-targets:start -->
```yaml
- id: C-PDP-01
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
- id: C-PDP-02
  section: ProductDetail
  layer: pdp-title
  recipe: C-M-01
  trigger: load
  what: "Ürün adı şifre çözülür gibi belirir"
  from: { chars: rastgele }
  to: { chars: gerçek metin }
  timing: { duration: 0.7, perChar: 0.03, direction: soldan-sağa }
  impl: animejs (ya da setInterval)
  mobile: sadece inview, hover yok
  reducedMotion: kapalı (metin sabit)
  done: false
- id: C-PDP-03
  section: ProductDetail
  layer: pdp-image
  recipe: C-M-02
  trigger: inview
  what: "Galeri görselleri perdeyle açılır"
  from: { clip: "inset(100% 0 0 0)", image.y: 10% }
  to: { clip: "inset(0)", image.y: 0 }
  timing: { duration: 0.8, ease: ease-inout, stagger: 0.1 }
  impl: animejs + io-hook
  mobile: çapraz geçiş 0.5s
  reducedMotion: anında değişim
  done: false
- id: C-PDP-04
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
- id: C-PDP-05
  section: ProductDetail
  layer: variant-chip
  via: VariantChip
  recipe: M-28
  trigger: hover | click
  what: "Çip ters renge döner"
  from: { color: color-muted }
  to: { color: color-text }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
- id: C-PDP-06
  section: ProductDetail
  layer: faq-answer
  via: AccordionItem
  recipe: M-22
  trigger: click
  what: "Akordeon açılır, ikon döner"
  from: { height: 0, icon.rotate: 0 }
  to: { height: auto, icon.rotate: 45 }
  timing: { spring: "bounce 0, 0.5s" }
  impl: css-transition
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
- id: C-CRSL-01
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
- id: C-CRSL-02
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
- id: C-CRSL-03
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
- id: C-ABH-01
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
- id: C-ABH-02
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
- id: C-ABH-03
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
- id: C-PRS-01
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
- id: C-VAL-01
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
- id: C-VAL-02
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
- id: C-VAL-03
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
- id: C-VAL-04
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
- id: C-PRC-01
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
- id: C-PRC-02
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
- id: C-PRC-03
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
- id: C-TEAM-01
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
- id: C-TEAM-02
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
- id: C-TML-01
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
- id: C-TML-02
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
- id: C-CTA-01
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
- id: C-CTA-02
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
- id: C-ANC-01
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
- id: C-BLP-01
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
- id: C-BLP-02
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
- id: C-BLP-03
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
- id: C-BLP-04
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
- id: C-MQT-01
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
- id: C-CNT-01
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
- id: C-CNT-02
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
- id: C-CNT-03
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
- id: C-SUP-01
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
- id: C-SUP-02
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
- id: C-CRTP-01
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
- id: C-CRTP-02
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
- id: C-CRTP-03
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
- id: C-AUTH-01
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
- id: C-AUTH-02
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
- id: C-ACC-01
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
- id: C-ACC-02
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
- id: C-NF-01
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
- id: C-NF-02
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

Her sayfa için `C/Page/<Ad>@desktop` ve `@mobile`: dikey layout, `clip: true`, çocukları yalnızca section instance'ları.

| Sayfa | Bölümler (sırayla) |
|---|---|
| `Home` | Header · HeroSplit · TickerStrip · ProductIndex · LookbookScroll · CategoryMosaic · DropGrid · Manifesto (koyu) · StickerWall · JournalRows · TickerStrip · Footer |
| `Category` | Header · ProductList · Footer |
| `Collection` | Header · CollectionHero · ProductList · Footer |
| `Product` | Header · ProductDetail · ProductCarousel · ProductCarousel · StickerWall · Footer |
| `About` | Header · AboutHero · Manifesto · PressSlider · ValuesStack · ProcessSteps · TeamGrid · Timeline · CtaBanner · Footer (+ AnchorNav sabit) |
| `Journal` | Header · MarqueeTitle · JournalRows (tüm yazılar) · Footer |
| `JournalPost` | Header · BlogPost · JournalRows · Footer |
| `Contact` | Header · MarqueeTitle · Contact · ProductCarousel · Footer |
| `Support` | Header · SupportContent · Footer |
| `Cart` | Header · CartPage · Footer |
| `Auth (×4)` | Header · AuthForms · Footer |
| `Account` | Header · Account · Footer |
| `NotFound` | Header · NotFound · Footer |

### 6.4 Overlay frame'leri

6.2'de "Overlay" başlıklı her öğe için, yarı saydam bir sayfa görüntüsü yerine düz `$color-scrim` zemin üzerinde panel çizilir. Her biri desktop (1440×900) ve mobil (390×844), belirtilen durumlarıyla ayrı kök frame.

### 6.5 Motion States

Aşağıdaki tariflerin her biri için **bir** örnek üzerinde 2–3 kare çizilir (kök frame `C/Motion/<tarif> <bölüm>`; kareler soldan sağa, altlarında `note` ile yüzde/an bilgisi). Diğer kullanım yerleri aynı mantığı izler.

| Tarif | Örnek bölüm | Çizilecek kareler |
|---|---|---|
| M-03 | CollectionHero (`collection-title`) | başlık: kelimeler maske altında (görünmez) → yarısı girmiş → hepsi yerinde |
| M-09 | DropGrid (`image-back`) | ürün kartı: ön görsel → arka görsel + dönmüş ok |
| M-11 | CartDrawer (`checkout-button`) | buton: varsayılan → dolgu yarı yolda → ters dolgu |
| M-20 | CartDrawer (`cart-drawer`) | çekmece: kapalı (sayfa) → yarı açık + scrim → açık |
| M-21 | SearchOverlay (`search-panel`) | arama: kapalı → açık boş → açık sonuçlu |
| M-22 | ProductList (`filter-group`) | akordeon: kapalı → açık |
| M-23 | ValuesStack (`value-image`) | değer paneli: görsel 10° dönük ve aşağıda → 5° → 0° ve yerinde |
| M-24 | ValuesStack (`value-title`) | değer başlığı: tam opak → büyümüş ve yarı saydam → görünmez |
| C-M-01 | Header (`nav-link`) | metin: tamamen karışık karakterler → yarısı çözülmüş → gerçek metin |
| C-M-02 | MenuOverlay (`menu-preview`) | perde: eski görsel → yeni görsel alttan %50 açık → yeni görsel |
| C-M-03 | ProductIndex (`index-preview`) | liste: hover yok → bir satır ters renkte ve önizleme görseli imleç yanında |
| C-M-04 | LookbookScroll (`lookbook-track`) | şerit: baş konum → orta → son kare |
| C-M-05 | CategoryMosaic (`mosaic-hover`) | kart: varsayılan → spec paneli açık |
| C-M-06 | Manifesto (`manifesto-text`) | metin: hepsi soluk → yarısı belirgin → hepsi belirgin |
| C-M-07 | HeroSplit (`hero-sticker`) | sticker: büyük, fazla dönük, saydam → yerinde |
| C-M-08 | HeroSplit (`digit-mask`) | hane: rakam → iki rakam yarı yolda → yeni rakam |

## 7. Animasyon hedefleri özeti

Toplam **115 hedef**. Ayrıntılar 6.1 ve 6.2'deki `anim-targets` bloklarında.

| Bölüm | Hedef | Tarifler | ID aralığı |
|---|---|---|---|
| Header | 3 | M-14, C-M-01 | `C-HDR-01` … `C-HDR-03` |
| MenuOverlay | 4 | M-01, C-M-01, C-M-02 | `C-MENU-01` … `C-MENU-04` |
| CartDrawer | 3 | M-11, M-20 | `C-CART-01` … `C-CART-03` |
| SearchOverlay | 2 | M-01, M-21 | `C-SRCH-01` … `C-SRCH-02` |
| Footer | 3 | M-11, M-28, C-M-01 | `C-FTR-01` … `C-FTR-03` |
| HeroSplit | 6 | M-11, C-M-01, C-M-02, C-M-07, C-M-08 | `C-HERO-01` … `C-HERO-06` |
| TickerStrip | 1 | M-14 | `C-TICK-01` … `C-TICK-01` |
| ProductIndex | 4 | M-10, M-11, C-M-01, C-M-03 | `C-IDX-01` … `C-IDX-04` |
| LookbookScroll | 4 | M-08, M-27, C-M-04, C-M-07 | `C-LOOK-01` … `C-LOOK-04` |
| CategoryMosaic | 3 | M-09, M-14, C-M-05 | `C-MOS-01` … `C-MOS-03` |
| DropGrid | 4 | M-01, M-09, C-M-01, C-M-05 | `C-DROP-01` … `C-DROP-04` |
| Manifesto | 2 | M-11, C-M-06 | `C-MANI-01` … `C-MANI-02` |
| StickerWall | 4 | M-10, C-M-01, C-M-07 | `C-WALL-01` … `C-WALL-04` |
| JournalRows | 3 | M-01, M-10, C-M-02 | `C-JROW-01` … `C-JROW-03` |
| ProductList | 6 | M-01, M-13, M-18, M-22, C-M-01, C-M-05 | `C-PLP-01` … `C-PLP-06` |
| CollectionHero | 3 | M-01, M-03, M-27 | `C-COLL-01` … `C-COLL-03` |
| ProductDetail | 6 | M-11, M-13, M-22, M-28, C-M-01, C-M-02 | `C-PDP-01` … `C-PDP-06` |
| ProductCarousel | 3 | M-03, M-10, M-15 | `C-CRSL-01` … `C-CRSL-03` |
| AboutHero | 3 | M-01, M-03, M-27 | `C-ABH-01` … `C-ABH-03` |
| PressSlider | 1 | M-26 | `C-PRS-01` … `C-PRS-01` |
| ValuesStack | 4 | M-13, M-23, M-24 | `C-VAL-01` … `C-VAL-04` |
| ProcessSteps | 3 | M-01, M-03, M-27 | `C-PRC-01` … `C-PRC-03` |
| TeamGrid | 2 | M-01, M-03 | `C-TEAM-01` … `C-TEAM-02` |
| Timeline | 2 | M-01, M-03 | `C-TML-01` … `C-TML-02` |
| CtaBanner | 2 | M-03, M-11 | `C-CTA-01` … `C-CTA-02` |
| AnchorNav | 1 | M-25 | `C-ANC-01` … `C-ANC-01` |
| BlogPost | 4 | M-03, M-11, M-13, M-27 | `C-BLP-01` … `C-BLP-04` |
| MarqueeTitle | 1 | M-14 | `C-MQT-01` … `C-MQT-01` |
| Contact | 3 | M-01, M-11, M-22 | `C-CNT-01` … `C-CNT-03` |
| SupportContent | 2 | M-13, M-28 | `C-SUP-01` … `C-SUP-02` |
| CartPage | 3 | M-01, M-11, M-13 | `C-CRTP-01` … `C-CRTP-03` |
| AuthForms | 2 | M-01, M-11 | `C-AUTH-01` … `C-AUTH-02` |
| Account | 2 | M-18, M-28 | `C-ACC-01` … `C-ACC-02` |
| NotFound | 2 | M-11, M-14 | `C-NF-01` … `C-NF-02` |
| Sub/ProductCard | 2 | M-09, C-M-05 | `C-CMP-01` … `C-CMP-02` |
| Sub/ProductCardSmall | 1 | M-10 | `C-CMP-03` … `C-CMP-03` |
| Sub/BlogCard | 1 | M-09 | `C-CMP-04` … `C-CMP-04` |
| Sub/Button | 1 | M-11 | `C-CMP-05` … `C-CMP-05` |
| Sub/ArrowLink | 1 | M-10 | `C-CMP-06` … `C-CMP-06` |
| Sub/Hotspot | 1 | M-12 | `C-CMP-07` … `C-CMP-07` |
| Sub/Marquee | 1 | M-14 | `C-CMP-08` … `C-CMP-08` |
| Sub/Tabs | 1 | M-28 | `C-CMP-09` … `C-CMP-09` |
| Sub/VariantChip | 1 | M-28 | `C-CMP-10` … `C-CMP-10` |
| Sub/AccordionItem | 1 | M-22 | `C-CMP-11` … `C-CMP-11` |
| Sub/SectionHeading | 1 | M-03 | `C-CMP-12` … `C-CMP-12` |
| Sub/Sticker | 1 | C-M-07 | `C-CMP-13` … `C-CMP-13` |
| Sub/ScrambleText | 1 | C-M-01 | `C-CMP-14` … `C-CMP-14` |

| Tarif | Kullanım | Uygulama yolu |
|---|---|---|
| M-01 | 13 | css-keyframes |
| M-03 | 9 | animejs + io-hook |
| M-08 | 1 | css-transition |
| M-09 | 4 | css-transition |
| M-10 | 6 | css-transition |
| M-11 | 13 | css-transition |
| M-12 | 1 | css-keyframes + css-transition |
| M-13 | 6 | layout |
| M-14 | 6 | css-keyframes |
| M-15 | 1 | css-keyframes |
| M-18 | 2 | layout + css-transition |
| M-20 | 2 | css-transition + animejs |
| M-21 | 1 | css-transition |
| M-22 | 4 | css-transition |
| M-23 | 1 | scroll-scrub |
| M-24 | 2 | scroll-scrub |
| M-25 | 1 | io-hook + css-transition |
| M-26 | 1 | animejs |
| M-27 | 5 | scroll-scrub |
| M-28 | 6 | css-transition |
| C-M-01 | 12 | animejs (ya da setInterval) |
| C-M-02 | 5 | animejs |
| C-M-03 | 1 | scroll-scrub benzeri (pointermove + rAF) |
| C-M-04 | 1 | layout + scroll-scrub |
| C-M-05 | 4 | css-transition |
| C-M-06 | 1 | scroll-scrub |
| C-M-07 | 5 | animejs + io-hook |
| C-M-08 | 1 | css-transition + setInterval |

## 8. Aktarım sonrası: animasyon üretimi

Tasarım ikas'a aktarıldıktan (statik hali çalışır olduktan) sonra bu bölüm uygulanır.

**1) Hedefleri topla.** Bu dosyadaki tüm `anim-targets` bloklarını tek listeye çıkar:

```bash
python3 - <<'EOF'
import re, sys
src = open("docs/pendev/plan-C-serbest-yorum.md", encoding="utf-8").read()
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
Get(n => n.context && /C-[A-Z]{2,}-\d\d/.test(n.context) ? Print(n.context.match(/C-[A-Z]{2,}-\d\d/g).join(","), "|", n.name, "| context") : undefined)
```

İki çıktının birleşimi 7. bölümdeki listeyle karşılaştırılır.

**3) Ortak parçaları bir kez yaz** (`gizem/src/` altında):

| Parça | Yer | Hangi hedefler |
|---|---|---|
| Motion custom property'leri (`--ease-*`, `--dur-*`) | `src/global.css` | hepsi |
| `useInView(ref, {threshold, once})` | `src/utils/motion/useInView.ts` | `impl` içinde `io-hook` |
| `useScrollProgress(ref)` → CSS değişkeni | `src/utils/motion/useScrollProgress.ts` | `impl` içinde `scroll-scrub` |
| `splitWords(el)` + AnimeJS stagger | `src/utils/motion/revealWords.ts` | M-03 |
| `Marquee`, `Button`, `ArrowLink`, `Hotspot`, `AccordionItem`, `Drawer` | `src/sub-components/<Ad>/` | `via` alanı dolu olan hedefler (animasyon bileşenin içinde, bölümde tekrar yazılmaz) |
| `scrambleText(el, opts)` | `src/utils/motion/scramble.ts` | C-M-01 |
| `useCursorFollow(ref)` | `src/utils/motion/useCursorFollow.ts` | C-M-03 |
| `usePinnedHorizontal(ref)` | `src/utils/motion/usePinnedHorizontal.ts` | C-M-04 |
| `Sticker`, `Countdown` | `src/sub-components/<Ad>/` | C-M-07, C-M-08 |

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
- [ ] `Get(n => n.metadata?.anim …)` ve `context` taramasının (8. bölüm, 2. adım) birleşik çıktısındaki `id`'ler 7. bölümdeki listeyle birebir aynı.
- [ ] Her metin katmanında ya `metadata.prop` var ya da katman bir bileşen instance'ının parçası.
- [ ] Hiçbir frame'de kırpılmış ("clipped") içerik uyarısı yok (maske ve track'ler hariç; onlar bilinçli).
- [ ] Türkçe karakterler (`İ Ş Ğ Ü Ö Ç`) seçilen fontlarda doğru görünüyor.
- [ ] Referansın görselleri, metinleri ve logosu kullanılmadı.

Aktarım tarafı (ikas):
- [ ] Tema global'leri (renk, tipografi, kırılım) açıldı; `list_theme_globals` ile doğrulandı.
- [ ] Her section `check` ve `build` adımından hatasız geçti.
- [ ] 7. bölümdeki tüm hedefler `done: true`.

