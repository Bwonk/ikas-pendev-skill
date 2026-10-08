Sözleşme 2 zorunlu ekleri (lint ve `pendev_checks.js` arar):
- `Button` durumları arasında `eklendi` ve `stok yok` var (sepete ekle akışı; ProductDetail ve hızlı ekle bunları kullanır).
- `{{prefix}}/Overlay/FilterDrawer@mobile` (mobil filtre çekmecesi) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili.
- `{{prefix}}/Overlay/QuickBuy@desktop` ve `@mobile` (hızlı al penceresi: açık · seçim eksik · ekleniyor) 6.2'de Overlay olarak tanımlı ve 6.4'te çizili; ProductCard'ın sepet düğmesi açar.
- Ürün detayda ikas mağaza blokları (`pdp-rating`, `pdp-campaign`, `pdp-offers`, `pdp-pay`, `pdp-bundle`, `pdp-tiers`, `pdp-options`, `pdp-group`, `pdp-back-in-stock`), ayrı `ProductReviews` section'ı; sepet sayfası ve çekmecede kampanya satırları, uygulanan kupon, öneri şeridi; `OfferCard`, `BundleItem`, `RatingStars`, `ReviewCard` Sub'ları ve CartLineItem'ın indirimli · hediye · set · kişiselleştirilmiş halleri (06-page-coverage §3b).
- Mağaza tamamlama (06-page-coverage §3c): Toast, CookieBar, ImagePreview, LocaleSwitcher, AccountMenu overlay'leri (özel hesapta AddressModal + ConfirmModal); RichText ve OrderTracking section'ları; filtre tipleri, varyant swatch'ları, galeride video, sosyal/SMS giriş, sipariş detayı ve hesap ayarları katmanları; VariantSwatch, PriceRange, SocialLoginButton, Skeleton Sub'ları.
- Her section kök frame'i `backgroundColor` COLOR prop'unu taşır; her metin node'u `textClass` taşır.

