# Brief — Örnek

Bu dosya tüm fazların başlangıç noktasıdır. Her oturum önce bunu okur; en alttaki **Durum** tablosu ilk açık fazı gösterir. Kaynak sırası: bu brief > canlı .pen dosyası > `docs/` > skill varsayılanları.

> Not: Örnek skill'den önce üretildi; bu brief mevcut `docs/` dosyalarından (README, `referans/globals.md`, `pendev/plan-C-serbest-yorum.md`) **geriye doğru kuruldu**. Sözleşme `contract 1` (37 değişken, `textClass` yok); taşınmaz.

## 1. Girdiler

| Dosya / URL | Sayfa | Viewport genişliği | Not |
|---|---|---|---|
| https://referans.example/ | ana sayfa, `/shop/category/*`, `/shop/collections/*`, `/shop/<ürün>`, `/about`, `/journal`, `/journal/<yazı>`, `/contact`, `/support/*` | 1444 / 570 | canlı ölçüm; Framer katman adları (`data-framer-name`) |

- Canlı referans: https://referans.example/ (Referans Framer şablonu)
- Taranacak yollar: `/`, `/shop/category/*`, `/shop/collections/*`, `/shop/<ürün>`, `/about`, `/journal`, `/contact`, `/support/*`
- Girdi klasörü: `docs/referans/girdi/` (git'e girmez; `.gitignore`'a eklendi: hayır — skill öncesi proje)

## 2. Marka

| Alan | Değer |
|---|---|
| Marka adı | Örnek |
| Slug | ornek |
| Sektör | streetwear (giyim) |
| Ton (3 sıfat) | ham · gizemli · sert |

## 3. Yorum stratejisi

| Alan | Değer |
|---|---|
| Strateji | serbest yorum (Plan C; A = aynı iskelet, B = yakın klon da yazıldı) |
| Prefix harfi | C (aynı .pen dosyasında A/B denemeleriyle çakışmasın diye varyant harfi) |
| Sözleşme | contract 1 |
| Plan dosyası | `docs/pendev/plan-C-serbest-yorum.md` |

## 4. Referans politikası

- [x] Referans sadece bakmak için: görseli, metni, logosu ve marka adı canvas'a girmez.
- [x] Görseller `Generate("ai" | "stock")`, logo `Generate("svg")` ile özgün üretilir.
- Onay: plan-C §0 ve §9 ile sabitlendi. Canvas'taki `referans.example` adlı 8 frame ham import; içinden katman kopyalanmaz, silinmez, değiştirilmez.

## 5. Kapsamdaki sayfalar

Plan C §6.3'teki 16 sayfa (13 satır; Auth ×4):

| Sayfa tipi | Kapsamda | Not |
|---|---|---|
| `INDEX` | [x] | `Home` |
| `CATEGORY` | [x] | `Category` |
| `PRODUCT_DETAIL` | [x] | `Product` |
| `CART` | [x] | `Cart` (referansta yok, ikas için eklendi) |
| `ACCOUNT` | [x] | `Account` |
| `LOGIN` · `REGISTER` · `FORGOT_PASSWORD` · `RECOVER_PASSWORD` | [x] | `Auth (×4)`, tek `AuthForms` section'ı |
| `NOT_FOUND` | [x] | `NotFound` |
| `SEARCH` | [ ] | §6.3'te sayfa yok; ProductList arama için de kullanılacak, ayrıca `SearchOverlay` |
| `FAVORITES` | [ ] | §6.3'te sayfa yok; ProductList favoriler için de kullanılacak, `Account` içinde favoriler sekmesi |
| `BLOG` · `BLOG_POST` | [x] | `Journal`, `JournalPost` |
| `COLLECTION` | [x] | `Collection` (CollectionHero · ProductList) |
| `CUSTOMER_EMAIL_VERIFICATION` | [ ] | components.md'de listelendi, planda yok |
| Özel sayfalar | [x] | `About`, `Contact`, `Support` |

Overlay'ler: MenuOverlay · CartDrawer · SearchOverlay (Header içinde). FilterDrawer@mobile ayrı overlay olarak sayılmadı; ProductList bölümünün kontrol satırında ("mobil filtre çekmecesi ayrı overlay frame") istendi. Header ve Footer her sayfada.

## 6. Yerel ayarlar

| Alan | Değer |
|---|---|
| Dil / locale | tr-TR (canvas metinleri Türkçe) |
| Para biçimi | `1.850 TL` |
| Büyük harf politikası | hepsi büyük harf, gövde metni hariç; `İ Ş Ğ Ü Ö Ç` kontrolü |

## 7. Palet modları

- Seçim: ters bölümler (açık "kağıt" zemin varsayılan, `mode: light | dark` ekseni)
- Koyu (`mode: dark`) bölümler: Manifesto, Footer, MenuOverlay, TickerStrip. ikas'ta iki paletli color scheme (`Paper`, `Ink`).

## 8. Canvas ve cihazlar

| Alan | Değer |
|---|---|
| .pen dosyası | `pencil-new.pen` (plan önerisi `ornek-C.pen` idi; aynı dosyada `C/` önekiyle çalışıldı) |
| Masaüstü genişliği | 1440 |
| Mobil genişliği | 390 |
| Overlay boyutları | 1440×900 · 390×844 |

## 9. Motion iştahı

- Seviye: yoğun
- Not: 115 animasyon hedefi; imza hareketi şifre çözme (C-M-01); 8 yerel tarif (C-M-01 … C-M-08) + katalog M-01 … M-28 (M-17 Lenis kapsam dışı).

## 10. Durum

| Faz | Durum | Dosya | Tarih | Not |
|---|---|---|---|---|
| 0 intake | tamam | `docs/00-brief.md` | 2026-10-06 | geriye doğru kuruldu |
| 1 analyze | tamam | `docs/referans/globals.md`, `docs/referans/components.md` | 2026-10-06 | 1444 / 570 ölçüm; bazı değerler `[tahmini]` |
| 2 plan | tamam | `docs/pendev/plan-C-serbest-yorum.md` | 2026-10-06 | 31 section, 16 sayfa, 3 overlay, 115 hedef; A/B de yazıldı |
| 3 build | tamam | canvas (`pencil-new.pen`) | 2026-10-06 | build-log yok (skill öncesi) |
| 4 verify | istisna | — | 2026-10-06 | §9 tasarım tarafı elle geçti; CHK raporu yok; ~350 işaretsiz metin (contract 1 bazı) |
| 5 handoff | bekliyor | `docs/port/port-manifest.json`, `port-manifest.md`, `globals-runbook.md` | | sıradaki adım: ikas aktarımı |

Durum değerleri: `bekliyor` · `sürüyor` · `tamam` · `istisna`.
