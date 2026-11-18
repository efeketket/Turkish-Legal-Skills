# KutuPanel

All excerpts are synthetic. File headings indicate where each excerpt would be found in the example repository.

## README.md

KutuPanel prototipi CSV içe aktarımı ve toplu sayım gösterir. Kim tarafından işletileceği, hedef müşterileri ve ücretlendirme henüz açıklanmadı.

## src/import.ts

```ts
function summarize(csv) {
  const rows = csvParser.parse(csv)
  return { importedRows: rows.length }
}
```

## src/index.ts

```ts
app.post('/preview', async (req, res) => {
  res.json(summarize(req.body.csv))
})
```
