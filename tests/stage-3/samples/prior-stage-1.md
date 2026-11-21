# Aşama 1 · KurguZiyaret

- İnceleme kapsamı ve ortamı: Sentetik depo alıntıları ve görüşme
- İnceleme tarihi ve incelenen sürüm veya belge tarihi (biliniyorsa): Sürüm paylaşılmadı

## İşletme Tanıma Dosyası

| Kayıt | Konu | Tespit | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- |
| B-017 | İşletme ve iş modeli | KurguZiyaret A.Ş. Türkiye'deki ofislere abonelikle ziyaret yönetimi sunar. Ofis resepsiyon ekipleri girişleri yönetir. | K-004 | — |

## İş Süreçleri Haritası

| Süreç | Faaliyet ve operasyon adımları | İşletmeler ve sağlayıcılar | İlgili kişi grupları | Olası kişisel veri işlenmesi | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- |
| S-013 | Resepsiyonda giriş kaydı | Müşteri ofisinin resepsiyonu | Ziyaretçiler | Adın kâğıt deftere kaydedilmesi | K-011 | E-002 |
| S-028 | Ziyaret olayının kaydedilmesi | KurguZiyaret ve müşteri ofisi | Ziyaretçiler, anahtar ilişkisi doğrulanacak | Ziyaret referansı ve giriş zamanı | K-020 | E-009 |
| S-029 | Platformun kendi abonelik işlemleri | KurguZiyaret A.Ş. | Abone yetkilileri | Abonelik iletişimi araştırılacak | K-004 | — |

## Ön Veri Akış Haritası

| Akış | Süreç | İlgili kişi grubu ve veri kategorisi | Verinin kaynağı | Kullanım ve sistem | Erişen taraf ve erişim noktası | Olası aktarım, alıcı ve konum | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V-005 | S-013 | Ziyaretçiler, kimlik | Ziyaretçi beyanı | Resepsiyon defteri | Resepsiyon görevlisi kayıt açıyor | Bilinmiyor | K-011 | E-002 |
| V-018 | S-028 | Ziyaretçiler, ziyaret olayı | İşlev girdisi, üst kaynak belirsiz | Uygulama olay deposu | Bilinmiyor | Bilinmiyor | K-020 | E-009 |

## Ön Hukuki Rol Tablosu

| Rol kaydı | Faaliyet ve bağlantılı süreç / akış | Taraf | Sözleşmedeki nitelendirme | Fiilî işleyişe ilişkin gözlem | Olası rol ve gerekçe | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-006 | S-013 / V-005 | Müşteri ofisi | Paylaşılmadı | Resepsiyon kayıt işlemini yürüttüğünü belirtiyor | Ofisin kontrolü Aşama 3'te incelenecek | K-011 | E-002 |
| R-019 | S-028 / V-018 | KurguZiyaret ve müşteri ofisi | Paylaşılmadı | Uygulama kayıt işlevi var | Belirlenemedi | K-020 | E-009 |

## Eksik Bilgi ve Belge Listesi

| Açık kayıt | Durum (eksik / çelişkili / doğrulanamadı) | İlgili kayıtlar | Hukuki önem ve gerekçesi | Soru veya talep edilen belge | Sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| E-002 | doğrulanamadı | S-013, V-005, R-006, K-011 | Defterin erişimi ve imhası yaşam döngüsünü etkiler | Maskelenmiş erişim ve imha süreci açıklaması | Erişim ve imhayı izle |
| E-009 | eksik | S-028, V-018, R-019, K-020 | Kaynak, fiilî kullanım ve amaç bilinmiyor | Tetikleyici, iş akışı ve alan sözlüğü | Kaynak ve amaç araştırılacak |

## Ortak Kanıt Kaydı

| Kanıt kaydı | Tespit veya iddia | Kaynak türü | Kaynak ve konum | Doğrulama durumu ve sınırı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| K-004 | İş modeli ve taraflar | Belge | Dosya: README.md#L1 | Doğrulandı — paylaşılan README metni kapsamında | — |
| K-011 | Resepsiyon ziyaretçi adını kâğıt deftere kaydettiğini bildiriyor | İşletme beyanı | Sentetik görüşme, kâğıt defter | Kısmen doğrulandı — beyan alındı, fiziksel inceleme yapılmadı | E-002 |
| K-020 | İşlev ziyaret referansı ve giriş zamanını ekliyor | Doğrudan teknik gözlem / Kaynak kod | Dosya: src/events.ts#L1-L3 | Doğrulandı — kaynak kod alıntısındaki davranış kapsamında | E-009 |

## Aşama Geçiş Değerlendirmesi

| Geçiş ölçütü | Durum | Gerekçe ve ilgili kayıtlar |
| --- | --- | --- |
| Temel faaliyetler anlaşıldı | Karşılandı | Abonelik hizmeti tanımlı (B-017) |
| Kişisel veri işlenmesi muhtemel süreçler anlaşıldı | Karşılandı | Resepsiyon ve olay kaydı ayrı (S-013, S-028) |
| İlgili taraflar anlaşıldı | Karşılandı | Müşteri ofisi ve yazılım sağlayıcısı biliniyor (B-017, R-006, R-019) |
| Veri akışının genel çerçevesi anlaşıldı | Karşılandı | Defter ve olay deposu biliniyor (V-005, V-018) |
| Kritik bilgi eksiklikleri kaydedildi ve sonraki aşamalar için işaretlendi | Karşılandı | Yaşam döngüsü, kaynak ve amaç için takip kaydı var (E-002, E-009) |

- Geçiş durumu ve gerekçesi: Karşılandı. Temel işletme ve akış çerçevesi biliniyor (B-017, V-005, V-018).
- Açık kayıtlar ve sonraki aşamaya aktarılacak notlar: E-002 erişim ve imha bilgisi, E-009 kaynak ve amaç araştırılacak.
