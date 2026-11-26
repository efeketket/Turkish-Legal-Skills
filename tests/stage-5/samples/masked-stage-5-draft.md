# Aşama 5 KurguServis aktarım incelemesi

26 Kasım 2026. [Maskelenmiş sentetik dosya](../fixtures/masked-stage-5-input.md), A2-v3, A3-v2 ve A4-v2 kesitleri. Bu regresyon örneği devir, olgusal haritalama ve aday kararlarını gösterir. Ortam ve işlemler senaryoya özgüdür. Güncel resmî kaynak kontrolü çalışma sırasında açık kalmıştır.

## Devir ve hazırlık

| Faaliyet ve aktarım kapsamı | Aşama 2 kararı | Aşama 3 devir durumu | Esaslı incelemeye devir | Aşama 4 işleme şartı bağlantısı | Bilinen alıcı ve akış | Hazırlık işi, engel ve devam koşulu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-010 · TR barındırma | Devredilebilir · Aşama 5 | Devredilebilir · aynı kapsam | Devredilebilir | A4-v2 Aday 21 · aynı işlem · Ek kanıt gerekli | KurguHat A.Ş. · API · Türkiye | Aday taslağı. İki alanın bu alıcıya aktarım gerekliliğini belgele. | K-021, K-022, E-021 |
| A-010 · DE yedekleme | Devredilebilir · Aşama 5 | Devredilebilir · aynı kapsam | Devredilebilir | A4-v2 Aday 22 · aynı işlem · Ek kanıt gerekli | KurguKopya GmbH · otomatik ikinci kopya · Almanya | Koşullu aday taslağı. Yedekleme alanlarını, yeterliliği, hak ve başvuru yollarını ve güvenceyi doğrula. | K-021, K-023, E-025, E-028 |
| A-010 · TR test kurtarma | Devredilebilir · Aşama 5 | Devredilebilir · aynı kapsam | Devredilebilir | A4-v2 bağlantısı yok | KurguHat A.Ş. · ayrı test uç noktası · Türkiye | Olgusal haritalama. Kurtarma işlemini kapsayan işleme şartı kaydı için Aşama 4'e dön. | K-021, K-024, E-027 |
| A-011 · Haricî takvim | Devredilebilir · KurguTakvim A.Ş. | Devredilebilir · KurguTakvim Destek A.Ş. | Bekletilir | Eşleşen alıcı belirlenmeden bağlanmaz | İki ayrı tüzel kişi · Türkiye | Hazırlık notu. Fiilî muhatabı doğrula, Aşama 2 kapsamını ve Aşama 3 rolünü eşleştir. | K-025, E-022 |
| A-012 · Bildirim uç noktası | Bekletilir · Aşama 5 | Bekletilir · alıcı ve rol belirsiz | Bekletilir | Eksik kapsam | Belirsiz · bildirim uç noktası | Hazırlık notu. Hukuki kimlik ve rol belgesiyle Aşama 2 ve 3 kararlarını yeniden değerlendir. | K-026, E-023 |
| A-013 · Arşiv kopyası | Devredilebilir · Aşama 5 | Devredilebilir · aynı kapsam | Devredilebilir | A4-v2 Aday 23 · aynı işlem · Ek kanıt gerekli | KurguArşiv Ltd. · haftalık üretim kopyası · ülke belirsiz | Olgusal haritalama. Depo, erişim yetkisi ve fiilî erişim ülkelerini doğrula. | K-027, E-024, E-026 |

## Aktarım akışları

| Akış no. | Faaliyet ve aktarım kapsamı | Amaç, ilgili kişi, veri ve kişi bağlantısı | Aktaran ve rol | Alıcı ve rol | İletim veya erişim, ortam ve sıklık | Barındırma ülkesi | Erişim yetkisi ülkeleri | Erişim yetkisi | Fiilî erişim ülkeleri | Fiilî erişim ve indirme | Aktarım hedefi ve yön | Önceki akış no. | Mekanizma inceleme durumu | Kanıt, ortam sınırı ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A-010 · TR barındırma | Kurulum randevusu · sözleşme tarafı müşteri · hesabına bağlanan servis referansı ve randevu saati | KurguServis A.Ş. · veri sorumlusu | KurguHat A.Ş. · veri işleyen | API · senaryo içi üretim · her yeni randevuda | Türkiye | Türkiye | Yönetici | Türkiye | Yedi günlük özette erişim var, indirme kaydı yok | Türkiye · Yurt içi | — | Ek kanıt gerekli · alan gerekliliği | K-021, K-022, E-021 |
| 2 | A-010 · DE yedekleme | Servis devamlılığı · sözleşme tarafı müşteri · hesabına bağlanan servis referansı ve randevu saati | KurguServis A.Ş. · veri sorumlusu | KurguKopya GmbH · veri işleyen | Otomatik kopya · senaryo içi üretim · her gece | Almanya | Almanya | Yönetici | Almanya | Yedi günlük özette erişim var, indirme kaydı yok | Almanya · Yurt dışı | — | Ek kanıt gerekli · koşullu güvence | K-021, K-023, E-025, E-028 |
| 3 | A-010 · TR test kurtarma | Kurtarma tatbikatı · sözleşme tarafı müşteri · hesabına bağlanan servis referansı ve randevu saati | KurguServis A.Ş. · veri sorumlusu | KurguHat A.Ş. · veri işleyen | Ayrı test uç noktası · tek tatbikat | Türkiye | Türkiye | Tatbikat erişimi | Türkiye | Test erişimi var, indirme yok | Türkiye · Yurt içi | — | Ek kanıt gerekli · Aşama 4 kaydı yok | K-021, K-024, E-027 · testle sınırlı |
| 4 | A-013 · Arşiv kopyası | Servis itirazlarını inceleme · sözleşme tarafı müşteri · hesabına bağlanan servis referansı ve randevu saati | KurguServis A.Ş. · veri sorumlusu | KurguArşiv Ltd. · veri işleyen | Arşiv kopyası · senaryo içi üretim · haftalık | Belirsiz | Belirsiz | Konum açık | Belirsiz | Yönetim konumu ve indirme açık | Belirsiz | — | Ek kanıt gerekli · ülke saptanamadı | K-027, E-024, E-026 |

## Aktarım şartı ve mekanizma adayları

| Akış no. | Aday hüküm ve mekanizma | Aktarım için ileri sürülen işleme şartı | Aşama 4 kayıt kimliği ve kapsam eşleşmesi | Mekanizma koşulları ve kanıt sınırı | Hukuki kaynak | Taslak durum ve gerekçe | Açık kayıt ve istenecek kanıt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | m. 8/2-a · Yurt içi aktarım | m. 5/2-c | A4-v2 Aday 21 · KurguHat A.Ş.'ye aynı barındırma aktarımı · Ek kanıt gerekli | K-021 ve K-022 müşteri tarafını, sözleşme bağını ve bu alıcıya aktarılan iki alanı gösteriyor. İşlemin ve iki alanın gerekliliği açık. | H-021 | Ek kanıt gerekli · sözleşme bağından ayrı işlem ve alan gerekliliği ile güncel kaynak kontrolü bekleniyor. | E-021, E-029 |
| 2 | Koşullu m. 9/4-c · Standart sözleşme | m. 5/2-c | A4-v2 Aday 22 · KurguKopya GmbH'ye aynı yedek aktarımı · Ek kanıt gerekli | m. 9/1 araştırılıyor. K-021 ve K-023 ilgili taraf rollerini ve düzenli doğrudan Almanya kopyasını gösteriyor. Hak ve başvuru yolları, imzalı güvence, bildirim ve fiilî kapsam uyumu açık. Gecelik düzenli aktarım m. 9/6 adayını desteklemiyor. | H-022 | Ek kanıt gerekli · koşullu güvence, yedek alan gerekliliği ve kaynak kontrolü bekleniyor. | E-025, E-028, E-029 |

## Açık kayıtlar

| Açık kayıt ve kaynak | Etkilenen faaliyet ve kapsam | İstenecek kanıt ve devam koşulu |
| --- | --- | --- |
| E-021 · A4-v2 | A-010 · TR barındırma | İşlem ve alan bazında gereklilik ve daha az veriyle yürütme olanağı. |
| E-022 · A3-v2 | A-011 · Haricî takvim | Gerçek tüzel muhatabı gösteren maskelenmiş sözleşme eki ve iki aşamada ortak kapsam. |
| E-023 · A2-v3 ve A3-v2 | A-012 · Bildirim uç noktası | Uç noktanın hukuki sahibini ve rolünü gösteren kayıtla iki devri yeniden değerlendir. |
| E-024 · A2-v3 ve A3-v2 | A-013 · Arşiv kopyası | Depo bölgesi ile yetkili ve fiilî erişim ülkelerinin maskelenmiş dökümü. |
| E-025 · A4-v2 | A-010 · DE yedekleme | Yedekleme ve veri alanlarının bu alıcı bakımından gerekliliği. |
| E-026 · A4-v2 | A-013 · Arşiv kopyası | İtirazı değerlendirmek için alıcıya gönderilen alanların gerekliliği. |
| E-027 · Aşama 5 | A-010 · TR test kurtarma | Aynı amaç, veri, ilgili kişi, işlem ve alıcı için Aşama 4 aday veya karar kaydı. |
| E-028 · Aşama 5 | A-010 · DE yedekleme | Yeterlilik araştırması, ülkeye özgü hak ve başvuru kayıtları, imzalı metin ve ekleri, bildirim ve uygulama kanıtı. |
| E-029 · Aşama 5 | A-010 · TR barındırma ve DE yedekleme | İşlem tarihinde yürürlükteki resmî madde ve güvence metnini doğrula. |

## Hukuki kaynak kaydı

| Kaynak kimliği | Kaynak ve nitelik | Erişilen bölüm | Sürüm veya yürürlük tarihi | Desteklenen önerme | Erişim tarihi ve durumu | Güncellik kontrolü ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| H-021 | 6698 sayılı Kanun · kanun | m. 5 ve 8 için yerel metodoloji kaydı | İşlem günündeki metin kontrolü açık | İşleme şartı ve yurt içi aktarım aday yolu | Çevrimdışı yerel yönerge | E-029 |
| H-022 | 6698 sayılı Kanun · kanun | m. 9 için yerel metodoloji kaydı | İşlem günündeki metin kontrolü açık | Yeterlilik, uygun güvence, bildirim ve arızilik sırası | Çevrimdışı yerel yönerge | E-029 |

## Hukukçu karar ve onay kaydı

Belgelenmiş bir karar sunulmadı.

| Faaliyet ve akış no. | Hukukçunun kimliği ve rolü | Karar kayıt no., tarih ve kaynak | Amaç, veri, ilgili kişi ve alıcı | Fiilî akış ve ortam | Seçilen ve elenen adaylar | Aday bazında gerekçe ve hukuki dayanak | Aşama 2, 3 ve 4 rapor tarihleri veya sürümleri | Kanıt kimlikleri ve sürümleri | Hukuki kaynak kimlikleri ve erişim tarihleri | Kapsam dışı veya bekletilen hususlar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
