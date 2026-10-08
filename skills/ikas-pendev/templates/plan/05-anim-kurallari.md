
## 5. Animasyona hazır tasarım kuralları

pen.dev hareket göstermez. Aşağıdaki yapılar çizilmezse aktarımda katmanları yeniden kurmak gerekir.

1. **Bitiş hali çizilir.** Bölüm ve sayfa frame'leri animasyon bittikten sonraki görünümü gösterir. Başlangıç ve ara haller sadece `{{prefix}}/Motion/…` frame'lerinde.
2. **Maske = `clip: true` frame.** Kayarak giren her metin satırı kendi `…-mask` frame'inin içindedir; maske metinle aynı boyutta. Çok satırlı başlıkta her satır ayrı metin node'u ve ayrı maske.
3. **Roll eden öğeler çift kopyadır.** Buton, nav linki ve ok ikonunda `top` (görünen) ve `bottom` (maske dışında bekleyen) kopyaları birlikte çizilir; kap `clip: true`.
4. **Sonsuz kayanlar track + kopya.** `marquee` / `ticker` kabı `clip: true`; içindeki `…-track` içerik setini en az iki kez barındırır ve kabın dışına taşar.
5. **Yer değiştirenler kardeş frame.** Slaytlar, sekme içerikleri, ön/arka ürün görseli aynı ebeveynde üst üste (`layout: "none"`); görünmeyenler `opacity: 0` ile durur, silinmez.
6. **İlerleme göstergesi ayrı katman.** `progress-bar` dolgusu ebeveyninden ayrı bir dikdörtgen; yarı dolu çizilir.
7. **Sticky alanlar gerçek yükseklikte.** Sabit kalan öğenin kabı, kaydırma boyunca kat edeceği yükseklikte çizilir (ör. 4 görsellik galeri yanında tek detay sütunu).
8. **Overlay ayrı frame.** Menü, çekmece, arama: `scrim` + panel, sayfa frame'inin kopyası üzerinde değil, kendi kök frame'inde; açık ve boş/dolu halleri ayrı.
9. **Kaydırmaya bağlı öğeler serbest katman.** Dönen/kayan görsel ya da parallax arka plan, akıştan bağımsız (`layoutPosition: "absolute"`) ve kabından büyük çizilir.
10. **Hover hali ayrı frame.** Her etkileşimli bileşenin hover hali `{{prefix}}/Sub/<Ad> — hover` olarak çizilir; bölüm içinde tekrar çizilmez.
11. **Her hedef işaretli.** 6. bölümde `anim-targets` bloğunda geçen her `layer`, tasarımda aynı adla bulunur ve `metadata.anim` taşır{{#c2}}; id'ler `context` alanında da yazılıdır{{/c2}}.
12. **Mobil hali kararlaştırılmış.** Hedefin `mobile` alanı "kapalı" ya da farklıysa mobil frame o hale göre çizilir (ör. sticky yok → normal akış).

