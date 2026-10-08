Sözleşme 2 zorunlu ekleri (lint ve `pendev_checks.js` arar):
- `Button` durumları arasında `eklendi` ve `stok yok` var (sepete ekle akışı; ProductDetail ve hızlı ekle bunları kullanır).
- `{{prefix}}/Overlay/FilterDrawer@mobile` (mobil filtre çekmecesi) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili.
- `{{prefix}}/Overlay/QuickBuy@desktop` ve `@mobile` (hızlı al penceresi: açık · seçim eksik · ekleniyor) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili; ProductCard'ın sepet düğmesi açar.
- Her section kök frame'i `backgroundColor` COLOR prop'unu taşır; her metin node'u `textClass` taşır.

