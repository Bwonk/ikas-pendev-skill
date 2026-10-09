# Doğrulama raporu — Örnek (Plan C, contract 1)

Tarih: 2026-10-08 · Canvas: `pencil-new.pen` · Mod: `all` · Script: `pendev_checks.js` (yalnızca okuma)

## CHK sonuçları

| CHK | Sonuç | Sayı | Not |
|---|---|---|---|
| vars | PASS | 37/37 | §3'teki tüm değişkenler tanımlı |
| sections | PASS | 31/31 | her bölümün reusable @desktop + @mobile çifti var |
| overlays | PASS | 3 | MenuOverlay, CartDrawer, SearchOverlay (+ FilterDrawer@mobile, planda ek) |
| pages | PASS | 16/16 | Auth ×4: `Auth — giriş / kayıt / şifremi unuttum / şifre yenile` |
| anim | PASS | 115/115 | `metadata.anim` ∪ `context` birleşimi |
| textclass | WARN | none=237 | contract 1'de textClass yok; prop=495. Kalanlar ikas verisi (~140), kodla üretilen sayaçlar (~81), SVG yer tutucu (14) |
| hardcoded | WARN | 16 | logo/wordmark yer tutucuları sabit fontSize (SVG logo gelince kalkacak) |
| clip | WARN | — | roll kopyaları (`arrow-bottom`, `bottom`), gizli hover kardeşleri (`mosaic-hover`), yatay kaydırmalı satırlar (hesap siparişleri) — bilinçli |
| rootmeta | WARN | 52 | yalnızca durum frame'leri (`— <durum>`) metadata'sız; ana kökler tam |
| placeholder | PASS | 0 | |
| refassets | PASS | 0 | referans sitenin görseli kullanılmamış |
| ds | PASS | 6/5 | Colors, Typography, Spacing, Icons, Motion, Imagery |

## Elle yapılan kontroller
- Türkçe karakterler (İ Ş Ğ Ü Ö Ç) üç fontta da düzgün (önceki §9 turunda doğrulandı).
- Kontrast: `color-muted` açık zeminde `#6B675F` → 4.7:1 (AA). Uyarı kalanlar: muted/surface 4.19, accent/bg 2.99.

## İstisnalar (kullanıcı kabul etti)
1. Logo yer tutucuları sabit px (ileride `{logo:SVG}`).
2. Gradient şeffaf başlangıcı `#0D0D0D00` sabit (contract 2'de `color-transparent`).
3. Contract 1 canvas'ı contract 2'ye taşınmaz; data/code metinleri aktarımda bağlanır.
