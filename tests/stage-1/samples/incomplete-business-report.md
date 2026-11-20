# Aşama 1 · KutuPanel

- İnceleme kapsamı ve ortamı: Sentetik prototip ve depo alıntıları
- İnceleme tarihi ve incelenen sürüm veya belge tarihi (biliniyorsa): Sürüm bilgisi paylaşılmadı

## İşletme Tanıma Dosyası

| Kayıt | Konu | Tespit | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- |
| B-001 | İşletme kimliği ve gelir modeli | Bilinmiyor | K-001 | E-001 |

## İş Süreçleri Haritası

| Süreç | Faaliyet ve operasyon adımları | İşletmeler ve sağlayıcılar | İlgili kişi grupları | Olası kişisel veri işlenmesi | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- |
| S-001 | CSV ayrıştırma ve satır sayma | Bilinmiyor | Bilinmiyor | Bilinmiyor | K-002 / K-003 | E-001 / E-002 |

## Ön Veri Akış Haritası

| Akış | Süreç | İlgili kişi grubu ve veri kategorisi | Verinin kaynağı | Kullanım ve sistem | Erişen taraf ve erişim noktası | Olası aktarım, alıcı ve konum | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V-001 | S-001 | Bilinmiyor | İstek gövdesindeki CSV | Prototipte CSV ayrıştırma, yanıtta satır sayısı | `/preview` uç noktası, erişen taraf bilinmiyor | Bilinmiyor | K-002 / K-003 | E-002 |

## Ön Hukuki Rol Tablosu

| Rol kaydı | Faaliyet ve bağlantılı süreç / akış | Taraf | Sözleşmedeki nitelendirme | Fiilî işleyişe ilişkin gözlem | Olası rol ve gerekçe | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | S-001 / V-001 | Bilinmiyor | Bilinmiyor | Prototip CSV içe aktarma ve sayma işlevi gösteriyor | Belirlenemedi | K-002 / K-003 | E-001 / E-002 |

## Eksik Bilgi ve Belge Listesi

| Açık kayıt | Durum (eksik / çelişkili / doğrulanamadı) | İlgili kayıtlar | Hukuki önem ve gerekçesi | Soru veya talep edilen belge | Sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| E-001 | eksik | B-001 / S-001 / R-001 / K-001 | Kritik, faaliyet kapsamı ve rol değerlendirmesini etkiler | Prototipi kim işletiyor? Hedef kullanıcılar ve gelir modeli nedir? | İşletme bilgilerini takip et |
| E-002 | eksik | S-001 / V-001 / R-001 / K-002 / K-003 | Kritik, girdi kapsamını ve akışı etkiler | Maskelenmiş sütun şeması ve erişim açıklaması paylaşılabilir mi? | Veri kategorileri ve erişim kapsamını takip et |

## Ortak Kanıt Kaydı

| Kanıt kaydı | Tespit veya iddia | Kaynak türü | Kaynak ve konum | Doğrulama durumu ve sınırı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| K-001 | Prototipin amacı tanımlı, işletme bilgileri açıklanmamış | Belge | Dosya: README.md#L1 | Doğrulandı — README metni kapsamında | E-001 |
| K-002 | CSV satırları ayrıştırılır ve sayılır | Doğrudan teknik gözlem / Kaynak kod | Dosya: src/import.ts#L1-L4 | Doğrulandı — sağlanan fonksiyon alıntısı kapsamında | E-002 |
| K-003 | Uç nokta CSV girdisinden satır sayısı yanıtı döndürür | Doğrudan teknik gözlem / Kaynak kod | Dosya: src/index.ts#L1-L3 | Doğrulandı — sağlanan uç nokta alıntısı kapsamında | E-002 |

## Aşama Geçiş Değerlendirmesi

| Geçiş ölçütü | Durum | Gerekçe ve ilgili kayıtlar |
| --- | --- | --- |
| Temel faaliyetler anlaşıldı | Değerlendirilemedi | Prototip işlevi biliniyor, işletme kapsamı açık (B-001, E-001) |
| Kişisel veri işlenmesi muhtemel süreçler anlaşıldı | Değerlendirilemedi | CSV sütunları ve kişi grupları bilinmiyor (S-001, E-002) |
| İlgili taraflar anlaşıldı | Değerlendirilemedi | İşletmeci ve ilgili taraflar açıklanmadı (R-001, E-001) |
| Veri akışının genel çerçevesi anlaşıldı | Değerlendirilemedi | Girdi ve yanıt görüldü, gerçek veri kategorileri ve erişim açık (V-001, E-002) |
| Kritik bilgi eksiklikleri kaydedildi ve sonraki aşamalar için işaretlendi | Karşılandı | İki kritik açık işaretlendi (E-001 ve E-002) |

- Geçiş durumu ve gerekçesi: Değerlendirilemedi — işletme ve veri akışı bilgileri bekleniyor (E-001 ve E-002).
- Açık kayıtlar ve sonraki aşamaya aktarılacak notlar: E-001 işletme kapsamı ve E-002 CSV kategorileri takip edilecek.
