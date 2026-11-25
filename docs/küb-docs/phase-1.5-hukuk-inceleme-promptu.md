# Turkish-Legal-Skills · Aşama 2 ve Aşama 3 hukuk incelemesi

**İncelenecek sürüm** · 24 Kasım 2026 tarihli Phase 1.5 çalışma ağacı, `turkish-kvkk` `0.4.0` yayımlanmamış inceleme sürümü, Aşama 3 `draft-preview`.

Aşama 2’deki dokuz düzeltmenin hukuk ekibinin 22 Kasım 2026 tarihli raporunu karşılayıp karşılamadığını inceleyin. Aşama 3’ün rol metodolojisini, dayanaklarını, örnek değerlendirmelerini ve Aşama 2’den devraldığı olguları ayrıca inceleyin. **Her aşama için ayrı kapanış kararı verin.** Aşama 1, bu incelemede Aşama 2 başlangıç eşiği ve kayıt devriyle sınırlıdır.

İncelemeyi paylaşılan çalışma ağacı üzerinden yapın. Aşama 2 düzeltme raporundaki `3b9e4df`, ilk incelemenin dayanağıdır. Bu teslimdeki uygulama farklarını görmek için güncel dosyaları açın. Örnekler sentetiktir. Teknik kontroller rapor sözleşmesini, kayıt bağlantılarını ve örnek davranışları sınar. Hukuki değerlendirmeler için güncel resmî kaynakları ve bunların somut olaya uygulanabilirliğini ayrıca kontrol edin.

## İnceleme dosyaları

| Kapsam | Dosyalar |
| --- | --- |
| Aşama 2 hukuk revizyonu | [Dokuz düzeltme ve 13 kabul ölçütü](history/asama2-hukuk-revizyon-raporu.md) |
| Aşama 1 → 2 başlangıcı | [Keşif metodolojisi](../../skills/turkish-kvkk/references/stage-1-business-discovery.md) · [Geçiş şablonu](../../skills/turkish-kvkk/assets/stage-1-outputs.md#aşama-geçiş-değerlendirmesi) · [Örnek Aşama 1 raporu](../../tests/stage-2/samples/manual-and-incomplete-stage-1.md) |
| Aşama 2 uygulanmış revizyon | [Metodoloji ve düzeltme eşlemesi](../../skills/turkish-kvkk/references/stage-2-processing-activities.md) · [Çıktı şablonu](../../skills/turkish-kvkk/assets/stage-2-outputs.md) · [Sentetik girdi](../../tests/stage-2/fixtures/manual-and-incomplete.md) · [Örnek rapor](../../tests/stage-2/samples/manual-and-incomplete-stage-2.md) · [Kabul matrisi ve kaynak kontrolü](../../tests/stage-2/README.md#phase-15-acceptance-evidence) |
| Aşama 3 hukuk metni ve teknik uygulama | [Hukuk ekibinin taslağı](history/asama3-hukuk.md) · [Skill içindeki hukuk metni](../../skills/turkish-kvkk/references/stage-3-legal-roles.md) · [Teknik devir yönergesi](../../skills/turkish-kvkk/references/stage-3-integration.md) · [Çıktı şablonu](../../skills/turkish-kvkk/assets/stage-3-outputs.md) · [Kaynak inceleme kaydı](../stage-3-source-review.md) |
| Aşama 2 → 3 örnek zinciri | [Aşama 1 girdisi](../../tests/stage-3/samples/prior-stage-1.md) · [Aşama 2 girdisi](../../tests/stage-3/samples/prior-stage-2.md) · [Ek sentetik kanıtlar](../../tests/stage-3/fixtures/role-assessment.md) · [Örnek Aşama 3 raporu](../../tests/stage-3/samples/role-assessment-stage-3.md) · [Teknik denemeler](../../tests/stage-3/README.md) |

## Aşama 2 · Dokuz düzeltme ve kabul kararı

1. **Faaliyet sınırları.** Ortak platformdaki bağımsız işletmelerin ayrımını ve tek amaca bağlı çok sistemli adımların bir arada tutulmasını inceleyin. İşletme adına işlem, amaç, operasyon, karar yetkisi ve ayrıştırılabilirlik için kullanılan ölçütlerin yeterliliğini değerlendirin.
2. **Veri kategorileri.** Temel kategori, somut alt kategori ve işleme amacı ayrımını kontrol edin. Özel nitelikli veri ihtimali ile doğrulanmış kategorinin ayrı ele alındığını, özellikle görsel karşılaştırma ve sağlık alanı örneklerinde değerlendirin.
3. **Manuel kayıtlar.** Fiziksel kaydın varlığı ile veri kayıt sistemi niteliğinin ayrı gerekçelendirildiğini kontrol edin. Defterin sınıflandırılması, geçmiş kayda erişim ve düzenli kullanım için aranacak olguları ve üç değerlendirme sonucunu inceleyin.
4. **Otomatik analiz.** Yalnız puanlama, karar öncesi fiilî insan incelemesi ve insan müdahalesi olmadan gerçekleşen sonucun ayrı kaydedildiğini kontrol edin. Kararı değiştirme yetkisi ve kişi üzerindeki olumsuz etki için istenecek kanıtı, m. 11/1-g bakımından sonraki incelemeye devir sınırıyla birlikte değerlendirin.
5. **Başlangıç ve devir eşikleri.** Aşama 1 → 2 için gösterilen temel çerçeveyi ve Aşama 2’de her faaliyet ve hedef için uygulanan daha ayrıntılı eşiği değerlendirin. `A-001` sınırlı ilerlerken `A-002` için `E-009` gerekçesiyle bekletmenin yerindeliğini kontrol edin. Üç ölçüt durumunun gerekçe ve kanıtla kullanıldığını doğrulayın. Özellikle farklı faaliyet veya sistem kayıtlarından kendiliğinden çelişki çıkarılmamasını ve fiziksel kayıt veya belirsiz kişi bağlantısının özel nitelik taraması yerine geçmemesini inceleyin.
6. **Ön envanter.** Altı çıktı korunurken envanterin ön çalışma niteliğinin açık olduğunu ve sonraki hukuki değerlendirmelerin kapsamının doğru gösterildiğini kontrol edin.
7. **Rol incelemesine girdi.** Taraflar, `R-…` ön rolleri, sözleşme ve talimatlar, amaç ve temel vasıta kararları, teknik kararlar, erişim, paylaşım ve alt sağlayıcı bilgilerinin `K-…` ve `E-…` bağlarıyla yeterli olup olmadığını inceleyin. Teknik gönderimin hukuki aktarım incelemesinde nasıl ele alınacağını belirtin.
8. **Kanıt kapsamı.** Beyan, sözleşme veya politika, kod, yapılandırma, test gözlemi, üretim yapılandırması, üretimde fiilî çalışma ve çıkarım ayrımını değerlendirin. Kodun veya testin desteklediği hususun üretime taşındığı bir örnek varsa gösterin. Her kanıttaki olumlu ve olumsuz doğrulama sınırının yeterliliğini kontrol edin.
9. **Gerekçeli geçmiş.** `A-003 → A-004/A-005` bölünmesinde eski tespit, tarih, kapsam, önceki ve yeni kanıt, gerekçe, bağlı çıktılar ve `E-010` durumunun izlenebilirliğini kontrol edin. Aynı yaklaşımın birleşme ve ardışık revizyonlarda yeterli olup olmadığını değerlendirin.

22 Kasım raporundaki **13 kabul ölçütünün her birini** `Karşılandı`, `Kısmen karşılandı` veya `Karşılanmadı` olarak işaretleyin. Her satırda incelenen dosya veya kayıt kimliği ve kısa gerekçe yer alsın.

## Aşama 3 · Rol metodolojisi ve kapanış kararı

1. **Rolün birimi ve karar yetkisi.** Faaliyet, alt kapsam ve taraf ilişkisinin doğru kullanıldığını inceleyin. Amaç ve temel vasıta üzerindeki fiilî yetkiyi, teknik uygulama tercihlerini, kanuni yükümlülüğü ve sözleşmede yazan sıfatı ayrı değerlendirin. Örnek rapordaki kiracı giriş kaydı, platformun abonelik faaliyeti, ürün metrikleri ve ofisin iç resepsiyon işlevini karşılaştırın.
2. **Bağımsız kullanım ve faaliyet sınırı.** Platformun kendi ürün metrikleri amacıyla yaptığı kopyanın ayrı `A-…` faaliyeti olarak Aşama 2’ye geri dönmesi gerekip gerekmediğini özellikle karara bağlayın. Aynı soruyu ortak tekrar-ziyaret listesi için değerlendirin. Ayrıştırma gerekiyorsa yeni faaliyetin kapsamını, eski-yeni kimlik bağını ve etkilenen devirleri belirtin.
3. **Birlikte karar alma.** Ortak amaç ve temel vasıtalara katkı eşiğini, bağımsız veri sorumlularından ayrımı ve müşterek veri sorumluluğuna ilişkin taslak gerekçeyi inceleyin. M. 12/2 kapsamındaki güvenlik tedbirleri sorumluluğunu rol tespitinden ayrı değerlendirin. Demo kararı ile fiilî ortak işleme arasındaki kanıt sınırını kontrol edin.
4. **Talimat, alt sağlayıcı ve çelişki.** Barındırma zincirindeki yetkilendirme ve talimatları, alt hizmet sağlayıcının teknik takdirini ve alıcı konumunun olası etkisini değerlendirin. Sözleşmenin bağımsız kullanımı dışladığı, sentetik gözlemin metrik kopyası gösterdiği örnekte olgusal kanıt ağırlığının ve hukuki değerlendirmenin ayrı tutulup tutulmadığını inceleyin.
5. **Gerekçe, hukuki kaynak ve geçiş.** Güncel 6698 sayılı Kanun metnini ve taslağın dayandığı 2020/71, 2021/359, 2021/1303 ve ilgili 2021/1304 kaynaklarını kontrol edin. Her kaynak için erişilen bölümü, niteliğini ve hangi önermeyi desteklediğini yazın. Sektörel rehberlerin hangi bağlamda kullanılabileceğini ve ek doğrulama gerektiren kaynakları belirtin. Şablondaki altı çıktı, olgusal ve hukuki durum ayrımı, 15 geçiş ölçütü ve Aşama 4–7’ye devir sınırları hakkında kapanış kararı verin.
6. **Phase 1.5 devriyle uyum.** `A-002` için önceki bekletme gerekçesinin korunmasını ve yeni sentetik kanıtla kısmi yeniden değerlendirmeyi sınayın. Kimliği belirsiz alıcı alt kapsamındaki belirsizliğin etkisini ve hangi hedef incelemeleri kısıtladığını kontrol edin. `A-…`, `R-…`, `K-…`, `E-…` ile hukuki kaynak `H-…` bağlantılarının doğru işlevde kullanıldığını değerlendirin.

## Beklenen yanıt

1. **Aşama 2 kararı** ve **Aşama 3 kararı** için ayrı ayrı `Onaylandı`, `Düzeltme gerekli` veya `Ek kaynak ya da kanıt gerekli` seçeneklerinden birini verin. Onayı engelleyen hususları açıkça belirtin. Bir bulgu yalnız belirli bir kapsamı etkiliyorsa kapsamı yazın.
2. **Aşama 2 kabul matrisi** ve **Aşama 3 madde bazlı bulgularını** ekleyin. Her düzeltme için dosya veya bölüm, varsa kayıt kimliği, dayanak, metin ya da şablon değişikliği önerisi ve örnekte beklenen sonucu yazın.
3. **Kaynak doğrulama notunda** yürürlükteki mevzuatı, Kurul karar ve özetlerini ve açıklayıcı rehberleri kendi nitelikleriyle gösterin. Erişim veya güncellik belirsizliği kapanış kararını etkiliyorsa hangi belgenin veya bölümün gerektiğini belirtin.
4. **Kapanış için zorunlu düzeltmeleri** iyileştirme önerilerinden ayırın. Onay verdiğiniz aşamada onayın kapsadığı metodoloji, şablon ve devir sınırını yazın. Somut örneklerde geçici veya koşullu kalan rol değerlendirmelerinin hangi kanıtla yeniden ele alınacağını belirtin.

**Teknik değerlendirme kaydı.** Aşama 3, Phase 1.4’te sentetik Codex CLI denemelerine alındı. Phase 1.5’te güncellenen devir otomatik regresyonlarla ve sentetik rapor zinciriyle sınandı. Bu çalışma ortamındaki Phase 1.5 CLI denemesi ana dizin hatası nedeniyle oturum başlatamadı. Canlı ajan çalışmasına ilişkin kapsam ve sonuçlar test belgelerinde yer alır. [Aşama 2 test kaydı](../../tests/stage-2/README.md#phase-15-agent-run-status) · [Aşama 3 test kaydı](../../tests/stage-3/README.md#phase-14-observations)
