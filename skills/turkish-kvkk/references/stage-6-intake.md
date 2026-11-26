# Aşama 6 · Saklama, imha ve veri güvenliği için devir

`0.8.0` hazırlık önizlemesi. Gerçek dosyalarda devir, olgusal inceleme ve kanıt talebi üret. Hukuki değerlendirme yöntemini sentetik dosyalarda ve metodoloji incelemesinde göster. Gerçek dosyada esaslı değerlendirme kullanımı için belgelenmiş hukukçu onayı gerekir. [İnceleme metodolojisi](stage-6-retention-security.md) · [Çıktı şablonu](../assets/stage-6-outputs.md)

## Önceki aşamalardan alınacak kayıtlar

- **Aşama 2.** Güncel `A-…` kaydı, amaç, veri alanları ve ilgili kişi grupları, işlemler, sistem ve fiziksel kayıt ortamları, kopyalar, yaşam döngüsü, açıklar ve Aşama 6 hedefine özgü faaliyet kararı.
- **Aşama 3.** Aynı faaliyet, kapsam ve Aşama 6 hedefi için devir satırı. Saklama süresini, erişimi ve imhayı kimin belirlediği ile fiilen kimin uyguladığı. Veri sorumlusu, veri işleyen ve varsa alt sağlayıcının rolü, talimatı ve açıkları.
- **Aşama 4.** İşleme şartı kaydının tarihini, adayını veya belgelenmiş kararını, kapsamını, durumunu ve açıklarını aktar. Özel nitelikli veri için kapsam tespiti ve varsa m. 6/4 önlem kaydını bağla.
- **Aşama 5.** İlgili akış numarasını, tarafı ve rolü, ortamı, ülkeyi, erişim yetkisini, fiilî erişimi, varsa güvence ve açık kaydını aktar.

Raporların tarihini veya sürümünü kaydet. `A-…`, `K-…`, `E-…` ve `H-…` kimliklerini ait oldukları rapor zincirinde çözümle. Tarihsel faaliyetleri revizyon bağıyla göster. Aynı faaliyet içindeki farklı ortam, taraf veya işleyiş için ayrı kapsam satırı aç.

## Hazırlık ve olgusal inceleme

Önceki kararların izin verdiği ölçüde bilinen ortamları ve kopyaları yaz, mevcut kanıtın neyi gösterdiğini kaydet ve eksikler için maskelenmiş politika, sözleşme, ayar veya işlem kaydı iste. `Sınırlı devredilebilir` ve `Kısıtlı` kararlarındaki izin verilen işi aynen taşı. `Bekletilir` kapsamı için kanıt talebi ve izin verilen olgusal hazırlık sürer. Gerekçeli `Uygulanmaz` kararını kapsamı ve kaynağıyla göster. Kişi bağı veya hukuki kapsam belirsizse gözlemi bu sınırla yaz.

Otomatik olmayan işlemede kâğıt kaydın fiilen tutulması, kişi, tarih veya işlem gibi ölçütlerle düzenlenmesi, geçmiş kaydın bulunabilmesi ve düzenli kullanımı hakkında dayanak iste. Otomatik işlemede kişiyle ilişkilendirilebilirliği ve gerçek kullanım ortamını doğrula. [6698 sayılı Kanun, m. 2 ve 3](https://ceyhansolsahil.gov.tr/wp-content/uploads/2025/08/1.5.6698.pdf#page=1)

## Esaslı incelemeye devir

1. Aşama 2 ve 3’ün aynı güncel faaliyet, Aşama 6 hedefi, amaç, kişi grubu, veri, operasyon, ortam veya kopya ve taraf için verdiği açık ve gerekçeli kararları eşleştir. Kaynak kararın izin verdiği alt kapsamı göster. İki kapsam kesişiyorsa yalnız kesişen kısmı değerlendir.
2. İki karar esaslı incelemeye açıkça izin veriyorsa eşleşen alt kapsamı `Devredilebilir` kaydet. `Sınırlı devredilebilir` kararı yalnız açıkça izin verdiği işi taşır. Yalnız hazırlığa izin veriliyorsa esaslı devir `Bekletilir` kalır. Karar eksik veya kapsam dışıysa ya da m. 2, kişi bağlantısı veya taraf belirsizliği esaslı incelemeyi engelliyorsa `Bekletilir` yaz. Yeni kanıt ve gerekçeli Aşama 2–3 yeniden değerlendirmesiyle kararı güncelle.
3. Somut bulguya ait Aşama 4 ve 5 bağlantılarını aşağıdaki eşiklerle kontrol et. Esaslı devir kaydı, inceleme kapsamına ilişkin bir karardır. `0.8.0` gerçek dosya çıktısı hazırlık ve olgusal kayıtlarla sınırlıdır. Sentetik değerlendirmede de eksik sonuç koşullarını açık kayda ve istenecek kanıta bağla.

## Aşama 4 ve 5 bağlantıları

- **Aşama 4.** Saklama dayanağı, işleme şartının devamı ve imha yükümlülüğünün doğduğu tarih için aynı amaç, veri, kişi, saklama işlemi ve tarafı kapsayan Aşama 4 kaydını ara. Yalnız toplamayı kapsayan kaydı ve açıklarını olduğu gibi taşı. Eşleşme veya devam koşulu belirsizse hukuki gerekçeyi ve imha yükümlülüğü tarihini açık bırak. Fiilî saklama, erişim, yedek, geri yükleme ve tedbir olgularını Aşama 2–3 kapsamı ve mevcut kanıtla kaydet.
- **Aşama 5.** Sağlayıcı kopyası, uzaktan erişim, yurt dışında barındırma veya yedek, alt sağlayıcı, dış alıcı, sonraki aktarım ve alıcı nezdinde imha adımlarını ayrı ele al. Gerekli akış, taraf, ülke veya erişim kanıtı açıksa yalnız etkilenen adımın hukuki değerlendirmesini beklet. Diğer kapsamların olgularını kendi kanıtıyla kaydet. `Uygulanmaz` için ilgili ortamın dış sağlayıcı, alıcı ve aktarım adımı içermediğini destekleyen dayanağı göster. Sentetik gözlemi kaynak ortamıyla sınırla ve üretim durumunu ayrı kaydet.

Yeni kanıtı `K-…` ile kayda al ve etkilenen `E-…` ile karar kapsamını yeniden değerlendir. Bağımsız faaliyet, amaç veya operasyon ya da eksik devir kararı için Aşama 2’ye, rol ve talimat değişikliği için Aşama 3’e, işleme şartı veya özel nitelik kapsamı için Aşama 4’e, yeni alıcı veya aktarım akışı için Aşama 5’e dön. Açığı, sorumlu tarafı ve devam koşulunu belirt.
