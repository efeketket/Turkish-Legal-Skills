# DenemeDosya

All excerpts are synthetic. File headings indicate where each excerpt would be found in the example repository.

## İşletmenin görüşme beyanı

"Kullanıcımızın yüklediği dosyanın içeriği hiçbir dış sağlayıcıya gitmez. Depolama yalnızca Türkiye'de çalışır."

## README.md

DenemeDosya Bilişim Ltd. Şti., Türkiye'deki kurumsal müşterilerine yıllık abonelikle doküman paylaşım hizmeti verir. Ürün ve operasyon ekipleri bulunur. Müşteri çalışanları dosya yükler, müşteri yöneticileri paylaşım bağlantısı oluşturur.

## src/upload.ts

```ts
async function upload(request) {
  await objectStore.put(request.body.bytes, { key: request.body.filename })
  await scanner.submit(request.body.bytes)
  await events.track('upload_completed', { accountId: request.account.id })
}
```

## deploy/staging.yml

```yaml
environment: staging
objectStore:
  provider: DepoDemo
  region: demo-eu
scanner:
  provider: TaraDemo
events:
  provider: OlcumDemo
```

## docs/vendor-list.md

DepoDemo nesne depolama, TaraDemo zararlı içerik taraması ve OlcumDemo ürün analitiği sağlar. Liste test ortamı için hazırlanmıştır. Üretim yapılandırması bu örnekte paylaşılmadı.
