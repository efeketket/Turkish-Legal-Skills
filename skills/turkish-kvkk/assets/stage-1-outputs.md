# Aşama 1 · İşletmenin ve faaliyetlerinin tanınması

- İnceleme kapsamı ve ortamı: …
- İnceleme tarihi ve incelenen sürüm veya belge tarihi (biliniyorsa): …

Bu yapıdaki bölüm başlıklarını, tablo sütunlarını ve durum etiketlerini Markdown raporunda aynen kullan. Her tablo kaydına `B-001`, `S-001`, `V-001`, `R-001`, `E-001` veya `K-001` örneklerindeki gibi benzersiz bir kimlik ver. Aynı kayıt tekrar kullanıldığında kimliğini koru. Bilgi eksikse ilgili hücrede durumu açıkça belirt ve bir `E-…` kaydına bağla. Uygulanmayan alanlarda `—` kullanabilirsin. Bir bölüm doldurulamıyorsa tablo başlığını koru ve `Açık kayıt: E-001` biçiminde ilgili kimliği göster. Açık bulunmadığında Eksik Bilgi ve Belge Listesi tablosunun altına `Açık kayıt yok.` yaz.

## İşletme Tanıma Dosyası

Hukuki kimliği ve organizasyonu, faaliyet alanlarını ve ülkeleri, ürün ve hizmetleri, müşteri ilişkilerini ve gelir modelini, dijital hizmetin işleyişini ve üçüncü taraf sağlayıcıları kapsam içinde kaydet.

| Kayıt | Konu | Tespit | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- |
| B-… | … | … | K-… | … |

## İş Süreçleri Haritası

| Süreç | Faaliyet ve operasyon adımları | İşletmeler ve sağlayıcılar | İlgili kişi grupları | Olası kişisel veri işlenmesi | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- |
| S-… | … | … | … | … | K-… | … |

## Ön Veri Akış Haritası

| Akış | Süreç | İlgili kişi grubu ve veri kategorisi | Verinin kaynağı | Kullanım ve sistem | Erişen taraf ve erişim noktası | Olası aktarım, alıcı ve konum | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V-… | S-… | … | … | … | … | … | K-… | … |

## Ön Hukuki Rol Tablosu

| Rol kaydı | Faaliyet ve bağlantılı süreç / akış | Taraf | Sözleşmedeki nitelendirme | Fiilî işleyişe ilişkin gözlem | Olası rol ve gerekçe | Kanıt kaydı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-… | S-… / V-… | … | … | … | … | K-… | … |

## Eksik Bilgi ve Belge Listesi

| Açık kayıt | Durum (eksik / çelişkili / doğrulanamadı) | İlgili kayıtlar | Hukuki önem ve gerekçesi | Soru veya talep edilen belge | Sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| E-… | … | … | … | … | … |

## Ortak Kanıt Kaydı

Kaynak türünü ve doğrulama durumunu ayrı yaz. Koddan ve yapılandırmadan elde edilen doğrudan gözlemleri sırasıyla `Doğrudan teknik gözlem / Kaynak kod` ve `Doğrudan teknik gözlem / Teknik yapılandırma` olarak belirt. İşletmenin veya kullanıcının doğrudan verdiği bilgiyi `İşletme beyanı`, dokümandaki beyanı `Belge` olarak kaydet. Doğrulama durumunu ve kanıtın sınırını `Doğrulandı — yalnızca test yapılandırması kapsamında` örneğindeki gibi yaz.

Dosya konumunu `Dosya: src/ornek.ts#L12-L16` örneğindeki gibi yaz. Tek satır için `#L12` yeterli. Yalnızca bir alıntı paylaşıldıysa inceleme kapsamında bunu belirt ve alıntının dosya başlığını ve alıntı içi satırlarını kullan. Maskelenen bir değere atıf yaparken dosya, satır, sembol veya belge bölümü gibi bir kaynak konumu bırak.

Süreç, akış ve rol satırlarında ilgili kanıt kimliklerine atıf yap. Çelişen kaynaklara ayrı `K-…` kimlikleri ver ve bunları aynı `E-…` kaydında ilişkilendir. Yeni bir kaynağa yeni kanıt kimliği ver, tarihini ve kapsamını kaydet. Açık kaydın kimliğini koru ve sonraki aşama notuna güncel durumu ve yeni kanıt bağlantısını ekle.

| Kanıt kaydı | Tespit veya iddia | Kaynak türü | Kaynak ve konum | Doğrulama durumu ve sınırı | Açık kayıt / sonraki aşama notu |
| --- | --- | --- | --- | --- | --- |
| K-… | … | … | … | … | … |

## Aşama Geçiş Değerlendirmesi

Bu değerlendirme Aşama 2'ye başlangıç eşiğidir. İşletme, süreçler, bilinen taraflar ve olası veri işleme alanları araştırmaya başlanabilecek kadar açık olmalıdır. Faaliyetlerin kesin sınırları ve fiilî kullanım Aşama 2'de araştırılır. Her ölçütü dayanağıyla değerlendir ve hangi açığın başlangıcı engellediğini gerekçede göster. `E-…` açılması ilgili inceleme ölçütünün sağlandığını tek başına göstermez.

| Geçiş ölçütü | Durum | Gerekçe ve ilgili kayıtlar |
| --- | --- | --- |
| Temel faaliyetler anlaşıldı | … | … |
| Kişisel veri işlenmesi muhtemel süreçler anlaşıldı | … | … |
| İlgili taraflar anlaşıldı | … | … |
| Veri akışının genel çerçevesi anlaşıldı | … | … |
| Kritik bilgi eksiklikleri kaydedildi ve sonraki aşamalar için işaretlendi | … | … |

- Geçiş durumu ve gerekçesi: …
- Açık kayıtlar ve sonraki aşamaya aktarılacak notlar: …

Geçiş değerlendirmesinde her ölçütün dayanak kayıtlarını göster. Açık kalan her `E-…` kimliğini aktarım notuna ekle. Genel durumu ve gerekçeyi `Değerlendirilemedi — işletme kimliği eksik (E-001)` örneğindeki gibi birlikte yaz. Sonradan değişen bir değerlendirmede önceki kararın tarihine ve dayanaklarına atıf yap.
