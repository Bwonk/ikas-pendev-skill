
## 0. Bu dosya nasıl kullanılır

Bu dosya pen.dev'de tasarım üretecek ajana (ya da tasarımcıya) verilen **tek başına yeterli** brifdir. Ölçülerin kaynağı ve motion tariflerinin ayrıntısı için `docs/referans/globals.md`, prop listeleri için `docs/referans/components.md`.

**Sıra:** 3 → 6.0 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5. Her adımın sonunda o adımın kontrol listesi ve ekran görüntüsü.

**Nereye çizilir:** tercihen bu varyant için yeni bir .pen dosyası (`{{penFile}}`). Aynı dosyada çalışılacaksa tüm kök frame adları `{{prefix}}/` ile başlar ve `FindEmptySpace` ile boş alana yerleştirilir.{{#canvasImportNote}} {{canvasImportNote}}{{/canvasImportNote}}

**Ajan için hazır komutlar** (sırayla, her biri ayrı tur):
1. `docs/pendev/{{file}} dosyasını oku. 3. bölümdeki değişkenleri tanımla ve 6.0'daki Design System frame'lerini üret.`
2. `Aynı planın 6.1 bölümündeki bileşenleri, durumlarıyla birlikte üret.`
3. `6.2'den <bölüm adı> bölümünü desktop ve mobil olarak üret; katman adları ve metadata plandaki gibi olsun.` (bölüm bölüm tekrarla)
4. `6.3'teki sayfaları section instance'larından kur.`
5. `6.4 overlay'lerini ve 6.5 Motion States karelerini üret.`
6. `9. bölümdeki bitiş kontrolünü çalıştır ve eksikleri raporla.`

