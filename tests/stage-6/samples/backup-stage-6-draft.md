# Aşama 6 · Saklama, imha ve veri güvenliği raporu

Rapor niteliği: Hukukçu incelemesi taslağı

26 Kasım 2026 tarihli sentetik KurguArşiv örneği. KurguArşiv, müşteri destek kayıtlarının veri sorumlusu ve kendi test ortamının işletmecisidir. Olaylar ve sayıların tamamı kurgusaldır. Kimlikler bu örnek zincirine aittir.

## Sentetik devir girdileri

| Kaynak | Faaliyet ve kapsam | Hedef ve karar | Gerekçe |
| --- | --- | --- | --- |
| Aşama 2 · 25.11.2026 | A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Aşama 6 · Devredilebilir | Kapalı destek kaydına ait talep numarası ve kapanış zamanı, kayıt sahibi bağlantısı ve iki ortam sentetik envanterde kayıtlı. K-001, K-002 |
| Aşama 3 · 25.11.2026 | A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Aşama 6 · Devredilebilir | Süreyi ve erişimi KurguArşiv belirliyor. Uygulama ve yedek ekipleri aynı tüzel kişinin içinde. K-001, K-002 |
| Aşama 4 · 25.11.2026 | A-010 · Destek talebinin toplanması | Aday kaydı · Kapsam açık | Aynı destek amacı için toplama adımı incelenmiş. Saklama, yedek ve geri yükleme bağlantısı açık. E-001 |

## Sentetik kanıt girdileri

| Kanıt | Kaynak ve ortam | Gösterdiği olgu ve sınır |
| --- | --- | --- |
| K-001 | KurguArşiv saklama politikası taslağı v2 ve rol matrisi, 25.11.2026 | Kapanıştan 30 gün sonra silme beyanı ve yedek erişimi için yetki matrisi. Mevzuat dayanağı ve fiilî uygulama açık. |
| K-002 | Test yapılandırma özeti, 25.11.2026 | Kapanıştan 90 gün sonra arayüzde gizleme ayarı ve 14 gün yedek saklama ayarı. Gerçek süre ve sona erme olayları gözlenmedi. |
| K-003 | Maskelenmiş test olayı, 26.11.2026 | Eski sentetik kayıt arayüzde görünmüyor. Yönetim görünümünde aynı kayıt okunabiliyor. Diğer erişim yolları incelenmedi. |
| K-004 | Maskelenmiş geri yükleme tatbikatı, 26.11.2026 | Önceki yedek ayrı bir test ortamına geri yüklendi. Standart destek rolü kayıt numarasını yeniden görüntüledi. Üretim, yedek sona ermesi ve sonraki imha incelenmedi. |

## Devir ve hazırlık

| Faaliyet ve kapsam | Aşama 2 kararı | Aşama 3 devir durumu | Esaslı incelemeye devir | Aşama 4 ve 5 bağlantıları | Hazırlık işi, engel ve devam koşulu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Devredilebilir | Devredilebilir | Devredilebilir · Sentetik olgu incelemesi | Aşama 4 kaydı toplama kapsamıyla sınırlı. Aşama 5 bağlantısı, aktarıma işaret eden taraf veya adım bulunmadığı bu test kapsamı için uygulanmaz. | Saklama işlemi için dayanak iste. Görünürlük, yedek erişimi ve geri yükleme gözlemlerini ilgili test ortamıyla sınırla. | K-001, K-002, K-003, K-004, E-001 |

## Saklama ve kopyalar

| Ortam no. | Faaliyet ve kapsam | Kayıt ortamı, kopya ve taraf | Veri, ilgili kişi ve amaç | Başlangıç olayı, süre ve gerekçe | Politika beyanı | Yapılandırılan süre | Fiilî saklama ve ortam | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A-010 · Birincil kayıt | Test veritabanı · KurguArşiv | Talep no. ve kapanış zamanı · Destek talebi sahibi · Talep takibi | Kapanış. Sürenin hukuki dayanağı açık. | Kapanıştan 30 gün sonra silme | Kapanıştan 90 gün sonra arayüzde gizleme | Tek sentetik olayda gizlenen kayıt yönetim görünümünde mevcut. Fiilî toplam süre açık. | Kısmen doğrulandı · K-001, K-002, K-003, E-001, E-002 |
| 2 | A-010 · Kurum içi yedek | Test yedeği · KurguArşiv | Aynı alanlar ve kişi grubu · Hizmeti geri yükleme | Yedek oluşturma. Ayrı süre gerekçesi açık. | Yedek süresine ilişkin beyan yok | 14 günlük test yedeği | Yedek, geri yükleme tatbikatında kullanıldı. Yedek sona ermesi açık. | Kısmen doğrulandı · K-002, K-004, E-001, E-003 |
| 3 | A-010 · Geri yüklenen kopya | 2 no.lu yedekten oluşturulan ayrı test kopyası · KurguArşiv | Aynı alanlar ve kişi grubu · Geri yükleme tatbikatı | Geri yükleme. Ayrı süre gerekçesi açık. | Geri yüklenen kopyanın süresine ilişkin beyan yok | Süre ayarı açık | Kayıt geri yükleme sırasında gözlendi. Sonraki saklama açık. | Kısmen doğrulandı · K-004, E-001, E-005 |

## İmha ve doğrulama

| Ortam no. | Tetikleyici, tarih ve uygulanacak süre | Yöntem ve uygulayan taraf | Fiilî işlem ve tarihi | Erişim, yeniden kullanım veya geri yükleme kanıtı | İmha kaydı ve kayıt süresi | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Kapanış politikada geçiyor. İmha yükümlülüğünün doğduğu tarih açık. | KurguArşiv’in uygulamasında arayüzde gizleme | 26.11.2026 testinde görünürlük değişti. | Yönetim görünümünde kayıt erişilebilir. Yönetim rolünün ilgili kullanıcı niteliği ve diğer erişim yolları açık. | Ayrı imha kaydı ve süresi açık. | Doğrulandı · Yalnız testteki görünürlük ve erişim olgusu · K-003, E-002 |
| 2 | Yedek oluşturma ve 14 günlük ayar. Kapsam ve yükümlülük tarihi açık. | KurguArşiv’in yedek sona erme işlemi | Sona erme açık. | 26.11.2026 testinde yedekten 3 no.lu kopya oluşturuldu. | Yedek imha işlem kaydı ve süresi açık. | Kısmen doğrulandı · K-002, K-004, E-003 |
| 3 | Tatbikat sonrasındaki işlem ve yükümlülük tarihi açık. | Yöntem açık · KurguArşiv | İmha gözlenmedi. | Standart destek rolü 26.11.2026 tarihinde test kopyasında kayıt numarasını yeniden gördü. | Geri yüklenen kopyanın imha kaydı ve süresi açık. | Kısmen doğrulandı · K-004, E-005 |

## Teknik ve idari tedbirler

| Ortam no. | Risk ve tedbir | Uygulayan ve denetleyen taraf | Politika, talimat veya beklenen işleyiş | Fiilî gözlem ve sınırı | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- |
| 3 | Geri yükleme sonrası önceki kayıtların yeniden erişime açılması · Kullanıma açmadan önce yetki ve imha kontrolü | KurguArşiv yedek ekibi ve güvenlik sorumlusu | K-001 yedek erişimine ilişkin rol matrisi içeriyor. Geri yüklenen kayıt için kontrol adımı açık. | K-004’te standart destek rolü test kopyasına erişti. Üretim uygulaması ve denetim kaydı açık. | Kısmen doğrulandı · K-001, K-004, E-005 |

## Taslak değerlendirme

| Faaliyet, kapsam ve ortam no. | İncelenen konu | Hukuki kaynak | Olgusal dayanak ve sınırı | Durum, gerekçe ve açık kayıt |
| --- | --- | --- | --- | --- |
| A-010 · 1, 2 ve 3 | Saklama dayanağı ve imha yükümlülüğünün doğduğu tarih | H-001, H-002 | Toplama kaydı var. Politikadaki ve yapılandırmadaki süreler farklı işlemleri ifade ediyor. | Ek kanıt gerekli · Her ortam için eşleşen gerekçe ile kaynak karşılaştırması açık. E-001, E-004 |
| A-010 · 1 | Arayüzde gizleme ve erişim | H-002 | Yönetim görünümünde test kaydına erişim gözlendi. | Ek kanıt gerekli · İlgili kullanıcı erişimi, yeniden kullanım ve imha kaydı açık. E-002 |
| A-010 · 2 | Yedek sona ermesi | H-002, H-003 | Yedekten geri yükleme gerçekleşti. Yedek sona ermesi ve üretim gözlenmedi. | Ek kanıt gerekli · Sona erme ve imha kanıtı açık. E-003 |
| A-010 · 3 | Geri yükleme sonrası erişim ve imha | H-002, H-003 | Testte destek rolü kayda erişebildi. Kopyanın sonraki imhası ve üretim gözlenmedi. | Ek kanıt gerekli · Geri yükleme sonrası kontrol ve kopyanın imhası açık. E-005 |

## Açık kayıtlar ve sonraki aşamaya devir

| Açık kayıt ve kaynak | Faaliyet, kapsam ve ortam no. | Eksik olgu veya karar | İstenecek maskelenmiş kanıt veya soru | Sorumlu taraf, hedef aşama ve devam koşulu |
| --- | --- | --- | --- | --- |
| E-001 · Aşama 4 | A-010 · 1, 2 ve 3 | Üç ortamdaki saklamayı kapsayan işleme şartı ve süre gerekçesi | Uygulanabilir hüküm ve amaç, başlangıç ve süre gerekçesi | KurguArşiv ve hukuk ekibi · Aşama 4 ve 6 · İşlem kapsamı doğrulanır. |
| E-002 · Aşama 6 | A-010 · 1 | Gizleme sonrası ilgili kullanıcı erişimi ve imha kaydı | Rol bazlı erişim ve yeniden kullanım kontrolü, maskelenmiş işlem kaydı | KurguArşiv uygulama ekibi · Aşama 6 · Ortama özgü kanıt sağlanır. |
| E-003 · Aşama 6 | A-010 · 2 | Yedek sona ermesi ve imha kaydı | Maskelenmiş sona erme ve imha işlem kaydı | KurguArşiv yedek ekibi · Aşama 6 · Yedek sona ermesi ve fiilî işlem doğrulanır. |
| E-004 · Aşama 6 | A-010 · 1, 2 ve 3 | Merkezî kanun metniyle güncellik karşılaştırması | İşlem tarihindeki merkezî metin ve varsa sektörel düzenleme | Hukuk ekibi · Aşama 6 · Kaynak sürümü doğrulanır. |
| E-005 · Aşama 6 | A-010 · 3 | Geri yükleme sonrası erişim kontrolü ve kopyanın imhası | Erişim prosedürü, maskelenmiş yetki gözlemi ve kopyanın imha kaydı | KurguArşiv yedek ve güvenlik ekibi · Aşama 6 · Erişim ve imha ayrı doğrulanır. |

## Hukuki kaynak kaydı

| Kaynak kimliği | Kaynak ve nitelik | Erişilen hüküm veya bölüm | Sürüm veya yürürlük | Erişim tarihi ve durumu | Güncellik ve açık kayıt |
| --- | --- | --- | --- | --- | --- |
| H-001 | [6698 sayılı Kanun · resmî kurum kopyası](https://ceyhansolsahil.gov.tr/wp-content/uploads/2025/08/1.5.6698.pdf) | m. 4/2-d, 7 ve 12 | RG 07.04.2016 · 29677 | 26.11.2026 · Kurum kopyası erişildi | Merkezî metinle güncellik karşılaştırması açık. E-004 |
| H-002 | [İmha Yönetmeliği · KVKK yayını](https://www.kvkk.gov.tr/Icerik/5441/KISISEL-VERILERIN-SILINMESI-YOK-EDILMESI-VEYA-ANONIM-HALE-GETIRILMESI-HAKKINDA-YONETMELIK) | m. 5, 7–12 | RG 28.10.2017 · 30224 | 26.11.2026 · Kurum yayınının indekslenen metni erişildi | Hukuk incelemesinde işlem tarihindeki sürüm kontrol edilir. |
| H-003 | [Kurumun teknik ve idari tedbirler rehberi](https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/7512d0d4-f345-41cb-bc5b-8d5cf125e3a1.pdf) | Yetki ve yedekleme bölümleri | Erişilen Kurum PDF’si | 26.11.2026 · PDF erişildi | Somut ortam ve risk için değerlendirme açık. E-003, E-005 |

## Hukukçu karar ve onay kaydı

| Karar tarihi, inceleyen ve belge | Faaliyet, kapsam ve ortam no. | Sonuç ve koşullar | Kanıt ve kaynak sürümleri |
| --- | --- | --- | --- |
