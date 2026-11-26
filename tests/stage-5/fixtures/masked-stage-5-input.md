# KurguServis · Maskelenmiş sentetik aktarım dosyası

Tarih 26 Kasım 2026. Aşağıdaki rapor kesitleri, sözleşme ve ortam kayıtları kurgusaldır. Maskelenmiş bir gerçek dosya teslimini taklit eder. Gerçek kişi bilgisi veya ham üretim kaydı yoktur. Bir kayıt üretim ortamı olarak işaretlendiyse bu, yalnızca senaryo içindeki ortamı gösterir.

## Aşama 2 · Envanter ve devredilen kapsam

Rapor A2-v3. KurguServis A.Ş. (Türkiye) aktaran ve veri sorumlusudur. Güncel `A-010`, servis sözleşmesine taraf müşterinin talebini yerine getirme ve kurulum kaydını servis süresince yönetme faaliyetidir. `A-010` kapsamındaki her akış aynı müşteriyle bağlantılı servis referansı ve randevu saatini işler. Referans, KurguServis'teki güncel müşteri hesabına güvenilir biçimde bağlanır. `A-011`, `A-012` ve `A-013` aynı veri ve kişi bağlantısını kullanan ve aşağıda kendi amaçları belirtilen güncel faaliyetlerdir.

| Faaliyet ve kapsam | Amaç ve işlem | Alıcı | Hedef ve gerekçeli karar |
| --- | --- | --- | --- |
| A-010 · TR barındırma | Kurulum randevusunu yürütmek için API ile barındırma | KurguHat A.Ş. | Aşama 5 · Devredilebilir · K-021 ve K-022 belirli alıcıyı, veri sınırını ve iletimi gösteriyor. |
| A-010 · DE yedekleme | Servis devamlılığı için otomatik ikinci kopya | KurguKopya GmbH | Aşama 5 · Devredilebilir · K-021 ve K-023 veri, alıcı ve yedek akışını gösteriyor. |
| A-010 · TR test kurtarma | Bakım için ayrı bir kurtarma ortamına veri gönderimi | KurguHat A.Ş. | Aşama 5 · Devredilebilir · K-021 ve K-024 ayrı alıcı uç noktasını ve işlemi gösteriyor. |
| A-011 · Haricî takvim | Randevuyu bir iş ortağının takvimine yazma | KurguTakvim A.Ş. | Aşama 5 · Devredilebilir · K-025 Türkiye'de bulunan takvim hedefini ve gönderimi gösteriyor. |
| A-012 · Bildirim uç noktası | Kurulum hatırlatmasını iletme | Hukuki kimliği belirsiz bildirim uç noktası | Aşama 5 · Bekletilir · K-026 uç noktayı gösteriyor. E-023 alıcıyı açık bırakıyor. |
| A-013 · Arşiv kopyası | Açık servis itirazlarını incelemek için akıllı depolamaya kopyalama | KurguArşiv Ltd. | Aşama 5 · Devredilebilir · K-027 alıcıyı, amacını ve kopya işlemini gösteriyor. E-024 ülke için hazırlık ve araştırma kaydıdır. |

## Aşama 3 · Rol ve hedef devir kayıtları

Rapor A3-v2. Her satırda aktaran KurguServis A.Ş. ve rolü veri sorumlusudur. Aşağıdaki aynı kapsam atıfları A2-v3'teki operasyon, amaç, veri, kişi ve aktaranla eşleşir.

| Faaliyet ve kapsam | Alıcı ve rol | Hedef ve gerekçeli karar |
| --- | --- | --- |
| A-010 · TR barındırma | KurguHat A.Ş., yazılı talimatla veri işleyen | Aşama 5 · Devredilebilir · K-021 ile kapsam ve talimat eşleşti. |
| A-010 · DE yedekleme | KurguKopya GmbH, doğrudan yazılı talimatla veri işleyen | Aşama 5 · Devredilebilir · K-021 ile kapsam ve talimat eşleşti. |
| A-010 · TR test kurtarma | KurguHat A.Ş., yazılı talimatla veri işleyen | Aşama 5 · Devredilebilir · K-021 ve K-024 kurtarma uç noktasının talimatını gösteriyor. |
| A-011 · Haricî takvim | KurguTakvim **Destek** A.Ş., takvim kaydını alan ayrı tüzel kişi olarak rol değerlendirmesine konu edilmiş | Aşama 5 · Devredilebilir · K-025'teki taşıma eki yalnız KurguTakvim Destek A.Ş. için incelendi. E-022 hangi muhatabın rol raporuna bağlanacağını açık bırakıyor. |
| A-012 · Bildirim uç noktası | Hukuki kimlik ve rol belirsiz | Aşama 5 · Bekletilir · K-026 göndereni ve uç noktayı gösteriyor. E-023 alıcıyı açık bırakıyor. |
| A-013 · Arşiv kopyası | KurguArşiv Ltd., yazılı talimatla veri işleyen | Aşama 5 · Devredilebilir · K-027 ile kapsam ve talimat eşleşti. E-024 ülke için hazırlık ve araştırma kaydıdır. |

## Aşama 4 · İşleme şartı kayıtları

Rapor A4-v2. Aşağıdaki kayıtlar A2-v3 ile aynı amaç, veri, kişi ve aktarım işlemini belirtilen alıcı için kapsar. A-010 TR test kurtarmaya ilişkin işleme şartı kaydı yoktur. Hukukçuya ait nihai karar sunulmamıştır.

| Kayıt | Faaliyet ve kapsam | Alıcı | İşleme şartı ve durum |
| --- | --- | --- | --- |
| Aday 21 | A-010 · TR barındırma | KurguHat A.Ş. | m. 5/2-c · Ek kanıt gerekli · K-021 müşteriyle servis sözleşmesini ve randevu işlemini doğrudan ilişkilendiriyor. E-021 aktarımda iki alanın da gerekliliğini açık bırakıyor. |
| Aday 22 | A-010 · DE yedekleme | KurguKopya GmbH | m. 5/2-c · Ek kanıt gerekli · K-021 servis devamlılığı ilişkisini açıklıyor. E-025 yedek kopyanın kapsamı ve alan gerekliliğini açık bırakıyor. |
| Aday 23 | A-013 · Arşiv kopyası | KurguArşiv Ltd. | m. 5/2-e · Ek kanıt gerekli · K-027 itirazların incelenmesini gösteriyor. E-026 alıcıya aktarılacak alanların itiraz incelemesi için gerekliliğini açık bırakıyor. |

## Maskelenmiş kanıtlar

| Kimlik | Kayıt, olgu ve sınır |
| --- | --- |
| K-021 | Hizmet sözleşmesi ve imzalı talimat ekleri v3. KurguServis müşteriye kurulum taahhüdü veriyor. KurguHat A.Ş. randevu barındırma ve sınırlı kurtarma testi, KurguKopya GmbH servis devamlılığı için kopyalama talimatı alıyor. İlgili kişinin hesabına yalnız KurguServis'in servis referansı üzerinden bağlanılıyor. Almanya için reddedilmiş veya onaylanmış hukukçu kararı, güncel yeterlilik taraması, standart sözleşmenin imzalı metni ve hak kullanma veya başvuru yolu incelemesi sunulmadı. Taraf rolleri ve standart sözleşme taslağındaki veri sorumlusu–veri işleyen kurgusu hizmet ekiyle uyumlu. |
| K-022 | Maskelenmiş yapılandırma v8 ve yedi günlük erişim özeti v1. Üretimde servis referansı ve randevu saati her yeni randevuda Türkiye'deki KurguHat A.Ş. uç noktasına API ile gönderildi. Barındırma, yetkili erişim ve gözlenen yönetici erişimi Türkiye. Özet kapsamındaki olaylarda indirme kaydı yok. |
| K-023 | Maskelenmiş üretim ayarı v8 ve yedi günlük işlem özeti v1. KurguServis aynı iki alanı her gece otomatik olarak Almanya'daki KurguKopya GmbH yedek deposuna gönderdi. Depo Almanya'da, yönetici yetkisi ve gözlenen erişim Almanya'da. Gözlenen olaylar yedekleme ile sınırlı ve indirme kaydı içermiyor. |
| K-024 | Test ayarı v2 ve maskelenmiş tek kurtarma tatbikatı özeti. Aynı iki alan KurguHat A.Ş.'nin ayrı, Türkiye'deki kurtarma uç noktasına iletildi. Erişim yetkisi ve gözlenen erişim Türkiye, indirme yok. Test ortamında tek sefer çalıştırıldı. |
| K-025 | Maskelenmiş üretim uç noktası ve taşıma eki v1. Alıcı kayıtlarında KurguTakvim A.Ş. ve KurguTakvim Destek A.Ş. geçiyor. İkisi ayrı tüzel kişi ve Aşama 2 ile Aşama 3'ün karşı tarafları farklı. |
| K-026 | Maskelenmiş üretim yönlendirme izi. Bildirim ana bilgisayarı takma adla kayıtlı. Alıcı kimliği ve rolü belirlenemedi. |
| K-027 | Maskelenmiş saklama ayarı v1 ve talimat eki v2. KurguArşiv Ltd. itiraz dosyalarından çıkan servis referansı ve randevu saatini talimatla üretimde haftalık olarak kendi deposuna alıyor. Depo bölgesi maskelenmiş, alıcı erişim yetkisi ülkeleri ve fiilî yönetim konumu açıklanmamış. Türkiye ile yurt dışı arasında sınıflandırmaya yeterli ülke bilgisi yok. |

`E-021` barındırma alan gerekliliği, `E-022` takvim taraf uyuşmazlığı, `E-023` bildirim alıcısı, `E-024` arşiv ülkesi, `E-025` yedek alan gerekliliği ve `E-026` arşiv alan gerekliliği önceki raporlardan açıktır.
