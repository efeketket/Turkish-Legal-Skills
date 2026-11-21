# Aşama 2 · KurguZiyaret

- Rapor niteliği: Ön çalışma
- İnceleme kapsamı, işletmeler, ortamlar, tarih ve incelenen sürüm: KurguZiyaret ve müşteri ofisleri, görüşme ve sentetik alıntılar, 21 Kasım 2026, sürüm paylaşılmadı
- Aşama 1 raporu, tarihi ve geçiş sonucu: [KurguZiyaret Aşama 1 raporu](manual-and-incomplete-stage-1.md), tarih belirtilmedi, Karşılandı
- Aşama 2 başlangıç değerlendirmesi ve dayanak kayıtları: B-017, V-005 ve V-018 başlangıç için yeterli çerçeve sağlar. E-002 ve E-009 devredildi.
- Hukuki kapsam: Nihai roller, işleme şartları, aktarım, saklama, imha, güvenlik ve hukuki belgelerin uygunluk değerlendirmesi sonraki aşamalara devredilir.

## Kişisel Veri İşleme Faaliyetleri Envanteri

| Faaliyet | İşletme ve kapsam | Operasyonel işlev | Somut amaç özeti | Aşama 1 süreçleri | Ön akışlar ve roller | Doğrulama durumu ve sınırı | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | Müşteri ofisinin resepsiyonu | Kâğıt defterde giriş kaydı | Ziyaretçiyi tanıma ve bina erişimini yönetme | S-013 | V-005, R-006 | Kısmen doğrulandı — işletme beyanı mevcut, fiziksel inceleme yapılmadı | K-011 | E-002 |
| A-002 | KurguZiyaret uygulaması | Ziyaret olayının olay deposuna eklenmesi | Belirlenemedi | S-028 | V-018, R-019 | Doğrulanamadı — kod mevcut, fiilî kullanım açık | K-020, K-021 | E-009 |

## Kişisel Veri Kategorileri ve İlgili Kişi Grupları Matrisi

| Faaliyet | İlgili kişi grubu | Temel kategori ve varsa alt kategori | Veri alanı | Toplama kaynağı | Özel nitelik ve inceleme notu | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | Ziyaretçiler | Kimlik | Ziyaretçi adı | Doğrudan ziyaretçi beyanıyla | Alıntıda özel nitelik göstergesi yok | K-011 | — |
| A-002 | Olası ziyaretçiler | Müşteri İşlem / Ziyaret olayı | visitRef | İşlev girdisi, üst kaynak bilinmiyor | Gerçek kişiyle bağlantı doğrulanacak | K-020, K-021 | E-009 |
| A-002 | Olası ziyaretçiler | Müşteri İşlem / Ziyaret olayı | checkedInAt | İşlev girdisi, üst kaynak bilinmiyor | Gerçek kişiyle bağlantı doğrulanacak | K-020, K-021 | E-009 |

## Veri Akış ve Yaşam Döngüsü Haritası

| Faaliyet | Sıra ve yaşam döngüsü adımı | Veri alanı veya kategorisi | Kaynak ve hedef | Ortam, erişen grup veya alıcı | Fiilî saklama veya imha bilgisi | Doğrulama durumu ve sınırı | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | 1. Elde etme, kayıt ve girişte kullanım (V-005) | Ziyaretçi adı | Ziyaretçi → defter | Resepsiyon görevlisi, kâğıt defter | — | Kısmen doğrulandı — beyan kapsamında | K-011 | E-002 |
| A-001 | 2. Sonraki erişim, kopya, saklama ve imha | Ziyaretçi adı | Kâğıt defter, sonraki hedef bilinmiyor | Defterin diğer erişimleri ve varsa alıcısı bilinmiyor | Süre ve yöntem doğrulanmadı | Doğrulanamadı — fiziksel kayıt akışı incelenmedi | K-011 | E-002 |
| A-002 | 1. İşlevden depoya kayıt (V-018) | visitRef ve checkedInAt | İşlev girdisi → olay deposu | Kod alıntısı, gerçek ortam bilinmiyor | — | Doğrulandı — yalnızca kod içindeki kayıt çağrısı | K-020 | E-009 |
| A-002 | 2. Erişim, aktarım, yedekleme, saklama ve imha | visitRef ve checkedInAt | Olay deposu, sonraki yol bilinmiyor | Erişen ve alıcı bilinmiyor | Süre ve yöntem bilinmiyor | Doğrulanamadı — ilgili ortam bilgisi paylaşılmadı | — | E-009 |

## İşleme Amaçları Matrisi

| Faaliyet | İlgili kişi grubu | Veri alanı | Somut işleme amacı | Amaç durumu ve dayanak sınırı | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| A-001 | Ziyaretçiler | Ziyaretçi adı | Girişte ziyaretçiyi tanıma | Kısmen doğrulandı — beyan kapsamında | K-011 | — |
| A-001 | Ziyaretçiler | Ziyaretçi adı | Bina erişimini yönetme | Kısmen doğrulandı — beyan kapsamında | K-011 | — |
| A-002 | Olası ziyaretçiler | visitRef | Belirlenemedi | Doğrulanamadı — kayıt işlevinden somut amaç çıkarılamıyor | K-020 | E-009 |
| A-002 | Olası ziyaretçiler | checkedInAt | Belirlenemedi | Doğrulanamadı — kayıt işlevinden somut amaç çıkarılamıyor | K-020 | E-009 |

## Teknik Sistem ve İşleme Operasyonları Eşleştirme Tablosu

| Faaliyet | Sistem veya kayıt ortamı | Ortam | İşleme operasyonu | Doğrulama durumu ve sınırı | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- | --- | --- |
| A-001 | Kâğıt ziyaretçi defteri | Müşteri ofisinin resepsiyonu | Elde etme, yazma ve girişte kullanma | Kısmen doğrulandı — işletme beyanı | K-011 | E-002 |
| A-002 | Uygulama olay deposu | Kod alıntısı, üretim bilinmiyor | İşlev girdisinden olayı ekleme | Doğrulandı — kod içindeki kayıt çağrısı | K-020 | E-009 |

## Doğrulanamayan Faaliyetler ve Eksik Bilgiler Listesi

| Açık kayıt | İlgili kayıtlar | Durum | Eksik bilgi, çelişki veya gerekçeli düzeltme | Kanıt kaydı | Etki ve varsa engel | Soru, talep veya kapanış dayanağı | Sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E-002 | A-001, S-013, V-005, R-006 | Doğrulanamadı | Deftere erişim, kopyalama, saklama ve imha | K-011 | Yaşam döngüsünü ve erişim sınırını değerlendirmek için gerekli | Erişim grupları ve fiilî imha yöntemine ilişkin maskelenmiş açıklama | Aşama 6'ya erişim ve imha açığını aktar |
| E-009 | A-002, S-028, V-018, R-019 | Eksik | Üst kaynak, kişiyle bağlantı, fiilî kullanım ve amaç | K-020, K-021 | Amacı, işleme şartını ve temel akışı değerlendirmeyi etkiliyor | Alan sözlüğü, olay tetikleyicisi, iş amacı ve ilgili ortamdaki kullanım hakkında açıklama | Aşama 3 ve 4'e işlev ve amaç açığını, Aşama 5 ve 6'ya akış ve yaşam döngüsü açığını aktar |

## Aşama 1 Süreç Kapsamı

| Süreç | Faaliyetler | İnceleme sonucu ve gerekçe | Kanıt kaydı | Açık kayıt |
| --- | --- | --- | --- | --- |
| S-013 | A-001 | Kâğıt defter operasyonu beyana dayanıyor | K-011 | E-002 |
| S-028 | A-002 | Olay kaydı kodda tanımlı, fiilî kullanım açık | K-020, K-021 | E-009 |

## Ortak Kanıt Kaydı

| Kanıt kaydı | İlgili kayıtlar | Tespit veya iddia | Kaynak türü | Kaynak ve konum | Ortam ve tarih | Doğrulama durumu ve sınırı | Açık kayıt | Sonraki inceleme |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K-021 | A-002, S-028 | Şema açıklaması alan adlarını tanımlıyor, referansın bağlantısını vermiyor | Belge | Dosya: docs/event-schema.md#L1 | Sentetik belge, tarih bilinmiyor | Doğrulandı — paylaşılan dokümantasyon kapsamında | E-009 | Alanın gerçek kişiyle ilişkilendirilme şeklini sor |

## Aşama Geçiş Değerlendirmesi

| Geçiş ölçütü | Durum | Gerekçe ve ilgili kayıtlar | Eksik bilgiler | Devamı engelleyen hususlar | Sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| Aşama 1 iş süreçleri incelendi | Karşılandı | İki süreç gözden geçirildi (S-013, S-028) | — | — | Kapsamı koru |
| Önemli faaliyetler ayrı ve izlenebilir | Karşılandı | Fiziksel kayıt ve uygulama olayı ayrı işlevler (A-001, A-002) | E-009 | — | İkinci kaydın fiilî statüsünü incele |
| İlgili kişi grupları ve veri kategorileri tespit edildi veya eksikleri kaydedildi | Karşılandı | Ziyaretçiler işlendi, olay anahtarı için açık var (A-001, E-009) | E-009 | — | Kişiyle ilişkiyi doğrula |
| Veri kaynakları ve temel operasyonlar belirlendi | Değerlendirilemedi | Olay girdisinin üst kaynağı belirsiz (A-002, K-020) | E-009 | E-009 | Olay tetikleyicisini incele |
| Amaçlar somutlaştırıldı veya açıklığa kavuşturulacak hususlar kaydedildi | Karşılandı | Defter amaçları beyan edildi, olay amacı açık kayıtta (K-011, E-009) | E-009 | — | Olay amacını Aşama 4 için sor |
| Temel yaşam döngüsü aşamaları ortaya çıkarıldı | Değerlendirilemedi | İlk kayıtlar izleniyor, sonraki kullanım ve imha belirsiz (A-001, A-002) | E-002, E-009 | — | Yaşam döngüsü dayanağı iste |
| Manuel ve yazılım dışı faaliyetler incelemeye dahil edildi | Karşılandı | Defter işlemi kaydedildi (A-001, K-011) | E-002 | — | Fiziksel kayıt işleyişini incele |
| Teknik bulgular ile işletme beyanları arasındaki önemli çelişkiler belirlendi | Karşılandı | Paylaşılan kod ile beyan farklı kayıt ortamlarını anlatıyor (K-011, K-020) | — | — | — |
| Özel nitelikli veriler ve özel inceleme gerektiren faaliyetler işaretlendi | Karşılandı | Fiziksel kayıt sistemi ve belirsiz kişi bağlantısı takip için işaretlendi (A-001, A-002) | E-002, E-009 | — | Fiziksel kayıt sistemi ve kişi bağlantısı hakkında inceleme |
| Kritik eksiklikler ve etkileri açıklandı | Karşılandı | Kaynak ve amaç açığı ile yaşam döngüsü etkileri açıklandı (E-002, E-009) | E-002, E-009 | — | Açıkları devirde koru |
| Önceki kayıtlar ve kanıt bağlantıları korundu | Karşılandı | Süreç, akış, rol, kanıt ve açık bağlantıları korundu (S-013, S-028, V-005, V-018, R-006, R-019, K-011, K-020, E-002, E-009) | — | — | Aşama 1 raporunu kaynak olarak koru |

- Geçiş durumu ve gerekçesi: Değerlendirilemedi — olayın üst veri kaynağı ve yaşam döngüsü belirsiz (E-009, E-002).
- Açık kayıtlar ve sonraki aşamaya aktarılacak notlar: E-002 ve A-001 için Aşama 6'ya fiziksel kayıt, erişim ve imha. E-009 ve A-002 için Aşama 3'e ilgili taraflar, Aşama 4'e amaç, Aşama 5 ve 6'ya kaynak, akış ve yaşam döngüsü.
