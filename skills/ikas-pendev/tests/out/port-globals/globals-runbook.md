# Globals runbook — Gizem (C)

`port-manifest.json` → `globals` için tek seferlik kurulum. Sıra: oku → tablo → **kullanıcı onayı** → oluştur → yeniden listele. Bu runbook bir kez çalıştırılır; tekrar çalıştırmak token'ları çoğaltır.

## Ön koşullar

- `ikas theme dev` çalışıyor ve editör bağlı.
- Oturum `.mcp.json` dosyasını taşıyan tema klasöründen başlatıldı (yoksa ikas MCP araçları görünmez).
- Kod yazılmaz, bileşen düzenlenmez; yalnızca tema global'leri kurulur.

## 1. Oku

`list_theme_globals` çağrılır; mevcut her renk, tipografi, kırılım, keyframe, renk şeması ve global değişken not edilir. Aynı ad ve değerdeki token yeniden kullanılır (`var (aynı)`); aynı ad farklı değer `çakışma` olur ve açık soru olarak kullanıcıya sorulur, üzerine yazılmaz.

## 2. Token tablosu

Tür başına sayı: breakpoint 3 · color 2 · colorScheme 2 · typography 11 · globalVariable 1 · keyframe 3 · toplam 22.

| Tür | Ad | Değer | pen.dev kaynağı | Durum |
|---|---|---|---|---|
| breakpoint | Kırılım / Laptop | 1199 px | globals.md §4 (`laptop`) | _doldurulacak_ |
| breakpoint | Kırılım / Tablet | 991 px | globals.md §4 (`tablet`) | _doldurulacak_ |
| breakpoint | Kırılım / Mobil | 767 px | globals.md §4 (`mobile`) | _doldurulacak_ |
| color | Renk / Vurgu | #FF3B1F | `color-accent` | _doldurulacak_ |
| color | Renk / Vurgu Üstü Metin | #0D0D0D | `color-accent-text` | _doldurulacak_ |
| colorScheme | Gizem / Gün | Background #FFFFFF, Text #111111, PrimaryButton/Background #111111 | mode `gun`: `color-bg`, `color-text`, `color-inverse-bg` | _doldurulacak_ |
| colorScheme | Gizem / Gece | Background #000000, Text #EEEEEE, PrimaryButton/Background #EEEEEE | mode `gece`: `color-bg`, `color-text`, `color-inverse-bg` | _doldurulacak_ |
| typography | Tipografi / Display | Barlow · 600 · 90px / 80px / 60px / 40px (≥1200 / laptop / tablet / mobil) · satır 1.0 · harf -0.02em | `text-display` + `font-display` · globals.md §2a | _doldurulacak_ |
| typography | Tipografi / Başlık H2 | Sofia Sans Extra Condensed · ağırlık ? · 112px / 52px (mobil CSS) · satır 0.9 | `text-h2` + `font-display` | _doldurulacak_ |
| typography | Tipografi / Başlık H3 | Sofia Sans Extra Condensed · ağırlık ? · 64px / 40px (mobil CSS) · satır 0.9 | `text-h3` + `font-display` | _doldurulacak_ |
| typography | Tipografi / Başlık H4 | Sofia Sans Extra Condensed · ağırlık ? · 36px / 26px (mobil CSS) · satır 0.9 | `text-h4` + `font-display` | _doldurulacak_ |
| typography | Tipografi / Ürün Adı | Archivo Narrow · 700 · 22px / 18px (mobil CSS) · satır 1.1 | `text-title` + `font-ui` | _doldurulacak_ |
| typography | Tipografi / Arayüz | Archivo Narrow · 700 · 18px / 16px (mobil CSS) · satır 1.1 | `text-ui` + `font-ui` | _doldurulacak_ |
| typography | Tipografi / Arayüz Küçük | Archivo Narrow · 700 · 15px / 14px (mobil CSS) · satır 1.1 | `text-ui-sm` + `font-ui` | _doldurulacak_ |
| typography | Tipografi / Rozet | Archivo Narrow · 700 · 12px / 11px (mobil CSS) · satır 1.1 | `text-badge` + `font-ui` | _doldurulacak_ |
| typography | Tipografi / Etiket | Barlow · 500 · 12px / 12px / 11px / 11px (≥1200 / laptop / tablet / mobil) · satır 1.2 · harf 0.04em · uppercase | `text-label` + `font-mono` · globals.md §2a | _doldurulacak_ |
| typography | Tipografi / Gövde | Archivo Narrow · 500 · 16px / 15px (mobil CSS) · satır 1.35 | `text-body` + `font-body` | _doldurulacak_ |
| typography | Tipografi / Fiyat | Archivo Narrow · 700 · 22px / 18px (mobil CSS) · satır ? | `text-price` + `font-price` | _doldurulacak_ |
| globalVariable | Çizgi / Varsayılan | BORDER `{"width": {"value": 2, "unit": "px"}, "style": "solid", "color": "#0D0D0D"}` | `size-line`, `color-line` | _doldurulacak_ |
| keyframe | Animasyon / Hotspot pulse + kart | { outer.scale: 1, outer.opacity: 1 } → { outer.scale: 2.2, outer.opacity: 0 } | M-12 (C-CMP-07) | _doldurulacak_ |
| keyframe | Animasyon / Metin marquee | { x: 0 } → { x: -50% } | M-14 (C-CMP-08, C-HDR-01, C-TICK-01, C-MOS-02, C-MQT-01, C-NF-01) | _doldurulacak_ |
| keyframe | Animasyon / Yükleme fade-up | { y: 40, opacity: 0 } → { y: 0, opacity: 1 } | M-01 (C-ABH-03, C-TML-02, C-CNT-03, C-CRTP-03, C-AUTH-02) | _doldurulacak_ |

`Durum` adım 1'den sonra doldurulur: `yeni`, `var (aynı)` ya da `çakışma`.

## 3. Onay

**KULLANICI ONAYI BEKLE.** Tür başına sayılar ve yukarıdaki tablo kullanıcıya gösterilir. Açık bir "evet" gelmeden hiçbir `create_theme_global` çağrısı yapılmaz. `çakışma` satırları için karar kullanıcınındır.

## 4. Oluştur

`create_theme_global` aşağıdaki sırayla, her satır bir çağrı. Görünen adlar Türkçe `Grup / Ad`.

```json
{"kind": "breakpoint", "name": "Kırılım / Laptop", "width": 1199}
{"kind": "breakpoint", "name": "Kırılım / Tablet", "width": 991}
{"kind": "breakpoint", "name": "Kırılım / Mobil", "width": 767}
{"kind": "color", "name": "Renk / Vurgu", "value": "#FF3B1F"}
{"kind": "color", "name": "Renk / Vurgu Üstü Metin", "value": "#0D0D0D"}
{"kind": "colorScheme", "name": "Gizem / Gün", "colors": [{"newSlotName": "Background", "value": "#FFFFFF"}, {"newSlotName": "Text", "value": "#111111"}, {"newSlotName": "PrimaryButton/Background", "value": "#111111"}]}
```

Ara adım: `list_theme_globals` → ilk şemanın slot id'leri okunur; ikinci şema aynı slotlara `slotId` ile bağlanır.

```json
{"kind": "colorScheme", "name": "Gizem / Gece", "colors": [{"slotId": "<Background slotId>", "value": "#000000"}, {"slotId": "<Text slotId>", "value": "#EEEEEE"}, {"slotId": "<PrimaryButton/Background slotId>", "value": "#EEEEEE"}]}
{"kind": "typography", "name": "Tipografi / Display", "font_family": "Barlow", "font_size": "90px", "font_weight": "600", "line_height": "1.0", "letter_spacing": "-0.02em", "breakpoints": [{"breakpoint_id": "<Kırılım / Laptop id>", "font_size": "80px"}, {"breakpoint_id": "<Kırılım / Tablet id>", "font_size": "60px"}, {"breakpoint_id": "<Kırılım / Mobil id>", "font_size": "40px"}]}
{"kind": "typography", "name": "Tipografi / Başlık H2", "font_family": "Sofia Sans Extra Condensed", "font_size": "112px", "line_height": "0.9"}
{"kind": "typography", "name": "Tipografi / Başlık H3", "font_family": "Sofia Sans Extra Condensed", "font_size": "64px", "line_height": "0.9"}
{"kind": "typography", "name": "Tipografi / Başlık H4", "font_family": "Sofia Sans Extra Condensed", "font_size": "36px", "line_height": "0.9"}
{"kind": "typography", "name": "Tipografi / Ürün Adı", "font_family": "Archivo Narrow", "font_size": "22px", "font_weight": "700", "line_height": "1.1"}
{"kind": "typography", "name": "Tipografi / Arayüz", "font_family": "Archivo Narrow", "font_size": "18px", "font_weight": "700", "line_height": "1.1"}
{"kind": "typography", "name": "Tipografi / Arayüz Küçük", "font_family": "Archivo Narrow", "font_size": "15px", "font_weight": "700", "line_height": "1.1"}
{"kind": "typography", "name": "Tipografi / Rozet", "font_family": "Archivo Narrow", "font_size": "12px", "font_weight": "700", "line_height": "1.1"}
{"kind": "typography", "name": "Tipografi / Etiket", "font_family": "Barlow", "font_size": "12px", "font_weight": "500", "line_height": "1.2", "letter_spacing": "0.04em", "text_transform": "uppercase", "breakpoints": [{"breakpoint_id": "<Kırılım / Tablet id>", "font_size": "11px"}, {"breakpoint_id": "<Kırılım / Mobil id>", "font_size": "11px"}]}
{"kind": "typography", "name": "Tipografi / Gövde", "font_family": "Archivo Narrow", "font_size": "16px", "font_weight": "500", "line_height": "1.35"}
{"kind": "typography", "name": "Tipografi / Fiyat", "font_family": "Archivo Narrow", "font_size": "22px", "font_weight": "700"}
{"kind": "globalVariable", "display_name": "Çizgi / Varsayılan", "type": "BORDER", "value": {"width": {"value": 2, "unit": "px"}, "style": "solid", "color": "#0D0D0D"}}
{"kind": "keyframe", "name": "Animasyon / Metin marquee", "points": [{"point": "0%", "styles": [{"property": "transform", "value": "translateX(0px)"}]}, {"point": "100%", "styles": [{"property": "transform", "value": "translateX(-50%)"}]}]}
{"kind": "keyframe", "name": "Animasyon / Yükleme fade-up", "points": [{"point": "0%", "styles": [{"property": "transform", "value": "translateY(40px)"}, {"property": "opacity", "value": "0"}]}, {"point": "100%", "styles": [{"property": "transform", "value": "translateY(0px)"}, {"property": "opacity", "value": "1"}]}]}
```

Toplam 21 çağrı.

- Kırılımlar ilk sırada: CSS `@media (max-width: bp(<id>))` bunlara dayanır (`var()` medya sorgusunda çalışmaz).
- `mode` ekseni → palet başına bir renk şeması. İkinci şemadaki `<Slot slotId>` yer tutucuları, ilk şemadan sonra yapılan `list_theme_globals` çıktısıyla değiştirilir.
- Tipografi kırılım boyutları (`globals.md` §2a) `breakpoints` dizisiyle aynı çağrıda yazılır; `<Kırılım / … id>` yer tutucuları kırılımlar oluşturulduktan sonra `list_theme_globals` çıktısıyla değiştirilir.
- Varsayılan şema: `Gizem / Gün` → oluşturulduktan sonra `update_theme_color_scheme` `is_default: true`.
- Bölümlerin varsayılan şeması (`globals.md` §1a):
  - **Gün:** Header, Footer.
  - **Gece:** Hero.
- Ağırlığı planda olmayan tipografiler (`font_weight` gönderilmez; kullanıcıya sorulur): Tipografi / Başlık H2, Tipografi / Başlık H3, Tipografi / Başlık H4.
- Noktaları otomatik çıkarılamayan keyframe'ler (alt öğe anahtarları ya da serbest metin); noktalar elle yazılır ya da animasyon bileşen CSS'inde kalır: Animasyon / Hotspot pulse + kart (`{ outer.scale: 1, outer.opacity: 1 }` → `{ outer.scale: 2.2, outer.opacity: 0 }`).

## 5. `src/global.css`

Boşluk, ölçü, opaklık ve alfa renkler için ikas'ta tür yok; bunlar `src/global.css` içine yazılır (MCP çağrısı yapılmaz).

```css
:root {
  --color-scrim: #0D0D0D99;
  --space-page: 32px;
  --space-grid: 0;
  --space-card: 12px;
  --space-panel: 24px;
  --space-xs: 6px;
  --space-sm: 12px;
  --space-md: 16px;
  --space-section: 120px;
  --size-header: 96px;
  --size-line: 2px;
  --opacity-inactive: 0.3;
}
@media (max-width: bp(<mobile id>)) {
  :root {
    --space-page: 16px;
    --space-card: 10px;
    --space-panel: 16px;
    --space-xs: 4px;
    --space-sm: 10px;
    --space-md: 12px;
    --space-section: 64px;
    --size-header: 88px;
  }
}
/* Gizem / Gece şemasının className'i ile */
.<gece className> {
  --color-scrim: #0D0D0DB3;
}
```

## 6. Doğrula

`list_theme_globals` yeniden çağrılır; tablodaki her satır tam bir kez bulunmalı. Ardından aşağıdaki canlı tablo doldurulur. Kod canlı id'leri yalnızca buradan okur, görünen adlardan değil; `cssVar` dizesi aynen kopyalanır (büyük/küçük harf id'den farklı olabilir).

## 7. Canlı token tablosu

### Renkler (kind: color)

| Token adı | ID | cssVar |
|---|---|---|
| Renk / Vurgu | _doldurulacak_ | _doldurulacak_ |
| Renk / Vurgu Üstü Metin | _doldurulacak_ | _doldurulacak_ |

### Tipografi (kind: typography)

| Token adı | ID | className |
|---|---|---|
| Tipografi / Display | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Başlık H2 | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Başlık H3 | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Başlık H4 | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Ürün Adı | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Arayüz | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Arayüz Küçük | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Rozet | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Etiket | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Gövde | _doldurulacak_ | _doldurulacak_ |
| Tipografi / Fiyat | _doldurulacak_ | _doldurulacak_ |

### Global değişkenler

| Token adı | variableName | Tip |
|---|---|---|
| Çizgi / Varsayılan | _doldurulacak_ | BORDER |

### Kırılımlar (kind: breakpoint)

| Token adı | ID | Genişlik | Kullanım |
|---|---|---|---|
| Kırılım / Laptop | _doldurulacak_ | 1199 | `@media (max-width: bp(<id>))` |
| Kırılım / Tablet | _doldurulacak_ | 991 | `@media (max-width: bp(<id>))` |
| Kırılım / Mobil | _doldurulacak_ | 767 | `@media (max-width: bp(<id>))` |

### Renk şemaları (kind: colorScheme)

| Palet | ID | className |
|---|---|---|
| Gizem / Gün | _doldurulacak_ | _doldurulacak_ |
| Gizem / Gece | _doldurulacak_ | _doldurulacak_ |

| Slot | slotId | cssVar |
|---|---|---|
| Background | _doldurulacak_ | _doldurulacak_ |
| Text | _doldurulacak_ | _doldurulacak_ |
| PrimaryButton/Background | _doldurulacak_ | _doldurulacak_ |

### Keyframe'ler (kind: keyframe)

| Token adı | ID | ref (animation-name) |
|---|---|---|
| Animasyon / Hotspot pulse + kart | _doldurulacak_ | _doldurulacak_ |
| Animasyon / Metin marquee | _doldurulacak_ | _doldurulacak_ |
| Animasyon / Yükleme fade-up | _doldurulacak_ | _doldurulacak_ |
