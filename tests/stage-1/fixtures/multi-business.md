# OrtakSepet

All excerpts are synthetic. File headings indicate where each excerpt would be found in the example repository.

## README.md

OrtakSepet Teknoloji A.Ş. Türkiye'de satıcılara çevrimiçi sipariş paneli sunar. Ürün, finans ve destek ekipleri vardır. Satıcılar abonelik öder, kendi mağazalarını yönetir ve siparişleri gönderir. Satıcı çalışanları paneli kullanır, alıcılar mağaza sayfasından sipariş verir.

## docs/seller-agreement.md

Hizmetin tüm işlemlerinde OrtakSepet yalnızca satıcının veri işleyenidir. Teslimat için istenen alanları ve gönderim işlemlerini satıcı belirler.

## src/fulfilment.ts

```ts
async function routeOrder(order, storeSettings) {
  const parcel = pick(order, storeSettings.deliveryFields)
  await storeQueue(storeSettings.storeId).send(parcel)
}
```

## src/fraud.ts

```ts
async function flagAcrossStores(order) {
  const fingerprint = hash(order.buyerEmail)
  const score = await platformFraudIndex.scoreAcrossAllStores(fingerprint)
  if (score > PLATFORM_FRAUD_THRESHOLD) await platformReviewQueue.send(order.id)
}
```

## docs/operations.md

OrtakSepet'in risk ekibi mağazalar arası dolandırıcılık kontrolünü kendi operasyon politikası için yürütür. Eşik değerini kendi belirler. Satıcılar bu eşiği değiştiremez. Destek ekibi satıcı hesapları hakkında açılan talepleri ayrı bir kuyrukta işler.
