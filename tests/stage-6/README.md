# Aşama 6 · `0.8.2` doğrulama kaydı

27 Kasım 2026 kapanış incelemesi, `0.8.1` için gerçek dosyada devir, olgusal hazırlık, kanıt talebi ve belgelenmiş yöntem kararının olgu olarak aktarılmasını kabul etti. `0.8.2`, bu kapsamı koruyan bakım revizyonudur. İmha kaydının muhafazası ve yöntemin politika/prosedür bağlantısı için sentetik kanıt ile sınır durumları eklendi. Esaslı gerçek dosya taslağı için ayrı sürüm onayı ve faaliyet, ortam, kopya ve taraf bazında uygulanabilir koşulların doğrulanması gerekir. [Kapanış kararı](../../docs/küb-docs/history/asama6-kapanisimsibisey.md) · [Gelecek sürüm koşulları](../../skills/turkish-kvkk/references/stage-6-intake.md#sonraki-sürümde-esaslı-taslağın-açılması-için-koşullar)

## Kapanış raporunun sentetik senaryoları

| Senaryo | Doğrulanan örnek sonucu | Test |
| --- | --- | --- |
| Resen imhada aksi Kurul kararı | Kurgusal K-021 kapsamında yok etme seçildi. Uygulama E-020’de açık. | `test_contrary_board_decision_governs_only_the_documented_scope` |
| Resen imhada yöntem seçimi belgesiz | KurguArşiv’de politika ve arayüz gözlemi ayrı. Yöntem E-009’da açık. | `test_policy_and_observed_visibility_leave_method_selection_and_roles_open` |
| Talep edilen yöntem farklı, gerekçe açıklanmamış | Ortam 2’de seçilen yöntem ve teslim kayıtlı. Yanıttaki gerekçe E-021’de açık. | `test_explanation_content_and_delivery_leave_different_gaps` |
| Gerekçeli yanıt var, teslim kanıtı eksik | Ortam 3’te içerik ve gönderim kayıtlı. Teslim E-022’de açık. | `test_explanation_content_and_delivery_leave_different_gaps` |
| Birincil kayıt silindi, yedek veya geri yüklenen kopya kaldı | Birincil test kaydı ile K-024’te görülen iki ayrı kopya izleniyor. Kopyalar E-023’te açık. | `test_primary_deletion_does_not_close_remaining_copies_or_production` |
| Alıcıya bildirim yapıldı, alıcı işlemi tamamlanmadı | KurguAtölye’de K-014 teslimi kaydedildi. Alıcı nezdindeki uygulama ve doğrulama E-011’de açık. | `test_method_reason_delivery_and_recipient_disposal_are_independent` |
| Üç yıllık imha kaydı muhafazası gösterilemiyor | İşlem izi var. Ayrı sicil ve en az üç yıllık muhafaza E-025’te açık. | `test_operation_log_leaves_retention_and_policy_evidence_separately_open` |
| Yöntem politika veya prosedürde açıklanmamış | İşlem kanıtı, belge ve sürüm eksiğini gidermiyor. E-026 açık. | `test_operation_log_leaves_retention_and_policy_evidence_separately_open` |
| Test bulgusunun üretime genellenmesi | Birincil işlem, kopyalar ve rol yetkileri test kapsamında. Üretim E-024’te açık. | `test_primary_deletion_does_not_close_remaining_copies_or_production`, `test_related_user_scope_uses_actual_duties_and_effective_permissions` |
| İşlem tarihindeki mevzuat güncelliği doğrulanamıyor | H-001 ve H-004 karşılaştırması ve H-005/H-008 değişiklik kaydı mevcut. H-007 zaman aşımı ve E-004 açık. | `test_central_text_timeout_preserves_the_source_gap` |

KurguAtölye’de pozitif kanıt, fiziki yok etme ve test arşivinde silme işlemlerinin politika ve prosedürle bağını K-015’te, imha işlemi kayıtlarının ayrı sicilde tutulduğunu ve en az üç yıllık muhafaza ayarını K-016’da gösterir. `test_disposal_register_and_written_methods_match_recorded_operations` iki bağı ve alıcı kopyasındaki açık kaydı kontrol eder. İlgili kullanıcı örneği teknik bakım görevini müşteri işlemi yürüten destek görevinden fiilî yetki ve erişim iziyle ayırır. [KurguAtölye](samples/disposal-method-stage-6-draft.md) · [Kanıt sınırları](samples/evidence-limits-stage-6-draft.md) · [KurguArşiv](samples/backup-stage-6-draft.md) · [KurguZiyaret](samples/phase-1.5-stage-6-intake.md)

## Yerel doğrulama

```powershell
python -X utf8 tests/validate_skills.py
python -X utf8 -m unittest discover -s tests -p 'test_stage_6_examples.py'
python -X utf8 -m unittest discover -s tests
```

27 Kasım 2026’da 13 Aşama 6 testi, 91 depo testi ve iki beceri doğrulaması geçti. 126 yerel belge bağlantısı ile 12 Markdown bağlantı hedefi doğrulandı. Bu testler sentetik Markdown örneklerini ve kayıt bağlantılarını denetler. Canlı CLI doğrulaması kullanıcı dizini hatası nedeniyle açıktır. [Test dosyası](../test_stage_6_examples.py)
