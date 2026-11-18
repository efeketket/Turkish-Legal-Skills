# AŞAMA 1 — İŞLETMENİN VE FAALİYETLERİNİN TANINMASI

**Amaç**

KVKK incelemesine başlamadan önce işletmenin hukuki ve organizasyonel yapısını, iş modelini, sunduğu hizmetleri, operasyonel süreçlerini ve kişisel veri işlenmesiyle ilişkili faaliyetlerini anlamak.

**Uygulama talimatları**

1. İşletmenin hukuki kimliğini, organizasyon yapısını, faaliyet alanını ve faaliyet gösterdiği ülkeleri araştır.
2. İşletmenin sunduğu ürün ve hizmetleri, müşteri ilişkilerini ve gelir modelini belirle.
3. Yazılımın veya dijital hizmetin temel işlevlerini ve operasyonel işleyişini öğren.
4. Müşteri, kullanıcı, çalışan, tedarikçi ve diğer ilgili kişi gruplarını birbirinden ayır.
5. Kişisel veri işlenmesi muhtemel bütün iş süreçlerini belirle.
6. Verilerin elde edildiği kaynakları, kullanıldığı sistemleri, erişim noktalarını ve olası aktarım ilişkilerini araştır.
7. Bulut, barındırma, ödeme, mesajlaşma, analitik ve diğer üçüncü taraf hizmet sağlayıcılarını tespit et.
8. İşletmenin mevcut sözleşmelerini, politikalarını, prosedürlerini ve teknik belgelerini talep et.
9. Her işleme faaliyeti bakımından olası veri sorumlusu ve veri işleyen tarafları ön değerlendirmeye tabi tut.
10. Eksik, çelişkili veya doğrulanamayan bilgileri kaydet ve hukuki önemlerine göre sınıflandır.

**Temel kurallar**

- İşletmenin beyanlarını doğrulanmış olgu olarak kabul etme.
- Sözleşmelerdeki hukuki nitelendirmeleri fiilî uygulamayla karşılaştır.
- Aynı işletmenin farklı faaliyetlerinde farklı hukuki roller üstlenebileceğini dikkate al.
- İşletmenin bütün faaliyetlerini tek bir veri işleme faaliyeti olarak değerlendirme.
- Teknik sistemlerin işleyişini anlamadan kesin hukuki nitelendirme yapma.
- Eksik bilgileri varsayımla tamamlama.
- Hukuki değerlendirmeyi etkileyen eksikliklerde açıklayıcı sorular yönelt.
- Gerçek kişilere ait gereksiz kişisel verilerin inceleme ortamına aktarılmasını önle.

**Aşama çıktıları**

- İşletme Tanıma Dosyası
- İş Süreçleri Haritası
- Ön Veri Akış Haritası
- Ön Hukuki Rol Tablosu
- Eksik Bilgi ve Belge Listesi

**Aşama geçiş kriteri**

İşletmenin temel faaliyetleri, kişisel veri işlenmesi muhtemel süreçleri, ilgili tarafları ve veri akışının genel çerçevesi anlaşılmış olmalıdır.

Kritik bilgi eksiklikleri açıkça kaydedilmeli ve sonraki aşamalarda değerlendirilmek üzere işaretlenmelidir.

Bu aşamanın tamamlanması, işletmenin KVKK’ya uygun olduğunun veya aykırılık bulunduğunun tespiti anlamına gelmez.

## Ajanın uygulama adımları

1. **Erişilebilir kaynaklardan başla.** İncelenecek işletmeyi, ürünü ve ortamı mevcut girdilerden belirle. Bir depo varsa README ve mimari belgeleri, ilgili kaynak kodunu, şema ve migrasyonları, entegrasyon tanımlarını, bağımlılıkları, örnek yapılandırmayı ve dağıtım tanımlarını konuyla ilgili oldukları ölçüde incele. Erişilebilir maskelenmiş sözleşme, politika, prosedür ve teknik belgeleri de kullan. İşletmenin kimliği ve faaliyetleri için ilgili ve erişilebilir kayıtları incele.
2. **Salt okunur çalış.** İncelenen uygulama kodu, veritabanı, yapılandırma ve hukuki belgelerde her değişiklik için ayrı kullanıcı onayı gerekir. İnceleme için sentetik veya maskelenmiş örnekler ve veri kategorileri kullan. Gerçek kişilere ait gereksiz verileri, API anahtarlarını, erişim belirteçlerini, diğer sırları veya ham üretim kayıtlarını isteme ve çıktılara taşıma.
3. **Süreç ve kaynak bazında kayıt tut.** Her bulguyu mümkünse dosya ve satır, sembol, belge bölümü veya tanımlanabilir başka bir kaynakla ilişkilendir. Kaynak türü için `İşletme beyanı`, `Belge`, `Doğrudan teknik gözlem` veya `Teknik çıkarım` kullan. Doğrulama durumunu ayrıca `Doğrulandı`, `Kısmen doğrulandı`, `Doğrulanamadı` veya `Çelişkili` olarak yaz ve kanıtın neyi desteklediğini belirt. Depoda tanımlı bir davranışı kaynak kodu kapsamında kaydet. Üretimde fiilen çalıştığını doğrulamak için o ortama ilişkin kanıt gerekir. Çelişen kaynakları ayrı kanıt kayıtlarıyla göster ve aynı açık kayda bağla.
4. **Açıkları kaydet ve ön rolleri faaliyet bazında ele al.** Mevcut kaynakları inceledikten sonra hukuki değerlendirmeyi etkileyen açıklar için odaklı sorular sor veya gerekli sözleşmenin, politikanın, prosedürün ya da teknik belgenin maskelenmiş örneğini iste. Beyan veya belgenin doğrulanması gerekiyorsa eksik kanıtı ya da kapsam açıklamasını iste. Eldeki bilgiden ön çıktıları hazırla. Her açık için hukuki önemini ve gerekçesini kaydet ve kritik olanları işaretle. Rol tablosunda taraf başına sözleşmedeki nitelendirmeyi, fiilî işleyişe ilişkin kanıtı ve gerekçeli ön değerlendirmeyi göster. Dayanak yetersizse rolü `Belirlenemedi` olarak açık bırak. Her türlü kesin KVKK uygunluk veya aykırılık kararı ve nihai hukuki görüş Aşama 1 kapsamı dışındadır.

## Çıktı ve devir kaydı

[Markdown şablonunu](../assets/stage-1-outputs.md) doldur. Beş çıktıyı tek dosyada ayrı başlıklar altında tut. Böylece süreç, akış, rol ve açık kayıtları aynı kanıtları yeniden kopyalamadan referanslayabilir. Kapsamı, kanıt kaydını ve aşama geçiş değerlendirmesini de aynı dosyada sakla. Kullanıcı raporu başka bir konumda istiyorsa kayıt kimliklerini ve bağlantıları birlikte taşı.

- Her kayda benzersiz bir kimlik ver. Aynı bulgu tekrar kullanıldığında kanıt kimliğini koru. Kanıtı olmayan bilgiyi açık kayıtla ilişkilendir ve durumunu göster.
- Şablondaki her geçiş ölçütü için gerekçeyi ve kayıt kimliklerini yaz. Kanıt ölçütün sağlandığını gösteriyorsa `Karşılandı`, sağlanmadığını gösteriyorsa `Karşılanmadı`, eldeki bilgi karar için yetersizse `Değerlendirilemedi` yaz. Genel geçiş durumunu da açıkça yaz: tüm ölçütler karşılandıysa `Karşılandı`, bir ölçütün karşılanmadığı belirlenmişse `Karşılanmadı`, diğer durumlarda `Değerlendirilemedi`. Kritik açıkların işaretlenmesini ve sonraki aşamaya taşınmasını geçiş kaydında göster.
- Sonraki aşamaya kapsamı, ilgili süreç, akış ve rol kayıtlarını, bunların kaynak ve doğrulama durumlarını, açık kayıt kimliklerini ve takip notlarını aktar. Bilgi daha sonra doğrulanırsa mevcut kimliği koruyarak yeni kanıtı ve güncel durumu ekle.

## Hukukçu inceleme notları

- Metodoloji, eksik bilginin hukuki önemini sınıflandırmayı ve kritik açıkları işaretlemeyi öngörüyor. Hukuk ekibi, ortak önem seviyeleri veya farklı faaliyetlere özgü ölçütler gerekip gerekmediğini değerlendirmeli.
- Metodoloji, genel çerçeveyi anlamayı ve kritik açıkları sonraki aşamaya işaretlemeyi öngörüyor. Sınır durumlarında hangi kritik eksikliklerin geçiş kararını etkilediği hukuk ekibinin değerlendirmesine açık.
