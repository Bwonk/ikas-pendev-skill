# Components — bileşen envanteri ve ikas eşlemesi

Kaynak: <referans URL / ekran görüntüleri> katman ağacı + ekran ölçümleri (… / …).
Token adları ve motion tarifleri (`M-xx`) için: [`globals.md`](./globals.md).

Üç seviye:
- **Section** — ikas `type: section`; `src/components/` altında; editörde sayfaya eklenir. pen.dev'de `<P>/Section/<Ad>@desktop` + `@mobile`.
- **Component** — bir section'ın `COMPONENT_LIST` slotuna giren çocuk; `src/components/` altında, `type` yok. pen.dev'de slot grubunun öğe katmanı (`{slot:COMPONENT_LIST}`).
- **Sub** — sadece kod içinde kullanılan yardımcı; `src/sub-components/`; `ikas.config.json`'da yer almaz. pen.dev'de `<P>/Sub/<Ad>`.

Ağaç notasyonu: `{ad:TİP}` = prop (30 tipten biri) · `{data:kaynak}` = mağaza verisinden gelen metin (ör. `product.name`) · `{code:ad}` = kodun ürettiği metin (sayaç, rakam).

Prop tabloları **öneridir**; prop'lar CLI ile eklenir (`npx ikas-component config add-component --props '[...]'`), dosyalar elle düzenlenmez.

---

## 1. Sayfa → section bileşimi

| Sayfa (ikas sayfa tipi) | Referans URL | Section'lar (sırayla) |
|---|---|---|
| … (…) | … | … |
| Her sayfa | — | Header (üstte) · Footer (altta) |
| Overlay'ler | — | … |

**Referansta olmayan ama ikas'ta gereken sayfalar** (tasarımda ayrıca üretilecek, aynı dil ile):

| Sayfa | ikas şablonu | Not |
|---|---|---|
| … | … | … |

---

## 2. Global section'lar

### Header  `--isHeader`
Referans: … ikas şablonu: `header-section`.

```
header
└─ …
```

Durumlar: …
Mobil: …

| Prop | Tip | Varsayılan | Grup |
|---|---|---|---|
| … | … | … | … |
| `backgroundColor` | COLOR | — | Görünüm |

Çocuk component'ler: …
Sub: …
Motion: …

### <Overlay> (Header overlay)  — M-xx
Referans: …

```
…
```
Durumlar: …

### Footer  `--isFooter`
Referans: … ikas şablonu: `footer-section`.

```
footer
└─ …
```
Mobil: …

| Prop | Tip | Grup |
|---|---|---|
| … | … | … |
| `backgroundColor` | COLOR | Görünüm |

Motion: …

---

## 3. Ana sayfa section'ları

### <Section>
Referans: … ikas şablonu: `…` / (özel).

```
…
```
Durumlar: …
Mobil: …

| Prop | Tip | Varsayılan |
|---|---|---|
| … | … | … |
| `backgroundColor` | COLOR | — |

---

## 4. Mağaza section'ları

### <Section>
Referans: … ikas şablonu: `…`.

```
…
```
Mobil: …

| Prop | Tip |
|---|---|
| … | … |
| `backgroundColor` | COLOR |

---

## 5. İçerik section'ları

### <Section>
Referans: … Prop: … · `backgroundColor`.

---

## 6. Sub-component'ler

| Sub | Referans ölçüsü | Durumlar | Motion |
|---|---|---|---|
| … | … | … | … |

---

## 7. ikas'a aktarım kuralları

**Proje:** `<tema klasörü>/` (Preact + TS). MCP sunucusu `<tema klasörü>/.mcp.json` içinde tanımlı → Claude Code'u o klasörde başlat; aksi halde MCP araçları bağlanmaz.

**MCP ne sağlar:**
- Doküman: `get_section_template` (28 şablon), `get_section_child`, `get_framework_guide`, `get_model_guide`, `get_function_doc`, `get_prop_types`, `search_docs`.
- Canlı editör (`ikas theme dev` + editörde Connect gerekir): `import_section`, `add_sections_to_page`, `update_section_prop`, `upload_image(s)`, `search_products`, `list_categories`, `create_page`, `publish_theme` (`confirm: true` olmadan kuru çalışma).
- Tema global'leri: `list_theme_globals`, `create_theme_global` (color, typography, breakpoint, keyframe, colorScheme, globalVariable).

**Sıra:**
1. Tema global'lerini aç (`docs/port/globals-runbook.md`; kullanıcı onayıyla).
2. `src/global.css` içine boşluk/ölçü/motion custom property'leri.
3. Sub-component'ler (`src/sub-components/<Ad>/index.tsx` + `styles.css`; mağaza verisi okuyan alt bileşen `observer(function Ad(){})`).
4. Section başına: `get_section_template` → ENUM gerekiyorsa önce `config add-enum` → `config add-component --type section --props '[...]'` → `index.tsx` + `styles.css` → `npx ikas-component check --json` → `npx ikas-component build`.
5. Header `--isHeader`, Footer `--isFooter`.
6. Editörde sayfalara yerleştir, içerik/görsel yükle.
7. Animasyon turu (planın 8. bölümü).

**Kısıtlar:**
- `ikas.config.json`, `types.ts`, `global-types.ts`, `src/components/index.ts` elle düzenlenmez.
- JSX'te sabit metin yok: her metin TEXT prop (buton yükleme durumu için iki ayrı prop). Mağaza verisinden gelen metinler (`{data:…}`) ve kodun ürettiği metinler (`{code:…}`) prop olmaz.
- Her section'da `backgroundColor` COLOR prop'u; 5+ prop varsa prop grubu.
- Kök bileşen `observer()` ile sarılmaz; alt bileşenler sarılır.
- CSS sadece sınıf seçicileriyle (otomatik `.cc_<id>` öneki); element seçici sızar.
- `@keyframes` / `@font-face` adları bileşene göre yeniden adlandırılır → bileşenler arası paylaşılamaz (paylaşım için tema keyframe token'ı).
- İzinli paketler: `preact`, `mobx`, `@ikas/bp-storefront*`, `@ikas/component-utils`, `animejs`, `three`. Diğerleri build hatası.
- SSR var: `window` / `document` / `IntersectionObserver` sadece `useEffect` içinde.
- Ürün görseli zinciri: `getSelectedProductVariant` → `getProductVariantMainImage` → `.image` → `getDefaultSrc` / `createMediaSrcset`; para biçimi `formatCurrency`.
- Tüccar verisi prop'larında (IMAGE, PRODUCT_LIST, CATEGORY…) `defaultValue` olmaz.
