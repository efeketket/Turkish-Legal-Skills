TURKISH-LEGAL-SKILLS

Aşama 6 – Saklama, İmha ve Veri Güvenliği

Geliştirme Ekibi İçin Hukuki İnceleme ve Düzeltme Raporu

İncelenen sürüm: turkish-kvkk 0.8.0
İnceleme kapsamı: Aşama 6 – Saklama, imha ve veri güvenliği
İnceleme tarihi: 27 Kasım 2026
Genel sonuç: DÜZELTME GEREKLİ

⸻

1. Genel değerlendirme

Aşama 6’nın mevcut metodolojik yapısı, önceki aşamalardan devralınan faaliyet ve taraf kapsamını koruması, kanıt ile hukuki değerlendirmeyi birbirinden ayırması ve gerçek dosyada henüz kesin hukuki sonuç üretmemesi bakımından genel olarak doğru yöndedir.

Özellikle şu yaklaşım ve kontroller korunmalıdır:

* Aşama 2 ve Aşama 3’ten aynı faaliyet ve kapsam için açık, gerekçeli devir kararı aranması.
* Sınırlı devredilebilir kararının yalnızca hazırlık ve olgusal incelemeye izin vermesi.
* Bekletilir kararının yeni kanıt geldi diye kendiliğinden kaldırılmaması.
* Test ortamındaki bulguların üretim ortamına ilişkin kesin kanıt sayılmaması.
* Saklama süresi, sistem ayarı, kullanıcı arayüzünde gizleme ve fiilî silme işlemlerinin birbirinden ayrılması.
* Veri sorumlusunun ve veri işleyenin görevlerinin somut işlem ve kanıtlarla incelenmesi.
* Gerçek dosyada eksik olguların ve kanıt sınırlarının açıkça gösterilmesi.

Bununla birlikte, Kişisel Verileri Silme, Yok Etme veya Anonim Hâle Getirme Yönetmeliği’nin 7. maddesinin 5. fıkrasındaki yöntem seçimi ve gerekçelendirme yükümlülüğünün metodolojiye açık biçimde eklenmesi gerekmektedir. Ayrıca kaynak doğrulama kaydında tamamlanmamış bir husus bulunmaktadır.

Bu nedenle mevcut sürümün sınırlı hazırlık işlevleri kullanılabilir; ancak gerçek dosyada saklama, imha ve güvenlik konularında hukukçuya sunulacak esaslı değerlendirme taslağı oluşturma yetkisi henüz açılmamalıdır.

2. Geliştirme ekibi için düzeltme listesi

2.1. Yönetmelik m.7/5 – Yöntem seçimi ve gerekçelendirme

Öncelik: Kritik

Mevcut metodolojide Yönetmelik m.7 kapsamındaki imha kayıtları ve yöntem açıklamaları ele alınmakla birlikte, m.7/5’in getirdiği yöntem seçimi kuralı yeterince açık değildir.

İlgili hüküm uyarınca:

* Kişisel Verileri Koruma Kurulu tarafından aksine bir karar verilmediği sürece, veri sorumlusu resen silme, yok etme veya anonim hâle getirme yöntemlerinden uygun olanı seçer.
* İlgili kişinin silme veya yok etme talebi söz konusu olduğunda veri sorumlusu uygun yöntemi seçer ve seçtiği yöntemin gerekçesini açıklar.

Geliştirme gerekliliği:

Aşama 6 metodolojisine ayrı bir değerlendirme alanı eklenmelidir:

1. İşlem resen mi, ilgili kişinin talebi üzerine mi gerçekleştiriliyor?
2. Seçilen yöntem hangisi: silme, yok etme veya anonim hâle getirme?
3. Yöntem hangi hukuki ve teknik gerekçeyle seçildi?
4. Yöntemin ilgili veri, ortam, kopya ve kullanıcı grubu bakımından yeterliliği nasıl doğrulandı?
5. İlgili kişinin talebi üzerine işlem yapılıyorsa yöntem seçiminin gerekçesi ilgili kişiye açıklanabilecek şekilde kayıt altına alındı mı?

Yöntem seçimi yalnızca teknik bir tercih olarak ele alınmamalıdır. Hukuki yükümlülük, veri sorumlusunun seçim yetkisi ve somut olayın teknik koşulları birlikte değerlendirilmelidir.

2.2. Kaynak doğrulama – E-004 kaydı

Öncelik: Orta

Mevcut kaynak kayıtlarında H-001 kurumsal mevzuat kopyası ile H-004 TBMM kabul metni karşılaştırılmıştır. Ancak 6698 sayılı Kanun’un güncel metnine ilişkin merkezi mevzuat kaynağına erişim denemesi 27 Kasım 2026 tarihinde zaman aşımına uğramıştır.

7499 sayılı Kanun’un kabul ve yayımlanma bilgileri resmî kaynaklardan kontrol edilmiş olmakla birlikte, bu durum merkezi mevzuat metninin güncelliğinin ayrıca doğrulandığı anlamına gelmez.

Geliştirme gerekliliği:

* E-004 kaydı, merkezi mevzuat metninin kontrol edildiği izlenimini vermeyecek şekilde açık tutulmalıdır.
* 7499 sayılı Kanun’un Resmî Gazete’deki resmî nüshası kaynak dosyasına eklenmelidir.
* İlgili işlem tarihi itibarıyla yürürlükte bulunan mevzuatın kontrol edildiği ayrıca kaydedilmelidir.
* H-001, H-004 ve ilgili değişiklik kaynakları arasındaki karşılaştırma kayıtları korunmalıdır.
* Merkezi kaynağa erişilememesi, alternatif resmî kaynaklarla doğrulanabilen sınırlı olgusal hazırlık çalışmalarını otomatik olarak engellememelidir.

2.3. Gerçek dosya ve test ortamı ayrımı

Öncelik: Yüksek

Aşama 6’nın test ortamı bulgularını gerçek sistem davranışından ayırması doğru bir yaklaşımdır. Bu ayrım korunmalı ve çıktılarda görünür olmalıdır.

Özellikle:

* K-002, yalnızca belgelenmiş test ortamındaki üç iç ortam için Uygulanmaz sonucunu desteklemektedir. Üretim ortamında üçüncü taraf hizmet sağlayıcısı veya dış ortam bulunmadığını kanıtlamaz.
* K-003, yönetici arayüzünde erişim bulunduğunu gösterebilir; tek başına verinin silinmediğini veya silme işleminin başarısız olduğunu kanıtlamaz.
* K-004, sentetik test kopyasının destek rolü tarafından erişilebilir olduğunu göstermektedir. Bu bulgu doğrudan üretim ortamına taşınamaz.
* E-003 kapsamında yedeklerin sona erme süresi ile fiilî silinme ve geri yükleme davranışı birbirinden ayrılmalıdır.
* E-006 kapsamındaki olası hizmet sağlayıcı arşivi, yalnızca mimari tasarım veya varsayım üzerinden gerçek veri kopyası olarak kabul edilmemelidir.

Geliştirme gerekliliği:

Her bulguda aşağıdaki ayrım korunmalıdır:

* Test ortamında gözlemlenen durum
* Üretim ortamına ilişkin mevcut kanıt
* Kanıtlanmamış hususlar
* Gerekli ek kanıt
* Hukuki değerlendirmeye geçiş için gereken koşullar

2.4. Saklama süresi ve imha takvimi

Öncelik: Yüksek

30 günlük politika beyanı, 90 günlük arayüzde gizleme ayarı ve 14 günlük yedek ayarı aynı hukuki veya teknik sonucu ifade etmez.

Bu süreler ayrı kayıt türleri olarak tutulmalıdır:

* Politika veya sözleşmede belirtilen saklama süresi
* Uygulamadaki yapılandırma süresi
* Verinin kullanıcı arayüzünden gizlendiği süre
* Fiilî silme veya yok etme zamanı
* Yedeklerin sona erme ve geri yükleme davranışı
* Üçüncü taraf sistemlerdeki kopyaların durumu

Geliştirme gerekliliği:

Saklama ve imha takvimi, her veri ve kopya için ayrı ayrı değerlendirilebilmelidir. Bir sistemdeki silme işleminin diğer ortamlardaki kopyaları da kapsadığı varsayılmamalıdır.

2.5. İlgili kullanıcı ve teknik görev ayrımı

Öncelik: Orta

Yönetmelik m.4/1-b’deki ilgili kullanıcı tanımı bakımından, kişisel verilerin teknik olarak depolanması, korunması ve yedeklenmesinden sorumlu kişilerin kapsam dışında tutulduğu dikkate alınmalıdır.

Bu nedenle yönetici veya destek rolünün varlığı tek başına ilgili kullanıcı niteliği ya da hukuka aykırı erişim sonucunu doğurmamalıdır.

Geliştirme gerekliliği:

Erişim değerlendirmesinde şu unsurlar ayrı ayrı kaydedilmelidir:

* Kullanıcının rolü ve yetkisi
* Erişimin amacı
* Erişimin teknik niteliği
* Verinin görüntülenmesi, değiştirilmesi, dışarı aktarılması veya silinmesi imkânı
* Erişimin işleme talimatlarıyla uyumu
* Erişimin kayıt altına alınıp alınmadığı

2.6. Üçüncü taraflar ve yedek kopyalar

Öncelik: Yüksek

Hizmet sağlayıcı, bulut altyapısı, yedekleme, replikasyon ve geri yükleme süreçleri birbirinden bağımsız değerlendirme alanları olarak ele alınmalıdır.

Geliştirme gerekliliği:

Üçüncü taraf veya haricî kopya ihtimali bulunduğunda aşağıdaki bilgiler aranmalıdır:

* Hizmet sağlayıcının kimliği
* Veri sorumlusu/veri işleyen rolü
* Sözleşme ve talimat ilişkisi
* Fiilî arşiv veya kopya bulunup bulunmadığı
* Kopyalanan veri kategorileri
* Verinin bulunduğu ülke ve uzaktan erişim ülkeleri
* Alt hizmet sağlayıcılar
* Saklama ve imha sorumluluğu
* Yedekleme ve geri yükleme uygulaması
* İmha işleminin üçüncü taraf sistemlerde doğrulanması

Yurt dışı aktarım ihtimali bulunuyorsa Aşama 5 bağlantısı kurulmalı; aktarımın hukuki mekanizması ayrıca değerlendirilmelidir.

2.7. İlgili kişinin silme ve yok etme talebi

Öncelik: Yüksek

Yönetmelik m.12 kapsamındaki talep süreci ayrı bir kontrol alanı olmalıdır.

Metodoloji şu ayrımları açıkça yapmalıdır:

* İşleme şartlarının tamamı ortadan kalkmışsa talep üzerine silme veya yok etme işleminin en geç 30 gün içinde tamamlanması ve ilgili kişinin bilgilendirilmesi.
* İşleme şartları devam ediyorsa talebin gerekçeli olarak reddedilmesi ve ilgili kişinin 30 gün içinde bilgilendirilmesi.
* Verinin üçüncü kişilere aktarılmış olması hâlinde, gerekli işlemin yapılması için üçüncü kişiye bildirimde bulunulması ve gerekli aksiyonun alınmasının sağlanması.

Yönetmelikte açıkça öngörülmeyen ayrı bir üçüncü taraf işlem süresi oluşturulmamalıdır.

2.8. İmha kayıtlarının tutulması

Öncelik: Yüksek

Yönetmelik m.7/3 uyarınca gerçekleştirilen bütün silme, yok etme ve anonim hâle getirme işlemleri kayıt altına alınmalıdır. Bu kayıtlar, diğer hukuki yükümlülükler saklı kalmak üzere, en az üç yıl süreyle muhafaza edilmelidir.

Ayrıca Yönetmelik m.7/4 uyarınca kullanılacak yöntemlerin politika ve prosedürlerde açıklanması gerekir.

Geliştirme gerekliliği:

İmha kaydı aşağıdaki bilgileri içerebilecek şekilde yapılandırılmalıdır:

* İşlem tarihi
* İlgili faaliyet ve veri kapsamı
* İşlem yapılan ortam ve kopya
* Kullanılan yöntem
* İşlemi gerçekleştiren kişi veya sistem
* İşlemin doğrulanma yöntemi
* Sonuç ve varsa hata
* İlgili kanıt kaydı
* Kayıtların saklanma süresi

3. Mevzuat hükümlerinin metodolojideki karşılığı

Aşağıdaki hükümler Aşama 6 incelemesinde esas alınmalı ve ilgili kontrol noktalarıyla ilişkilendirilmelidir.

Mevzuat	Metodolojide ele alınması gereken konu
KVKK m.4/2-d	Verilerin gerekli süre kadar muhafaza edilmesi
KVKK m.7	İşleme şartları sona erdiğinde silme, yok etme veya anonim hâle getirme
KVKK m.12/1	Uygun teknik ve idari güvenlik tedbirleri
KVKK m.12/2	Veri işleyenin sorumluluğu ve veri sorumlusunun ortak sorumluluğu
KVKK m.12/3	Denetim yükümlülüğü
KVKK m.12/4	Gizlilik ve amaç dışı kullanmama yükümlülüğünün devamı
KVKK m.12/5	Veri güvenliği ihlali bildirimi
Silme, Yok Etme veya Anonim Hâle Getirme Yönetmeliği m.5–6	Saklama ve imha politikası yükümlülüğü ve içeriği
Yönetmelik m.7	İmha kayıtları, yöntem açıklaması ve yöntem seçimi
Yönetmelik m.8	Silme yöntemi
Yönetmelik m.9	Yok etme yöntemi
Yönetmelik m.10	Anonim hâle getirme yöntemi
Yönetmelik m.11	Periyodik imha ve süreler
Yönetmelik m.12	İlgili kişinin talebi üzerine yapılacak işlemler

Önemli süreler:

* Periyodik imha aralığı, Yönetmelik m.11/2 uyarınca altı ayı aşamaz.
* Saklama ve imha politikası hazırlama yükümlülüğü bulunmayan veri sorumluları için Yönetmelik m.11/3’te öngörülen süre, imha yükümlülüğünün ortaya çıkmasından itibaren üç aydır.
* İlgili kişinin talebine ilişkin Yönetmelik m.12 süresi, koşulların ortadan kalktığı veya devam ettiği durumlara göre değerlendirilmelidir.
* İmha kayıtları en az üç yıl muhafaza edilmelidir.

Politika hazırlama yükümlülüğü, Yönetmelik m.5 uyarınca Sicile kayıt yükümlülüğü bulunan veri sorumluları bakımından değerlendirilmelidir.

4. Veri güvenliği ve özel nitelikli kişisel veriler

Aşama 6, güvenlik tedbirlerini soyut bir kontrol listesi olarak değil, somut risklerle ilişkilendirilmiş biçimde incelemelidir.

Her güvenlik riski için mümkün olduğunca şu bağlantı kurulmalıdır:

Risk → Tedbir → Sorumlu kişi/rol → Uygulama kanıtı → Denetim → Kalan risk

KVKK m.12/1–4 kapsamında teknik ve idari tedbirler, veri işleyenle ilişki, denetim ve gizlilik yükümlülükleri birlikte değerlendirilmelidir.

Özel nitelikli kişisel veriler bakımından:

* Öncelikle verinin gerçekten KVKK m.6/1 kapsamında özel nitelikli kişisel veri olup olmadığı belirlenmelidir.
* Sentetik veya test verisindeki bir alan, üretim ortamında özel nitelikli kişisel veri işlendiğini tek başına kanıtlamaz.
* Fotoğrafın varlığı tek başına biyometrik veri işlendiği anlamına gelmez. Kişinin benzersiz biçimde tanımlanması veya kimliğinin doğrulanması amacıyla özel teknik işleme yapılıp yapılmadığı araştırılmalıdır.
* KVKK m.6/3 kapsamındaki işleme şartı ile m.6/4 kapsamındaki yeterli önlemler birbirinden ayrı değerlendirilmelidir.
* Kurulun 2018/10 sayılı kararı, özel nitelikli kişisel verilerin işlenmesinde alınması gereken yeterli önlemler bakımından dikkate alınmalıdır.

5. Veri güvenliği ihlali yönlendirmesi

KVKK m.12/5 ve Kurulun 2019/10 sayılı kararı kapsamında, kişisel verilerin kanuni olmayan yollarla başkaları tarafından elde edilmesi hâlinde bildirim yükümlülüğü değerlendirilmelidir.

Metodolojide şu ayrım korunmalıdır:

* Her güvenlik alarmı otomatik olarak veri ihlali değildir.
* İhlal öğrenildiği anda bildirim süresinin değerlendirilmesi gerekir.
* Kurula bildirim, öğrenmeden itibaren gecikmeksizin ve en geç 72 saat içinde yapılmalıdır.
* Etkilenen ilgili kişiler belirlenebildiğinde, makul olan en kısa sürede bilgilendirme yapılmalıdır.

Aşama 6, ihlal tespit ettiğinde konuyu yalnızca saklama ve imha başlığı altında bırakmamalı; ilgili olayın uygun veri güvenliği ihlali sürecine yönlendirilmesini sağlamalıdır.

6. Aşama 7’ye aktarılacak konular

Aşama 6 kapsamında elde edilen bulguların sonraki aşamaya aktarılması gerekir.

Özellikle aşağıdaki konular Aşama 7 için devir notunda yer almalıdır:

* İlgili kişi başvuruları ve silme/yok etme talepleri
* Talebin kabul veya reddi ve gerekçeleri
* Üçüncü taraflara yapılan bildirimler
* Veri sorumlusunun aydınlatma ve bilgilendirme süreçleri
* Sözleşmelerdeki saklama ve imha hükümleri
* Sözleşme hükümleri ile fiilî uygulama arasındaki farklılıklar
* Güvenlik ihlali ve ilgili kişi bilgilendirmesi kayıtları
* Açık kalan kanıt ve değerlendirme ihtiyaçları

Aşama 6, Aşama 7’nin kendi değerlendirme alanını üstlenmemelidir.

7. Gerçek dosyada hukukçuya sunulacak taslak için aktivasyon koşulları

Mevcut 0.8.0 sürümünde gerçek dosyaya ilişkin esaslı hukuki değerlendirme taslağı oluşturma özelliği açılmamalıdır.

Bu özelliğin ileride açılabilmesi için aşağıdaki koşulların tamamı sağlanmalıdır:

1. İlgili faaliyet Aşama 2 ana envanterinde bulunmalıdır.
2. Aynı faaliyet, veri, ilgili kişi grubu, işlem ve ortam için gerekçeli Aşama 2 Devredilebilir kararı bulunmalıdır.
3. Aynı kapsam için Aşama 3’te tarafların rolleri ve sorumlulukları değerlendirilmiş olmalı ve açık devir kararı bulunmalıdır.
4. Aşama 4’te aynı faaliyet ve işleme amacıyla bağlantılı hukuki işleme şartı kaydı bulunmalıdır.
5. Hizmet sağlayıcı, haricî erişim, yedek veya üçüncü taraf kopyası söz konusuysa Aşama 5 bağlantısı kurulmalıdır.
6. Üretim, test, yedek, arşiv, kâğıt ortam ve geri yükleme kopyaları birbirinden ayrılmalıdır.
7. Saklama süresinin başlangıç ve bitiş olayları, hukuki dayanağı ve fiilî uygulaması kanıtlarla ilişkilendirilmelidir.
8. Yönetmelik m.7/5 kapsamında yöntem seçimi ve gerekçesi kaydedilmelidir.
9. Silme, yok etme veya anonim hâle getirme işleminin ilgili bütün kopyalar bakımından yeterliliği değerlendirilmelidir.
10. Risk, tedbir, uygulayıcı, denetim ve kalan risk bağlantısı kurulmalıdır.
11. Özel nitelikli kişisel veri veya veri güvenliği ihlali varsa ilgili özel değerlendirme süreci işletilmelidir.
12. İşlemin gerçekleştiği tarihte yürürlükte bulunan mevzuat doğrulanmalıdır.
13. Eksik olgular ve kanıt sınırlılıkları taslakta açıkça gösterilmelidir.
14. Nihai hukuki değerlendirme, gerekçeli ve izlenebilir bir hukukçu kararıyla ayrı olarak kaydedilmelidir.

Hukukçu karar kaydı en azından faaliyet/kapsam, ortam, rapor ve doküman sürümleri, K/E/H referansları, değerlendirme gerekçesi, sonuç, koşullar ve yeniden değerlendirme tetikleyicisini içermelidir.

Bu koşullar tamamlanmadan sistemin gerçek dosyada hukuka uygunluk sonucu veya nihai saklama/imha değerlendirmesi üretmesine izin verilmemelidir.

8. Sürüm bazında geliştirme kararı

Mevcut sürüm: 0.8.0

Korunabilecek işlevler:

* Önceki aşamalardan devir kontrolü
* Faaliyet ve veri kapsamının olgusal olarak incelenmesi
* Kanıt ve belge talep listesi hazırlanması
* Saklama, imha ve güvenlik süreçlerine ilişkin mevcut durumun haritalanması
* Eksik bilgi ve çelişkilerin kaydedilmesi
* Hazırlık ve devir notu oluşturulması

Açılmaması gereken işlevler:

* Gerçek dosyada nihai hukuki saklama süresi belirlenmesi
* Gerçek dosyada hukuka uygun imha yöntemi hakkında kesin sonuç verilmesi
* Üretim ortamında silme veya anonimleştirmenin gerçekleştiğine ilişkin kanıtsız kabul
* Gerçek dosyada veri güvenliği tedbirlerinin yeterli olduğuna ilişkin otomatik sonuç
* Hukukçu incelemesi olmaksızın hukuka uygunluk değerlendirmesi

Sonraki sürüm için zorunlu işler

1. Yönetmelik m.7/5 yöntem seçimi ve gerekçelendirme kontrolünün eklenmesi.
2. E-004 kaynak doğrulama kaydının tamamlanması veya açık sınırlılıkla korunması.
3. Gerçek dosya/test ortamı ayrımının tüm ilgili çıktılarda görünür hâle getirilmesi.
4. Saklama, arayüzde gizleme, fiilî silme, yedek ve geri yükleme ayrımının korunması.
5. Üçüncü taraf ve haricî kopya kontrollerinin güçlendirilmesi.
6. İlgili kişi talebi ve üçüncü taraf bildirim sürecinin açıklaştırılması.
7. Sentetik test örneklerinin yeni kontrolleri kapsayacak biçimde güncellenmesi.
8. SKILL.md, Aşama 6 intake, referans metodoloji ve çıktı dokümanlarının birbiriyle tutarlı hâle getirilmesi.
9. Yeni sürümün gerçek dosya hazırlık kapsamı ve hukukçu onay sınırlarının yeniden kontrol edilmesi.

9. Nihai karar

Aşama 6 – 0.8.0 için karar: DÜZELTME GEREKLİ.

Mevcut sürümün sınırlı hazırlık, olgusal inceleme, kanıt talebi ve devir notu işlevleri korunabilir.

Ancak Yönetmelik m.7/5’teki yöntem seçimi ve gerekçelendirme yükümlülüğü metodolojiye açıkça eklenmeden ve kaynak doğrulama kaydı gerekli açıklıkta tamamlanmadan Aşama 6’nın gerçek dosyada hukukçuya sunulacak esaslı değerlendirme taslağı üretmesine izin verilmemelidir.

Bu rapor, geliştirme ekibine yönelik hukuki metodoloji ve sürüm kapsamı geri bildirimidir. Kod değişikliği, entegrasyon veya test çalışmasının gerçekleştirildiği anlamına gelmez.

Hukuki inceleme sonucu: Mevcut sınırlı kullanım korunmalı; belirtilen düzeltmeler sonraki sürümde tamamlanmalı; gerçek dosyada esaslı hukuki taslak üretimi ancak yeni sürümün ayrıca incelenip onaylanmasından sonra değerlendirilmelidir.
