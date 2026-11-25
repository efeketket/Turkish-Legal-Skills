# KurguZiyaret

Sentetik işletme ve depo alıntıları. Her dosya başlığı örnekteki kaynak konumunu gösterir.

## README.md

KurguZiyaret A.Ş. Türkiye'deki ofislere abonelikle ziyaret yönetimi sunar. Ofis resepsiyon ekipleri ziyaretçi girişini yönetir. KurguZiyaret'in destek ekibi uygulama sorunlarını takip eder.

## src/events.ts

```ts
async function storeVisitEvent(input) {
  await events.append({ visitRef: input.visitRef, checkedInAt: input.checkedInAt })
}
```

## docs/event-schema.md

`visitRef` bir ziyaret referansı ve `checkedInAt` giriş zamanı olarak şemada adlandırılmıştır. Referansın hangi kayıtla ilişkilendirildiği belirtilmemiştir.

## İşletmenin görüşme beyanı

Resepsiyon görevlileri beklenen ziyaretçilerin adını ziyaretçiden alıp kâğıt ziyaretçi defterine yazar. Defter girişte ziyaretçiyi tanımak ve bina erişimini yönetmek için kullanılır. Defter ayrı bir manuel kayıt ortamıdır. Deftere kimlerin eriştiği ve kayıtların ne zaman imha edildiği henüz doğrulanmadı. Uygulamadaki ziyaret olayının hangi kaynaktan geldiği ve saklanmasının somut amacı paylaşılmadı.

## tests/event-append.md

21 Kasım 2026 sentetik entegrasyon testi. Yapay girdi ve bellek içi depo ile `storeVisitEvent` çağrısı bir olay ekledi. Üretim sistemine gidilmedi.

## docs/pilot-initial.md

20 Kasım 2026 ilk pilot notu. KurguPlatform üzerinde AlfaAtölye ve BetaStüdyo için tek ortak giriş süreci öngörüldü. Amaçları ve karar yetkileri ayrı incelenmedi.

## docs/pilot-agreement.md

22 Kasım 2026 tarihli maskelenmiş sentetik protokol. AlfaAtölye atölye katılımı, BetaStüdyo stüdyo ziyaretini kendi adına ve bağımsız olarak yönetir. Her biri kendi alan, erişim ve sonuç kararını alır. KurguPlatform talimatları kapsamında form ve depo işletir.
AlfaAtölye form, katılım deposu, bildirim kuyruğu ve nöbetçi defterini aynı atölye giriş sürecinde kullanır. BetaStüdyo ayrı ziyaret formu kullanır. Bir ofisin verisi diğerinin sürecine girdi olmaz.

## docs/alfa-fields.md

Sentetik alan sözlüğü. `accessAccommodation` hareket kısıtlılığına ilişkin sağlık bilgisi beyanının alanıdır. `riskScore` giriş kontrolüne yönelik test puanıdır. Değerler paylaşılmadı.
Maskelenmiş defter düzeni. Nöbetçiler giriş sırasında aynı başlıkları kullanır, kayıtlar tarih ve ziyaret koduna göre düzenlenir. Geçmiş kayıt bu iki kriterle bulunup giriş teyidinde kullanılır. Örnek erişim görevlilerle sınırlı, imha süresi paylaşılmadı.

## tests/alfa-entry.md

Sentetik giriş senaryosu testi. Birinci yol puan gösterir, herhangi bir giriş kararı üretmez.
İkinci yolda görevli başvuruyu karar öncesi inceler, puanı geçersiz kılabilir ve sentetik denemede girişe izin verir.
Üçüncü yolda kural düşük puanda giriş isteğini incelemesiz reddeder. Sentetik kullanıcı onay alamaz. Üretim çalışması incelenmedi.

## docs/beta-policy.md

BetaStüdyo politikası. Ziyaret girişi için `profilePhoto` istenebildiği ve arayüzde bir görüntü karşılaştırma seçeneği bulunduğu yazıyor. Karşılaştırmanın yöntemi, kişi tanımlama amacı ve kullanımı belgede açıklanmıyor.
Nöbetçinin bazen gelişigüzel kâğıt not aldığı yazıyor. Düzenli olup olmadığı, notların sınıflandırılması, aranabilirliği ve imhası bilinmiyor.

## config/alfa-prod-example.md

22 Kasım 2026 maskelenmiş sentetik üretim yapılandırması örneğinde formdan katılım deposuna yazma bağlantısı etkin. Kapsam yalnız yapılandırma. Üretimde gerçekleşen kayda ilişkin çalışma kaydı sağlanmadı.
