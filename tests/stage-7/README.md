# Aşama 7 · Tasarım ve sentetik doğrulama

27 Kasım 2026 tarihli `0.8.2` incelemesi Aşama 7’nin tasarım ve sentetik hazırlığına geçişi kabul etti. Örneklerde metin, sunum ve fiilî uygulama ayrı dayanaklara bağlanır. Aşama 6 açıkları kendi faaliyet, kaynak rapor ve ortamlarıyla korunur. [Geçiş kararı](../../docs/küb-docs/efekalpkubra.md) · [Hukuk incelemesi](../../docs/küb-docs/asama-7-hukuk-inceleme-promptu.md)

## Senaryolar

| Senaryo | Beklenen kayıt |
| --- | --- |
| Metindeki alıcı grubu fiilî alıcıdan farklı | Açıklanan takvim işletmecisi ile gözlenen SMS sağlayıcısı ayrı. `E-101` açık. |
| Saklama açıklaması yapılandırmayla çelişiyor | 30 günlük beyan, 90 günlük gizleme ve 14 günlük yedek ayarı kendi amaç ve ortamlarıyla gösterilir. Üretim imhası açık. |
| Dolaylı elde etmede geç aydınlatma | Sentetik ilk aktarım ve ilk iletişim, ilk gösterimden önce. `E-102` açık. |
| Aydınlatma ve rıza tek olay | Birleşik metin ve tek onay kanıtı, ayrı sunum ve rıza adımlarının araştırılmasına bağlanır. `E-103` açık. |
| Yanıt hazırlanmış ve gönderilmiş, teslim kanıtı yok | İkinci A-012 başvurusu. Aşama 6 `E-022` açık. |
| İç ret gerekçesi ilgili kişiye açıklanmamış | A-013 kararında gerekçe var, teslim edilen yanıtta ret sonucu var. `E-105` açık. |
| Kabul edilmiş imha talebinde yöntem gerekçesi açıklanmamış | İlk A-012 başvurusu. Aşama 6 `E-021` açık. |
| Alıcıya bildirim teslim edilmiş, işlem kanıtı eksik | A-011 ortam 3 için teslim ve imha ayrı. KurguAtölye `E-011` açık. |
| Sözleşmede silme taahhüdü var, kopya uygulaması açık | A-011 ana kayıt, yedek ve geri yükleme için fiilî sağlayıcı uygulaması açık. |
| Devralınan kaydın kapsamı ve durumu | `E-004`, `E-009` ve `E-011` kaynak dosya ve ortamına bağlı. KurguZiyaret’te altı kapsam önceki kararlarıyla beklemede. |

[Aydınlatma ve başvuru örneği](samples/notices-and-requests-stage-7-draft.md) · [KurguZiyaret devir örneği](samples/phase-1.5-stage-7-intake.md) · [Örnek kontrolleri](../test_stage_7_examples.py)

```powershell
python -X utf8 tests/validate_skills.py
python -X utf8 -m unittest discover -s tests -p 'test_stage_7_examples.py'
python -X utf8 -m unittest discover -s tests
```

Bu kontroller depodaki örneklerin şablon, kanıt ve devir ilişkilerini denetler. Gerçek dosya yönlendirmesi için ayrıca hukukçu incelemesi gerekiyor.
