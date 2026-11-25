# Turkish-Legal-Skills Phase 1.6 Aşama 3 hukuk incelemesi

Arkadaşlar, 26 Kasım 2026 tarihli hukuk incelemesinde belirlenen dokuz zorunlu düzeltmeyi güncel çalışma ağacında yeniden değerlendirmenizi rica ediyoruz. Her madde için uygulanan kuralı ve kuralın sentetik raporlardaki sonucunu birlikte inceleyin. Aşama 3’ün rol metodolojisi, çıktı şablonu ve faaliyet bazlı devri hakkında gerekçeli bir kapanış kararı verin. İnceleme sürümü `turkish-kvkk` `0.4.0`, Aşama 3 statüsü `draft-preview`. [26 Kasım hukuk inceleme raporu](history/stage2-3-review.md) · [Beceri ve aşama yönlendirmesi](../../skills/turkish-kvkk/SKILL.md)

Aşama 2’nin onaylı metodolojisini incelemenin başlangıç noktası olarak alın. Aşama 2’ye ilişkin kontrolü, bağımsız amaç için kullanılan `Yeni faaliyet` revizyon kaydının mevcut faaliyet sınırları, kimlik geçmişi, altı çıktı ve devir eşikleriyle uyumuna odaklayın. Kapanışı etkileyen bir Aşama 2 gerilemesi görürseniz ilgili kuralı ve örneği gösterin. [Aşama 2 metodolojisi](../../skills/turkish-kvkk/references/stage-2-processing-activities.md) · [Aşama 2 çıktı şablonu](../../skills/turkish-kvkk/assets/stage-2-outputs.md)

## İncelenecek dosyalar

| Kapsam | Dosyalar |
| --- | --- |
| Aşama 3 kuralları ve çıktıları | [Rol metodolojisi](../../skills/turkish-kvkk/references/stage-3-legal-roles.md) · [Teknik devir yönergesi](../../skills/turkish-kvkk/references/stage-3-integration.md) · [Çıktı şablonu](../../skills/turkish-kvkk/assets/stage-3-outputs.md) |
| Güncel Phase 1.5 zinciri | [Aşama 1](../../tests/stage-2/samples/manual-and-incomplete-stage-1.md) · [Aşama 2](../../tests/stage-2/samples/manual-and-incomplete-stage-2.md) · [Aşama 3](../../tests/stage-3/samples/phase-1.5-to-stage-3.md) |
| Ayrı KurguZiyaret rol senaryosu | [Önceki Aşama 2](../../tests/stage-3/samples/prior-stage-2.md) · [Aşama 2 yeniden incelemesi](../../tests/stage-3/samples/reviewed-stage-2.md) · [Aşama 3](../../tests/stage-3/samples/role-assessment-stage-3.md) |
| Kanıtlar ve doğrulama | [Sentetik kanıt alıntıları](../../tests/stage-3/fixtures/role-assessment.md) · [Hukuki kaynak incelemesi](../stage-3-source-review.md) · [Sentetik testler ve CLI kaydı](../../tests/stage-3/README.md) |

Kayıt kimliklerini ait oldukları zincir içinde okuyun. Güncel zincirde `A-003` tarihsel pilot kaydı, `A-004` AlfaAtölye, `A-005` BetaStüdyo faaliyetidir. Ayrı senaryoda `A-003` platform aboneliğini, `A-004` ürün metriklerini gösterir.

## Dokuz zorunlu düzeltmenin yeniden incelemesi

| Madde | İnceleme sorusu |
| --- | --- |
| Z1 · Faaliyet sınırı | Aynı faaliyetteki taraf ve operasyon bazlı rol farklılıkları mevcut kimlik altında gösterilebiliyor mu? Bağımsız amaç veya ayrı operasyonel işlev için Aşama 2’ye dönüş, kayıt geçmişi ve yeniden devir kuralları yeterli mi? |
| Z2 · Ürün metrikleri | Ayrı senaryoda `A-002` kiracı giriş kaydı olarak korunurken `A-004` için bağımsız amaç ve ayrı karar alanı yeterince gerekçelendirilmiş mi? `K-025` ile `E-010` bağlantısı gözlemin sentetik kapsamını ve bu gözlemin sözleşme ve beyanla çelişkisini doğru gösteriyor mu? |
| Z3 · Demo liste | MaviOfis ve YeşilOfis’in `K-026` ile belgelenen tasarım kararları yalnız plan kapsamında mı ele alınmış? `E-015` açık mı? Fiilî kişisel veri işleme doğrulanırsa Aşama 2’ye dönüş ve olası ortak rolün yeniden incelenmesi için aranan koşullar yeterli mi? |
| Z4 · Veri kayıt sistemi | KVKK m. 3 kapsamında sistemin kurulması, organizasyonu, yönetimi, kayıt düzeni ve erişim kuralları için karar yetkisi ayrı sorgulanıyor mu? Bu yetki amaç, temel vasıta ve teknik uygulama olgularıyla birlikte tartılıyor mu? |
| Z5 · 2021/1304 ilke kararı | İlke kararı ile 2021/1303 karar özetinin hukuki nitelikleri ve destekledikleri önermeler doğru ayrılmış mı? Araç kiralama ve kara liste bağlamı ile kaynakların bu örneğe uygulanabilirlik sınırı yeterince açık mı? |
| Z6 · Hukuki kaynak kaydı | `H-…` kayıtları kaynağın kimliğini, erişilen madde, bölüm veya sayfayı, hukuki niteliğini, desteklediği önermeyi, somut kayıt bağlantısını, kontrol tarihini ve doğrulama durumunu izlenebilir kılıyor mu? |
| Z7 · Taslak rol dili | *Güncel taslak rol değerlendirmesi* sütunu ve gerekçeler hukukçu onayı ihtiyacını görünür kılıyor mu? Eksik olguların veya doğrulanmamış kaynakların etkisi koşullu ifadeler ve açık kayıtlarla gösteriliyor mu? |
| Z8 · Faaliyet bazlı devir | `A-001` için m. 2 eşiği açıkken Aşama 4–7’nin esaslı değerlendirmesi kısıtlanıyor ve hazırlık kapsamı belirleniyor mu? `A-002` için sentetik tetikleyici ve amaç bulgusunun sınırı ile `visitRef` kişi bağına ilişkin `E-009` Aşama 4’e taşınıyor mu? Demo ve diğer faaliyetler için kısıt doğru kapsama uygulanıyor mu? |
| Z9 · Güncel sentetik zincir | Phase 1.5 envanterindeki `A-003 → A-004/A-005` geçmişi ve kapalı `E-010` korunuyor mu? Yeni metrik bulgusu `K-031/E-013` ile Aşama 2’ye dönüyor mu? `A-…`, `R-…`, `K-…`, `E-…` ve `H-…` bağlantıları iki zincirde de doğru kayda ulaşıyor mu? |

Hukuki dayanakları incelerken 6698 sayılı Kanun’un güncel metnini, özellikle m. 2, m. 3 ve m. 12/2’yi, ayrıca 2021/1304’ün yayımlanan gerekçe ve hükmünü kontrol edin. Kurul özetleri ve rehberler için eriştiğiniz bölümü ve hangi önermeyi hangi bağlamda desteklediğini belirtin. Karşılaştırmalı kaynak kullanırsanız Türk hukukundaki dayanağı ayrıca gösterin. Örneklerdeki `H-…` durumlarını çevrim dışı sentetik testin, kaynak inceleme kaydını ise ayrı kamuya açık kaynak kontrolünün sonucu olarak okuyun. Otomatik kontrollerin sonuçları ve oturum başlamadan duran canlı CLI denemeleri test kılavuzunda yer alıyor. [Kaynak inceleme kaydı](../stage-3-source-review.md) · [CLI denemeleri](../../tests/stage-3/README.md#phase-16-cli-attempts)

## Beklenen yanıt

1. **Aşama 3 kapanış kararı.** `Onaylandı`, `Düzeltme gerekli` veya `Ek kaynak ya da kanıt gerekli` seçeneklerinden birini gerekçesiyle yazın. Onayın kapsamını veya kapanışı engelleyen hususları belirtin.
2. **Z1–Z9 kabul matrisi.** Her maddeyi `Karşılandı`, `Kısmen karşılandı` veya `Karşılanmadı` olarak işaretleyin. Dosya/bölüm, varsa zincir ve kayıt kimliği, gerekçe ve gerekiyorsa önerilen değişiklik ile örnekte beklenen sonucu ekleyin.
3. **Kaynak notu ve kalan işler.** Kapanış kararını etkileyen kaynak veya kanıt eksiğini, hangi metnin, bölümün ya da olgunun gerektiğiyle birlikte yazın. Zorunlu düzeltmeleri ve isteğe bağlı iyileştirmeleri ayrı listelerde verin.
