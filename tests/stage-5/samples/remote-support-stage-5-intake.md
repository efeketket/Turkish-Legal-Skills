# Aşama 5 KurguDestek erişim ve sonraki aktarım örneği

26 Kasım 2026 tarihli bağımsız sentetik örnek. Aşama 2 ve 3'ün aynı tarihli kısaltılmış rapor kayıtları `A-001` randevu desteği faaliyeti için aşağıdaki üç kapsamı Aşama 5'e devrediyor. Her kayıtta aktaran, alıcı, amaç, işlem ve veri kapsamı K-001, K-002 veya K-003 ile eşleşiyor. Aşama 4 raporundaki aday 1 yalnızca ilgili kişiden randevu bilgisinin toplanmasını ele alıyor. Kimlikler bu rapor zincirine ait.

## Sentetik kanıt

| Kanıt | Olgu ve sınır |
| --- | --- |
| K-001 | Kurgusal hizmet eki ve test ayarı, KurguDestek'in randevu saatini ve hesapla bağlantılı numarayı testte KurguSunucu'nun Türkiye bölgesine yazdığını gösteriyor. |
| K-002 | Kurgusal destek eki ve rol ayarı, Almanya'daki KurguYardım hesabına Türkiye örneğindeki iki test alanını görüntüleme yetkisi veriyor. Maskelenmiş sentetik olay, Almanya'dan bir görüntüleme gösteriyor. İndirme ve üretim kapsamı gözlenmedi. |
| K-003 | Kurgusal alt sağlayıcı eki ve sentetik iş izi, KurguYardım'ın destek kaydından hesap numarasını Hollanda'daki KurguBilet test örneğine gönderdiğini gösteriyor. İzin, güvence ve üretim akışı açık. |

## Devir ve hazırlık

| Faaliyet ve aktarım kapsamı | Aşama 2 kararı | Aşama 3 devir durumu | Esaslı incelemeye devir | Aşama 4 işleme şartı bağlantısı | Bilinen alıcı ve akış | Hazırlık işi, engel ve devam koşulu | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 · Türkiye barındırma | Devredilebilir · Aşama 5, kayıt yazımı · K-001 | Devredilebilir / Devredilebilir · KurguSunucu talimatla barındırıyor. | Devredilebilir | Aday 1 sadece toplamayı kapsıyor · Kapsam uyuşmuyor. | KurguSunucu, Türkiye'ye test yazımı. | Akışı haritala. Barındırıcıya aktarımın şartı için Aşama 4'e dön. | K-001, E-001 |
| A-001 · Almanya destek erişimi | Devredilebilir · Aşama 5, destek erişimi · K-002 | Devredilebilir / Devredilebilir · KurguYardım talimatla destek veriyor. | Devredilebilir | Eşleşen Aşama 4 kaydı yok. | KurguYardım, Türkiye'deki kayda Almanya'dan test erişimi. | Yetki ve erişimi haritala. Destek erişimini kapsayan Aşama 4 kaydını iste. | K-002, E-002 |
| A-001 · Hollanda destek kaydı | Devredilebilir · Aşama 5, alt sağlayıcı gönderimi · K-003 | Devredilebilir / Devredilebilir · KurguBilet, KurguYardım'ın alt sağlayıcısı. | Devredilebilir | Eşleşen Aşama 4 kaydı yok. | KurguYardım'dan KurguBilet'e test gönderimi. | Sonraki akışı ve güvence bağlantısını kaydet. Bu gönderim için Aşama 4 kaydı, ilk güvence şartları ve alt sağlayıcı izinlerini iste. | K-003, E-003, E-004 |

## Aktarım akışları

| Akış no. | Faaliyet ve aktarım kapsamı | Amaç, ilgili kişi, veri ve kişi bağlantısı | Aktaran ve rol | Alıcı ve rol | İletim veya erişim, ortam ve sıklık | Barındırma ülkesi | Erişim yetkisi ülkeleri | Erişim yetkisi | Fiilî erişim ülkeleri | Fiilî erişim ve indirme | Aktarım hedefi ve yön | Önceki akış no. | Mekanizma inceleme durumu | Kanıt, ortam sınırı ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A-001 · Türkiye barındırma | Randevu yönetimi, test müşteri hesabına bağlı numara ve saat. | KurguDestek · taslak veri sorumlusu | KurguSunucu · taslak veri işleyen | Sentetik kayıt yazımı, örnekte bir olay. | Türkiye | Belirsiz | Bu adımda uygulamanın yazma yetkisi gözlendi. | Belirsiz | Test yazımı görüldü. Destek erişimi ayrı akışta. | Türkiye · Yurt içi | — | Ek kanıt gerekli · Aşama 4 kapsamı uyuşmuyor. | K-001, E-001 · Test yazımı ve hizmet eki. |
| 2 | A-001 · Almanya destek erişimi | Destek, test müşteri hesabına bağlı numara ve saat. | KurguDestek · taslak veri sorumlusu | KurguYardım · taslak veri işleyen | Sentetik destek paneli, testte bir görüntüleme. Üretim sıklığı açık. | Türkiye | Almanya | Görüntüleme yetkisi, sentetik rol ayarı. | Almanya | Testte bir görüntüleme. İndirme belirsiz. | Almanya · Yurt dışından erişim | — | Ek kanıt gerekli · Aşama 4 bağlantısı eksik. | K-002, E-002 · Yetki ve test görüntüleme ayrı olgular. |
| 3 | A-001 · Hollanda destek kaydı | Destek kaydı oluşturma, test müşterisiyle bağlantılı hesap numarası. | KurguYardım · taslak veri işleyen | KurguBilet · taslak alt veri işleyen | Destek sisteminden sentetik kayıt gönderimi, testte bir olay. | Hollanda | Belirsiz | Gönderim için test iş yetkisi görüldü. Alıcı erişim kapsamı açık. | Belirsiz | Gönderim görüldü. Alıcı erişimi ve indirme belirsiz. | Hollanda · Sonraki yurt dışı aktarım | 2 | Ek kanıt gerekli · Aşama 4 bağlantısı ve güvence açık. | K-003, E-003, E-004 · Test gönderimi ve kurgusal ek. |

## Aktarım şartı ve mekanizma adayları

| Akış no. | Aday hüküm ve mekanizma | Aktarım için ileri sürülen işleme şartı | Aşama 4 kayıt kimliği ve kapsam eşleşmesi | Mekanizma koşulları ve kanıt sınırı | Hukuki kaynak | Taslak durum ve gerekçe | Açık kayıt ve istenecek kanıt |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Sonraki aktarım ve güvence bağlantısı

| İlk akış no. | Önceki akış no. | Sonraki akış no. | Önceki güvencedeki sonraki aktarım hükümleri | Sonraki akışın m. 9 yolu ve güvence kaydı | Alt sağlayıcı sözleşmesi, izin ve şartlar | Kanıt ve açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 2 | 3 | Akış 2 için sonraki aktarıma ilişkin imzalı güvence şartı sunulmadı. | Akış 3'ün kendi m. 9 yolu ve güvence kaydı açık. | K-003 alt sağlayıcı ilişkisini tanımlıyor. Uygulanabilir şart ve izin kanıtı bekleniyor. | K-003, E-003, E-004 |

## Açık kayıtlar

| Açık kayıt ve kaynak | Etkilenen faaliyet ve kapsam | İstenecek kanıt ve devam koşulu |
| --- | --- | --- |
| E-001 · Aşama 5 | A-001 · Türkiye barındırma | Toplama kaydının kapsamını koru. Aşama 4'te aynı alıcı ve işlem için değerlendirme iste. |
| E-002 · Aşama 5 | A-001 · Almanya destek erişimi | Destek erişimi için eşleşen Aşama 4 kaydı. Fiilî erişim ve indirmeye ilişkin maskelenmiş üretim kanıtı. |
| E-003 · Aşama 5 | A-001 · Hollanda destek kaydı | Alt sağlayıcıya gönderimi kapsayan Aşama 4 kaydı ve fiilî kapsam kanıtı. |
| E-004 · Aşama 5 | A-001 · Hollanda destek kaydı | Akış 2 için sonraki aktarım şartları, akış 3 için bağımsız güvence ve alt sağlayıcıya ilişkin izin dayanakları. |
