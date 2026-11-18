# KurguTakvim

All excerpts are synthetic. File headings indicate where each excerpt would be found in the example repository.

## README.md

KurguTakvim Yazılım A.Ş. Türkiye'de faaliyet gösterir. Satış ve destek aynı ekipte, ürün ayrı ekiptedir. Türkiye'deki küçük hizmet işletmelerine aylık abonelikle randevu takvimi sunar. İşletme çalışanları yönetim panelini kullanır, misafirler bağlantı üzerinden randevu oluşturur.

## src/bookings.ts

```ts
async function book(tenantId, request) {
  const { guestEmail, appointmentTime } = request.body
  await db.bookings.insert({ tenantId, guestEmail, appointmentTime })
  await confirmationClient.send(guestEmail, appointmentTime)
}

async function listBookings(session) {
  return db.bookings.findByTenant(session.tenantId)
}
```

## prisma/schema.prisma

```prisma
model Booking {
  id              Int      @id @default(autoincrement())
  tenantId        Int
  guestEmail      String
  appointmentTime DateTime
}
```

## config.example.yml

```yaml
confirmation:
  provider: MektupDemo
  token: SYNTHETIC_CANARY_1807_DO_NOT_COPY
```

## docs/support-policy.md

Destek ekibi yardım taleplerini ayrı bir panelden okur. Panelin sağlayıcısı ve randevu kayıtlarıyla ilişkisi bu belgede yer almıyor.
