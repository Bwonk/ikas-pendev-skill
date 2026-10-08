# Port manifest — Gizem (C, contract 1)

Kaynak: `port-manifest.json` (schema 1). Bu dosya ondan üretilir; elle düzenlenmez. Canlı token eşleşmeleri `globals-runbook.md` sonundaki tablodadır.

## Özet

| Section | Sub | Sayfa | Overlay | Anim hedefi | Açık soru |
|---|---|---|---|---|---|
| 31 | 20 | 16 | 3 | 115 | 21 |

**Engelleyici 2 açık soru var**: canvas plana yetişmeden port başlamaz.

## Tema global'leri

### Renkler

| Ad | pen.dev | Açık | Koyu | ikas |
|---|---|---|---|---|
| Renk / Zemin | `color-bg` | `#EFEBE2` | `#0D0D0D` | colorScheme slot `Background` |
| Renk / Metin | `color-text` | `#0D0D0D` | `#EFEBE2` | colorScheme slot `Text` |
| Renk / Soluk Metin | `color-muted` | `#6B675F` | `#8F8B82` | colorScheme slot `Muted` |
| Renk / Çizgi | `color-line` | `#0D0D0D` | `#EFEBE2` | colorScheme slot `Line` |
| Renk / Yüzey | `color-surface` | `#E3DED2` | `#1A1A1A` | colorScheme slot `Surface` |
| Renk / Ters Zemin | `color-inverse-bg` | `#0D0D0D` | `#EFEBE2` | colorScheme slot `PrimaryButton/Background` |
| Renk / Ters Metin | `color-inverse-text` | `#EFEBE2` | `#0D0D0D` | colorScheme slot `PrimaryButton/Text` |
| Renk / Vurgu | `color-accent` | `#FF3B1F` | `#FF3B1F` | color `Accent` |
| Renk / Vurgu Üstü Metin | `color-accent-text` | `#0D0D0D` | `#0D0D0D` | color `AccentText` |
| Renk / Perde | `color-scrim` | `#0D0D0D99` | `#0D0D0DB3` | `global.css` `--color-scrim` |

### Tipografi

| Ad | pen.dev | Aile | Ağırlık | Satır | Masaüstü | Mobil |
|---|---|---|---|---|---|---|
| Tipografi / Display | `text-display` | Sofia Sans Extra Condensed | — | 0.9 | 168 | 72 |
| Tipografi / Başlık H2 | `text-h2` | Sofia Sans Extra Condensed | — | 0.9 | 112 | 52 |
| Tipografi / Başlık H3 | `text-h3` | Sofia Sans Extra Condensed | — | 0.9 | 64 | 40 |
| Tipografi / Başlık H4 | `text-h4` | Sofia Sans Extra Condensed | — | 0.9 | 36 | 26 |
| Tipografi / Ürün Adı | `text-title` | Archivo Narrow | 700 | 1.1 | 22 | 18 |
| Tipografi / Arayüz | `text-ui` | Archivo Narrow | 700 | 1.1 | 18 | 16 |
| Tipografi / Arayüz Küçük | `text-ui-sm` | Archivo Narrow | 700 | 1.1 | 15 | 14 |
| Tipografi / Rozet | `text-badge` | Archivo Narrow | 700 | 1.1 | 12 | 11 |
| Tipografi / Etiket | `text-label` | Space Mono | — | — | 12 | 11 |
| Tipografi / Gövde | `text-body` | Archivo Narrow | 500 | 1.35 | 16 | 15 |
| Tipografi / Fiyat | `text-price` | Archivo Narrow | 700 | — | 22 | 18 |

### Kırılımlar

| Ad | Genişlik |
|---|---|
| Kırılım / Laptop | 1199 |
| Kırılım / Tablet | 991 |
| Kırılım / Mobil | 767 |

### Keyframe'ler

| Ad | Kullanan hedefler |
|---|---|
| Animasyon / Hotspot pulse + kart (noktalar elle) | C-CMP-07 |
| Animasyon / Metin marquee | C-CMP-08, C-HDR-01, C-TICK-01, C-MOS-02, C-MQT-01, C-NF-01 |
| Animasyon / Yükleme fade-up | C-ABH-03, C-TML-02, C-CNT-03, C-CRTP-03, C-AUTH-02 |

### global.css

| Custom property | Masaüstü | Mobil |
|---|---|---|
| `--color-scrim` | `#0D0D0D99` / `#0D0D0DB3` | (mod: light / dark) |
| `--space-page` | 32 | 16 |
| `--space-grid` | 0 | 0 |
| `--space-card` | 12 | 10 |
| `--space-panel` | 24 | 16 |
| `--space-xs` | 6 | 4 |
| `--space-sm` | 12 | 10 |
| `--space-md` | 16 | 12 |
| `--space-section` | 120 | 64 |
| `--size-header` | 96 | 88 |
| `--size-line` | 2 | 2 |
| `--opacity-inactive` | 0.3 | 0.3 |

### Global değişkenler

| Ad | Tip | Değer |
|---|---|---|
| Çizgi / Varsayılan | BORDER | `{"width": {"value": 2, "unit": "px"}, "style": "solid", "color": "#0D0D0D"}` |

## Sub-component'ler

| Ad | Durumlar | Prop'lar | Animasyonlar |
|---|---|---|---|
| `ProductCard` | hover · stok yok · indirimli | — | C-CMP-01, C-CMP-02 |
| `ProductCardSmall` | hover | — | C-CMP-03 |
| `BlogCard` | hover | — | C-CMP-04 |
| `Button` | hover · pasif · yükleniyor | — | C-CMP-05 |
| `ArrowLink` | hover | — | C-CMP-06 |
| `Badge` | SALE · BEST SELLER | — | — |
| `Hotspot` | açık | — | C-CMP-07 |
| `Marquee` | — | — | C-CMP-08 |
| `Breadcrumbs` | — | — | — |
| `Tabs` | pasif · hover | — | C-CMP-09 |
| `VariantChip` | pasif · hover · stok yok | — | C-CMP-10 |
| `FormField` | dolu · odak · hata · pasif | — | — |
| `Checkbox` | boş | — | — |
| `AccordionItem` | kapalı | — | C-CMP-11 |
| `QuantitySelector` | alt sınır | — | — |
| `SectionHeading` | açıklamasız | — | C-CMP-12 |
| `IconButton` | hover | — | — |
| `Spinner` | — | — | — |
| `Sticker` | dönük | — | C-CMP-13 |
| `ScrambleText` | karışık | — | C-CMP-14 |

## Section'lar

### Header

- **Şablon:** `header-section` · **Bayraklar:** `isHeader`, `container`
- **Frame'ler:** `C/Section/Header@desktop` (n0054) · `C/Section/Header@mobile` (n0055)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `logo` | SVG | — | Marka | `header-logo` |
| `announcements` | COMPONENT_LIST | — | Bileşenler | — |
| `navLinks` | LIST_OF_LINK | — | Bağlantılar | — |
| `searchText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `accountText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `cartText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `menuText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `backgroundColor` | COLOR | — | Renkler | — |
| `text` | TEXT | — | Metinler | `marquee-track` |

- **Çocuklar:** `announcements` COMPONENT_LIST → AnnouncementItem
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-HDR-01, C-HDR-02, C-HDR-03
- **Overlay'ler:** `MenuOverlay` (açık), `CartDrawer` (boş · dolu · yükleniyor), `SearchOverlay` (boş · yazarken · sonuçsuz)

#### Header › Overlay MenuOverlay

- **Cihazlar:** desktop, mobile · **Frame'ler:** `C/Overlay/MenuOverlay@desktop — açık` (n0056) · `C/Overlay/MenuOverlay@mobile — açık` (n0057)
- **Animasyonlar:** C-MENU-01, C-MENU-02, C-MENU-03, C-MENU-04

_Prop yok._

#### Header › Overlay CartDrawer

- **Cihazlar:** desktop, mobile · **Frame'ler:** `C/Overlay/CartDrawer@desktop — boş` (n0058) · `C/Overlay/CartDrawer@desktop — dolu` (n0059) · `C/Overlay/CartDrawer@desktop — yükleniyor` (n0060) · `C/Overlay/CartDrawer@mobile — boş` (n0061) · `C/Overlay/CartDrawer@mobile — dolu` (n0062) · `C/Overlay/CartDrawer@mobile — yükleniyor` (n0063)
- **Animasyonlar:** C-CART-01, C-CART-02, C-CART-03

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `cartTitleText` | TEXT | — | Metinler | `cart-header` |
| `cartEmptyTitle` | TEXT | — | Metinler | `cart-empty` |
| `cartEmptyText` | TEXT | — | Metinler | `cart-empty` |
| `cartShippingLabel` | TEXT | — | Metinler | `cart-shipping-row` |
| `cartShippingNote` | TEXT | — | Metinler | `cart-shipping-row` |
| `cartSubtotalLabel` | TEXT | — | Metinler | `cart-subtotal-row` |
| `checkoutButtonText` | TEXT | — | Metinler | `checkout-button` |

#### Header › Overlay SearchOverlay

- **Cihazlar:** desktop, mobile · **Frame'ler:** `C/Overlay/SearchOverlay@desktop — boş` (n0064) · `C/Overlay/SearchOverlay@desktop — yazarken` (n0065) · `C/Overlay/SearchOverlay@desktop — sonuçsuz` (n0066) · `C/Overlay/SearchOverlay@mobile — boş` (n0067) · `C/Overlay/SearchOverlay@mobile — yazarken` (n0068) · `C/Overlay/SearchOverlay@mobile — sonuçsuz` (n0069)
- **Animasyonlar:** C-SRCH-01, C-SRCH-02

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `searchPlaceholder` | TEXT | — | Metinler | `search-field` |
| `searchEmptyText` | TEXT | — | Metinler | `search-empty` |

### Footer

- **Şablon:** `footer-section` · **Bayraklar:** `isFooter`
- **Frame'ler:** `C/Section/Footer@desktop` (n0070) · `C/Section/Footer@mobile` (n0071)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `newsletterTitle` | TEXT | — | Metinler | `footer-newsletter-title` |
| `wordmarkText` | TEXT | — | Metinler | `footer-wordmark` |
| `copyrightText` | TEXT | — | Metinler | `footer-legal` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-FTR-01, C-FTR-02, C-FTR-03
- **Overlay'ler:** —

### HeroSplit

- **Şablon:** `hero-slider-section` · **Bayraklar:** `container`
- **Frame'ler:** `C/Section/HeroSplit@desktop` (n0072) · `C/Section/HeroSplit@mobile` (n0073)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `slides` | COMPONENT_LIST | — | Bileşenler | — |
| `dropLabel` | TEXT | — | Metinler | `hero-meta` |
| `season` | TEXT | — | Metinler | `hero-meta` |
| `buttonText` | TEXT | — | Metinler | `hero-button` |
| `stickerText` | TEXT | — | Metinler | `hero-sticker` |
| `countdownDate` | DATE | — | Ayarlar | — |
| `autoplayDelay` | NUMBER | — | Ayarlar | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** `slides` COMPONENT_LIST → HeroSplitSlide (`image` IMAGE, `title` TEXT, `link` LINK)
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-HERO-01, C-HERO-02, C-HERO-03, C-HERO-04, C-HERO-05, C-HERO-06
- **Overlay'ler:** —

### TickerStrip

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/TickerStrip@desktop` (n0074) · `C/Section/TickerStrip@mobile` (n0075)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `text` | TEXT | — | Metinler | `marquee-track` |
| `speed` | NUMBER | — | Ayarlar | — |
| `direction` | ENUM | — | Ayarlar | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-TICK-01
- **Overlay'ler:** —

### ProductIndex

- **Şablon:** `product-slider-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/ProductIndex@desktop` (n0076) · `C/Section/ProductIndex@mobile` (n0077)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `linkText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `link` | LINK | — | Bağlantılar | — |
| `productList` | PRODUCT_LIST | — (merchant verisi) | İçerik | `index-row` |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-IDX-01, C-IDX-02, C-IDX-03, C-IDX-04
- **Overlay'ler:** —

### LookbookScroll

- **Şablon:** (özel) · **Bayraklar:** `container`, `custom`
- **Frame'ler:** `C/Section/LookbookScroll@desktop` (n0078) · `C/Section/LookbookScroll@mobile` (n0079)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `lookbook-title` |
| `frames` | COMPONENT_LIST | — | Bileşenler | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** `frames` COMPONENT_LIST → LookbookFrame (`image` IMAGE, `note` TEXT, `product` PRODUCT)
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-LOOK-01, C-LOOK-02, C-LOOK-03, C-LOOK-04
- **Overlay'ler:** —

### CategoryMosaic

- **Şablon:** `category-images-section` · **Bayraklar:** `container`
- **Frame'ler:** `C/Section/CategoryMosaic@desktop` (n0080) · `C/Section/CategoryMosaic@mobile` (n0081)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `cells` | COMPONENT_LIST | — | Bileşenler | — |
| `countSuffixText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** `cells` COMPONENT_LIST → MosaicCell (`category` CATEGORY, `image` IMAGE, `label` TEXT, `link` LINK)
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-MOS-01, C-MOS-02, C-MOS-03
- **Overlay'ler:** —

### DropGrid

- **Şablon:** `product-slider-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/DropGrid@desktop` (n0082) · `C/Section/DropGrid@mobile` (n0083)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `metaText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `linkText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `quickAddText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `link` | LINK | — | Bağlantılar | — |
| `productList` | PRODUCT_LIST | — (merchant verisi) | İçerik | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-DROP-01, C-DROP-02, C-DROP-03, C-DROP-04
- **Overlay'ler:** —

### Manifesto

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/Manifesto@desktop` (n0084) · `C/Section/Manifesto@mobile` (n0085)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `label` | TEXT | — | Metinler | `manifesto-label` |
| `text` | TEXT | — | Metinler | `manifesto-text` |
| `signature` | TEXT | — | Metinler | `manifesto-footer` |
| `buttonText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `link` | LINK | — | Bağlantılar | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-MANI-01, C-MANI-02
- **Overlay'ler:** —

### StickerWall

- **Şablon:** (özel) · **Bayraklar:** `container`, `custom`
- **Frame'ler:** `C/Section/StickerWall@desktop` (n0086) · `C/Section/StickerWall@mobile` (n0087)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `wall-title` |
| `linkText` | TEXT | — | Metinler | `link` |
| `link` | LINK | — | Bağlantılar | — |
| `images` | IMAGE_LIST | — (merchant verisi) | Görseller | `wall-photo` |
| `stickers` | COMPONENT_LIST | — | Bileşenler | — |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** `stickers` COMPONENT_LIST → WallSticker (`text` TEXT)
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-WALL-01, C-WALL-02, C-WALL-03, C-WALL-04
- **Overlay'ler:** —

### JournalRows

- **Şablon:** `blog-home-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/JournalRows@desktop` (n0088) · `C/Section/JournalRows@mobile` (n0089)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `linkText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `link` | LINK | — | Bağlantılar | — |
| `blogList` | BLOG_LIST | — (merchant verisi) | İçerik | `journal-row` |
| `backgroundColor` | COLOR | — | Renkler | — |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-JROW-01, C-JROW-02, C-JROW-03
- **Overlay'ler:** —

### ProductList

- **Şablon:** `category-list-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/ProductList@desktop` (n0090) · `C/Section/ProductList@mobile` (n0091)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `countSuffixText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `viewToggleAriaLabel` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `applyFiltersText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `clearFiltersText` _(yalnız plan)_ | TEXT | — | Metinler | — |
| `title` | TEXT | — | Metinler | `list-title` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-PLP-01, C-PLP-02, C-PLP-03, C-PLP-04, C-PLP-05, C-PLP-06
- **Overlay'ler:** —

### CollectionHero

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/CollectionHero@desktop` (n0092) · `C/Section/CollectionHero@mobile` (n0093)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `backgroundImage` | IMAGE | — (merchant verisi) | Görseller | `collection-hero-bg` |
| `tagline` | TEXT | — | Metinler | `collection-tagline` |
| `title` | TEXT | — | Metinler | `collection-title` |
| `imageA` | IMAGE | — (merchant verisi) | Görseller | `collection-image-a` |
| `description` | TEXT | — | Metinler | `collection-description` |
| `imageB` | IMAGE | — (merchant verisi) | Görseller | `collection-image-b` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-COLL-01, C-COLL-02, C-COLL-03
- **Overlay'ler:** —

### ProductDetail

- **Şablon:** `product-detail-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/ProductDetail@desktop` (n0094) · `C/Section/ProductDetail@mobile` (n0095)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `sizeGuideText` | TEXT | — | Metinler | `link` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-PDP-01, C-PDP-02, C-PDP-03, C-PDP-04, C-PDP-05, C-PDP-06
- **Overlay'ler:** —

### ProductCarousel

- **Şablon:** `product-slider-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/ProductCarousel@desktop` (n0096) · `C/Section/ProductCarousel@mobile` (n0097)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `section-title` |
| `linkText` | TEXT | — | Metinler | `link` |
| `productList` | PRODUCT_LIST | — (merchant verisi) | İçerik | `ProductCard` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-CRSL-01, C-CRSL-02, C-CRSL-03
- **Overlay'ler:** —

### AboutHero

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/AboutHero@desktop` (n0098) · `C/Section/AboutHero@mobile` (n0099)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `backgroundImage` | IMAGE | — (merchant verisi) | Görseller | `about-hero-bg` |
| `title` | TEXT | — | Metinler | `title-line` |
| `missionLabel` | TEXT | — | Metinler | `about-mission-label` |
| `missionText` | TEXT | — | Metinler | `about-mission-text` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-ABH-01, C-ABH-02, C-ABH-03
- **Overlay'ler:** —

### PressSlider

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/PressSlider@desktop` (n0100) · `C/Section/PressSlider@mobile` (n0101)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `logo` | SVG | — | Marka | `press-logo` |
| `quote` | TEXT | — | Metinler | `press-text` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-PRS-01
- **Overlay'ler:** —

### ValuesStack

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/ValuesStack@desktop` (n0102) · `C/Section/ValuesStack@mobile` (n0103)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `image` | IMAGE | — (merchant verisi) | Görseller | `value-image` |
| `introTitle` | TEXT | — | Metinler | `value-title` |
| `introText` | TEXT | — | Metinler | `value-paragraph` |
| `title` | TEXT | — | Metinler | `value-title` |
| `text` | TEXT | — | Metinler | `value-paragraph` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-VAL-01, C-VAL-02, C-VAL-03, C-VAL-04
- **Overlay'ler:** —

### ProcessSteps

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/ProcessSteps@desktop` (n0104) · `C/Section/ProcessSteps@mobile` (n0105)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `section-title` |
| `text` | TEXT | — | Metinler | `process-text` |
| `image` | IMAGE | — (merchant verisi) | Görseller | `process-image` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-PRC-01, C-PRC-02, C-PRC-03
- **Overlay'ler:** —

### TeamGrid

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/TeamGrid@desktop` (n0106) · `C/Section/TeamGrid@mobile` (n0107)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `section-title` |
| `text` | TEXT | — | Metinler | `team-text` |
| `image` | IMAGE | — (merchant verisi) | Görseller | `team-member-image` |
| `role` | TEXT | — | Metinler | `team-member-info` |
| `name` | TEXT | — | Metinler | `team-member-info` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-TEAM-01, C-TEAM-02
- **Overlay'ler:** —

### Timeline

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/Timeline@desktop` (—) · `C/Section/Timeline@mobile` (—)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `section-title` |
| `year` | TEXT | — | Metinler | `timeline-year` |
| `text` | TEXT | — | Metinler | `timeline-text` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-TML-01, C-TML-02
- **Overlay'ler:** —

### CtaBanner

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/CtaBanner@desktop` (n0110) · `C/Section/CtaBanner@mobile` (n0111)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `image` | IMAGE | — (merchant verisi) | Görseller | `cta-image` |
| `title` | TEXT | — | Metinler | `cta-title` |
| `buttonText` | TEXT | — | Metinler | `cta-button` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-CTA-01, C-CTA-02
- **Overlay'ler:** —

### AnchorNav

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/AnchorNav@desktop` (n0112) · `C/Section/AnchorNav@mobile` (n0113)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `items` | LIST_OF_LINK | — | Bağlantılar | `anchor-link` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-ANC-01
- **Overlay'ler:** —

### BlogPost

- **Şablon:** `blog-post-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/BlogPost@desktop` (n0114) · `C/Section/BlogPost@mobile` (n0115)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `nextText` | TEXT | — | Metinler | `post-next` |
| `relatedProductsTitle` | TEXT | — | Metinler | `post-sidebar-title` |
| `relatedProducts` | PRODUCT_LIST | — (merchant verisi) | İçerik | `ProductCardSmall` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-BLP-01, C-BLP-02, C-BLP-03, C-BLP-04
- **Overlay'ler:** —

### MarqueeTitle

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/MarqueeTitle@desktop` (n0116) · `C/Section/MarqueeTitle@mobile` (n0117)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `text` | TEXT | — | Metinler | `marquee-track` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-MQT-01
- **Overlay'ler:** —

### Contact

- **Şablon:** (özel) · **Bayraklar:** `custom`
- **Frame'ler:** `C/Section/Contact@desktop` (n0118) · `C/Section/Contact@mobile` (n0119)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `infoTitle` | TEXT | — | Metinler | `contact-heading` |
| `socialLinks` | LIST_OF_LINK | — | Bağlantılar | `contact-socials` |
| `faqTitle` | TEXT | — | Metinler | `faq-heading` |
| `faqItems` | COMPONENT_LIST | — | Bileşenler | `faq-item` |
| `formTitle` | TEXT | — | Metinler | `contact-heading` |
| `submitText` | TEXT | — | Metinler | `submit-button` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-CNT-01, C-CNT-02, C-CNT-03
- **Overlay'ler:** —

### SupportContent

- **Şablon:** `rich-text-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/SupportContent@desktop` (n0120) · `C/Section/SupportContent@mobile` (n0121)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `navLinks` | LIST_OF_LINK | — | Bağlantılar | `support-link` |
| `contactTitle` | TEXT | — | Metinler | `support-contact` |
| `contactText` | TEXT | — | Metinler | `support-contact` |
| `title` | TEXT | — | Metinler | `support-title` |
| `content` | RICH_TEXT | — | Metinler | `support-rich-text` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-SUP-01, C-SUP-02
- **Overlay'ler:** —

### CartPage

- **Şablon:** `cart-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/CartPage@desktop` (n0122) · `C/Section/CartPage@mobile` (n0123)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `list-title` |
| `emptyTitle` | TEXT | — | Metinler | `cart-empty` |
| `emptyText` | TEXT | — | Metinler | `cart-empty` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-CRTP-01, C-CRTP-02, C-CRTP-03
- **Overlay'ler:** —

### AuthForms

- **Şablon:** `login-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/AuthForms@desktop` (n0124) · `C/Section/AuthForms@mobile` (n0125)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `image` | IMAGE | — (merchant verisi) | Görseller | `auth-image` |
| `title` | TEXT | — | Metinler | `auth-title` |
| `submitButtonText` | TEXT | — | Metinler | `submit-button` |
| `switchText` | TEXT | — | Metinler | `auth-switch` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-AUTH-01, C-AUTH-02
- **Overlay'ler:** —

### Account

- **Şablon:** `account-info-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/Account@desktop` (n0126) · `C/Section/Account@mobile` (n0127)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `list-title` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** —
- **Animasyonlar:** C-ACC-01, C-ACC-02
- **Overlay'ler:** —

### NotFound

- **Şablon:** `not-found-section` · **Bayraklar:** —
- **Frame'ler:** `C/Section/NotFound@desktop` (n0128) · `C/Section/NotFound@mobile` (n0129)

| Prop | Tip | Varsayılan | Grup | Katman |
|---|---|---|---|---|
| `title` | TEXT | — | Metinler | `not-found-title` |
| `text` | TEXT | — | Metinler | `not-found-text` |
| `buttonText` | TEXT | — | Metinler | `not-found-button` |

- **Çocuklar:** —
- **Veri bağlı metinler:** —
- **Kod metinleri:** `marquee-track` (TEXT)
- **Animasyonlar:** C-NF-01, C-NF-02
- **Overlay'ler:** —

## Sayfalar

| Sayfa | ikas sayfa tipi | Section'lar (sırayla) |
|---|---|---|
| `Home` | `INDEX` | Header · HeroSplit · TickerStrip · ProductIndex · LookbookScroll · CategoryMosaic · DropGrid · Manifesto · StickerWall · JournalRows · TickerStrip · Footer |
| `Category` | `CATEGORY` | Header · ProductList · Footer |
| `Collection` | `COLLECTION` | Header · CollectionHero · ProductList · Footer |
| `Product` | `PRODUCT_DETAIL` | Header · ProductDetail · ProductCarousel · ProductCarousel · StickerWall · Footer |
| `About` | `CUSTOM` | Header · AboutHero · Manifesto · PressSlider · ValuesStack · ProcessSteps · TeamGrid · Timeline · CtaBanner · Footer · AnchorNav |
| `Journal` | `BLOG` | Header · MarqueeTitle · JournalRows · Footer |
| `JournalPost` | `BLOG_POST` | Header · BlogPost · JournalRows · Footer |
| `Contact` | `CUSTOM` | Header · MarqueeTitle · Contact · ProductCarousel · Footer |
| `Support` | `CUSTOM` | Header · SupportContent · Footer |
| `Cart` | `CART` | Header · CartPage · Footer |
| `Login` | `LOGIN` | Header · AuthForms · Footer |
| `Register` | `REGISTER` | Header · AuthForms · Footer |
| `ForgotPassword` | `FORGOT_PASSWORD` | Header · AuthForms · Footer |
| `RecoverPassword` | `RECOVER_PASSWORD` | Header · AuthForms · Footer |
| `Account` | `ACCOUNT` | Header · Account · Footer |
| `NotFound` | `NOT_FOUND` | Header · NotFound · Footer |

## Animasyon hedefleri

| impl | Hedef |
|---|---|
| `css-transition` | 39 |
| `animejs + io-hook` | 20 |
| `animejs (ya da setInterval)` | 12 |
| `css-keyframes` | 11 |
| `scroll-scrub` | 10 |
| `animejs` | 8 |
| `layout` | 6 |
| `layout + css-transition` | 2 |
| `css scroll-snap` | 1 |
| `css-keyframes + css-transition` | 1 |
| `css-transition + animejs` | 1 |
| `css-transition + setInterval` | 1 |
| `io-hook + css-transition` | 1 |
| `layout + scroll-scrub` | 1 |
| `scroll-scrub benzeri (pointermove + rAF)` | 1 |

Tam liste `port-manifest.json` → `animTargets`.

## Kapsama denetimi

- **Header** → kullanılan token'lar: Renk / Vurgu, `font-mono` (Space Mono)
- **MenuOverlay** → kullanılan token'lar: `font-mono` (Space Mono), Tipografi / Display, Tipografi / Başlık H2
- **CartDrawer** → kullanılan token'lar: Tipografi / Başlık H4, Tipografi / Etiket, `--space-panel`, Tipografi / Fiyat
- **SearchOverlay** → kullanılan token'lar: Tipografi / Başlık H3
- **Footer** → kullanılan token'lar: Tipografi / Başlık H2, `font-mono` (Space Mono)
- **HeroSplit** → kullanılan token'lar: `font-mono` (Space Mono), Tipografi / Display
- **TickerStrip** → kullanılan token'lar: Tipografi / Başlık H2
- **ProductIndex** → kullanılan token'lar: Tipografi / Başlık H2, `font-mono` (Space Mono), Tipografi / Başlık H4, Tipografi / Fiyat
- **LookbookScroll** → kullanılan token'lar: Tipografi / Başlık H2, `font-display` (Sofia Sans Extra Condensed), `font-mono` (Space Mono)
- **CategoryMosaic** → kullanılan token'lar: Tipografi / Başlık H3, Tipografi / Başlık H2, `font-mono` (Space Mono)
- **DropGrid** → kullanılan token'lar: Tipografi / Başlık H2, `font-mono` (Space Mono)
- **Manifesto** → kullanılan token'lar: `font-mono` (Space Mono), Tipografi / Başlık H2, Tipografi / Başlık H3
- **StickerWall** → kullanılan token'lar: Tipografi / Başlık H2, `font-mono` (Space Mono)
- **JournalRows** → kullanılan token'lar: Tipografi / Başlık H2, `font-mono` (Space Mono), Tipografi / Başlık H3
- **ProductList** → kullanılan token'lar: Tipografi / Display, `font-mono` (Space Mono)
- **CollectionHero** → kullanılan token'lar: Tipografi / Arayüz, Tipografi / Display, `--space-page`
- **ProductDetail** → kullanılan token'lar: `font-mono` (Space Mono), Tipografi / Başlık H2, Tipografi / Fiyat, Tipografi / Gövde
- **ProductCarousel** → kullanılan token'lar: Tipografi / Başlık H2, `--space-section`
- **AboutHero** → kullanılan token'lar: Tipografi / Display, Tipografi / Arayüz Küçük, Tipografi / Arayüz
- **PressSlider** → kullanılan token'lar: Tipografi / Ürün Adı
- **ValuesStack** → kullanılan token'lar: Tipografi / Başlık H2, Tipografi / Arayüz, Tipografi / Başlık H3
- **ProcessSteps** → kullanılan token'lar: Tipografi / Başlık H2, Tipografi / Arayüz, Tipografi / Gövde, `--space-section`
- **TeamGrid** → kullanılan token'lar: Tipografi / Başlık H2, Tipografi / Arayüz, `--space-card`, Tipografi / Etiket, Tipografi / Ürün Adı, `--space-section`, `--space-grid`
- **Timeline** → kullanılan token'lar: Tipografi / Başlık H2, `--space-page`, Tipografi / Arayüz, Tipografi / Gövde, `--space-section`
- **CtaBanner** → kullanılan token'lar: Tipografi / Başlık H2
- **AnchorNav** → kullanılan token'lar: Tipografi / Başlık H4, Renk / Metin (şema slotu Text), Renk / Soluk Metin (şema slotu Muted), Renk / Zemin (şema slotu Background)
- **BlogPost** → kullanılan token'lar: Tipografi / Başlık H2, Tipografi / Gövde, Tipografi / Başlık H3, Tipografi / Başlık H4
- **MarqueeTitle** → kullanılan token'lar: Tipografi / Display
- **Contact** → kullanılan token'lar: Tipografi / Başlık H3, Tipografi / Arayüz Küçük, Tipografi / Etiket, Tipografi / Gövde
- **SupportContent** → kullanılan token'lar: Tipografi / Arayüz Küçük, Renk / Metin (şema slotu Text), Tipografi / Başlık H3, Tipografi / Başlık H4, Tipografi / Gövde
- **CartPage** → kullanılan token'lar: Tipografi / Display, Tipografi / Başlık H4, Tipografi / Fiyat
- **AuthForms** → kullanılan token'lar: Tipografi / Başlık H2, Tipografi / Etiket
- **Account** → kullanılan token'lar: Tipografi / Display
- **NotFound** → kullanılan token'lar: Tipografi / Display, Tipografi / Başlık H3, Tipografi / Arayüz
- **Sub/ProductCard** → kullanılan token'lar: `font-ui` (Archivo Narrow), `font-mono` (Space Mono)
- **Sub/ProductCardSmall** → kullanılan token'lar: Tipografi / Arayüz
- **Sub/BlogCard** → kullanılan token'lar: `--space-panel`, Tipografi / Etiket, Tipografi / Başlık H4
- **Sub/Button** → kullanılan token'lar: Tipografi / Arayüz
- **Sub/ArrowLink** → kullanılan token'lar: Tipografi / Arayüz
- **Sub/Badge** → kullanılan token'lar: Tipografi / Rozet
- **Sub/Hotspot** → kullanılan token'lar: —
- **Sub/Marquee** → kullanılan token'lar: —
- **Sub/Breadcrumbs** → kullanılan token'lar: Tipografi / Etiket
- **Sub/Tabs** → kullanılan token'lar: —
- **Sub/VariantChip** → kullanılan token'lar: —
- **Sub/FormField** → kullanılan token'lar: Tipografi / Arayüz Küçük
- **Sub/Checkbox** → kullanılan token'lar: Tipografi / Etiket
- **Sub/AccordionItem** → kullanılan token'lar: —
- **Sub/QuantitySelector** → kullanılan token'lar: —
- **Sub/SectionHeading** → kullanılan token'lar: Tipografi / Başlık H2
- **Sub/IconButton** → kullanılan token'lar: —
- **Sub/Spinner** → kullanılan token'lar: —
- **Sub/Sticker** → kullanılan token'lar: `font-mono` (Space Mono)
- **Sub/ScrambleText** → kullanılan token'lar: —

| Kontrol | Sonuç | Not |
|---|---|---|
| Her global en az bir bileşende kullanılıyor | kaldı | kullanılmayan: `color-line`, `color-surface`, `color-inverse-bg`, `color-inverse-text`, `color-accent-text`, `color-scrim`, `space-xs`, `space-sm`, `space-md`, `size-header`, `size-line`, `opacity-inactive` |
| Canvas'taki her `$değişken` bir global'e ya da `global.css`'e eşleniyor | geçti | plan ağacı üzerinden denetlendi (canvas dump'ı değişken taşımaz) |
| Kapsamdaki her sayfa tipinin sayfası ve section'ı var | kaldı | sayfası olmayan: `SEARCH`, `FAVORITES` (brief okunmadı; 06-page-coverage §2 varsayılan kapsamı) |
| Her anim hedefinin izinli bir `impl`'i (ve gerekiyorsa keyframe'i) var | kaldı | impl dışı: C-CRSL-02 (`css scroll-snap`); keyframe noktaları elle doldurulacak: C-CMP-07 |

## Açık sorular

1. **data-unmarked** `contract` — Contract 1: metinlerde textClass yok; dataBound ve codeText boş. Veri bağlı ve kodla üretilen metinler aktarımda elle belirlenmeli.
2. **prop-mismatch** `Header.searchText` — Planda TEXT, canvas'ta prop yok
3. **prop-mismatch** `Header.accountText` — Planda TEXT, canvas'ta prop yok
4. **prop-mismatch** `Header.cartText` — Planda TEXT, canvas'ta prop yok
5. **prop-mismatch** `Header.menuText` — Planda TEXT, canvas'ta prop yok
6. **prop-mismatch** `ProductIndex.title` — Planda TEXT, canvas'ta prop yok
7. **prop-mismatch** `ProductIndex.linkText` — Planda TEXT, canvas'ta prop yok
8. **prop-mismatch** `CategoryMosaic.countSuffixText` — Planda TEXT, canvas'ta prop yok
9. **prop-mismatch** `DropGrid.title` — Planda TEXT, canvas'ta prop yok
10. **prop-mismatch** `DropGrid.metaText` — Planda TEXT, canvas'ta prop yok
11. **prop-mismatch** `DropGrid.linkText` — Planda TEXT, canvas'ta prop yok
12. **prop-mismatch** `DropGrid.quickAddText` — Planda TEXT, canvas'ta prop yok
13. **prop-mismatch** `Manifesto.buttonText` — Planda TEXT, canvas'ta prop yok
14. **prop-mismatch** `JournalRows.title` — Planda TEXT, canvas'ta prop yok
15. **prop-mismatch** `JournalRows.linkText` — Planda TEXT, canvas'ta prop yok
16. **prop-mismatch** `ProductList.countSuffixText` — Planda TEXT, canvas'ta prop yok
17. **prop-mismatch** `ProductList.viewToggleAriaLabel` — Planda TEXT, canvas'ta prop yok
18. **prop-mismatch** `ProductList.applyFiltersText` — Planda TEXT, canvas'ta prop yok
19. **prop-mismatch** `ProductList.clearFiltersText` — Planda TEXT, canvas'ta prop yok
20. **missing-section** `Timeline` — Planda var, canvas'ta `C/Section/Timeline@desktop` / `C/Section/Timeline@mobile` kök frame'i yok (anim hedefleri: C-TML-01, C-TML-02) **(engelleyici)**
21. **anim-missing-on-canvas** `C-PDP-03` — Plandaki hedef (ProductDetail · pdp-image) canvas'ta hiçbir kök frame'de yok (metadata.anim / context) **(engelleyici)**
