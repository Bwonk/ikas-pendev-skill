# Components — bileşen envanteri ve ikas eşlemesi

Kaynak: https://referans.example/ katman ağacı (`data-framer-name`) + ekran ölçümleri (1444px / 570px).
Token adları ve motion tarifleri (`M-xx`) için: [`globals.md`](./globals.md).

Üç seviye:
- **Section** — ikas `type: section`; `src/components/` altında; editörde sayfaya eklenir. pen.dev'de `Section/Ad`.
- **Component** — bir section'ın `COMPONENT_LIST` slotuna giren çocuk; `src/components/` altında, `type` yok. pen.dev'de `Component/Ad`.
- **Sub** — sadece kod içinde kullanılan yardımcı; `src/sub-components/`; `ikas.config.json`'da yer almaz. pen.dev'de `Sub/Ad`.

Prop tabloları **öneridir**; prop'lar CLI ile eklenir (`npx ikas-component config add-component --props '[...]'`), dosyalar elle düzenlenmez.

---

## 1. Sayfa → section bileşimi

| Sayfa (ikas sayfa tipi) | Referans URL | Section'lar (sırayla) |
|---|---|---|
| Ana sayfa (INDEX) | `/` | HeroSlider · FeaturedCollection (promo solda) · FeaturedCollection (promo sağda) · ShoppableImages · CategoryCards · SplitBanners · SocialFeed · JournalFeatured |
| Kategori (CATEGORY) | `/shop/category/*` | ProductList |
| Koleksiyon (CATEGORY ya da özel sayfa) | `/shop/collections/*` | CollectionHero · ProductList |
| Ürün detay (PRODUCT_DETAIL) | `/shop/<ürün>` | ProductDetail · ProductCarousel (koleksiyondan) · ProductCarousel (benzer) · JournalFeatured · SocialFeed |
| Hakkında (özel sayfa) | `/about` | AboutHero · PressSlider · ValuesStack · ProcessSteps · TeamGrid · Timeline · CtaBanner · AnchorNav |
| Journal liste (BLOG) | `/journal` | BlogList |
| Journal yazı (BLOG post) | `/journal/<yazı>` | BlogPost · JournalFeatured (ilgili yazılar) |
| İletişim (özel sayfa) | `/contact` | MarqueeTitle · Contact · ProductCarousel |
| Destek / politika (özel sayfa) | `/support/*` | SupportContent |
| Her sayfa | — | Header (üstte) · Footer (altta) |
| Overlay'ler | — | Megamenu, MobileMenu, CartDrawer, SearchOverlay (Header içinde) · InfoDrawer (ProductDetail içinde) |

**Referansta olmayan ama ikas'ta gereken sayfalar** (tasarımda ayrıca üretilecek, aynı dil ile):

| Sayfa | ikas şablonu | Not |
|---|---|---|
| Sepet (CART) | `cart-section` | Referansta sadece çekmece var; ikas'ta tam sayfa da gerekir |
| Giriş / Kayıt / Şifremi unuttum / Şifre yenile | `login-section`, `register-section`, `forgot-password-section`, `recover-password-section` | Tek form, ortalanmış ya da bölünmüş düzen |
| Hesabım (ACCOUNT) | `account-info-section` | Sekmeler: bilgiler, siparişler, adresler, favoriler, sipariş detay |
| Favoriler | `favorites` | ProductList ızgarasını kullanır |
| 404 | `not-found-section` | Büyük başlık + ana sayfaya dönüş |
| E-posta doğrulama | `email-verification-section` | Durum mesajı |
| Arama sonuçları | `category-list-section` | ProductList'i arama başlığıyla kullanır |

---

## 2. Global section'lar

### Header  `--isHeader`
Referans: `Main Nav` 1444×60, üst+alt çizgi, sabit (fixed), zemin siyah. ikas şablonu: `header-section`.

```
header
├─ header-logo            106×60, yatay boşluk 20
├─ announcement-mask      688×60, clip  ← M-04
│   └─ announcement-text ×N
├─ header-nav
│   ├─ nav-link (Shop, caret'li)   132×60, sol çizgi  ← M-05, M-06
│   ├─ nav-link (About / Journal / Contact)           ← M-05
│   └─ header-actions     122×60: search-button 42 · account-button 40 · cart-button 40 + cart-count
└─ (mobil) menu-button · header-logo · header-actions
```

Durumlar: varsayılan · link hover (ters dolgu) · megamenu açık · mobil menü açık.
Mobil: hamburger sol, logo orta, ikonlar sağ; duyuru ve linkler MobileMenu içinde.

| Prop | Tip | Varsayılan | Grup |
|---|---|---|---|
| `logo` | SVG | — | Marka |
| `logoAltText` | TEXT | "Örnek" | Marka |
| `announcements` | COMPONENT_LIST (`AnnouncementItem`) | 3 öğe | Duyuru |
| `announcementInterval` | NUMBER | 3 | Duyuru |
| `navLinks` | LIST_OF_LINK | Shop, About, Journal, Contact | Menü |
| `megamenuColumns` | COMPONENT_LIST (`MegamenuColumn`) | Kategoriler, Koleksiyonlar | Megamenu |
| `megamenuCards` | COMPONENT_LIST (`MegamenuCard`) | 2 kart | Megamenu |
| `mobileSecondaryLinks` | LIST_OF_LINK | Kargo, İade | Menü |
| `searchPlaceholder`, `searchEmptyText`, `searchAriaLabel` | TEXT | — | Metinler |
| `accountAriaLabel`, `cartAriaLabel`, `menuAriaLabel`, `closeAriaLabel` | TEXT | — | Metinler |
| `cartTitleText`, `cartEmptyTitle`, `cartEmptyText`, `cartSubtotalLabel`, `cartShippingLabel`, `cartShippingNote`, `checkoutButtonText` | TEXT | — | Sepet metinleri |
| `backgroundColor` | COLOR | — | Görünüm |

Çocuk component'ler: `AnnouncementItem` (text TEXT, link LINK) · `MegamenuColumn` (title TEXT, links LIST_OF_LINK) · `MegamenuCard` (image IMAGE, title TEXT, subtitle TEXT, link LINK).
Sub: `NavLink`, `Megamenu`, `MobileMenu`, `CartDrawer`, `CartLineItem`, `SearchOverlay`, `IconButton`.
Motion: M-04, M-05, M-06, M-20 (sepet), M-21 (arama).

### Megamenu (Header overlay)
Referans: header altında 1444×354; 3 eşit sütun (481): linkler (2 kolon: Categories 8 link, Collections 4 link) · görsel kart · görsel kart. Kartlarda alttan gradyan, `text-h4` başlık + `text-ui-sm` alt başlık.

### MobileMenu (Header overlay)
Tam ekran, header altında: duyuru şeridi · `text-h3` linkler (Shop akordeon) · alt çizgili satırlar · `color-muted` ikincil linkler.

### CartDrawer (Header overlay)  — M-20
Referans: sağdan, genişlik ~500, tam yükseklik, sol çizgi; arkada blur'lu scrim.

```
cart-drawer
├─ cart-header     "0 ITEMS IN YOUR BAG." + kapat
├─ cart-body       boş durum (başlık + alt metin)  |  dolu: cart-line-item ×N
└─ cart-footer     shipping & taxes satırı · SUBTOTAL + tutar · checkout butonu (boşken soluk)
```
`CartLineItem`: 100×~130 görsel · ad · varyant · adet seçici · fiyat · kaldır.
Durumlar: boş · dolu · yükleniyor.

### SearchOverlay (Header overlay)  — M-21
Referansta ölçülemedi (tarayıcı aracı hata verdi). Yapı modülden: arama alanı + sonuç ızgarası. Tasarımda: header altında açılan panel; boş, yazarken ve sonuçsuz durumları.

### Footer  `--isFooter`
Referans: içeriğin arkasında sticky (M-16), yükseklik ~725. ikas şablonu: `footer-section`.

```
footer
├─ footer-banner     ~280: siyah-beyaz görsel + "MOVE YOUR WAY." (text-h2) + dev wordmark (parallax) + logo işareti
├─ footer-columns    4 sütun: Categories · Support · About · Social Media  (başlık text-ui, link text-ui-sm muted)
└─ footer-bottom     üst çizgi: newsletter-form (input 337 + buton 222, yükseklik 48) + onay kutusu · yasal linkler + telif
```
Mobil: sütunlar 2×2; form tam genişlik.

| Prop | Tip | Grup |
|---|---|---|
| `bannerImage` | IMAGE | Banner |
| `bannerTitle`, `wordmarkText` | TEXT | Banner |
| `logoMark` | SVG | Banner |
| `columns` | COMPONENT_LIST (`FooterColumn`: title TEXT, links LIST_OF_LINK) | Linkler |
| `newsletterPlaceholder`, `newsletterButtonText`, `newsletterSubmittingText`, `newsletterSuccessText`, `newsletterErrorText`, `newsletterConsentText` | TEXT | Bülten |
| `legalLinks` | LIST_OF_LINK | Alt |
| `copyrightText` | TEXT | Alt |
| `backgroundColor` | COLOR | Görünüm |

Motion: M-16, M-28, M-11.

---

## 3. Ana sayfa section'ları

### HeroSlider
Referans: 1444×703 (viewport − header). ikas şablonu: `hero-slider-section`.

```
hero-slider
├─ hero-slides
│   └─ hero-slide ×N:  hero-slide-mask (clip) → hero-slide-image → gradient-mask
├─ hero-text           sol alt, kenardan 20
│   ├─ hero-badge      çerçeveli etiket butonu (117×44)   ← M-11
│   ├─ hero-title      text-display, maske içinde          ← M-07
│   └─ hero-description  text-ui muted, maks. genişlik 500
├─ hero-thumbs         sağ alt: hero-thumb ×N (151×105, aralık 5) + progress-bar  ← M-08
└─ hero-click-left / hero-click-right   görünmez yarı ekran tıklama alanları
```
Mobil: yükseklik ~330; açıklama ve thumbnail yok; altta ince ilerleme çizgisi.

| Prop | Tip | Varsayılan |
|---|---|---|
| `slides` | COMPONENT_LIST (`HeroSlide`) | 3 |
| `autoplay` | BOOLEAN | true |
| `autoplayDelay` | NUMBER | 4 |
| `showThumbnails` | BOOLEAN | true |
| `prevAriaLabel`, `nextAriaLabel` | TEXT | — |
| `backgroundColor` | COLOR | — |

`HeroSlide`: `image` IMAGE · `mobileImage` IMAGE · `badgeText` TEXT · `title` TEXT · `description` TEXT · `link` LINK.
Motion: M-01/M-02 (ilk yükleme), M-07, M-08, M-11.

### FeaturedCollection
Referans: `New Arrivals` / `Best Sellers` blokları, 1444×835. Bir yanda 576 genişlik sticky promo panel (576×432), diğer yanda 2 sütun × 2 satır ürün kartı. İkinci kullanımda taraflar yer değiştirir.

```
featured-collection
├─ promo-panel (sticky)                          ← M-13
│   ├─ promo-image + hotspot                      ← M-12
│   └─ promo-header: link ("SHOP NOW ↗") + promo-title (text-h2, maske)  ← M-10, M-03
└─ product-grid: ProductCard ×4
```
Mobil: panel tam genişlik üstte; ürünler yatay kaydırmalı.

| Prop | Tip |
|---|---|
| `title`, `linkText` | TEXT |
| `link` | LINK |
| `promoImage` | IMAGE |
| `hotspotProduct` | PRODUCT |
| `hotspotX`, `hotspotY` | NUMBER (0–100) |
| `productList` | PRODUCT_LIST |
| `promoPosition` | ENUM (`left`, `right`) |
| `badgeNewText`, `badgeSaleText`, `badgeBestSellerText` | TEXT |
| `backgroundColor` | COLOR |

### ShoppableImages
Referans: `Product Display`, 2 görsel × 720×540, her birinde hotspot.
Prop: `items` COMPONENT_LIST (`ShoppableImage`: image IMAGE, product PRODUCT, hotspotX NUMBER, hotspotY NUMBER) · `backgroundColor`.
Mobil: alt alta. Motion: M-12.

### CategoryCards
Referans: 4 kart × 357×362. Kartta üstte marquee metin (kategori adı, `text-h2`, `color-muted`), ortada ürün görseli, altta kategori adı + "SHOP NOW ↗". ikas şablonu: `category-images-section`.

```
category-card
├─ marquee → marquee-track → kategori adı ×≥3     ← M-14
├─ category-image
└─ category-footer: category-label + link         ← M-10
```
Hover: marquee `muted→text`, etiket soluklaşır, link altı çizilir.
Prop: `cards` COMPONENT_LIST (`CategoryCard`: category CATEGORY, image IMAGE, label TEXT, linkText TEXT, link LINK) · `backgroundColor`.
Mobil: yatay kaydırmalı.

### SplitBanners
Referans: `Collections / About Us`, 2 × 720×780; tam kaplama görsel, sol altta link + çok satırlı `text-h2` başlık ("EXPLORE / OUR / COLLECTIONS").
Prop: `banners` COMPONENT_LIST (`SplitBanner`: image IMAGE, linkText TEXT, link LINK, title TEXT çok satırlı) · `backgroundColor`.
Mobil: alt alta, yükseklik ~380. Motion: M-03, M-10.

### SocialFeed
Referans: `Follow Us` / `Instagram Ticker`, üst boşluk 100; başlık (`text-h2`) + açıklama + "FOLLOW US ↗"; altında 5 görsel görünür (300×428, aralık 5), kesintisiz kayar.
Prop: `title`, `description`, `linkText` TEXT · `link` LINK · `images` IMAGE_LIST · `backgroundColor`.
Motion: M-03, M-15.

### JournalFeatured
Referans: `Journal`, üst boşluk 100; başlık satırı (başlık + açıklama + "VIEW ALL ↗"); öne çıkan yazı (818 görsel + 626 metin: tarih, `text-h3`, özet, "READ ENTRY ↗"); altında 3 `BlogCard`.
Prop: `title`, `description`, `viewAllText`, `readMoreText` TEXT · `viewAllLink` LINK · `blogList` BLOG_LIST · `showFeatured` BOOLEAN · `backgroundColor`.
Mobil: öne çıkan alt alta; kartlar yatay kaydırmalı. Motion: M-03, M-10.

---

## 4. Mağaza section'ları

### ProductList
Referans: PLP. Başlık alanı 126 (`text-display`), sticky filtre barı 72 (`text-h4` boyutunda sekmeler, aktif beyaz / pasif muted), 3 sütun ızgara. ikas şablonu: `category-list-section` (sayfalama / sonsuz kaydırma / filtre / sıralama oradan).

```
product-list
├─ list-header: list-title
├─ filter-bar (sticky): filter-tab ×N               ← M-18
└─ product-grid: ProductCard ×N  (3 sütun, aralık 5)
```
Mobil: tek sütun; sekmeler yatay kaydırmalı.

| Prop | Tip |
|---|---|
| `productList` | PRODUCT_LIST |
| `title` | TEXT (boşsa kategori adı) |
| `filterLinks` | LIST_OF_LINK |
| `showFilters`, `showSort`, `isInfinite` | BOOLEAN |
| `desktopColumns` | NUMBER |
| `emptyTitle`, `emptyText`, `loadMoreText`, `loadingText`, `sortLabel`, `filterLabel` | TEXT |
| `badgeNewText`, `badgeSaleText`, `badgeBestSellerText` | TEXT |
| `backgroundColor` | COLOR |

### CollectionHero
Referans: koleksiyon sayfası; arka plan görseli + koleksiyon adı (`text-display`) + slogan + açıklama + iki yardımcı görsel (3:4 ve 4:3).
Prop: `backgroundImage`, `imageA`, `imageB` IMAGE · `title`, `tagline`, `description` TEXT · `backgroundColor`.

### ProductDetail
Referans: PDP. Solda 500 genişlik sticky detay sütunu (viewport yüksekliğinde, sağ çizgi), sağda 944 galeri (her görsel bir viewport), sağ üstte dikey thumbnail şeridi (60×75, aralık 5). ikas şablonu: `product-detail-section`.

```
product-detail
├─ pdp-details (sticky)                              ← M-13
│   ├─ pdp-top: breadcrumbs · pdp-title (text-h3) · pdp-description (text-ui) · info-tabs (Materials / Care / Shipping)
│   └─ pdp-bottom: variant-chips · size-guide-link · (üst çizgi) pdp-price + shipping-note · add-to-cart-button
├─ pdp-gallery: pdp-image ×N
├─ pdp-thumbs                                         ← M-19
└─ mini-buy-bar (galeri sonrası alttan)               ← M-19
```
Durumlar: varyant seçili / pasif / stok yok · butonda yükleniyor · eklendi.
Mobil: galeri yatay; detaylar altında; sticky yok.

| Prop | Tip |
|---|---|
| `product` | PRODUCT |
| `components`, `bottomComponents` | COMPONENT_LIST (ikas şablonundaki slot yapısı) |
| `infoTabs` | COMPONENT_LIST (`InfoTab`: title TEXT, image IMAGE, content RICH_TEXT) |
| `homeBreadcrumbText`, `sizeGuideText`, `shippingNoteText`, `addToCartText`, `addingToCartText`, `addedToCartText`, `outOfStockText` | TEXT |
| `sizeGuideContent` | RICH_TEXT |
| `aspectRatio`, `objectFit` | ENUM |
| `backgroundColor` | COLOR |

### InfoDrawer (ProductDetail overlay)  — M-20
Referans: soldan, 460 genişlik; üstte marquee başlık (M-14) + görsel (460×~300); altında sekme başlıkları (`text-h4`, aktif beyaz) + zengin metin; arkada blur'lu scrim. Beden rehberi aynı çekmeceyi kullanır.

### ProductCarousel
Referans: `From this collection`, `You may also like`. Başlık satırı (`text-h2` + sağda link), altında yatay kaydırılan ProductCard'lar (478 genişlik, 3 görünür). ikas şablonu: `product-slider-section`.
Prop: `title`, `linkText` TEXT · `link` LINK · `productList` PRODUCT_LIST · `desktopColumns` NUMBER · rozet metinleri · `backgroundColor`.
Motion: M-03, M-10; sürükleme / scroll-snap.

---

## 5. İçerik section'ları

### AboutHero
Tam viewport; arka plan görseli (parallax M-27); sol altta 3 satır `text-display` başlık; sağda 300 genişlik misyon bloğu (etiket `text-ui-sm` muted + metin `text-ui`).
Prop: `backgroundImage` IMAGE · `title` TEXT · `missionLabel`, `missionText` TEXT · `backgroundColor`. Mobil: misyon başlığın altında.

### PressSlider
Yükseklik 410, alt+üst çizgi; ortada 600 genişlik kart: logo + alıntı (`text-h4` boyutuna yakın, ortalı); yan kartlar soluk.
Prop: `quotes` COMPONENT_LIST (`PressQuote`: logo SVG, quote TEXT) · `autoplayDelay` NUMBER · `backgroundColor`. Motion: M-26.

### ValuesStack
4 panel, her biri tam viewport ve sticky (üst üste biner): giriş paneli (`text-h2` + paragraf) + 3 değer (`text-h3` başlık + `text-ui` alt metin). Her panelde kenarda döndürülmüş görsel (4:3 solda / 3:4 sağda, sırayla).
Prop: `introTitle`, `introText` TEXT · `values` COMPONENT_LIST (`ValueItem`: title TEXT, text TEXT, image IMAGE, imageSide ENUM) · `backgroundColor`.
Motion: M-13, M-23, M-24. Mobil: normal akış, görsel üstte.

### ProcessSteps
1200 genişlik kap: başlık + paragraf; 3 sütun adım (başlık `text-ui` + `text-body`); altında tam genişlik görsel (788).
Prop: `title`, `text` TEXT · `steps` COMPONENT_LIST (`ProcessStep`: title, text) · `image` IMAGE · `backgroundColor`.

### TeamGrid
Başlık + paragraf; 4 sütun üye kartı (görsel + rol `text-label` + ad `text-title`).
Prop: `title`, `text` TEXT · `members` COMPONENT_LIST (`TeamMember`: image IMAGE, role TEXT, name TEXT) · `backgroundColor`. Mobil: yatay kaydırma.

### Timeline
`OUR JOURNEY`: 5 satır; yıl (`text-h2`) + başlık + paragraf, satırlar arası çizgi.
Prop: `title` TEXT · `items` COMPONENT_LIST (`TimelineItem`: year, title, text) · `backgroundColor`.

### CtaBanner
Tam genişlik görsel + `text-h2` başlık + buton.
Prop: `image` IMAGE · `title`, `buttonText` TEXT · `link` LINK · `backgroundColor`.

### AnchorNav
Altta sabit çubuk (yükseklik 72, üst çizgi), ortalı `text-h4` sekmeler: Mission · Press · Values · Process · Team · Journey.
Prop: `items` LIST_OF_LINK (çapa hedefleri) · `backgroundColor`. Motion: M-25.

### BlogList
Öne çıkan yazı (tam genişlik, 818 + 626) + 2 sütun kart ızgarası. ikas şablonu: `blog-home-section`.
Prop: `blogList` BLOG_LIST · `readMoreText`, `loadMoreText`, `emptyText` TEXT · `backgroundColor`.

### BlogPost
Hero (tam viewport görsel, tarih + `text-h2` başlık + özet, parallax) → 1200 genişlik gövde: solda içerik (breadcrumb, `text-h3` ara başlıklar, `text-body` paragraflar, görseller), sağda 372 genişlik sticky yan sütun (NEXT bağlantısı + RELATED PRODUCTS: `ProductCardSmall` ×3). ikas şablonu: `blog-post-section`.
Prop: `blog` BLOG · `relatedProducts` PRODUCT_LIST · `nextText`, `prevText`, `relatedProductsTitle`, `homeBreadcrumbText`, `journalBreadcrumbText` TEXT · `backgroundColor`.
Motion: M-27, M-13.

### MarqueeTitle
Tam genişlik kayan sayfa başlığı (`text-display`, "CONTACT CONTACT …"), alt çizgi.
Prop: `text` TEXT · `speed` NUMBER · `backgroundColor`. Motion: M-14.

### Contact
İki sütun (ortada çizgi). Sol: "WAYS TO REACH US" (e-posta, telefon, adres, sosyal linkler) + "FAQ" akordeon. Sağ: "GET IN TOUCH" formu (konu, ad, soyad, e-posta, telefon, sipariş no, mesaj; hücreler çizgili, bitişik) + tam genişlik gönder butonu.
Prop: `infoTitle`, `emailLabel`, `email`, `phoneLabel`, `phone`, `addressLabel`, `address`, `socialTitle` TEXT · `socialLinks` LIST_OF_LINK · `faqTitle` TEXT · `faqItems` COMPONENT_LIST (`FaqItem`: question TEXT, answer RICH_TEXT) · `formTitle` + alan etiketleri + `submitText`, `submittingText`, `successText`, `errorText` TEXT · `backgroundColor`.
Motion: M-22. ikas: form işlemleri için `form-handling` rehberi.

### SupportContent
Sol yan menü (destek linkleri + iletişim kutusu) + sağda zengin metin (`text-h3` başlık, `text-h4` ara başlıklar, `text-body`). ikas şablonu: `rich-text-section`.
Prop: `navLinks` LIST_OF_LINK · `title` TEXT · `content` RICH_TEXT · `contactTitle`, `contactText` TEXT · `contactLink` LINK · `backgroundColor`.

---

## 6. Sub-component'ler

| Sub | Referans ölçüsü | Durumlar | Motion |
|---|---|---|---|
| `ProductCard` | 429×415 / 478×451; dört kenar çizgi; `card-badges` (sol üst, boşluk 10) · `card-images` (4:3) · `card-info` (boşluk 10): kategori `text-label` muted · ad `text-title` · fiyat + eski fiyat · sağ altta ok | varsayılan · hover · stok yok | M-09 |
| `ProductCardSmall` | satır: 100×110 görsel + kategori + ad + fiyat + ok | varsayılan · hover | M-09 |
| `BlogCard` | görsel 478×268 + tarih + `text-h4` başlık + "READ ENTRY ↗" | varsayılan · hover | M-10 |
| `Button` | yükseklik 44–48; `text-ui`; dolu (beyaz zemin) / çerçeveli (1px) | varsayılan · hover · pasif · yükleniyor | M-11 |
| `ArrowLink` | `text-ui` + 20×20 ok + 1px alt çizgi | varsayılan · hover | M-10 |
| `Badge` | `text-badge`, zeminsiz | NEW · SALE · BEST SELLER | — |
| `Price` | `text-price` + üstü çizili eski fiyat | normal · indirimli | — |
| `Hotspot` | 48×48 dokunma alanı, 15×15 halka | kapalı · açık (mini ürün kartı) | M-12 |
| `Marquee` | clip + track | — | M-14 |
| `Breadcrumbs` | `text-label`, altı çizili linkler, son öğe muted | — | M-28 |
| `Tabs` | `text-h4` / `text-ui-sm`; aktif beyaz, pasif muted | aktif · pasif · hover | M-28 |
| `VariantChip` | yükseklik 28, 1px çerçeve, yatay boşluk 20; Manrope benzeri normal genişlik 13px | seçili (beyaz çerçeve + metin) · pasif (muted) · stok yok | M-28 |
| `Input` / `Textarea` | yükseklik 48, 1px çerçeve, `text-ui-sm` placeholder muted | boş · odak · hata · pasif | — |
| `Checkbox` | 12×12 | işaretli · boş | — |
| `AccordionItem` | satır yüksekliği ~44, sağda artı/eksi | açık · kapalı | M-22 |
| `Drawer` | scrim + panel kabuğu (sol/sağ) | açık · kapalı | M-20 |
| `SectionHeading` | başlık (`text-h2`) + açıklama + sağda `ArrowLink` | — | M-03 |
| `IconButton` | 40–42×60 dokunma alanı | varsayılan · hover | M-28 |
| `QuantitySelector` | eksi · adet · artı | — | — |
| `Spinner` | 16–20 | — | döngü |

---

## 7. ikas'a aktarım kuralları

**Proje:** `ornek/` (Preact + TS). MCP sunucusu `ornek/.mcp.json` içinde tanımlı → Claude Code'u `ornek/` klasöründe başlat; aksi halde MCP araçları bağlanmaz.

**MCP ne sağlar** (CLAUDE.md'deki 12 araçtan fazlası var, ~60 araç):
- Doküman: `get_section_template` (28 şablon), `get_section_child`, `get_framework_guide` (37 konu), `get_model_guide`, `get_function_doc`, `get_prop_types`, `search_docs`. `get_code_example` 2.9.8 sürümünde boş döner — kullanma.
- Canlı editör (`ikas theme dev` + editörde Connect gerekir): `import_section`, `add_sections_to_page`, `update_section_prop`, `upload_image(s)`, `search_products`, `list_categories`, `create_page`, `publish_theme` (`confirm: true` olmadan kuru çalışma).
- Tema global'leri: `list_theme_globals`, `create_theme_global` (color, typography, breakpoint, keyframe, colorScheme, globalVariable).

**Sıra:**
1. Tema global'lerini aç (`globals.md` → renk, tipografi, kırılım, paylaşılan keyframe).
2. `src/global.css` içine boşluk/ölçü/motion custom property'leri.
3. Sub-component'ler (`src/sub-components/<Ad>/index.tsx` + `styles.css`; mağaza verisi okuyan alt bileşen `observer(function Ad(){})`).
4. Section başına: `get_section_template` → ENUM gerekiyorsa önce `config add-enum` → `config add-component --type section --props '[...]'` → `index.tsx` + `styles.css` → `npx ikas-component check --json` → `npx ikas-component build`.
5. Header `--isHeader`, Footer `--isFooter`.
6. Editörde sayfalara yerleştir, içerik/görsel yükle.
7. Animasyon turu (seçilen pen.dev planının 8. bölümü).

**Kısıtlar:**
- `ikas.config.json`, `types.ts`, `global-types.ts`, `src/components/index.ts` elle düzenlenmez.
- JSX'te sabit metin yok: her metin TEXT prop (buton yükleme durumu için iki ayrı prop). pen.dev'de metin katmanı adı = prop adı olduğu için bu liste tasarımdan çıkar.
- Her section'da `backgroundColor` COLOR prop'u; 5+ prop varsa prop grubu.
- Kök bileşen `observer()` ile sarılmaz; alt bileşenler sarılır.
- CSS sadece sınıf seçicileriyle (otomatik `.cc_<id>` öneki); element seçici sızar.
- `@keyframes` / `@font-face` adları bileşene göre yeniden adlandırılır → bileşenler arası paylaşılamaz (paylaşım için tema keyframe token'ı).
- İzinli paketler: `preact`, `mobx`, `@ikas/bp-storefront*`, `@ikas/component-utils`, `animejs`, `three`. Diğerleri build hatası.
- SSR var: `window` / `document` / `IntersectionObserver` sadece `useEffect` içinde.
- Ürün görseli zinciri: `getSelectedProductVariant` → `getProductVariantMainImage` → `.image` → `getDefaultSrc` / `createMediaSrcset`; para biçimi `formatCurrency`.
- Tüccar verisi prop'larında (IMAGE, PRODUCT_LIST, CATEGORY…) `defaultValue` olmaz.
