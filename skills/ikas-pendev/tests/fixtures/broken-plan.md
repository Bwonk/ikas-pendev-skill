# Plan Z — Kusurlu örnek
<!-- ikas-pendev contract:2 -->

Tema: **Kusurlu** (test) · Hedef: pen.dev canvas → ikas Code Components · Referans: https://ornek.example.com/

Bu dosya `lint_plan.py` testleri içindir; her kontrol için en az bir kasıtlı hata içerir. Kalan yer tutucu: @@SLUG@@

## 3. Değişkenler

```js
SetVariables({
  "color-bg": {type:"color", value:[{value:"#F2F0EA", theme:{mode:"light"}}, {value:"#111111", theme:{mode:"dark"}}]},
  "color-text": {type:"color", value:[{value:"#111111", theme:{mode:"light"}}, {value:"#F2F0EA", theme:{mode:"dark"}}]},
  "color-muted": {type:"color", value:[{value:"#A09C94", theme:{mode:"light"}}, {value:"#8F8B82", theme:{mode:"dark"}}]},
  "color-line": {type:"color", value:[{value:"#11111180", theme:{mode:"light"}}, {value:"#F2F0EA", theme:{mode:"dark"}}]},
  "color-surface": {type:"color", value:[{value:"#E6E2D8", theme:{mode:"light"}}, {value:"#1C1C1C", theme:{mode:"dark"}}]},
  "color-inverse-bg": {type:"color", value:[{value:"#111111", theme:{mode:"light"}}, {value:"#F2F0EA", theme:{mode:"dark"}}]},
  "color-inverse-text": {type:"color", value:[{value:"#F2F0EA", theme:{mode:"light"}}, {value:"#111111", theme:{mode:"dark"}}]},
  "color-accent": {type:"color", value:[{value:"#2B50FF", theme:{mode:"light"}}, {value:"#2B50FF", theme:{mode:"dark"}}]},
  "color-accent-text": {type:"color", value:[{value:"#FFFFFF", theme:{mode:"light"}}, {value:"#FFFFFF", theme:{mode:"dark"}}]},
  "color-scrim": {type:"color", value:[{value:"#11111199", theme:{mode:"light"}}, {value:"#111111B3", theme:{mode:"dark"}}]},
  "color-transparent": {type:"color", value:"#F2F0EA80"},
  "color-danger": {type:"color", value:[{value:"#C62828", theme:{mode:"light"}}, {value:"#FF6B6B", theme:{mode:"dark"}}]},
  "font-display": {type:"string", value:"Big Shoulders Display"},
  "font-ui": {type:"string", value:"Inter"},
  "font-body": {type:"string", value:"Barlow"},
  "font-price": {type:"string", value:"Barlow"},
  "font-mono": {type:"string", value:"Space Mono"},
  "text-display": {type:"number", value:[{value:120, theme:{device:"desktop"}}, {value:56, theme:{device:"mobile"}}]},
  "text-h2": {type:"number", value:[{value:80, theme:{mode:"light"}}, {value:40, theme:{mode:"dark"}}]},
  "text-h3": {type:"number", value:[{value:56, theme:{device:"desktop"}}, {value:36, theme:{device:"mobile"}}]},
  "text-h4": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:24, theme:{device:"mobile"}}]},
  "text-title": {type:"number", value:[{value:22, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "text-ui": {type:"number", value:[{value:18, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "text-ui-sm": {type:"number", value:[{value:15, theme:{device:"desktop"}}, {value:14, theme:{device:"mobile"}}]},
  "text-badge": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-label": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:11, theme:{device:"mobile"}}]},
  "text-body": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:15, theme:{device:"mobile"}}]},
  "text-price": {type:"string", value:[{value:22, theme:{device:"desktop"}}, {value:18, theme:{device:"mobile"}}]},
  "space-page": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-grid": {type:"number", value:0},
  "space-card": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:10, theme:{device:"mobile"}}]},
  "space-panel": {type:"number", value:[{value:24, theme:{device:"desktop"}}, {value:16, theme:{device:"mobile"}}]},
  "space-xs": {type:"number", value:[{value:6, theme:{device:"desktop"}}, {value:4, theme:{device:"mobile"}}]},
  "space-sm": {type:"number", value:[{value:12, theme:{device:"desktop"}}, {value:10, theme:{device:"mobile"}}]},
  "space-md": {type:"number", value:[{value:16, theme:{device:"desktop"}}, {value:12, theme:{device:"mobile"}}]},
  "space-section": {type:"number", value:[{value:120, theme:{device:"desktop"}}, {value:64, theme:{device:"mobile"}}]},
  "size-header": {type:"number", value:[{value:72, theme:{device:"desktop"}}, {value:60, theme:{device:"mobile"}}]},
  "size-logo": {type:"number", value:[{value:32, theme:{device:"desktop"}}, {value:24, theme:{device:"mobile"}}]},
  "size-line": {type:"number", value:1},
  "opacity-inactive": {type:"number", value:0.3},
  "radius-card": {type:"number", value:4},
})
```

## 4. Adlandırma ve metadata sözleşmesi

```js
metadata: {type:"kusurlu", role:"section", ikas:"Hero", device:"desktop", variant:"Z", contract:2}
```

## 5. Animasyona hazır tasarım kuralları

### 5.1 Bu plana özgü motion tarifleri

| ID | Ad | Hareket | Zorunlu katman yapısı | Uygulama | Mobil | Azaltılmış hareket |
|---|---|---|---|---|---|---|
| **Z-M-01** | Perde | `{ clip: "inset(100% 0 0 0)" } → { clip: "inset(0)" }` | `hero-stage` (clip) | animejs | aynı | anında |
| **Q-M-01** | Yanlış önek | — | — | css-transition | aynı | anında |

## 6. Yapım sırası

### 6.0 Design System frame'leri

| Kök frame | İçerik |
|---|---|
| `Z/DS/Colors` | renkler |
| `Z/DS/Typography` | yazı stilleri |
| `Z/DS/Spacing` | boşluklar |
| `Z/DS/Icons` | ikonlar |
| `Z/DS/Motion` | motion lejantı |

### 6.1 Bileşenler (`Z/Sub/…`)

| Bileşen | Yapı | Durumlar (ayrı frame) |
|---|---|---|
| `ProductCard` | `card-images` (clip): `image-front` + `image-back` · `card-title` {data:product.name} | varsayılan · hover · stok yok |
| `Button` | `button` (clip) içinde `top` + `bottom` | varsayılan · hover · pasif · yükleniyor · stok yok |
| `Marquee` | `marquee` (clip) → `marquee-track` → metin ×3 | — |

Bileşen animasyon hedefleri:

<!-- anim-targets:start -->
```yaml
- id: Z-CMP-01
  section: Sub/ProductCard
  layer: image-back
  recipe: M-09
  trigger: hover
  what: "Ön görsel arka görsele geçer"
  from: { front.opacity: 1 }
  to: { front.opacity: 0 }
  timing: { duration: 0.4 }
  impl: css-transition
  mobile: kapalı
  reducedMotion: anında
  done: false
- id: Z-CMP-02
  section: Sub/Ghost
  layer: ghost
  recipe: M-10
  trigger: hover
  what: "Olmayan bileşen"
  from: { x: 0 }
  to: { x: 1 }
  timing: { duration: 0.3 }
  impl: css-transition
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

### 6.2 Bölümler ve overlay'ler

#### Section/Header
- **Kullanıldığı yer:** tüm sayfalar
- **ikas:** header-section (--isHeader)
- **Prop'lar:** `logo` SVG · `navLinks` LIST_OF_LINK · `searchText` TEXT · `backgroundColor` COLOR
- **Desktop:** tek satır.
- **Mobil:** menü butonu solda.

```
header
├─ ticker-strip (clip)
│   └─ marquee-track                 {text:TEXT} ×6
└─ header-row
    ├─ header-logo                   {logo:svg}
    ├─ nav-link ×4                   {Nav_label:TEXT}
    └─ search-button                 "SEARCH"
```

<!-- anim-targets:start -->
```yaml
- id: Z-HDR-01
  section: Header
  layer: marquee-track
  via: Marquee
  recipe: M-14
  trigger: auto-loop
  what: "Şerit kayar"
  from: { x: 0 }
  to: { x: -50% }
  timing: { speed: "60px/s" }
  impl: css-keyframes
  mobile: aynı
  reducedMotion: durur
  done: false
- id: Z-HDR-01
  section: Header
  layer: nav-link
  recipe: M-17
  trigger: hover
  what: "Yinelenen id ve yasak tarif"
  from: { y: 0 }
  to: { y: 1 }
  timing: { duration: 0.3 }
  impl: gsap
  mobile: aynı
  reducedMotion: anında
  done: false
- id: Z-hdr-3
  section: Header
  layer: cart-button
  via: Ghost
  recipe: M-99
  trigger: wiggle
  what: Anahtar eksik: mobile yok
  from: { y: 0 }
  to: { y: 1
  timing: { duration: 0.3 }
  impl: css-transition
  reducedMotion: anında
  done: no
  speed: 3
```
<!-- anim-targets:end -->

#### Section/Hero
- **Kullanıldığı yer:** Home
- **ikas:** hero-slider-section
- **Desktop:** tam ekran görsel.
- **Mobil:** kısa.

```
hero
├─ hero-stage (clip)                 {slides:COMPONENT_LIST}
└─ hero-title                        {title:TEXT}
```

<!-- anim-targets:start -->
```yaml
- id: Z-HERO-01
  section: Hero
  layer: hero-stage
  recipe: Z-M-01
  trigger: state-change
  what: "Görsel perdeyle değişir"
  from: { clip: "inset(100% 0 0 0)" }
  to: { clip: "inset(0)" }
  timing: { duration: 1.0 }
  impl: animejs
  mobile: aynı
  reducedMotion: anında
  done: false
```
<!-- anim-targets:end -->

#### Overlay/CartDrawer
- **Kullanıldığı yer:** Header
- **ikas:** Header sub-component
- **Desktop:** sağdan çekmece.
- **Mobil:** tam genişlik.

```
cart-overlay
├─ scrim
└─ cart-drawer                       {cartTitleText:TEXT}
```

### 6.3 Sayfalar

| Sayfa | Bölümler (sırayla) |
|---|---|
| `Home` | Header · Hero · CartDrawer · Missing |

### 6.5 Motion States

| Tarif | Örnek bölüm | Çizilecek kareler |
|---|---|---|
| M-22 | Header (`faq-item`) | akordeon: kapalı → açık |

## 7. Animasyon hedefleri özeti

Toplam **7 hedef**.

| Bölüm | Hedef | Tarifler | ID aralığı |
|---|---|---|---|
| Header | 2 | M-14 | `Z-HDR-01` … `Z-HDR-02` |
| Hero | 1 | Z-M-01 | `Z-HERO-01` … `Z-HERO-01` |
| Sub/ProductCard | 1 | M-09 | `Z-CMP-01` … `Z-CMP-01` |

| Tarif | Kullanım | Uygulama yolu |
|---|---|---|
| M-09 | 1 | css-transition |
| M-14 | 2 | css-keyframes |

```
açık kalan fence
