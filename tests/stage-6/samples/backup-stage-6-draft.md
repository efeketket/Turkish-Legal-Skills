# Aşama 6 · Saklama, imha ve veri güvenliği raporu

Rapor niteliği: Sentetik metodoloji taslağı

27 Kasım 2026 revizyonlu sentetik KurguArşiv örneği. KurguArşiv, müşteri destek kayıtlarının veri sorumlusu ve kendi test ortamının işletmecisidir. Sentetik test olayları 26 Kasım 2026 tarihlidir. Kimlikler bu örnek zincirine aittir.

## Sentetik devir girdileri

| Kaynak | Faaliyet ve kapsam | Hedef ve karar | Gerekçe |
| --- | --- | --- | --- |
| Aşama 2 · 25.11.2026 | A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Aşama 6 · Devredilebilir | Talep numarası, kapanış zamanı, kişi bağlantısı, birincil kayıt, yedek ve geri yükleme hedefi sentetik envanterde kayıtlı. K-001, K-002 |
| Aşama 3 · 25.11.2026 | A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Aşama 6 · Devredilebilir | Süreyi ve erişimi KurguArşiv belirliyor. Uygulama ve yedek ekipleri aynı tüzel kişinin içinde. K-001, K-002 |
| Aşama 4 · 25.11.2026 | A-010 · Destek talebinin toplanması | Aday kaydı · Kapsam açık | Aynı destek amacı için toplama adımı incelenmiş. Saklama, yedek ve geri yükleme bağlantısı açık. E-001 |
| Aşama 2 · 27.11.2026 | A-010 · Olası sağlayıcı arşivi | Aşama 6 · Sınırlı devredilebilir | Planlanan kopyanın varlığı ve veri kapsamı araştırılabilir. K-005, E-006 |
| Aşama 3 · 27.11.2026 | A-010 · Olası sağlayıcı arşivi | Aşama 6 · Kısıtlı / Bekletilir | Sağlayıcı kimliği, rolü ve talimatı için hazırlık yapılabilir. K-005, E-006 |

## Kanıt kaydı

| Kanıt kimliği | Kaynak veya konum | Tarih veya sürüm | Kanıt türü ve ortam | Gösterdiği olgu ve sınırı |
| --- | --- | --- | --- | --- |
| K-001 | KurguArşiv saklama politikası taslağı ve rol matrisi | 25.11.2026 · Politika v2 | Politika beyanı ve rol belgesi · Sentetik | Kapanıştan 30 gün sonra silme beyanı ve yedek erişimi için yetki matrisi. Mevzuat dayanağı ve fiilî uygulama açık. |
| K-002 | Test yapılandırma ve topoloji özeti | 25.11.2026 | Yapılandırma ve altyapı belgesi · Sentetik test | Kapanıştan 90 gün sonra arayüzde gizleme ayarı ve 14 gün yedek saklama ayarı. Üç ortam da KurguArşiv’e ait kapalı altyapıda. Topoloji, hedefler ve hesap özeti dış sağlayıcı, alıcı ve uzaktan destek adımı içermiyor. Üretim, fiilî süre ve yedek sona ermesi kapsam dışında. |
| K-003 | Maskelenmiş test olayı | 26.11.2026 | Erişim gözlemi · Sentetik test | Eski sentetik kayıt arayüzde görünmüyor. Yönetim görünümünde aynı kayıt okunabiliyor. Diğer erişim yolları incelenmedi. |
| K-004 | Maskelenmiş geri yükleme tatbikatı | 26.11.2026 | Geri yükleme ve rol bazlı gözlem · Sentetik test | Önceki yedek ayrı bir test ortamına geri yüklendi. Standart destek rolü kayıt numarasını yeniden görüntüledi. Üretim, yedek sona ermesi ve sonraki imha incelenmedi. |
| K-005 | Sentetik mimari seçenek notu | 27.11.2026 | Tasarım beyanı · Üretim için seçenek | Dış arşiv hizmeti düşünülüyor. Sağlayıcı, ülke, erişim ve kopyanın fiilen oluştuğu açık. |

## Devir ve hazırlık

| Faaliyet ve kapsam | Operasyon, ortam veya kopya ve taraf | Aşama 2 kararı | Aşama 3 devir durumu | Esaslı incelemeye devir | Aşama 4 bağlantısı | Aşama 5 bağlantısı | İzin verilen hazırlık, engel ve devam koşulu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-010 · Destek kaydının test veritabanında saklanması, kurum içi yedeği ve geri yüklenmesi | Saklama, yedek ve geri yükleme · Ortam 1, 2 ve 3 · KurguArşiv | Devredilebilir | Devredilebilir | Devredilebilir · Sentetik metodoloji kapsamı | Toplama kaydı · Saklama ve yedek kapsamı açık · E-001 | Uygulanmaz · K-002’de belgelenen kapalı test altyapısı ve üç kurum içi ortam | Saklama işlemi için eşleşen dayanağı iste. Görünürlük ve geri yükleme bulgularını ilgili test ortamıyla sınırla. | K-001, K-002, K-003, K-004, E-001 |
| A-010 · Olası sağlayıcı arşivi | Olası dış kopya ve erişim · Üretim tasarımı · Sağlayıcı belirsiz | Sınırlı devredilebilir | Kısıtlı / Bekletilir | Bekletilir | Arşiv işlemi ve şartı açık · E-006 | Sağlayıcı, akış, ülke ve erişim açık · E-006 | Mimari seçenek için fiilî kopya, sağlayıcı, rol, talimat ve Aşama 5 akış kaydı iste. Kurum içi test kapsamı kendi kayıtlarıyla sürer. | K-005, E-006 |

## Saklama ve kopyalar

| Ortam no. | Faaliyet ve operasyon | Kayıt ortamı ve kopya | Karar, uygulama ve sağlayıcı tarafı | Veri, ilgili kişi ve amaç | Başlangıç ve bitiş olayı, tarihler | Süre hesabı ve hukuki dayanak kaydı | Politika beyanı | Yapılandırılan süre | Fiilî saklama ve ortam | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A-010 · Birincil kayıt | Test veritabanı | KurguArşiv karar ve uygulama · Kurum içi | Talep no. ve kapanış zamanı · Destek talebi sahibi · Talep takibi | Başlangıç olarak talep kapanışı beyan edilmiş. Fiilî bitiş ve kapanış tarihi açık. | İki süre farklı işlemleri anlatıyor. Saklama dayanağı E-001’de açık. | Kapanıştan 30 gün sonra silme | Kapanıştan 90 gün sonra arayüzde gizleme | Tek sentetik olayda gizlenen kayıt yönetim görünümünde mevcut. Fiilî toplam süre açık. | Kısmen doğrulandı · K-001, K-002, K-003, E-001, E-002 |
| 2 | A-010 · Kurum içi yedek | Test yedeği | KurguArşiv karar ve uygulama · Kurum içi | Aynı alanlar ve kişi grubu · Hizmeti geri yükleme | Yedek oluşturma olası başlangıç. Oluşturma zamanı, ayarın başlangıç olayı ve bitiş açık. | Ayarın hesabı ve süre gerekçesi E-001 ve E-003’te açık. | Yedek süresine ilişkin beyan yok | 14 günlük test yedeği | Yedek, geri yükleme tatbikatında kullanıldı. Yedek sona ermesi açık. | Kısmen doğrulandı · K-002, K-004, E-001, E-003 |
| 3 | A-010 · Geri yüklenen kopya | 2 no.lu yedekten oluşturulan ayrı test kopyası | KurguArşiv karar ve uygulama · Kurum içi | Aynı alanlar ve kişi grubu · Geri yükleme tatbikatı | Geri yükleme 26.11.2026. Kopyanın bitişi açık. | Ayrı süre ve dayanak E-001 ve E-005’te açık. | Geri yüklenen kopyanın süresine ilişkin beyan yok | Süre ayarı açık | Kayıt geri yükleme sırasında gözlendi. Sonraki saklama açık. | Kısmen doğrulandı · K-004, E-001, E-005 |

## Sicil ve saklama-imha politikası

| Veri sorumlusu | Sicil ve politika yükümlülüğü, dayanak | Politika sürümü, onay ve kapsam | Periyodik imha aralığı ve sorumlu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- |
| KurguArşiv | Sicil yükümlülüğü ve varsa istisna açık · H-002 | v2 taslak · 1 no.lu ortam için beyan var. Onay ve diğer ortamlar açık. | Belgelenmiş periyodik takvim ve sorumlu açık. | K-001, E-007 |

## Resen imha ve ilgili kişi talebi

| Ortam no. ve yol | Tetikleyici veya başvuru, tarih | Uygulanacak süre ve son tarih | Fiilî işlem ve tarih | Karar, yanıt ve teslim | Üçüncü kişi bildirimi ve işlemi | Hukuki kaynak, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| 1, 2 ve 3 · Resen | İşleme şartlarının sona erdiği olay ve tarih açık. | İlk periyodik imha veya üç aylık yolun uygulanabilirliği ve son tarih açık. | İmha uygulaması açık. Ortam kayıtlarına bak. | — · Talep yolu ayrı kayıt | — · Bu satır resen yol içindir | H-002, K-001, E-001, E-007 |
| 1, 2 ve 3 · İlgili kişi talebi · Hazırlık | Örnek kapsamında başvuru kaydı sunulmadı. | m. 12’deki en geç 30 günlük süre. Başvuru tarihi olmadığından somut son tarih açık. | Talebe bağlı işlem açık. | Kabul veya ret, yanıt ve teslim için ayrı kanıt istenir. | Belgelenen kapalı test için dış alıcı uygulanmaz. Olası sağlayıcı kapsamı ayrı bekletilir. | H-002, K-002, E-006, E-008 |

## İmha ve doğrulama

| Ortam no. | Tetikleyici, tarih ve uygulanacak süre | Yöntem ve uygulayan taraf | Fiilî işlem ve tarihi | Erişim, yeniden kullanım veya geri yükleme kanıtı | İmha kaydı ve kayıt süresi | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Kapanış politikada geçiyor. İmha yükümlülüğünün doğduğu tarih açık. | KurguArşiv’in uygulamasında arayüzde gizleme | 26.11.2026 testinde görünürlük değişti. | Yönetim görünümünde kayıt erişilebilir. Yönetim rolünün ilgili kullanıcı niteliği ve diğer erişim yolları açık. | Ayrı imha kaydı ve süresi açık. | Doğrulandı · Yalnız testteki görünürlük ve erişim olgusu · K-003, E-002 |
| 2 | 14 günlük ayarın başlangıç olayı ve imha yükümlülüğü tarihi açık. | KurguArşiv’in yedek sona erme işlemi | Sona erme açık. | 26.11.2026 testinde yedekten 3 no.lu kopya oluşturuldu. | Yedek imha işlem kaydı ve süresi açık. | Kısmen doğrulandı · K-002, K-004, E-003 |
| 3 | Tatbikat sonrasındaki işlem ve yükümlülük tarihi açık. | Yöntem açık · KurguArşiv | İmha gözlenmedi. | Standart destek rolü 26.11.2026 tarihinde test kopyasında kayıt numarasını yeniden gördü. | Geri yüklenen kopyanın imha kaydı ve süresi açık. | Kısmen doğrulandı · K-004, E-005 |

## Teknik ve idari tedbirler

| Ortam no. | Risk, veri ve olası etki | Teknik veya idari tedbir | Uygulayan ve denetleyen taraf | Politika, talimat veya yapılandırma | Fiilî uygulama ve sınırı | Denetim kanıtı | Kalan risk ve izlenecek iş | Olgusal durum, kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | Geri yüklenen talep numarasının destek rolüne yeniden açılması | Kullanıma açmadan önce yetki ve imha kontrolü | KurguArşiv yedek ekibi · Güvenlik sorumlusu | K-001 yedek erişim matrisi. Geri yüklenen kopya için talimat açık. | K-004’te standart destek rolü test kopyasına erişti. Üretim gözlenmedi. | Denetim kaydı açık. | Geri dönen kaydın yeniden erişim riski. Kontrol uygulaması ve kopya imhası için kanıt iste. | Kısmen doğrulandı · K-001, K-004, E-005 |

## Taslak değerlendirme

| Faaliyet, kapsam ve ortam no. | İncelenen konu | Hukuki kaynak | Olgusal dayanak ve sınırı | Durum, gerekçe ve açık kayıt |
| --- | --- | --- | --- | --- |
| A-010 · 1, 2 ve 3 | Saklama dayanağı ve imha yükümlülüğünün doğduğu tarih | H-001, H-002, H-004, H-005, H-006 | Toplama kaydı mevcut. 30 günlük silme beyanı ile 90 günlük gizleme ayarı arasındaki uygulama farkı açıklama bekliyor. 14 gün yedek ayarına ait. | Ek kanıt gerekli · Her ortamın saklama dayanağı, politika kapsamı ve merkezî metin karşılaştırması açık. E-001, E-002, E-004, E-007 |
| A-010 · 1 | Arayüzde gizleme ve erişim | H-002 | Yönetim görünümünde test kaydına erişim gözlendi. Arayüzdeki görünürlük değişikliği gözlenen olgudur. | Ek kanıt gerekli · Yönetim rolünün ilgili kullanıcı niteliği, diğer erişim yolları, yeniden kullanım ve imha kaydı açık. E-002 |
| A-010 · 2 | Yedek sona ermesi | H-002, H-003 | Yedekten geri yükleme gerçekleşti. Yedek sona ermesi ve üretim gözlenmedi. | Ek kanıt gerekli · Sona erme ve imha kanıtı açık. E-003 |
| A-010 · 3 | Geri yükleme sonrası erişim ve imha | H-002, H-003 | Testte destek rolü kayda erişebildi. Kopyanın sonraki imhası ve üretim gözlenmedi. | Ek kanıt gerekli · Geri yükleme sonrası kontrol ve kopyanın imhası açık. E-005 |

## Açık kayıtlar ve sonraki aşamaya devir

| Açık kayıt ve kaynak | Faaliyet, kapsam ve ortam no. | Eksik olgu veya karar | İstenecek maskelenmiş kanıt veya soru | Sorumlu taraf, hedef aşama ve devam koşulu |
| --- | --- | --- | --- | --- |
| E-001 · Aşama 4 | A-010 · 1, 2 ve 3 | Üç ortamdaki saklamayı kapsayan işleme şartı ve süre gerekçesi | Uygulanabilir hüküm ve amaç, başlangıç ve süre gerekçesi | KurguArşiv ve hukuk ekibi · Aşama 4 ve 6 · İşlem kapsamı doğrulanır. |
| E-002 · Aşama 6 | A-010 · 1 | Gizleme sonrası ilgili kullanıcı erişimi ve imha kaydı | Rol bazlı erişim ve yeniden kullanım kontrolü, maskelenmiş işlem kaydı | KurguArşiv uygulama ekibi · Aşama 6 · Ortama özgü kanıt sağlanır. |
| E-003 · Aşama 6 | A-010 · 2 | Yedek sona ermesi ve imha kaydı | Maskelenmiş sona erme ve imha işlem kaydı | KurguArşiv yedek ekibi · Aşama 6 · Yedek sona ermesi ve fiilî işlem doğrulanır. |
| E-004 · Aşama 6 | A-010 · 1, 2 ve 3 | H-001, H-004 ve H-005 ile sınırlı karşılaştırma yapıldı. Merkezî metin 27.11.2026’da zaman aşımına uğradı · H-007. | 26.11.2026 işlem tarihindeki merkezî metni ve varsa sektörel düzenlemeyi doğrula. | Hukuk ekibi · Aşama 6 · İşlem tarihindeki kaynak sürümü doğrulanır. |
| E-005 · Aşama 6 | A-010 · 3 | Geri yükleme sonrası erişim kontrolü ve kopyanın imhası | Erişim prosedürü, maskelenmiş yetki gözlemi ve kopyanın imha kaydı | KurguArşiv yedek ve güvenlik ekibi · Aşama 6 · Erişim ve imha ayrı doğrulanır. |
| E-006 · Aşama 2–3 ve 5 | A-010 · Olası sağlayıcı arşivi | Üretimdeki sağlayıcı, kopya, rol, ülke ve fiilî akış | Maskelenmiş üretim mimarisi, sözleşme, erişim özeti ve Aşama 5 akış kaydı | KurguArşiv · Aşama 2–5 · Yalnız sağlayıcı arşivi için gerekçeli eşleşen karar ve akış aranır. |
| E-007 · Aşama 6 | A-010 · 1, 2 ve 3 | Sicil ve politika yükümlülüğü ile resen imha takvimi | Sicil veya istisna dayanağı, onaylı politika, kapsam, takvim ve sorumlular | KurguArşiv · Aşama 6 · Uygulanacak yol ve takvim doğrulanır. |
| E-008 · Aşama 6 | A-010 · 1, 2 ve 3 | Talep süreci ve varsa uygulama kaydı | Prosedür ve varsa maskelenmiş başvuru, karar, yanıt ve teslim kayıtları | KurguArşiv · Aşama 7 · Talep ve takip belgeleri incelenir. |

## Hukuki kaynak kaydı

| Kaynak kimliği | Kaynak ve nitelik | Erişilen hüküm veya bölüm | Sürüm veya yürürlük | Erişim tarihi ve durumu | Güncellik ve açık kayıt |
| --- | --- | --- | --- | --- | --- |
| H-001 | [6698 sayılı Kanun · resmî kurum kopyası](https://ceyhansolsahil.gov.tr/wp-content/uploads/2025/08/1.5.6698.pdf) | m. 4/2-d, 7 ve 12 | RG 07.04.2016 · 29677 · Kopyada 7499 değişiklikleri var | 27.11.2026 · Kurum kopyası erişildi | Bu hükümlerin içeriği H-004 ile örtüşüyor. Merkezî güncellik açık. E-004 |
| H-002 | [İmha Yönetmeliği · KVKK yayını](https://www.kvkk.gov.tr/Icerik/5441/KISISEL-VERILERIN-SILINMESI-YOK-EDILMESI-VEYA-ANONIM-HALE-GETIRILMESI-HAKKINDA-YONETMELIK) | m. 4–12 ve 14 | RG 28.10.2017 · 30224 · Yürürlük 01.01.2018 · 28.04.2019 değişikliği H-006 | 27.11.2026 · Kurum yayınının indekslenen metni erişildi | İşlem tarihindeki kapsam ve varsa sektörel düzenleme E-004’te açık. |
| H-003 | [Kurumun teknik ve idari tedbirler rehberi](https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/7512d0d4-f345-41cb-bc5b-8d5cf125e3a1.pdf) | Yetki ve yedekleme bölümleri | Erişilen Kurum PDF’si | 26.11.2026 · PDF erişildi | Somut ortam ve risk için değerlendirme açık. E-003, E-005 |
| H-004 | [6698 sayılı Kanun · TBMM kabul metni](https://cdn.tbmm.gov.tr/KKBSPublicFile/D26/Y1/T1/KanunMetni/49b3460d-3d92-413d-9a12-555cfa749b1f.html) | m. 4/2-d, 7 ve 12 | Kabul 24.03.2016 · Özgün metin | 27.11.2026 · HTML erişildi | H-001’in belirtilen hükümleriyle karşılaştırıldı. Sonraki değişiklik için H-005, merkezî sürüm için H-007. |
| H-005 | [7499 sayılı Kanun · TBMM kabul metni](https://cdn.tbmm.gov.tr/KKBSPublicFile/D28/Y2/KanunMetni/48c107c3-a4dc-468e-bcf2-f7c8c24af1b0.htm) | m. 33–36 ve 40 | RG 12.03.2024 · 32487 · m. 33–36 yürürlük 01.06.2024 | 27.11.2026 · HTML erişildi | Bu değişiklikler m. 6, 9, 18 ve geçici m. 3’e ilişkin. H-001’de bu örnekte kullanılan m. 4/2-d, 7 ve 12 için merkezî sürüm kontrolü açık. |
| H-006 | [İmha Yönetmeliği değişikliği · Kurum duyurusu](https://www.kvkk.gov.tr/Icerik/5444/28-4-2019-tarih-ve-30758-sayili-Resmi-Gazete-de-Yayinlanan-Mevzuat-Degisiklikleri) | Yönetmelik değişikliğinin yayımı · H-002’deki m. 7/4 ve 12/1 notu | RG 28.04.2019 · 30758 | 27.11.2026 · Kurum duyurusunun indekslenen metni erişildi | Değişiklik yayımı kaydedildi. |
| H-007 | [Merkezî Mevzuat Bilgi Sistemi · 6698 sayılı Kanun](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6698.pdf) | m. 4/2-d, 7 ve 12 kontrol edilmek istendi | Sürüm erişim bekliyor | 27.11.2026 · Zaman aşımı | Merkezî metinle karşılaştırma tamamlanmadı. E-004 |

## Hukukçu karar ve onay kaydı

| Karar tarihi | Kararı veren hukukçu veya görevi | Faaliyet, alt kapsam ve ortam no. | Karar belgesi ve incelenen sürümler | K/E/H dayanakları, tarih veya sürüm | Gerekçe | Sonuç, koşullar ve kapsam sınırı | Yeniden değerlendirme olayı |
| --- | --- | --- | --- | --- | --- | --- | --- |
