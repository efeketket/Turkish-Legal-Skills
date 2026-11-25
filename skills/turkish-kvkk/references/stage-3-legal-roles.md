# AŞAMA 3 — VERİ SORUMLUSU VE VERİ İŞLEYEN ROLLERİNİN BELİRLENMESİ

- Proje: Turkish-Legal-Skills

- Skill: turkish-kvkk

- İlk taslağın dayanak sürümü: 0.3.0

- Güncel inceleme sürümü: 0.4.0 · `draft-preview`

- Taslak durumu: Hukukçu incelemesine açık

- Hazırlanma tarihi: 22.11.2026

- Ön koşul: Aşama 1 ve Aşama 2 çıktıları

> Bu metodoloji taslaktır. Hukukçu değerlendirmesi ve proje onayı tamamlanmadan kesinleşmiş kabul edilmemelidir.
> Phase 1.6 çalışma metni, 26.11.2026 tarihli hukuk incelemesindeki zorunlu düzeltmeleri yansıtır ve yeniden hukukçu incelemesine açıktır.

# 1. Amaç

İşletmenin kişisel veri işleme faaliyetlerinde yer alan tarafların hukuki konumlarını, her bir faaliyet bakımından ayrı ayrı belirlemek; veri sorumlusu, veri işleyen, birden fazla veri sorumlusunun bulunduğu durumlar ve diğer ilgili taraflar arasındaki ayrımı somut olgular üzerinden değerlendirmek.

İncelemenin temel birimi, Aşama 2'de belirlenen kişisel veri işleme faaliyetidir.

Her faaliyet bakımından:

- İşleme faaliyetinde yer alan taraflar belirlenmelidir.

- Tarafların hukuki kimlikleri ve fiilî görevleri araştırılmalıdır.

- İşleme amaçlarına ve temel vasıtalarına ilişkin kararların kim tarafından alındığı incelenmelidir.

- Veri sorumlusu ve veri işleyen ilişkisi değerlendirilmelidir.

- Birden fazla tarafın karar alma süreçlerine katılması hâlinde hukuki konumları ayrı ayrı incelenmelidir.

- Sözleşmelerde belirtilen roller ile fiilî uygulama karşılaştırılmalıdır.

- Hukuki rol değerlendirmesi, dayanak kanıtlar ve mevzuat hükümleriyle gerekçelendirilmelidir.

Aynı gerçek veya tüzel kişi, farklı faaliyetlerde farklı hukuki sıfatlara sahip olabilir. Bir faaliyette veri sorumlusu olan kuruluş, başka bir faaliyette veri işleyen olarak hareket edebilir.

Bu nedenle kuruluşlara genel ve değişmez bir hukuki rol atanmamalıdır.

Aşama 3'ün tamamlanması, ilgili veri işleme faaliyetlerinin KVKK'ya uygun bulunduğu anlamına gelmez.

# 2. Uygulama talimatları

## 2.1. Önceki aşamalardan devir

1. Aşama 1 ve Aşama 2 raporlarını incele.

2. Aşama 2'deki Kişisel Veri İşleme Faaliyetleri Envanterini temel çalışma kaynağı olarak kullan.

3. Her faaliyetin `A-…` kimliğini koru.

4. Faaliyetle bağlantılı ilgili kişi gruplarını, veri kategorilerini, amaçları, operasyonları, sistemleri ve yaşam döngüsü kayıtlarını incele.

5. Aşama 1'deki Ön Hukuki Rol Tablosunda bulunan tahminleri başlangıç verisi olarak değerlendir; bunları doğrulanmış hukuki sonuç olarak kabul etme.

6. Önceki aşamalarda belirlenmiş bilgileri gereksiz yere yeniden araştırma.

7. Rol değerlendirmesini etkileyen eksik veya çelişkili hususları ilgili `E-…` kayıtlarıyla ilişkilendir.

8. Yeni kanıtları mevcut kayıtların üzerine yazmadan yeni `K-…` kimlikleriyle kaydet.

9. Önceki rol tahminleriyle çelişen yeni değerlendirmelerin gerekçesini açıkça göster.

Aynı Aşama 2 faaliyeti içinde taraflar veya operasyonlar farklı rollere sahipse mevcut faaliyet kimliği altında kapsam ve taraf bazında ayrı rol kayıtları aç.

Bağımsız amaç veya Aşama 2'nin sınır ölçütlerine göre ayrı faaliyet gerektiren operasyonel işlev tespit edilirse gerekçeyi ve kanıtı kaydedip Aşama 2'ye dön. Ayrı kimliği Aşama 2 ana envanterinde oluştur, önceki kaydı ve revizyon ilişkisini koru. Yeni faaliyet için rol incelemesine Aşama 2'den uygun devir sağlandığında başla. Plan veya demo ile belgelenen kararları tasarım verisi olarak kaydet. Fiilî kişisel veri işleme doğrulanırsa faaliyet sınırının tespiti için Aşama 2'ye dön.

## 2.2. Faaliyetlere katılan tarafların belirlenmesi

Her `A-…` faaliyeti için kişisel verilerin işlenmesine doğrudan veya dolaylı biçimde katılan tarafları belirle.

Özellikle:

- Hizmeti sunan işletme

- Hizmetten yararlanan müşteri işletme

- Verileri işlenen gerçek kişiler

- Yazılım ve SaaS sağlayıcıları

- Bulut ve barındırma sağlayıcıları

- Ödeme hizmeti sağlayıcıları

- Mesajlaşma ve bildirim servisleri

- Teknik destek ve bakım sağlayıcıları

- Entegrasyon ve API hizmeti sağlayıcıları

- Alt hizmet sağlayıcıları

- Veri aktarımının alıcıları

- İlgili kamu kurumları ve diğer kuruluşlar

Her taraf bakımından öncelikle hukuki kimliği belirle.

Bir marka, ürün, uygulama veya departmanı doğrudan ayrı bir veri sorumlusu ya da veri işleyen olarak kabul etme. Faaliyeti gerçekleştiren gerçek veya tüzel kişiyi tespit et.

Özellikle:

- Bir şirketin insan kaynakları, muhasebe veya teknik destek departmanlarını ayrı veri sorumlusu olarak değerlendirme.

- Aynı şirketler topluluğundaki ayrı tüzel kişilikleri tek bir kuruluş gibi kabul etme.

- Bir şirketin çalışanlarını veya yetkililerini, yalnızca görevleri nedeniyle şirketten ayrı veri sorumlusu olarak nitelendirme.

- Bir hizmet sağlayıcının yalnızca sözleşmenin tarafı olmasına dayanarak rol belirleme.

Bir tüzel kişinin kendi organizasyonu içindeki birimler ayrı veri işleyen değildir. Ayrı tüzel kişiliğe sahip grup şirketlerinin ise somut faaliyetleri bakımından ayrı değerlendirilmesi gerekir.

### İlgili kişi ile diğer tarafların ayrılması

İlgili kişi, kişisel verisi işlenen gerçek kişidir.

İlgili kişi ile veri sorumlusu, veri işleyen veya veri aktarımının alıcısı aynı hukuki kategoriler değildir.

Örneğin bir SaaS uygulamasında:

- Müşteri işletme hizmet alan kuruluştur.

- Müşteri işletmenin müşterileri ilgili kişidir.

- Müşteri işletmenin çalışanları uygulamayı kullanan gerçek kişiler olabilir.

- Yazılım şirketi veri sorumlusu veya veri işleyen olarak hareket edebilir.

- Bulut sağlayıcısı ayrı bir hizmet sağlayıcı veya alt veri işleyen olabilir.

Bir tarafın ilgili kişi, veri sorumlusu, veri işleyen veya alıcı konumunda bulunup bulunmadığını birbirinden bağımsız sorular olarak incele.

Veri aktarımının alıcısı olmak, tek başına veri sorumlusu veya veri işleyen sıfatını belirlemez.

## 2.3. Veri sorumlusunun belirlenmesi

6698 sayılı Kanun'un 3. maddesindeki veri sorumlusu tanımını esas al.

Bir gerçek veya tüzel kişinin veri sorumlusu olup olmadığını belirlemek için işleme amaçlarını ve temel vasıtalarını kimin belirlediğini ve veri kayıt sisteminin kurulmasından ve yönetilmesinden kimin sorumlu olduğunu araştır.

İlk olarak aşağıdaki sorulara cevap ara:

1. İşleme faaliyetinin gerçekleştirilmesine kim karar vermiştir?

2. Kişisel veriler hangi somut amaçla işlenmektedir?

3. Bu amacı kim belirlemiştir?

4. Hangi kişilerin verilerinin işleneceğine kim karar vermiştir?

5. Hangi veri kategorilerinin işleneceğini kim belirlemiştir?

6. Verilerin hangi amaçlarla kullanılabileceğine kim karar vermiştir?

7. Verilerin başka taraflarla paylaşılıp paylaşılmayacağına kim karar vermektedir?

8. İşleme faaliyetinin temel yöntem ve araçlarını kim belirlemektedir?

9. Verilerin ne kadar süreyle tutulacağına ilişkin temel kararı kim vermektedir?

10. Verilere hangi tarafların erişebileceğini kim belirlemektedir?

11. İşleme faaliyetinin sonuçlarından ve ilgili kişilerle ilişkiden kim sorumludur?

12. Bir başka taraf adına işlem yapılması söz konusuysa talimat verme yetkisi kimdedir?

13. Veri kayıt sisteminin kurulmasına kim karar vermiştir?

14. Sistemin organizasyonunu ve yönetim kurallarını kim belirlemektedir?

15. Kayıt düzenini, kayıtların bulunma ölçütlerini ve erişim kurallarını kim belirlemekte ve kim uygulamaktadır?

16. Sistem kararları hangi amaç ve temel vasıtayı belirlemektedir? Hangi tercihler verilen talimatların teknik uygulamasıdır?

### Ölçütlerin hukuki ağırlığı

Yukarıdaki sorular eşit ağırlıkta mekanik bir kontrol listesi olarak kullanılmamalıdır.

Sistemin kurulması veya yönetilmesiyle ilgili yetkiyi, amaç, temel vasıta ve talimat olgularıyla birlikte değerlendir. Teknik işletim veya erişim yetkisi tek başına bir rol tayin etmeye yetmez.

Öncelikle şu unsurları değerlendir:

**A. Temel ölçütler**

- İşleme amacının belirlenmesi.

- İşlenecek veri kategorilerinin ve ilgili kişi gruplarının belirlenmesi.

- Verilerin hangi amaçlarla kullanılacağının belirlenmesi.

- İşlemenin temel araçlarının ve yönteminin belirlenmesi.

- Verilerin paylaşılacağı tarafların ve paylaşım amacının belirlenmesi.

- İşleme faaliyetinin temel unsurları üzerinde bağımsız karar yetkisi bulunması.

Bu unsurlar veri sorumlusunun belirlenmesinde esas alınmalıdır.

**B. Destekleyici göstergeler**

- İlgili kişilerle doğrudan muhatap olunması.

- Veri işleme faaliyetinden doğrudan menfaat sağlanması.

- Başka bir veri işleyen görevlendirme yetkisinin bulunması.

- Veri işleme faaliyetinin işletmenin kendi iş modelinin parçası olması.

- İşleme faaliyetinin sonuçları üzerinde karar yetkisi bulunması.

Bu göstergeler temel ölçütleri destekleyebilir; ancak tek başlarına kesin sonuç doğurmaz.

Özellikle hizmet bedeli veya ekonomik kazanç elde edilmesini tek başına veri sorumlusu sıfatının göstergesi olarak kabul etme. Bir veri işleyen de sunduğu hizmet karşılığında ücret alabilir.

### Temel ve teknik vasıtaların ayrılması

İşleme vasıtalarını incelerken temel kararlar ile teknik uygulama ayrıntılarını birbirinden ayır.

Veri sorumlusu, işleme faaliyetinin temel amaçlarını ve temel araçlarını belirler.

Ancak veri sorumlusu, bazı teknik kararları veri işleyene bırakabilir.

Örneğin:

- Hangi bilgi teknolojileri sisteminin kullanılacağı.

- Verilerin teknik olarak hangi yöntemle depolanacağı.

- Güvenlik tedbirlerinin teknik ayrıntıları.

- Verilerin aktarımında kullanılacak teknik yöntem.

- Saklama süresinin teknik olarak nasıl uygulanacağı.

- Silme ve yok etme işlemlerinin teknik yöntemi.

Bu tür kararların veri işleyene bırakılması, tek başına veri işleyenin veri sorumlusuna dönüşmesine neden olmaz.

Buna karşılık hizmet sağlayıcı, teknik karar alanını aşarak kendi amaçları doğrultusunda verilerin kullanımını veya paylaşımını belirliyorsa bu faaliyet ayrıca değerlendirilmelidir.

### Kanundan kaynaklanan karar yetkileri

İlgili mevzuatın belirli bir kişisel veri işleme faaliyetinin amacını veya temel unsurlarını doğrudan belirlediği durumları ayrıca incele.

Bir tarafın veri işleme faaliyetini doğrudan kanuni yükümlülük nedeniyle gerçekleştirmesi, rol değerlendirmesinde önem taşır.

Tarafın yalnızca başka bir işletmenin talimatını yerine getirmediği, kendi kanuni yükümlülüğünü yerine getirdiği durumlarda veri sorumlusu sıfatı gündeme gelebilir.

## 2.4. Veri işleyenin belirlenmesi

6698 sayılı Kanun'un 3. maddesindeki veri işleyen tanımını esas al.

Bir tarafın veri işleyen olarak nitelendirilebilmesi için özellikle şu unsurları araştır:

1. Başka bir gerçek veya tüzel kişi adına kişisel veri işlenmesi.

2. Veri sorumlusunun verdiği yetki veya talimat çerçevesinde hareket edilmesi.

3. İşleme faaliyetinin temel amacının ve temel vasıtalarının veri sorumlusu tarafından belirlenmiş olması.

4. Hizmet sağlayıcının ilgili faaliyet kapsamında verileri kendi bağımsız amaçları için kullanmaması.

Veri işleyenin faaliyetleri çoğunlukla teknik veya operasyonel niteliktedir.

Örnekler:

- Verilerin barındırılması.

- Veritabanının işletilmesi.

- Yedekleme yapılması.

- Veri sorumlusunun talimatıyla bildirim gönderilmesi.

- Teknik destek verilmesi.

- Yetkilendirilmiş kullanıcı erişiminin sağlanması.

- Veri sorumlusunun belirlediği saklama ve silme kurallarının uygulanması.

### Veri işleyenin teknik karar serbestisi

Veri işleyen, kendisine bırakılan teknik uygulama alanında belirli ölçüde karar serbestisine sahip olabilir.

Örneğin veri sorumlusunun belirlediği amaç ve kapsam çerçevesinde uygun sunucu altyapısını, yedekleme yöntemini veya güvenlik teknolojisini seçebilir.

Bu karar serbestisi tek başına veri sorumlusu sıfatını doğurmaz.

Değerlendirmede şu sorulara cevap ara:

- Karar teknik uygulama ayrıntısıyla mı ilgilidir?

- Veri sorumlusunun belirlediği amaç ve kapsam korunmakta mıdır?

- Hizmet sağlayıcı, işleme faaliyetinin temel amacını değiştirebilmekte midir?

- Yeni veri kategorileri veya ilgili kişi grupları belirleyebilmekte midir?

- Verileri farklı amaçlarla kullanabilmekte midir?

- Verilerin yeni alıcılara açılmasına bağımsız olarak karar verebilmekte midir?

### Verilerin kendi amaçları için kullanılması

Bir veri işleyenin kendisine verilen talimatların dışına çıkarak kişisel verileri kendi amaçları doğrultusunda işlemesi durumunda bu yeni işleme faaliyeti ayrıca incelenmelidir.

Örneğin:

- Müşteri verilerinin bağımsız pazarlama amacıyla kullanılması.

- Farklı müşterilerin verilerinin ortak bir ticari veri havuzunda birleştirilmesi.

- Verilerin bağımsız profil oluşturma amacıyla kullanılması.

- Müşteri verilerinin başka işletmelere açılması.

- Müşteri verilerinin bağımsız ticari ürün veya hizmet geliştirme amacıyla kullanılması.

Bu tür durumlarda hizmet sağlayıcı, ilgili yeni işleme faaliyeti bakımından veri sorumlusu olabilir.

Ancak bir faaliyetteki rol değişikliğini otomatik olarak bütün hizmet ilişkisine yayma. Yeni amacın ve operasyonun kapsamını ayrı değerlendir.

## 2.5. Birden fazla tarafın yer aldığı faaliyetler

Bir faaliyette birden fazla kuruluşun bulunması, bu kuruluşların aynı hukuki sıfata sahip olduğu anlamına gelmez.

Her tarafın karar yetkisini, talimat ilişkisini ve işleme faaliyetindeki rolünü ayrı değerlendir.

### A. Birbirinden bağımsız veri sorumluları

Birden fazla tarafın kişisel verileri kendi amaçları ve kendi kararları doğrultusunda işlemesi durumunda bağımsız veri sorumluluğu söz konusu olabilir.

Örneğin bir işletmenin verileri başka bir işletmeye aktarması ve alıcı işletmenin bu verileri kendi bağımsız amacı için kullanması hâlinde, yalnızca veri aktarımı gerçekleştiği için ortak veri sorumluluğu kabul edilmemelidir.

Her iki tarafın işleme amaçları ve temel vasıtaları ayrı ayrı incelenmelidir.

### B. Birden fazla veri sorumlusunun ortak karar alması

KVKK'da müşterek veri sorumluluğu kavramı açık bir kanuni tanım olarak düzenlenmemiştir.

Bununla birlikte Kurulun yayımladığı kararlar ve Kurumun sektörel rehberleri, aynı veri işleme faaliyeti bakımından birden fazla tarafın amaç ve temel vasıtaları birlikte belirlemesi durumunda birden fazla veri sorumlusunun bulunabileceğini kabul eden bir yaklaşım içermektedir.

Bu nedenle:

- Tarafların aynı veri tabanını kullanması tek başına yeterli değildir.

- Tarafların birbirlerine veri aktarması tek başına yeterli değildir.

- Aynı sözleşmenin tarafı olmaları tek başına yeterli değildir.

- Teknik iş birliği içinde olmaları tek başına yeterli değildir.

Ortak veri sorumluluğu değerlendirmesinde tarafların somut işleme amacının ve temel araçlarının belirlenmesine birlikte katılıp katılmadığı araştırılmalıdır.

Bu hukuki nitelendirme, KVKK'daki açık bir müşterek veri sorumluluğu hükmüne değil, Kurulun yaklaşımına ve yorumuna dayandığı için gerekçesi özellikle açıklanmalıdır.

GDPR m.26'daki düzenlemeler doğrudan KVKK hükmü gibi uygulanmamalıdır. Karşılaştırmalı hukuk kaynakları kullanılacaksa bunların yorum desteği olduğu açıkça belirtilmelidir.

### C. Alt veri işleyen ve alt hizmet sağlayıcılar

Bir veri işleyenin, veri sorumlusuna sunduğu hizmetin bir bölümünü başka bir kuruluşa gördürmesi durumunda bu kuruluşun konumunu ayrıca incele.

Şu hususları araştır:

- Alt hizmet sağlayıcı hangi faaliyeti gerçekleştirmektedir?

- Hangi verileri işlemektedir?

- Kimin adına hareket etmektedir?

- Veri sorumlusunun talimatlarıyla bağlantısı nedir?

- İlk veri işleyenin talimatlarıyla mı hareket etmektedir?

- Verileri kendi amaçları için kullanmakta mıdır?

- Alt hizmet sağlayıcı kullanımı sözleşmede düzenlenmiş midir?

- Veri sorumlusunun bilgisi veya onayı aranmış mıdır?

- Veriler hangi sistemlere ve ülkelere aktarılmaktadır?

KVKK'da alt veri işleyen ilişkisine dair genel ve kapsamlı bir kanuni düzenleme bulunduğu varsayılmamalıdır. Kurumun ilgili rehberleri ve sektörel düzenlemeleri ayrıca incelenmelidir.

Alt veri işleyen kavramı, rol incelemesinde işlevsel bir tanımlama olarak kullanılabilir; ancak doğrudan kanuni bir rol kategorisi gibi sunulmamalıdır.

### D. Veri aktarımının alıcısı

Veri aktarımının alıcısını ayrıca kaydet.

Alıcı:

- Veri sorumlusu olabilir.

- Veri işleyen olabilir.

- Başka bir bağımsız veri sorumlusu olabilir.

- Somut durumda farklı bir hukuki konumda bulunabilir.

Bir tarafın veri alıcısı olması, onun veri sorumlusu veya veri işleyen olduğunu tek başına göstermez.

Aktarımın hukuki şartları Aşama 5'te değerlendirilecektir.

## 2.6. Yazılım ve SaaS sistemlerinin incelenmesi

Yazılım şirketlerinin hukuki konumunu yalnızca yazılımı geliştirmeleri, sunucuları işletmeleri veya müşteri verilerine erişebilmeleri üzerinden belirleme.

Her işleme faaliyetinin amacı, temel vasıtaları, teknik uygulaması ve tarafların karar yetkileri ayrı incelenmelidir.

Özellikle şu faaliyetleri birbirinden ayır:

- Müşteri işletmenin kendi müşterilerine ilişkin verileri işlemesi.

- SaaS sağlayıcının bu verileri barındırması ve işletmesi.

- SaaS sağlayıcının kendi abonelerine ilişkin hesap ve sözleşme verilerini işlemesi.

- SaaS sağlayıcının faturalandırma ve ödeme işlemlerini yürütmesi.

- Teknik destek ve güvenlik kayıtlarının oluşturulması.

- Platformun hizmet geliştirme ve analiz faaliyetleri.

- Müşteriler arasında veri paylaşımı veya ortak veri havuzu oluşturulması.

- Bulut sağlayıcının altyapı hizmetleri.

### Örnek değerlendirme

Bir yazılım şirketinin işletmelere müşteri yönetimi uygulaması sunduğu varsayılsın.

| Faaliyet | Ön değerlendirme |

| --- | --- |

| Müşteri işletmenin kendi müşterilerine ilişkin bilgileri kaydetmesi | Müşteri işletme, kendi işleme amacını ve temel vasıtaları belirliyorsa veri sorumlusu olabilir. |

| SaaS şirketinin müşteri verilerini barındırması | Müşteri işletmenin talimatları ve belirlediği amaçlar doğrultusunda hareket ediyorsa veri işleyen olabilir. |

| SaaS şirketinin kendi abonelerinin hesap ve sözleşme verilerini işlemesi | Kendi hizmet ilişkisini yürütmek amacıyla karar veriyorsa veri sorumlusu olabilir. |

| SaaS şirketinin kendi faturalandırma ve muhasebe faaliyetleri | Somut hukuki ve fiilî koşullara göre ayrıca değerlendirilmelidir. |

| Bulut sağlayıcının müşteri verilerini barındırması | SaaS şirketi adına ve onun belirlediği amaçlar çerçevesinde hareket ediyorsa alt veri işleyen olabilir. |

| Ödeme kuruluşunun ödeme işlemlerini yürütmesi | Ödeme kuruluşunun kendi yasal yükümlülükleri ve karar alanları ayrıca incelenmelidir. |

| Mesajlaşma servisinin bildirim göndermesi | Yalnızca talimatla gönderim yapması ile kendi amaçları için veri işlemesi ayrılmalıdır. |

| Teknik destek sağlayıcısının müşteri kayıtlarına erişmesi | Erişimin niteliği, amacı, yetkisi ve fiilî işlemler araştırılmalıdır. |

| SaaS şirketinin müşteri verilerini farklı müşteriler arasında paylaşması | Bağımsız amaç ve karar yetkisi varsa veri sorumluluğu veya birden fazla veri sorumlusunun bulunduğu durumlar gündeme gelebilir. |

Bu tablo yalnızca başlangıç değerlendirmesidir. Gerçek sözleşmeler, teknik yapı ve fiilî uygulama araştırılmadan kesin rol ataması yapılmamalıdır.

Kurulun 2021/1303 sayılı karar özeti ile 2021/1304 sayılı ilke kararını ayrı kaynaklar olarak incele. Araç kiralama örneğinde standart SaaS hizmeti ile müşteriler arasında kara liste verilerini açan işleme ayrılır.

Bu karar, yazılım şirketinin teknik altyapıyı yönetmesinin veya verilerin içeriğine doğrudan erişememesinin her durumda veri işleyen olduğu anlamına gelmediğini göstermektedir.

## 2.7. Sözleşme ve fiilî uygulamanın karşılaştırılması

Her tarafın hukuki rolünü belirlerken sözleşmelerde kullanılan unvanları tek başına esas alma.

Aşağıdaki belgeleri ve uygulamaları incele:

- Hizmet sözleşmeleri.

- Veri işleme protokolleri.

- Kullanım koşulları.

- Gizlilik ve aydınlatma metinleri.

- Alt hizmet sağlayıcı listeleri.

- Teknik mimari belgeleri.

- Yetkilendirme ve erişim politikaları.

- Ürün yapılandırmaları.

- API ve entegrasyon dokümantasyonu.

- Teknik destek prosedürleri.

- Veri saklama ve silme süreçleri.

- İşletme beyanları.

- Fiilî sistem davranışları.

Sözleşmelerdeki rol tanımı ile fiilî uygulama arasında farklılık varsa bu farklılığı açıkça kaydet.

Örneğin sözleşmede hizmet sağlayıcı veri işleyen olarak tanımlanmış olsa bile:

- Verileri bağımsız pazarlama amacıyla kullanıyor olabilir.

- Verileri başka müşterilere açıyor olabilir.

- Kendi belirlediği amaçlarla ortak veri havuzu oluşturuyor olabilir.

- Müşteri işletmenin belirlemediği yeni işleme amaçları oluşturuyor olabilir.

Bu durumlarda sözleşmedeki unvanın fiilî uygulamayla örtüşüp örtüşmediği değerlendirilmelidir.

## 2.8. Hukuki kaynakların doğrulanması

Rol değerlendirmesinde öncelikle yürürlükteki mevzuatı ve resmî Kurum/Kurul kaynaklarını kullan.

Kaynakları hukuki niteliklerine göre ayır:

1. Kanun ve uygulanabilir ikincil mevzuat.

2. Kişisel Verileri Koruma Kurulu kararları.

3. Kurum tarafından yayımlanan rehberler ve resmî açıklamalar.

4. Yargı kararları.

5. Akademik çalışmalar ve doktrin.

6. Karşılaştırmalı hukuk kaynakları.

Her kaynak için:

- Kaynağın adı.

- Yayımlayan makam.

- Madde veya karar numarası.

- Karar veya yayın tarihi.

- Yürürlük durumu (uygunsa).

- Resmî bağlantı.

- İnceleme tarihi.

- Somut rol değerlendirmesiyle ilişkisi.

kaydedilmelidir.

Kurul kararlarının somut olay bağlamını dikkate al. Bir kararın belirli bir olayda yaptığı değerlendirmeyi bütün SaaS hizmetleri veya bütün hizmet sağlayıcılar için genel ve değişmez kural olarak kullanma.

Rehberlerdeki açıklamaları kanun hükmü gibi sunma.

GDPR, EDPB veya Avrupa Birliği kaynakları kullanıldığında bunları Türk hukukunda doğrudan uygulanabilir hükümler olarak değil, karşılaştırmalı yorum kaynağı olarak göster.

## 2.9. Kanıt ve belirsizliklerin yönetimi

Her hukuki rol değerlendirmesi, somut bir faaliyet ve tarafla ilişkilendirilmelidir.

Her tespit için:

- İlgili `A-…` faaliyet kimliği.

- Değerlendirilen taraf.

- İncelenen karar veya yetki.

- Dayanak `K-…` kanıt kimliği.

- Varsa ilgili `E-…` açık kaydı.

- Hukuki kaynak.

- Değerlendirme gerekçesi.

gösterilmelidir.

Eksik veya çelişkili bilgi bulunduğunda kesin hukuki rol ataması yapma.

Özellikle:

- Sözleşmeye erişilemiyorsa bunu belirt.

- Fiilî uygulama doğrulanamıyorsa bunu belirt.

- Teknik yetkiler bilinmiyorsa hedefli bilgi talep et.

- Birden fazla tarafın karar alma sürecine katılması hâlinde her birinin katkısını araştır.

- Bir tarafın verileri kendi amaçları için kullandığı iddia ediliyor ancak kanıtlanamıyorsa bunu doğrulanmamış iddia olarak kaydet.

- Hukuki yorum tartışmalıysa alternatif değerlendirmeleri ve dayanaklarını göster.

### Olgusal doğrulama ve hukuki değerlendirme ayrımı

İki ayrı değerlendirme yap:

**Olgusal doğrulama:** Tarafların fiilen hangi işlemleri yaptığı ve hangi karar yetkilerine sahip olduğu doğrulanmış mıdır?

**Hukuki değerlendirme:** Doğrulanmış olguların KVKK bakımından hangi hukuki role işaret ettiği yeterince açık mıdır?

Bir olgunun doğrulanmış olması, hukuki nitelendirmenin de tartışmasız olduğu anlamına gelmez.

## 2.10. Sonraki aşamalara devir

Rol değerlendirmesi sonucunda ortaya çıkan hukuki yükümlülük bağlantılarını sonraki aşamalara aktar.

Özellikle:

- Veri sorumlusunun işleme şartlarına ilişkin sorumluluğu — Aşama 4.

- Veri sorumlusu ve veri işleyen arasındaki aktarım ilişkileri — Aşama 5.

- Veri güvenliği ve teknik/idari tedbirler — Aşama 6.

- Saklama, imha ve veri sorumlusunun karar yetkileri — Aşama 6.

- Aydınlatma yükümlülüğü ve ilgili kişi başvuruları — Aşama 7.

- Veri işleme ve hizmet sözleşmelerindeki eksiklikler — Aşama 7.

Aşama 3'te bu yükümlülüklerin varlığı ve hangi tarafla ilişkili olduğu belirlenebilir; ancak sonraki aşamaların ayrıntılı hukuka uygunluk incelemesi yapılmamalıdır.

# 3. Temel kurallar

- Hukuki rol değerlendirmesinin temel birimi kişisel veri işleme faaliyetidir.

- Aynı kuruluşun farklı faaliyetlerde farklı hukuki sıfatlara sahip olabileceği kabul edilmelidir.

- Veri sorumlusu ve veri işleyen sıfatları işletmeye genel olarak ve değişmez biçimde atanmamalıdır.

- İlgili kişi, veri sorumlusu, veri işleyen ve veri aktarımının alıcısı kavramları birbirinden ayrılmalıdır.

- Bir veri aktarımının gerçekleşmesi tek başına ortak veri sorumluluğu oluşturmaz.

- Bir hizmet sağlayıcının veriye teknik erişimi bulunması tek başına veri sorumlusu olduğu anlamına gelmez.

- Veriye doğrudan erişememek de tek başına veri sorumlusu olmayı engellemez.

- Yazılımı geliştirmek, sunucuyu yönetmek veya veri tabanını işletmek tek başına hukuki rolü belirlemez.

- Veri sorumlusunun temel amaç ve araçları belirlemesi ile veri işleyenin teknik uygulama kararları birbirinden ayrılmalıdır.

- Veri işleyenin teknik konularda belirli bir karar serbestisine sahip olması veri sorumlusu sıfatını otomatik olarak doğurmaz.

- Hizmet sağlayıcının kendi amaçları için veri işlemesi ayrı bir faaliyet olarak incelenmelidir.

- Sözleşmelerde kullanılan rol tanımları tek başına belirleyici kabul edilmemelidir.

- Sözleşme hükümleri ile fiilî uygulama karşılaştırılmalıdır.

- İç organizasyon birimleri ayrı veri sorumlusu veya veri işleyen olarak değerlendirilmemelidir.

- Ayrı tüzel kişilikler, aynı şirketler topluluğunda yer alsalar bile somut faaliyetleri bakımından ayrı değerlendirilmelidir.

- Alt hizmet sağlayıcıları ve alt veri işleyen ilişkileri ayrıca incelenmelidir.

- Müşterek veri sorumluluğu değerlendirmesi otomatik yapılmamalı; ortak amaç ve temel araçların belirlenmesine katılım araştırılmalıdır.

- GDPR hükümleri KVKK'nın açık düzenlemesi gibi sunulmamalıdır.

- Kurul kararları somut olayın özellikleri dikkate alınarak kullanılmalıdır.

- Olgusal doğrulama ile hukuki nitelendirme ayrı gösterilmelidir.

- Her değerlendirme faaliyet, taraf, kanıt ve hukuki kaynakla ilişkilendirilmelidir.

- Önceki aşamalardaki kayıt kimlikleri korunmalıdır.

- Belirsiz veya çelişkili bilgiler kesin hukuki sonuç gibi sunulmamalıdır.

- Rol değerlendirmesinin tamamlanması KVKK'ya uyum sonucunu doğurmaz.

# 4. Aşama çıktıları

Aşama 3 çıktıları, Aşama 2'deki ana faaliyet envanteriyle bağlantılı tek bir rapor içinde hazırlanmalıdır.

## 4.1. Faaliyet Bazlı Hukuki Rol Matrisi

Her faaliyet ve taraf için hukuki rol değerlendirmesini gösteren ana tablo.

Önerilen sütunlar:

| Faaliyet | Faaliyet kapsamı | Taraf | Hukuki kimlik | İlgili kişi grubu | İşleme amacı | Ön değerlendirme | Güncel taslak rol değerlendirmesi | Olgusal doğrulama | Hukuki değerlendirme durumu | Kanıt | Açık kayıt |

|---|---|---|---|---|---|---|---|---|---|---|---|

Aynı faaliyet sınırındaki rol farklılıklarını kapsam bazında göster. Bağımsız faaliyet bulgusunu Aşama 2'ye geri gönder. Olgusu veya hukuki dayanağı doğrulanamayan rolü koşullu ifade et ya da açık bırak.

## 4.2. Karar Alma Yetkileri ve Talimat Matrisi

Tarafların hangi kararları aldığını ve hangi kararları başka bir taraftan gelen talimat doğrultusunda uyguladığını gösteren tablo.

Önerilen sütunlar:

| Faaliyet | Taraf | Karar alanı | Kararı alan taraf | Kararın niteliği | Talimat ilişkisi | Dayanak kanıt | Açıklama |

|---|---|---|---|---|---|---|---|

Karar alanları en azından şunları içermelidir:

- İşleme amacı.

- İlgili kişi grubu.

- Veri kategorileri.

- Veri toplama yöntemi.

- Temel işleme araçları.

- Teknik uygulama araçları.

- Saklama ve imha kararları.

- Erişim yetkileri.

- Veri kayıt sistemini kurma, organize etme, yönetme, kayıt düzenini ve erişim kurallarını belirleme yetkisi.

- Veri paylaşımı ve alıcılar.

- Başka hizmet sağlayıcılarının kullanılması.

- İşleme faaliyetinin sonuçları.

## 4.3. Sözleşme ve Fiilî Uygulama Karşılaştırması

Sözleşmelerdeki düzenlemelerle gerçek uygulama arasındaki uyumu gösteren tablo.

| Faaliyet | Taraflar | Sözleşmedeki düzenleme | Fiilî uygulama | Farklılık | Hukuki etkisi | Kanıt | Açık kayıt |

|---|---|---|---|---|---|---|---|

Sözleşme veya teknik belgeye erişilemiyorsa bu durum ayrıca kaydedilmelidir.

## 4.4. Hukuki Rol Değerlendirme ve Gerekçe Kayıtları

Özellikle karmaşık, tartışmalı veya birden fazla tarafın karar alma sürecine katıldığı faaliyetler için gerekçeli değerlendirme kaydı oluştur.

Her kayıt şu unsurları içermelidir:

- İlgili faaliyet kimliği.

- Değerlendirilen taraflar.

- Faaliyetin somut kapsamı.

- İlgili işleme amacı.

- Temel karar yetkileri.

- Talimat ilişkisi.

- Sözleşme ve fiilî uygulama bulguları.

- Uygulanan mevzuat hükümleri.

- İlgili Kurul kararları ve rehberler.

- Hukuki değerlendirme.

- Alternatif yorumlar.

- Belirsizlikler.

- Sonraki aşamalara aktarılacak hususlar.

## 4.5. Belirsiz Roller ve Eksik Bilgiler Listesi

Mevcut `E-…` kayıtları korunarak rol değerlendirmesini etkileyen eksik veya çelişkili bilgiler listelenmelidir.

Her açık kayıt:

- İlgili faaliyetle.

- Değerlendirilen tarafla.

- Eksik karar veya yetki bilgisiyle.

- Dayanak kanıtlarla.

- Hukuki değerlendirmeye etkisiyle.

- Gerekli bilgi veya belgeyle.

ilişkilendirilmelidir.

Yeni bir açık kayıt oluşturulması gerekiyorsa mevcut son `E-…` numarasından devam edilmelidir.

## 4.6. Sonraki Aşamalara Devir Notları

Aşama 4, 5, 6 ve 7 için tarafların hukuki konumlarından kaynaklanan önemli hususlar aktarılmalıdır.

Faaliyet bazında hazırlık ve bilgi toplamayı esaslı uygunluk değerlendirmesine devirden ayır. Aşama 2'den devralınan hedefe özgü kısıtları ve yeni kanıtın açık bıraktığı alt soruları göster. Bir fiziksel kaydın KVKK m. 2 kapsamındaki veri kayıt sistemi niteliği belirsizse Aşama 4–7 için hazırlıkla sınırlı ilerle. Planlanan işlemler için fiilî kullanım doğrulanana kadar hazırlık kaydı tut.

Her devir notu ilgili `A-…`, `K-…` ve `E-…` kimliklerini içermelidir.

# 5. Aşama geçiş kriteri

Aşama 3'ün tamamlanabilmesi için:

- Aşama 2'de belirlenen bütün kişisel veri işleme faaliyetleri rol incelemesine alınmış olmalıdır.

- Her faaliyet kapsamında yer alan gerçek veya tüzel kişiler belirlenmiş veya eksiklikleri kaydedilmiş olmalıdır.

- Tarafların hukuki kimlikleri ve organizasyonel konumları açıklığa kavuşturulmuş olmalıdır.

- Her faaliyette işleme amaçlarına ilişkin karar yetkileri araştırılmış olmalıdır.

- Temel vasıtalar ile teknik uygulama kararları birbirinden ayrılmış olmalıdır.

- Veri sorumlusu ve veri işleyen değerlendirmeleri somut faaliyetlere dayandırılmış olmalıdır.

- Birden fazla tarafın karar alma süreçlerine katıldığı durumlar ayrıca incelenmiş olmalıdır.

- Bağımsız veri sorumluları ile birlikte karar alan taraflar birbirinden ayrılmış olmalıdır.

- Alt hizmet sağlayıcıları ve veri alıcılarının konumları değerlendirilmiş olmalıdır.

- Sözleşmelerdeki rol tanımları ile fiilî uygulama karşılaştırılmış olmalıdır.

- Önemli çelişkiler ve eksiklikler ilgili `E-…` kayıtlarına bağlanmış olmalıdır.

- Her hukuki değerlendirme ilgili kanıt ve hukuki kaynakla ilişkilendirilmiş olmalıdır.

- Önceki aşamaların faaliyet ve kanıt kimlikleri korunmuş olmalıdır.

- Sonraki aşamalara aktarılacak hukuki sorumluluk bağlantıları gösterilmiş olmalıdır.

- Kesinleştirilemeyen hukuki roller açıkça belirtilmiş olmalıdır.

Her faaliyetin rolünün kesin olarak belirlenmesi zorunlu değildir.

Ancak kesinleştirilemeyen durumlarda:

- Hangi olguların eksik olduğu,

- Hangi tarafların değerlendirmeye konu olduğu,

- Belirsizliğin hangi hukuki sonuçları etkilediği,

- Sonraki aşamalarda hangi hususların ayrıca araştırılması gerektiği

açıklanmalıdır.

Olgusal olarak doğrulanmış ancak hukuki yorumu tartışmalı olan durumlar ayrıca gösterilmelidir.

Kritik bir belirsizlik sonraki aşamanın güvenilir biçimde yürütülmesini engelliyorsa ilgili faaliyet için geçiş kısıtlaması belirtilmelidir. Diğer faaliyetler, bu kısıtlamadan etkilenmedikleri ölçüde incelemeye devam edebilir.

Aşama 3'ün tamamlanması, işletmenin veya faaliyetlerin KVKK'ya uygun olduğu anlamına gelmez.

---

# 6. Hukuki kaynaklar ve değerlendirme notları

## 6.1. Kanuni kaynaklar

### 6698 sayılı Kişisel Verilerin Korunması Kanunu

Özellikle:

- Madde 2 — Kanunun kapsamı.

- Madde 3 — İlgili kişi, kişisel veri, kişisel verilerin işlenmesi, veri işleyen, veri kayıt sistemi ve veri sorumlusu tanımları.

- Madde 8 — Kişisel verilerin yurt içinde aktarılması.

- Madde 9 — Kişisel verilerin yurt dışına aktarılması.

- Madde 10 — Aydınlatma yükümlülüğü.

- Madde 11 — İlgili kişinin hakları.

- Madde 12 — Veri güvenliğine ilişkin yükümlülükler.

- Madde 16 — Veri Sorumluları Sicili.

- Madde 18 — Kabahatler ve idari yaptırımlar.

Özellikle Madde 12/2'de veri sorumlusu ile veri işleyenin veri güvenliği tedbirleri bakımından birlikte sorumluluğu düzenlenmiştir.

Bu sorumluluk, birden fazla veri sorumlusunun bulunduğu hukuki durumla karıştırılmamalıdır. İki kavram farklı hukuki temellere dayanır.

## 6.2. Kurul kararları

### 30.01.2020 tarihli ve 2020/71 sayılı Kurul Kararı

Veri sorumlusu ve veri işleyen ayrımında amaç, temel araçlar, karar yetkileri ve talimat ilişkisine ilişkin önemli ölçütler içermektedir.

### 13.04.2021 tarihli ve 2021/359 sayılı Kurul Kararı

Hizmet sağlayıcı ve uygulama sağlayıcı arasındaki veri sorumlusu/veri işleyen ayrımını incelemek bakımından önemlidir.

### 23.12.2021 tarihli ve 2021/1303 sayılı Kurul Karar Özeti

Yazılım şirketlerinin SaaS hizmetleri ve ortak veri tabanlarında veri sorumluluğu bakımından özellikle önemlidir.

Standart SaaS hizmeti ile yazılım şirketinin kendi amaçları doğrultusunda yürüttüğü ek işleme faaliyetleri birbirinden ayrılmalıdır.

### 23.12.2021 tarihli ve 2021/1304 sayılı Kurul İlke Kararı

20.01.2022 tarihli, 31725 sayılı Resmî Gazete'de yayımlanan ilke kararı araç kiralama sektöründeki kara liste uygulamalarını ele alır. Kararın gerekçe ve sonuç bölümünde, firmaların kendi işletmesiyle sınırlı kayıtlar ile yazılım üzerinden diğer firmalara açılan kayıtlar ayrılır. Kanunun 4, 5 ve 8. maddelerine aykırı kara liste işleme bağlamında Kurul, veriler üzerinde hâkimiyeti bulunan kiralama şirketleriyle yazılım şirketlerinin ortak veri sorumluluğu değerlendirmesini açıklar.

Bu yaklaşım, ilgili faaliyet için tarafların ortak amaca, paylaşım mimarisine, erişime ve diğer temel vasıtalara fiilî katkısının araştırılmasını destekler. Her ortak liste veya veri paylaşımı için aynı sonucu çıkarmadan önce sektör ve işleme olgularını karşılaştır. Demo tasarım kararını fiilî işleme ve ortak rolün kanıtı sayma. Türk hukuku değerlendirmesini KVKK ve Kurul uygulaması üzerinden kur. [Kurum kararı](https://www.kvkk.gov.tr/Icerik/7414/2021-1304) · [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2022/01/20220120-10.pdf)

## 6.3. Kurum rehberleri

- Kişisel Verilerin Korunması Kanunu Hakkında Sıkça Sorulan Sorular, Mart 2025.

- Kişisel Verilerin Korunmasına İlişkin Bankacılık Sektörü İyi Uygulamalar Rehberi, Aralık 2024.

- Örneklerle Kişisel Verilerin Korunmasına İlişkin Rehber.

- Veri Sorumlusu ve Veri İşleyen ilişkilerine dair Kurum açıklamaları.

- Veri İşleyenler İçin Bağlayıcı Şirket Kuralları yardımcı kılavuzu.

Sektörel rehberler kendi kapsamları dikkate alınarak kullanılmalıdır.

## 6.4. Hukuki yorum gerektiren konular

1. KVKK'da müşterek veri sorumluluğu kavramının açıkça tanımlanmamış olması.

2. Kurul kararları ve rehberler üzerinden müşterek veri sorumluluğunun kapsamının belirlenmesi.

3. Temel vasıtalar ile teknik uygulama kararları arasındaki sınır.

4. Veri işleyenin bağımsız amaçla işlemeye başlaması hâlinde rolün kapsamı.

5. SaaS sağlayıcılarının farklı faaliyetler bakımından farklı rollere sahip olması.

6. Alt veri işleyen ilişkisinin genel KVKK sistemi içindeki hukuki niteliği.

7. Veri işleyen ile veri alıcısı arasındaki ayrım.

8. Veri güvenliği bakımından Madde 12/2'de düzenlenen birlikte sorumluluğun kapsamı.

## 6.5. Çözülmemiş belirsizlikler

- Müşterek veri sorumluluğunun KVKK'daki hukuki sınırları ve sorumluluk dağılımı.

- Alt veri işleyen kavramının genel KVKK uygulamasındaki kapsamı.

- SaaS sağlayıcılarının ürün geliştirme, analiz ve güvenlik faaliyetlerinde hangi durumlarda kendi amaçlarıyla veri işlediği.

- Teknik karar serbestisinin hangi noktada temel araçlar üzerinde bağımsız karar yetkisine dönüştüğü.

- Birden fazla tarafın aynı işleme faaliyetine katıldığı durumlarda sorumlulukların somut olay bazında nasıl dağıtılacağı.

## 6.6. Uzman değerlendirmesi gerektiren hususlar

- Birden fazla veri sorumlusunun bulunduğu iddialı veya karmaşık iş modelleri.

- Sözleşme ile fiilî uygulamanın ciddi biçimde farklılaştığı durumlar.

- Veri işleyenin kendi amaçları için veri kullandığı iddiaları.

- Ortak veri havuzları, çapraz müşteri veri paylaşımı ve profilleme faaliyetleri.

- Kanuni yükümlülükler nedeniyle ortaya çıkan özel rol değerlendirmeleri.

- Müşterek veri sorumluluğunun hukuki sonuçları ve taraflar arasındaki sorumluluk dağılımı.

Bu hususlarda AI tarafından oluşturulan değerlendirme, hukukçu incelemesine sunulmalıdır.

---

# 7. Kaynak bağlantıları

1. [6698 sayılı Kişisel Verilerin Korunması Kanunu — Mevzuat](https://www.aile.gov.tr/kvkk/mevzuat/)

2. [Kurulun 2020/71 sayılı Karar Özeti](https://www.kvkk.gov.tr/Icerik/6874/2020-71)

3. [Kurulun 2021/359 sayılı Karar Özeti](https://www.kvkk.gov.tr/Icerik/6966/2021-359)

4. [Kurulun 2021/1303 sayılı Karar Özeti](https://www.kvkk.gov.tr/Icerik/7288/2021-1303)

5. [KVKK — Kişisel Verilerin Korunması Kanunu Hakkında Sıkça Sorulan Sorular](https://www.kvkk.gov.tr/Icerik/4196/Kisisel-Verilerin-Korunmasi-Kanunu-Hakkinda-Sikca-Sorulan-Sorular)

6. [KVKK — Bankacılık Sektörü İyi Uygulamalar Rehberi](https://kvkk.gov.tr/SharedFolderServer/CMSFiles/12236bad-8de1-4c94-aad6-bb93f53271fb.pdf)

7. [KVKK — Veri Sorumlusu Kimdir?](https://www.kvkk.gov.tr/Icerik/2032/Veri-Sorumlusu-Kimdir)

8. [KVKK — Veri İşleyenler İçin Bağlayıcı Şirket Kuralları Yardımcı Kılavuzu](https://kvkk.gov.tr/Icerik/7937/Veri-Isleyenler-Icin-Baglayici-Sirket-Kurallarinda-Bulunmasi-Gereken-Temel-Hususlar-Yardimci-Kilavuz)

Kaynakların güncelliği ve somut olaya uygulanabilirliği, gerçek inceleme sırasında yeniden kontrol edilmelidir.
