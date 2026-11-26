# Aşama 6 · Saklama, imha ve veri güvenliği raporu

Rapor niteliği: Hazırlık ve olgusal inceleme

27 Kasım 2026 revizyonlu sentetik KurguZiyaret örneği. Aşama 2’nin 22 Kasım pilot revizyonunu ve Aşama 3’ün Phase 1.6 raporunu kullanır. Aşama 4 ve 5 hazırlık notları yaşam döngüsü hakkında ilave dayanak sağlamıyor. [Aşama 2](../../stage-2/samples/manual-and-incomplete-stage-2.md) · [Aşama 3](../../stage-3/samples/phase-1.5-to-stage-3.md) · [Aşama 4](../../stage-4/samples/phase-1.5-stage-4-intake.md) · [Aşama 5](../../stage-5/samples/phase-1.5-stage-5-intake.md)

## Devir ve hazırlık

| Faaliyet ve kapsam | Operasyon, ortam veya kopya ve taraf | Aşama 2 kararı | Aşama 3 devir durumu | Esaslı incelemeye devir | Aşama 4 bağlantısı | Aşama 5 bağlantısı | İzin verilen hazırlık, engel ve devam koşulu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 · Faaliyetin tamamı | Saklama, erişim ve imha · Fiziksel defter · MaviOfis ve resepsiyon | Sınırlı devredilebilir | Kısıtlı / Bekletilir | Bekletilir | Saklama şartı açık | Varsa kopyalama ve alıcı açık | K-011’deki defter beyanını maskelenmiş sayfa, sınıflandırma, geçmiş kayda erişim ve düzenli kullanım kanıtıyla tamamla. m. 2 kapsamı ve esaslı devir açık. | K-011, K-033, E-002 |
| A-002 · Kiracı giriş kaydı | Saklama ve erişim · Teknik kayıt · Kiracı, KurguZiyaret ve Barınak | Bekletilir | Kısıtlı / Bekletilir | Bekletilir | Kişi bağlantısı ve saklama şartı açık | Üretim akışı açık | `visitRef` kişi bağlantısını, kiracı talimatını, Barınak’ın yetkisini ve üretim ortamındaki yaşam döngüsünü doğrula. | K-029, K-030, E-009 |
| A-002 · Belirsiz alıcıya yönlendirme | Erişim ve kopya · Yönlendirme izi · Gönderici ve belirsiz alıcı | Bekletilir | Kısıtlı / Bekletilir | Bekletilir | Kişi bağlantısı ve alıcı saklaması açık | Alıcı ve akış açık · E-016 | Gönderici yetkisi ve erişim olgusunu araştır. Alıcı kimliği, talimatı ve kopyanın saklama ve imhası için kanıt iste. | K-034, E-009, E-016 |
| A-004 · Faaliyetin tamamı | Erişim, saklama, yedek ve imha · Form, katılım deposu, kuyruk ve nöbetçi defteri · AlfaAtölye ve KurguPlatform | Sınırlı devredilebilir | Kısıtlı / Bekletilir | Bekletilir | Saklama şartı ve üretimde özel nitelik kapsamı açık | Sağlayıcı ve fiilî akış açık | K-025’teki tarih ve ziyaret koduyla düzenlenen nöbetçi defteri veri kayıt sistemi incelemesine dayanak sağlar. Dört ortamın fiilî uygulamasını ayrı iste. Sentetik `accessAccommodation` sağlık alanını üretim ve m. 6/4 kanıtı için açık tut. | K-024, K-025, K-026, K-028, E-011 |
| A-005 · Stüdyo ziyaret formu | Görsel saklama ve erişim · Form ve olası kopyalar · BetaStüdyo ve KurguPlatform | Sınırlı devredilebilir | Kısıtlı / Bekletilir | Bekletilir | Görsel işleme yöntemi ve saklama şartı açık | Fiilî erişim ve varsa sonraki alıcı açık | Görselin ortamını, erişen tarafı ve imha yolunu sor. Biyometrik nitelik için teknik işleme yöntemini ve benzersiz tanıma/doğrulama amacını araştır. | K-024, K-027, E-012 |
| A-005 · Olası kâğıt not | Erişim, saklama ve imha · Olası fiziksel not · BetaStüdyo | Sınırlı devredilebilir | Kısıtlı / Bekletilir | Bekletilir | Kâğıt kaydın kapsamı açık | Varlığı ve varsa gönderimi açık | Notun fiilî kullanımını, düzenini, aranabilirliğini, erişimini ve imhasını araştır. m. 2 kapsamını ve devir kararlarını yeni kanıtla değerlendir. | K-027, E-012 |

Tarihsel `A-003`, Aşama 2 revizyon geçmişine bağlıdır. `K-031` ve `E-013` altındaki bağımsız metrik bulgusu Aşama 2 incelemesindedir.

## Açık kayıtlar ve sonraki aşamaya devir

| Açık kayıt ve kaynak | Faaliyet, kapsam ve ortam no. | Eksik olgu veya karar | İstenecek maskelenmiş kanıt veya soru | Sorumlu taraf, hedef aşama ve devam koşulu |
| --- | --- | --- | --- | --- |
| E-002 · Aşama 2–3 | A-001 · Fiziksel defter | Defterin veri kayıt sistemi niteliği ve yaşam döngüsü | Düzen, arama, kopya, erişim ve imha süreci örneği | MaviOfis · Aşama 2–3 · Kapsam ve devir kararı güncellenir. |
| E-009 · Aşama 2–3 | A-002 · Kiracı giriş kaydı ve yönlendirme | Kişi bağlantısı ve üretim işleyişi | Maskelenmiş eşleme, yetki ve yaşam döngüsü kaydı | Kiracı ve teknik işletmeci · Aşama 2–3 · Kapsam ve rol bağı doğrulanır. |
| E-016 · Aşama 3 | A-002 · Belirsiz alıcıya yönlendirme | Alıcı ve kopya işlemi | Alıcı, talimat ve maskelenmiş kopya veya erişim kanıtı | KurguZiyaret · Aşama 3 ve 5 · Rol ve akış doğrulanır. |
| E-011 · Aşama 2–3 | A-004 · Fiziksel ve teknik ortam | Defter ve teknik kayıtlarda fiilî erişim, saklama ve imha | Ayrı fiziksel süreç kaydı ve maskelenmiş sistem kanıtı | AlfaAtölye ve KurguPlatform · Aşama 2–3 · Yaşam döngüsü kapsamı doğrulanır. |
| E-012 · Aşama 2–3 | A-005 · Form ve olası kâğıt not | Görsel işleme yöntemi, kâğıt kaydın kapsamı ve imha | Maskelenmiş form ve kayıt düzeni, erişim ve saklama adımları | BetaStüdyo · Aşama 2–4 · Ortam, rol ve veri niteliği açıklığa kavuşur. |

Esaslı inceleme satırı ve hukukçu karar kaydı açılmamıştır.
