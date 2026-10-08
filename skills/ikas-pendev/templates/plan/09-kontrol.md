
## 9. Bitiş kontrol listesi

{{^c2}}
Tasarım tarafı (pen.dev):
- [ ] `GetVariables()` 3. bölümdeki tüm değişkenleri içeriyor; tasarımda sabit hex / sabit yazı boyutu yok.
- [ ] 6.2'deki her bölümün `@desktop` ve `@mobile` kök frame'i var, ikisi de `reusable`.
- [ ] 6.3'teki her sayfa yalnızca section instance'larından oluşuyor.
- [ ] `Get(n => n.metadata?.anim …)`{{#contextScan}} ve `context` taramasının (8. bölüm, 2. adım) birleşik{{/contextScan}} çıktısındaki `id`'ler 7. bölümdeki listeyle birebir aynı.
- [ ] Her metin katmanında ya `metadata.prop` var ya da katman bir bileşen instance'ının parçası.
- [ ] Hiçbir frame'de kırpılmış ("clipped") içerik uyarısı yok (maske ve track'ler hariç; onlar bilinçli).
- [ ] Türkçe karakterler (`İ Ş Ğ Ü Ö Ç`) seçilen fontlarda doğru görünüyor.
- [ ] Referansın görselleri, metinleri ve logosu kullanılmadı.
{{/c2}}
{{#c2}}
Tasarım tarafı (pen.dev). Her madde `pendev_checks.js` içindeki bir CHK id'sidir (`extract_targets.py --js all` → `execute`; çıktı `CHK|<id>|PASS|FAIL|WARN|…`):
- [ ] `CHK vars`: `GetVariables()` 3. bölümdeki 41 çekirdek değişkeni ve eksenleri (`device`{{#modes}}, `mode`{{/modes}}) içeriyor.
- [ ] `CHK hardcoded`: tasarımda sabit hex dolgu, sabit yazı boyutu ya da sabit font ailesi yok; hepsi `$…`.
- [ ] `CHK sections`: 6.2'deki her bölümün `@desktop` ve `@mobile` kök frame'i var, ikisi de `reusable`.
- [ ] `CHK pages`: 6.3'teki her sayfa yalnızca section instance'larından oluşuyor; cihaz ekleri eşleşiyor.
- [ ] `CHK overlays`: 6.4'teki her overlay kök frame'i durumlarıyla birlikte var.
- [ ] `CHK anim`: `metadata.anim` ∪ `context` taramasındaki (8. bölüm, 2. adım) `id`'ler 7. bölümdeki listeyle birebir aynı.
- [ ] `CHK textclass`: her metin node'unda `textClass` var (`prop` → `prop` + `propType`; `data` → `source`).
- [ ] `CHK clip`: kırpılmış ("clipped") içerik yok; mask, track, marquee, ticker, pin, stage ve curtain kapları bilinçli olarak hariç.
- [ ] `CHK rootmeta`: her kök frame'de `type`, `role`, `ikas`, `device`, `variant`, `contract: 2` metadata'sı var.
- [ ] `CHK bgprop`: her section kök frame'i `prop: "backgroundColor"`, `propType: "COLOR"` taşıyor.
- [ ] `CHK placeholder`: hiçbir kök frame `placeholder: true` olarak kalmadı.
- [ ] `CHK refassets`: referansın görselleri, metinleri ve logosu kullanılmadı{{#policy}} ({{policy}}){{/policy}}; hiçbir `fill` referans alan adını içermiyor.
- [ ] `CHK ds`: `{{prefix}}/DS/Colors`, `Typography`, `Spacing`, `Icons`, `Motion`, `Imagery` frame'leri var.
- [ ] Türkçe karakterler (`İ Ş Ğ Ü Ö Ç`) seçilen fontlarda doğru görünüyor (ekran görüntüsüyle).
{{/c2}}

Aktarım tarafı (ikas):
- [ ] Tema global'leri (renk, tipografi, kırılım) açıldı; `list_theme_globals` ile doğrulandı.
- [ ] Her section `check` ve `build` adımından hatasız geçti.
- [ ] 7. bölümdeki tüm hedefler `done: true`.

