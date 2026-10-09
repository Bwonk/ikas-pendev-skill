# Globals — referans token'ları ve motion tarifleri

Kaynak: https://referans.example/ (Referans Framer şablonu), 1444px ve 570px genişlikte ölçüldü.
Bu dosya referansın **ölçülen** değerlerini verir. Örnek'in kendi kimlik değerleri her pen.dev planının "Değişkenler" bölümündedir; buradaki **token adları** üç planda da aynıdır, sadece değerler değişir.

Etiketler: **[ölçüldü]** = siteden/CSS'ten/Framer modülünden okundu · **[tahmini]** = gözlemle kestirildi, aktarımda ayarlanacak.

Sütunlar: referans değeri → pen.dev değişkeni (`$ad`) → ikas karşılığı.

---

## 1. Renk

| Token | Referans | pen.dev | ikas |
|---|---|---|---|
| Zemin | `#000000` | `color-bg` | colorScheme slot `Background` |
| Metin | `#FFFFFF` | `color-text` | colorScheme slot `Text` |
| İkincil metin + çizgi | `#7A7A7A` | `color-muted`, `color-line` | tema rengi `Muted`, `Line` |
| Yüzey (koyu gri) | `#1C1C1C` | `color-surface` | tema rengi `Surface` |
| Ters zemin (buton, hover dolgu) | `#FFFFFF` | `color-inverse-bg` | slot `PrimaryButton/Background` |
| Ters metin | `#000000` | `color-inverse-text` | slot `PrimaryButton/Text` |
| Pasif öğe opaklığı | `0.3` (thumbnail), gri metin (sekme) | `opacity-inactive` | `global.css` `--opacity-inactive` |
| Overlay karartma | siyah ~%60 + arka plan blur [tahmini] | `color-scrim` | `global.css` `--color-scrim` |
| Vurgu | referansta **yok** (tam monokrom) | `color-accent` | tema rengi `Accent` |

Kurallar [ölçüldü]:
- Tüm çizgiler `1px solid #7A7A7A`. Kart = dört kenar; header = üst+alt; liste satırı = sadece alt.
- Köşe yarıçapı her yerde `0`.
- Gölge yok. Derinlik sadece görsel üstü siyah gradyan maske ile (alttan yukarı, metin okunurluğu için).

ikas notu: renkler `create_theme_global` (kind `color` / `colorScheme`) ile açılır; kodda `cssVar` kullanılır (canlı güncellenir). Bölümler `backgroundColor` prop'u da taşımak zorunda.

---

## 2. Tipografi

Referans font: **Mona Sans Variable**, tamamı büyük harf, `letter-spacing: 0.5px`. Genişlik ekseni `wdth 75` (başlık/UI) ve `wdth 80` (etiket). Fiyat ve bazı küçük yazılar normal genişlikte Mona Sans 700/900.

**pen.dev kısıtı [doğrulandı]:** pen.dev'de variable-font ekseni ayarlanamıyor; `Mona Sans` var ama dar hali yok (`Mona Sans Condensed` geçersiz). Geçerli dar aileler: `Barlow Condensed`, `Sofia Sans Extra Condensed`, `Anton`, `Antonio`, `Oswald`, `Bebas Neue`, `Archivo Narrow`. Tasarımda bunlardan biri kullanılır; kodda gerçek font yüklenir.

### Preset'ler [ölçüldü]

| Token | Kullanım | ≥1200 | 992–1199 | 768–991 | <768 | Ağırlık | Satır |
|---|---|---|---|---|---|---|---|
| `text-display` | Sayfa başlığı (h1): hero, PLP başlık | 96 | 72 | 56 | 40 | 800 | 0.9 |
| `text-h2` | Bölüm başlığı, panel başlığı | 80 | 64 | 48 | 34 | 800 | 0.9 |
| `text-h3` | Mobil menü öğesi, about değer başlığı, journal öne çıkan | 54 | 46 | 36 | 32 | 800 | 1.0 |
| `text-h4` | Megamenu kart başlığı, journal kart başlığı | 32 | 28 | 26 | 24 | 800 | 1.0 |
| `text-title` | Ürün adı | 24 | 22 | 20 | 18 | 700 | 1.1 |
| `text-ui` | Nav, buton, link, duyuru, açıklama (caps) | 20 | 20 | 18 | 18 | 700 | 1.1 |
| `text-ui-sm` | Megamenu linki, footer linki, alt başlık | 16 | 16 | 14 | 14 | 700 | 1.1 |
| `text-badge` | NEW / SALE / BEST SELLER | 16 | 14 | 12 | 12 | 800 (`wdth 80`) | 0.8 |
| `text-label` | Kategori etiketi, tarih, breadcrumb | 12 | 12 | 11 | 11 | 600 (`wdth 80`) | 0.8 |
| `text-body` | Journal gövde metni (normal harf) | 16 | 16 | 14 | 14 | 500, `ls 0.2px` | 1.3 |
| `text-price` | Fiyat (normal genişlik) | 24 | 22 | 20 | 18 | 700 | 1.0 [tahmini] |

Notlar:
- İkincil renkli varyantlar ayrı preset değil, aynı preset + `color-muted`.
- Üstü çizili eski fiyat = `text-price` + `color-muted` + strikethrough.

| | pen.dev | ikas |
|---|---|---|
| Boyutlar | `device` eksenli sayı değişkenleri (`desktop` = ≥1200 sütunu, `mobile` = <768 sütunu) | preset başına `create_theme_global` kind `typography`; uygularken `className` |
| Aile | `font-display`, `font-ui`, `font-body`, `font-price` string değişkenleri | `font_family` alanı |
| Ara kırılımlar | tasarlanmaz | 992–1199 ve 768–991 değerleri bileşen CSS'inde `@media (max-width: bp(<id>))` ile |

**Açık soru (font yükleme):** ikas dokümanlarında özel font için tek yol typography token'ındaki `font_family`. Uzak `@import` muhtemelen CLI'da düşüyor; bileşen CSS'indeki `@font-face` adı bileşene göre yeniden adlandırılıyor. İlk aktarım adımında editörde `font_family` alanının Google Fonts adı kabul edip etmediği denenmeli.

---

## 3. Boşluk, grid, ölçü

| Token | Referans [ölçüldü] | pen.dev | ikas |
|---|---|---|---|
| Sayfa kenar boşluğu | 20 | `space-page` | `--space-page` |
| Grid aralığı (kartlar, paneller arası) | 5 | `space-grid` | `--space-grid` |
| Kart iç boşluğu | 10 | `space-card` | `--space-card` |
| Panel iç boşluğu | 20 | `space-panel` | `--space-panel` |
| Küçük aralık (etiket ↔ başlık) | 5 | `space-xs` | `--space-xs` |
| Orta aralık | 10 / 15 | `space-sm`, `space-md` | aynı adlar |
| Bölüm üst boşluğu (başlıklı bölümler) | 100 (mobil ~60 [tahmini]) | `space-section` (device eksenli) | `--space-section` |
| Header yüksekliği | 60 | `size-header` | `--size-header` |
| Çizgi kalınlığı | 1 | `size-line` | `--size-line` |
| Hero yüksekliği | viewport − header (1444'te 703) | `size-hero` | `calc(100svh - var(--size-header))` |
| İçerik genişliği | tam genişlik (max-width yok); journal yazısı 1200, about metin 800 | — | bileşen CSS |

Grid düzenleri [ölçüldü, 1444]:
- Ürün ızgarası (PLP): 3 sütun × 478, aralık 5. Kart: görsel 478×358 (4:3), bilgi alanı 93.
- Ana sayfa katalog bloğu: 576 genişlik sticky promo panel + 2 sütun × 429 ürün. Kart: 429×415 (görsel 429×322).
- Kategori kartları: 4 sütun × 357, yükseklik 362.
- Shoppable görseller / ikili banner: 2 sütun × 720, yükseklik 540 / 780.
- Journal: öne çıkan 818 görsel + 626 metin; altında 3 sütun × 478.
- PDP: 500 sticky detay sütunu + 944 galeri (her görsel bir viewport).
- Megamenu: 3 eşit sütun × 481, yükseklik 354.
- Footer: 4 sütun.

Mobil (<768) [ölçüldü, 570]:
- Header: hamburger sol, logo orta, arama/hesap/sepet sağ; duyuru şeridi açık menünün içinde.
- Hero: kısa (yaklaşık 330), açıklama gizli, thumbnail yerine alt kenarda ince ilerleme çizgisi.
- Katalog bloğu: promo panel tam genişlik, altında ürünler **yatay kaydırmalı** (kart ≈ %95 genişlik, sonraki kart kenardan görünür).
- Kategori kartları ve journal kartları: yatay kaydırmalı.
- PLP: tek sütun; filtre sekmeleri yatay kaydırmalı.
- PDP: önce galeri (yatay), sonra detaylar; sticky yok; altta mini satın alma çubuğu.
- Footer: 2×2 sütun; bülten formu tam genişlik.

---

## 4. Kırılımlar

| Ad | Aralık [ölçüldü] | pen.dev | ikas |
|---|---|---|---|
| desktop | ≥ 1200 | frame 1440, `device: desktop` | varsayılan stil |
| laptop | 992–1199 | tasarlanmaz | `create_theme_global` breakpoint `laptop` 1199 |
| tablet | 768–991 | tasarlanmaz | breakpoint `tablet` 991 |
| mobile | < 768 | frame 390, `device: mobile` | breakpoint `mobile` 767 |

CSS'te `@media (max-width: bp(<breakpointId>))` yazılır; `var()` medya sorgusunda çalışmaz.

---

## 5. Katman sırası

| Katman | z | Not |
|---|---|---|
| Footer (sticky, içeriğin arkasında) | 0 | M-16 |
| Sayfa içeriği | 1 | opak zemin şart |
| Sticky bölüm içi öğeler (filtre barı, promo panel) | 5 | |
| Header + megamenu | 10 | |
| About alt gezinme / mini satın alma çubuğu | 9 | |
| Scrim + çekmeceler + arama | 20 | |

---

## 6. İkonlar

Referans: çizgi ikon (arama), dolu ikon (hesap, sepet), 20×20; ok `↗` 20×20; caret 16×16; artı/eksi (akordeon); çarpı (kapat). pen.dev'de `icon` node'u (lucide/phosphor) kullanılır; logo için `Generate("svg")`. ikas'ta ikonlar sub-component olarak inline SVG; tüccarın değiştireceği logolar `SVG`/`IMAGE` prop.

---

## 7. Motion

### 7.1 Token'lar

| Token | Değer [ölçüldü] | Kullanım |
|---|---|---|
| `ease-standard` | `cubic-bezier(.4, 0, .2, 1)` | yükleme, genel tween |
| `ease-inout` | `cubic-bezier(.44, 0, .56, 1)` | ilerleme çubuğu, bölüm girişi |
| `ease-nav` | `cubic-bezier(.68, 0, .22, .83)` | header/megamenu |
| `spring-snappy` | spring bounce 0, 0.3s | küçük hover |
| `spring-soft` | spring bounce 0.2, 0.4s | **en yaygın**: ok, etiket, küçük durum değişimi |
| `spring-hover` | spring bounce 0.2, 0.6s | nav dolgu, menü öğesi |
| `spring-smooth` | spring bounce 0, 0.6s | görsel hover, thumbnail |
| `spring-card` | spring bounce 0.2, 0.8s | kategori kartı |
| `spring-hero` | spring bounce 0, 1.5s | slider maske + zoom |
| `spring-text` | spring bounce 0.2, 1.5–2s | kelime reveal |
| `spring-drawer` | stiffness 300, damping 40, mass 1 | çekmece |
| `spring-search` | stiffness 600 / 800, damping 40 / 60 | arama paneli / alanı |
| `spring-ui` | stiffness 500, damping 60, mass 1 | genel UI |
| `dur-autoplay` | 4s | hero slayt süresi |
| `dur-press` | 3s | basın slider aralığı |

CSS karşılıkları (AnimeJS kullanılmayan yerde): bounce 0 → `cubic-bezier(.22, 1, .36, 1)`; bounce 0.2 → `cubic-bezier(.34, 1.3, .64, 1)`. Gerçek spring gerekiyorsa `AnimeJS.createSpring({ stiffness, damping, mass })`.

### 7.2 Uygulama yolları (ikas)

| Kısa ad | Ne | Ne zaman |
|---|---|---|
| `css-transition` | `:hover` / durum sınıfı + `transition` | hover, aç/kapa, renk |
| `css-keyframes` | bileşen `styles.css` içinde `@keyframes` | sonsuz döngü (marquee, pulse). Ad bileşene göre yeniden adlandırılır → **her bileşen kendi keyframe'ini tanımlar** |
| `theme-keyframe` | `create_theme_global` kind `keyframe`, `animation-name: <ref>` | birden çok bileşenin paylaştığı keyframe |
| `io-hook` | `useEffect` içinde `IntersectionObserver` → `is-inview` sınıfı | görünürlükte bir kez tetiklenen giriş |
| `animejs` | `import { AnimeJS } from "@ikas/bp-storefront"` (v4.0.2), `useEffect` içinde | stagger, timeline, spring, kelime bölme |
| `scroll-scrub` | `useEffect` içinde scroll dinleyici + `requestAnimationFrame` → CSS değişkeni | scroll'a bağlı ilerleme |
| `layout` | `position: sticky` | animasyon değil, düzen davranışı |

Ortak kurallar: tarayıcı API'si sadece `useEffect` içinde (SSR var); SSR çıktısı **bitiş halini** göstermeli, başlangıç hali JS yüklenince sınıfla verilir (aksi halde JS'siz içerik görünmez kalır); `prefers-reduced-motion: reduce` altında döngüler durur, girişler anında olur; dışarıdan paket yok (sadece `animejs`, `three`).

### 7.3 Tarif kataloğu

Her tarif için "Katman yapısı" sütunu pen.dev tasarımında **zorunlu** olan yapıdır.

| ID | Ad | Hareket ve değerler | Katman yapısı | Uygulama | Mobil / azaltılmış hareket |
|---|---|---|---|---|---|
| **M-01** | Yükleme fade-up | `y 40→0`, `opacity 0→1`; 0.5s `ease-standard`; referansta delay 1.8s [ölçüldü] (öneri 0.2–0.4s) | hedef öğe tek katman | `css-keyframes` | aynı / anında |
| **M-02** | Yükleme fade | `opacity 0→1`; spring 1.2s, delay 1s [ölçüldü] | tek katman | `css-keyframes` | aynı / anında |
| **M-03** | Kelime kelime başlık reveal | her kelime: `opacity 0→1`, `y 50→0`, `rotateX 20→0`, `skewX 10→0`, `skewY 5→0`; `spring-text`; kelime başına 0.05s stagger; görünürlük eşiği 0.5; bir kez [ölçüldü] | başlık satırı kendi `clip` maske frame'inde; her satır ayrı metin node'u | `animejs` (kelime bölme) + `io-hook` | skew/rotate kaldır, sadece y+opacity / anında |
| **M-04** | Duyuru metin döngüsü | metinler dikey kayarak değişir; aralık ~3s [tahmini]; geçiş `spring-hover` | `announcement-mask` (clip) içinde üst üste tüm metinler; sadece ilki görünür | `css-keyframes` veya `animejs` timeline | mobilde menü içinde / ilk metin sabit |
| **M-05** | Nav hover dolgu + etiket roll | ters renkli alt katman `y 100%→0` kayar, üst etiket yukarı çıkar; `spring-hover` [ölçüldü] | `nav-link` (clip) içinde `top` (normal) ve `bottom` (ters zemin + ters metin) kopya | `css-transition` | mobilde yok |
| **M-06** | Megamenu aç/kapa | panel yukarıdan açılır (yükseklik/clip), caret 180° döner; `spring-soft` + `ease-nav` 0.4s; görsel kart hover `spring-smooth` [ölçüldü] | `megamenu` ayrı overlay frame: `megamenu-links` + 2× `megamenu-card` (görsel + `gradient-mask` + metin) | `css-transition` | mobilde akordeon / anında |
| **M-07** | Hero slayt geçişi | yeni slayt soldan **maske wipe** ile açılır (maske genişliği `0→100%`, `spring-hero`); görsel `scale ~1.2→1` [ölçek tahmini], parallax hız 60; metin: eski anında çıkar, yeni `spring 1.2s delay 1s` ile girer [ölçüldü] | `hero-slides` içinde tüm slaytlar kardeş: `hero-slide-mask` (clip) → `hero-slide-image` → `gradient-mask`; metin bloğu ayrı `hero-text` | `animejs` timeline | mobilde çapraz geçiş / anında değişim |
| **M-08** | Thumbnail ilerleme | aktif thumbnail'de çubuk `0→100%`, 4s `ease-inout`; sıfırlama 0.6s; pasifler `opacity 0.3`, hover/aktif `1` (`spring-smooth`) [ölçüldü] | `hero-thumb` içinde ayrı `progress-bar` katmanı (üstte, yarı saydam) | `css-transition` + süre = `dur-autoplay` | mobilde tek ince çizgi / çubuk gizli |
| **M-09** | Ürün kartı hover | ön görsel → arka görsel geçişi ~0.4s [tahmini]; ok ikonu çapraz roll (`spring-soft`) | `card-images` (clip) içinde üst üste `image-front` + `image-back`; `card-arrow` (clip) içinde `arrow-top` + `arrow-bottom` | `css-transition` | dokunmatikte yok; galeri kaydırma opsiyonel |
| **M-10** | Oklu link hover | ok çapraz roll + alt çizgi `0→100%` genişler, 0.4s | `link` içinde metin + `link-line` (1px) + `link-arrow` (clip, iki ok) | `css-transition` | yok |
| **M-11** | Buton hover dolgu | M-05 ile aynı mantık; `spring-snappy` + bounce 0.3 0.4s [ölçüldü] | `button` (clip) içinde `top` + `bottom` kopya | `css-transition` | yok |
| **M-12** | Hotspot pulse + kart | dış halka `scale 1→~2.2`, `opacity 1→0` sonsuz, spring 1–1.5s [ölçek tahmini]; hover/dokunma: ürün mini kartı açılır `spring-soft` | `hotspot` içinde `hotspot-outer` + `hotspot-inner`; ayrıca `hotspot-card` (kapalı hali gizli, açık hali `05 Motion States`'te) | `css-keyframes` + `css-transition` | dokunmayla açılır / pulse durur |
| **M-13** | Sticky panel | panel `top: header` konumunda sabit kalır, yanındaki içerik akar | sticky öğe ve onu saran yüksek kap **gerçek yükseklikte** çizilir | `layout` | mobilde sticky yok |
| **M-14** | Metin marquee | yatay sonsuz kayma, ~60px/s [tahmini]; kart hover: marquee metni `muted→text`, etiket soluklaşır (`spring-card`) | `marquee` (clip) içinde `marquee-track`; track içinde aynı metnin **en az 2 kopyası**, kap dışına taşar | `css-keyframes` | aynı / durur |
| **M-15** | Görsel ticker | görseller yatay sonsuz kayar, sürüklenebilir [tahmini]; hover'da yavaşlar | `ticker` (clip) → `ticker-track` → görseller ×2 set | `css-keyframes` (+ opsiyonel sürükleme) | aynı / durur, yatay kaydırma |
| **M-16** | Footer reveal | footer içeriğin arkasında sticky; içerik bitince altından ortaya çıkar; dev wordmark parallax (hız 80) [ölçüldü] | `footer` ayrı section; sayfa frame'inde normal akışta çizilir, reveal notu metadata'da; `footer-wordmark` ayrı katman | `layout` + `scroll-scrub` | mobilde normal akış |
| **M-17** | Yumuşak kaydırma | Lenis, yoğunluk 12 [ölçüldü] | — | ikas'ta Lenis **kullanılamaz** (paket izni yok). Varsayılan: uygulanmaz | — |
| **M-18** | Filtre barı | sticky `top: header`; sekme rengi `muted→text` 0.3s; ızgara değişiminde kısa fade | `filter-bar` ayrı katman; aktif ve pasif sekme stilleri ayrı | `layout` + `css-transition` | yatay kaydırma |
| **M-19** | PDP galeri scrollspy | detay sütunu sticky; kaydırdıkça aktif thumbnail çerçevesi değişir; galeri bitince mini satın alma çubuğu alttan girer | `pdp-details` (sticky), `pdp-gallery` (görseller alt alta, gerçek yükseklik), `pdp-thumbs` (aktif = beyaz çerçeve), `mini-buy-bar` ayrı overlay | `layout` + `io-hook` | mobilde yatay galeri + noktalar |
| **M-20** | Çekmece | panel kenardan kayar (`x 100%→0` sağ / `-100%→0` sol), `spring-drawer`; scrim fade + blur 0.4s; içerik satırları 0.2 / 0.3 / 0.4 / 0.5s gecikmeyle `spring-smooth` girer [ölçüldü] | ayrı overlay frame: `scrim` + `drawer` (başlık, gövde, alt bölüm ayrı katmanlar) | `css-transition` (+ `animejs` stagger) | tam genişlik / anında |
| **M-21** | Arama | panel `spring-search` ile açılır; sonuçlar listelenir | ayrı overlay frame: `search-panel` (giriş alanı + sonuç ızgarası), boş ve dolu hali ayrı | `css-transition` | tam ekran / anında |
| **M-22** | Akordeon | yükseklik `0→auto`, artı ikonu döner; spring bounce 0, 0.5s [ölçüldü] | `faq-item`: `faq-question` satırı + `faq-answer`; açık ve kapalı hali ayrı | `css-transition` (grid-rows hilesi) | aynı / anında |
| **M-23** | Scroll-scrub görsel | `rotate 10°→0°`, `y 0→-1200` kaydırmaya bağlı [ölçüldü] | sticky yığın: her `value-panel` tam viewport, `value-image` mutlak konumlu ve **bitiş (0°) halinde** çizilir | `scroll-scrub` | rotasyon yok, normal akış |
| **M-24** | Scroll-scrub metin | başlık `opacity 1→0`, `scale 1→1.2`; paragraf `y 0→-200` [ölçüldü] | başlık ve paragraf ayrı katman | `scroll-scrub` | kapalı |
| **M-25** | Scrollspy gezinme | altta sabit çubuk; görünen bölümün adı `muted→text` | `anchor-nav` ayrı katman; aktif/pasif stil ayrı | `io-hook` + `css-transition` | yatay kaydırma |
| **M-26** | Alıntı slider | otomatik 3s, sürüklenebilir; ortadaki tam opak, yanlar soluk [opaklık tahmini 0.4] | `press-track` içinde tüm alıntılar yan yana; ortadaki aktif | `animejs` veya CSS scroll-snap | scroll-snap / otomatik durur |
| **M-27** | Hero parallax | arka plan görseli içerikten yavaş kayar (hız 80) [ölçüldü] | `hero-bg` ayrı katman, kabından %10–20 yüksek | `scroll-scrub` | kapalı |
| **M-28** | Durum rengi | `muted→text` 0.3s (sekme, footer linki, varyant çipi) | aktif/pasif/hover stilleri ayrı | `css-transition` | aynı |

### 7.4 Referansta ölçülemeyenler

- M-04 aralığı, M-09 geçiş süresi, M-14/M-15 hızları, M-12 ve M-07 ölçek değerleri gözlemle kestirildi.
- Ürün kartı, footer ve duyuru bileşenlerinin Framer modülleri sayfa HTML'inde listelenmediği için transition nesneleri doğrudan okunamadı; değerler sitenin en yaygın geçişinden (`spring-soft`) alındı.
