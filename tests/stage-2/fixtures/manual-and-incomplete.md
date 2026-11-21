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
