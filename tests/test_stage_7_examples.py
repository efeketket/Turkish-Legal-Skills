import unittest
from pathlib import Path

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2
import validate_stage_3 as stage_3


TESTS = Path(__file__).parent
SAMPLES = TESTS / "stage-7/samples"
TEMPLATE = stage_1.SKILL / "assets/stage-7-outputs.md"
HANDOFF = "Devir ve hazırlık"
INHERITED = "Devralınan kayıtlar"
NOTICE = "Aydınlatma içeriği"
TIMING = "Aydınlatma kanalı, zamanı ve ispatı"
REQUESTS = "İlgili kişi başvuruları"
ANSWERS = "Başvuru kararı, yanıt ve teslim"
RETENTION = "Saklama ve imha açıklamalarının karşılaştırılması"
RECIPIENTS = "Üçüncü kişi bildirimi ve işlem takibi"
CONTRACTS = "Sağlayıcı sözleşmesi ve fiilî uygulama"
GAPS = "Açık kayıtlar ve sonraki aşamaya devir"


class StageSevenExamples(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE.read_text(encoding="utf-8")
        self.sample = (SAMPLES / "notices-and-requests-stage-7-draft.md").read_text(encoding="utf-8")

    def table(self, sample, section):
        header, *rows = stage_3.upstream_table(sample, section)
        expected, *_ = stage_3.upstream_table(self.template, section)
        self.assertEqual(header, expected)
        return [dict(zip(header, row, strict=True)) for row in rows]

    def test_limited_role_decisions_and_missing_target_do_not_expand_restricted_scope(self):
        sample = (SAMPLES / "phase-1.5-stage-7-intake.md").read_text(encoding="utf-8")
        second = (TESTS / "stage-2/samples/manual-and-incomplete-stage-2.md").read_text(encoding="utf-8")
        third = (TESTS / "stage-3/samples/phase-1.5-to-stage-3.md").read_text(encoding="utf-8")
        self.assertFalse(any(row["Hedef inceleme"] == "Aşama 7"
                             for row in stage_3.named_upstream_rows(second, stage_2.HANDOFF)))
        decisions = {
            (row["Faaliyet"], row["Faaliyet kapsamı"]): row
            for row in stage_3.named_upstream_rows(third, stage_3.HANDOFF)
            if row["Hedef aşama"] == "Aşama 7"
        }
        handoff = self.table(sample, HANDOFF)
        inherited = self.table(sample, INHERITED)
        scopes = [tuple(row["Faaliyet, operasyon, ortam ve taraf"].split(" · ", 2)[:2]) for row in handoff]
        self.assertCountEqual(scopes, decisions)
        for scope, row in zip(scopes, handoff, strict=True):
            upstream = decisions[scope]
            self.assertEqual(row["Aşama 2 hedef kararı"], "Aşama 7 kararı bulunmuyor")
            self.assertEqual(row["Aşama 3 esaslı devir kararı"],
                             f"{upstream['Geçiş durumu']} / {upstream['Esaslı değerlendirmeye devir']}")
            self.assertEqual(row["Aşama 7 devir durumu"], "Bekletilir")
            role_records, = [item for item in inherited if item["Devir no."] == row["Devir no."]
                             and item["Kaynak rapor, dosya yolu, tarih ve sürüm"].startswith("Aşama 3")]
            self.assertEqual(stage_3.ids(role_records["Kaynak kimlikleri"]),
                             stage_3.ids(upstream["Kanıt"] + " " + upstream["Açık kayıt"]))
        for section in (NOTICE, TIMING, REQUESTS, ANSWERS, RETENTION, RECIPIENTS, CONTRACTS):
            self.assertEqual(stage_3.upstream_rows(sample, section), [])

    def test_notice_keeps_actual_recipient_indirect_timing_and_consent_evidence(self):
        notice, = self.table(self.sample, NOTICE)
        timeline, = self.table(self.sample, TIMING)
        self.assertEqual(notice["Devir no."], timeline["Devir no."])
        self.assertIn("Takvim işletmecisi", notice["Alıcı grubu ve aktarım amacı"])
        finding = notice["Fiilî karşılaştırma, kaynak ve açık kayıt"]
        self.assertIn("SMS sağlayıcısı", finding)
        self.assertEqual(stage_3.ids(finding, "E"), {"E-101"})
        self.assertTrue(timeline["Elde etme kaynağı ve zamanı"].startswith("Dolaylı"))
        self.assertIn("İlk aktarım 13.11", timeline["Yeni amaç, ilk iletişim veya ilk aktarım"])
        self.assertIn("İlk iletişim 13.11", timeline["Yeni amaç, ilk iletişim veya ilk aktarım"])
        self.assertIn("İlk gösterim 14.11", timeline["Kanal, sunulan sürüm ve zaman"])
        self.assertIn("tek onay", timeline["Aydınlatma ve açık rıza olayları"])
        status = timeline["Kanıt kapsamı, durum ve açık kayıt"]
        self.assertEqual(stage_3.ids(status, "E"), {"E-102", "E-103"})
        self.assertIn("H-105", stage_3.ids(status, "H"))

    def test_retention_notice_and_configuration_keep_their_own_evidence_limits(self):
        record, = self.table(self.sample, RETENTION)
        self.assertIn("30 gün", record["Metindeki beyan ve sürüm"])
        self.assertIn("90 gün gizleme", record["Aşama 6 politika veya yapılandırma kaydı"])
        self.assertIn("14 gün ayarı", record["Aşama 6 politika veya yapılandırma kaydı"])
        self.assertNotRegex(record["Fiilî olgu, ortam ve kopya"], r"\b(?:30|90|14) gün\b")
        self.assertIn("üretim imhası açık", record["Karşılaştırma, kanıt sınırı ve açık kayıt"])

    def test_request_outcome_method_reason_and_delivery_keep_separate_evidence(self):
        requests = self.table(self.sample, REQUESTS)
        answer_rows = self.table(self.sample, ANSWERS)
        self.assertCountEqual(
            [(row["Başvuru no."], row["Hak ve talep kapsamı"]) for row in answer_rows],
            [(row["Başvuru no."], row["Hak ve talep kapsamı"]) for row in requests],
        )
        answers = {row["Başvuru no."]: row for row in answer_rows}
        omitted_reason = answers["2"]
        pending_delivery = answers["3"]
        unexplained_rejection = answers["4"]
        self.assertTrue(omitted_reason["Karar, tarih ve iç gerekçe"].startswith("Kabul"))
        self.assertIn("yöntem gerekçesi açıklanmamış", omitted_reason["İmha yöntemi ve açıklanan gerekçesi"])
        self.assertIn("gerekçe", pending_delivery["Yanıt içeriği ve gönderim"].lower())
        self.assertIn("Teslim ve öğrenme kanıtı açık", pending_delivery["Teslim veya öğrenme"])
        self.assertTrue(unexplained_rejection["Karar, tarih ve iç gerekçe"].startswith("Ret"))
        self.assertIn("ret gerekçesi yok", unexplained_rejection["İlgili kişiye açıklanan karar gerekçesi"])
        for number, gap in (("2", "E-021"), ("3", "E-022"), ("4", "E-105")):
            self.assertEqual(stage_3.ids(answers[number]["Kanıt kapsamı, durum ve açık kayıt"], "E"), {gap})

    def test_recipient_delivery_and_contract_do_not_close_recipient_operation(self):
        notification, = self.table(self.sample, RECIPIENTS)
        contract, = self.table(self.sample, CONTRACTS)
        self.assertEqual(notification["Devir no."], contract["Devir no."])
        self.assertEqual(stage_3.ids(notification["Bildirimin kapsamı, gönderim ve teslim"], "K"), {"K-014"})
        self.assertIn("fiilî işlem bilinmiyor", notification["Alıcı işlemi ve doğrulama"])
        self.assertIn("yedek ve geri yüklenen", contract["Sözleşme sürümü, hüküm ve kapsam"])
        self.assertIn("gözlenmedi", contract["Fiilî uygulama ve kanıt sınırı"])
        self.assertEqual(stage_3.ids(notification["Takip ve açık kayıt"], "E"), {"E-011"})
        self.assertEqual(stage_3.ids(contract["Fark, istenecek kanıt ve açık kayıt"], "E"), {"E-011"})

    def test_inherited_gaps_stay_with_the_original_report_and_environment(self):
        inherited = self.table(self.sample, INHERITED)
        gaps = self.table(self.sample, GAPS)
        scenarios = (
            ("1", "KurguArşiv Aşama 6", "backup-stage-6-draft.md", {"E-004", "E-009"}),
            ("2", "KurguAtölye Aşama 6", "disposal-method-stage-6-draft.md", {"E-011"}),
            ("3", "Kanıt sınırları Aşama 6", "evidence-limits-stage-6-draft.md", {"E-021", "E-022"}),
            ("5", "KurguArşiv Aşama 6", "backup-stage-6-draft.md", {"E-006"}),
        )
        for number, label, filename, expected in scenarios:
            with self.subTest(report=label):
                upstream = (TESTS / "stage-6/samples" / filename).read_text(encoding="utf-8")
                record, = [row for row in inherited if row["Devir no."] == number]
                source = record["Kaynak rapor, dosya yolu, tarih ve sürüm"]
                self.assertIn(label, source)
                self.assertIn("27.11.2026", source)
                self.assertIn("Rapor sürümü belirtilmedi", source)
                self.assertLessEqual(expected, stage_3.ids(upstream, "E"))
                self.assertLessEqual(expected, stage_3.ids(record["Kaynak kimlikleri"], "E"))
                scope_gap, = [row for row in gaps if row["Devir no."] == number
                              and label in row["Açık kayıt ve kaynak"]]
                self.assertEqual(stage_3.ids(scope_gap["Açık kayıt ve kaynak"], "E"), expected)
        provider, = [row for row in self.table(self.sample, HANDOFF) if row["Devir no."] == "5"]
        self.assertEqual(provider["Aşama 7 devir durumu"], "Bekletilir")
