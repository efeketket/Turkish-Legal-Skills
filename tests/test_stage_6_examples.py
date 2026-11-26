import unittest
from pathlib import Path

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2
import validate_stage_3 as stage_3


TESTS = Path(__file__).parent
SAMPLES = TESTS / "stage-6/samples"
TEMPLATE = stage_1.SKILL / "assets/stage-6-outputs.md"
HANDOFF = "Devir ve hazırlık"
STORAGE = "Saklama ve kopyalar"
PROVIDERS = "Sağlayıcı ve dış kopya"
POLICY = "Sicil ve saklama-imha politikası"
SCHEDULE = "Resen imha ve ilgili kişi talebi"
METHODS = "İmha yöntemi seçimi ve gerekçesi"
DISPOSAL = "İmha ve doğrulama"
ACCESS = "İlgili kullanıcı ve erişim"
CONTROLS = "Teknik ve idari tedbirler"
FINDINGS = "Taslak değerlendirme"
GAPS = "Açık kayıtlar ve sonraki aşamaya devir"
EVIDENCE = "Kanıt kaydı"
SOURCES = "Hukuki kaynak kaydı"
DECISIONS = "Hukukçu karar ve onay kaydı"


class StageSixExamples(unittest.TestCase):
    def report_table(self, sample, section):
        header, *rows = stage_3.upstream_table(sample, section)
        expected, *_ = stage_3.upstream_table(TEMPLATE.read_text(encoding="utf-8"), section)
        self.assertEqual(header, expected)
        return [dict(zip(header, row, strict=True)) for row in rows]

    def test_restricted_handoffs_retain_upstream_scopes_and_gaps(self):
        sample = (SAMPLES / "phase-1.5-stage-6-intake.md").read_text(encoding="utf-8")
        second = (TESTS / "stage-2/samples/manual-and-incomplete-stage-2.md").read_text(encoding="utf-8")
        third = (TESTS / "stage-3/samples/phase-1.5-to-stage-3.md").read_text(encoding="utf-8")
        second_decisions = {
            row["Faaliyet"]: row["Devir durumu"]
            for row in stage_3.named_upstream_rows(second, stage_2.HANDOFF)
            if row["Hedef inceleme"] == "Aşama 6"
        }
        third_decisions = {
            (row["Faaliyet"], row["Faaliyet kapsamı"]): row
            for row in stage_3.named_upstream_rows(third, stage_3.HANDOFF)
            if row["Hedef aşama"] == "Aşama 6"
        }
        handoffs = self.report_table(sample, HANDOFF)
        scopes = [tuple(row["Faaliyet ve kapsam"].split(" · ", 1)) for row in handoffs]
        self.assertCountEqual(scopes, third_decisions)
        gaps = self.report_table(sample, GAPS)
        open_ids = stage_3.ids(" ".join(row["Açık kayıt ve kaynak"] for row in gaps), "E")
        for (activity, scope), row in zip(scopes, handoffs, strict=True):
            with self.subTest(activity=activity, scope=scope):
                upstream = third_decisions[activity, scope]
                self.assertEqual(row["Aşama 2 kararı"], second_decisions[activity])
                self.assertEqual(row["Aşama 3 devir durumu"],
                                 f"{upstream['Geçiş durumu']} / {upstream['Esaslı değerlendirmeye devir']}")
                self.assertEqual(row["Esaslı incelemeye devir"], "Bekletilir")
                self.assertEqual(stage_3.ids(row["Kanıt ve açık kayıt"]),
                                 stage_3.ids(upstream["Kanıt"] + " " + upstream["Açık kayıt"]))
                self.assertLessEqual(stage_3.ids(row["Kanıt ve açık kayıt"], "E"), open_ids)
        for section in (STORAGE, METHODS, DISPOSAL, CONTROLS, FINDINGS, DECISIONS):
            self.assertEqual(stage_3.upstream_rows(sample, section), [])

    def test_backup_expiry_and_restored_copy_access_keep_separate_evidence_gaps(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        storage = self.report_table(sample, STORAGE)
        disposal = self.report_table(sample, DISPOSAL)
        controls = self.report_table(sample, CONTROLS)
        evidence_ids = {row["Kanıt kimliği"] for row in self.report_table(sample, EVIDENCE)}
        self.assertCountEqual([row["Ortam no."] for row in storage], ["1", "2", "3"])
        self.assertCountEqual([row["Ortam no."] for row in disposal], ["1", "2", "3"])
        self.assertEqual([row["Ortam no."] for row in controls], ["3"])

        disposal_by_copy = {row["Ortam no."]: row for row in disposal}
        for copy, evidence, gap in (("1", "K-003", "E-002"),
                                    ("2", "K-004", "E-003"), ("3", "K-004", "E-005")):
            self.assertEqual(stage_3.ids(disposal_by_copy[copy]["Olgusal durum, kanıt ve açık kayıt"], "E"), {gap})
            cited_evidence = stage_3.ids(disposal_by_copy[copy]["Olgusal durum, kanıt ve açık kayıt"], "K")
            self.assertIn(evidence, cited_evidence)
            self.assertLessEqual(cited_evidence, evidence_ids)

        gaps = self.report_table(sample, GAPS)
        open_ids = stage_3.ids(" ".join(row["Açık kayıt ve kaynak"] for row in gaps), "E")
        sources = {row["Kaynak kimliği"] for row in self.report_table(sample, SOURCES)}
        for row in self.report_table(sample, FINDINGS):
            status = row["Durum, gerekçe ve açık kayıt"]
            self.assertEqual(status.split(" · ", 1)[0], "Ek kanıt gerekli")
            self.assertLessEqual(stage_3.ids(status, "E"), open_ids)
            self.assertLessEqual(stage_3.ids(row["Hukuki kaynak"], "H"), sources)
        self.assertEqual(self.report_table(sample, DECISIONS), [])

    def test_provider_gap_leaves_internal_test_open_for_factual_review(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        internal, provider = self.report_table(sample, HANDOFF)
        self.assertEqual(internal["Esaslı incelemeye devir"].split(" · ")[0], "Devredilebilir")
        self.assertEqual(provider["Esaslı incelemeye devir"], "Bekletilir")
        self.assertEqual(stage_3.ids(internal["Aşama 4 bağlantısı"], "E"), {"E-001"})
        self.assertEqual(internal["Aşama 5 bağlantısı"].split(" · ")[0], "Uygulanmaz")
        self.assertEqual(stage_3.ids(internal["Aşama 5 bağlantısı"], "K"), {"K-002"})
        self.assertEqual(stage_3.ids(provider["Aşama 5 bağlantısı"], "E"), {"E-006"})
        proposed_copy, = self.report_table(sample, PROVIDERS)
        self.assertEqual(stage_3.ids(proposed_copy["Kopya durumu, veri kategorileri ve kanıt sınırı"], "K"), {"K-005"})
        self.assertEqual(stage_3.ids(proposed_copy["Aşama 5, kanıt ve açık kayıt"], "E"), {"E-006"})
        for section in (STORAGE, DISPOSAL, CONTROLS, FINDINGS):
            for row in self.report_table(sample, section):
                self.assertNotIn("E-006", stage_3.ids(" ".join(row.values()), "E"))

    def test_retention_settings_and_disposal_routes_keep_distinct_evidence(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        primary, backup, _ = self.report_table(sample, STORAGE)
        self.assertIn("30 gün", primary["Politika veya sözleşme beyanı"])
        self.assertIn("90 gün", primary["Yapılandırılan süre ve işlem"])
        self.assertIn("14 gün", backup["Yapılandırılan süre ve işlem"])
        self.assertEqual(stage_3.ids(primary["Gözlenen arayüz görünürlüğü ve ortam"], "K"), {"K-003"})
        for row in (primary, backup):
            self.assertNotRegex(row["Fiilî saklama ve ortam"], r"\b(?:30|90|14) gün\b")
        policy, = self.report_table(sample, POLICY)
        self.assertEqual(stage_3.ids(policy["Kanıt ve açık kayıt"], "E"), {"E-007"})
        automatic, request = self.report_table(sample, SCHEDULE)
        self.assertIn("Resen", automatic["Ortam no. ve yol"])
        self.assertIn("İlgili kişi talebi", request["Ortam no. ve yol"])
        self.assertEqual(stage_3.ids(automatic["Hukuki kaynak, kanıt ve açık kayıt"], "E"), {"E-001", "E-007"})
        self.assertEqual(stage_3.ids(request["Hukuki kaynak, kanıt ve açık kayıt"], "E"), {"E-006", "E-008"})

    def test_central_text_timeout_preserves_the_source_gap(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        sources = {row["Kaynak kimliği"]: row for row in self.report_table(sample, SOURCES)}
        self.assertIn("Zaman aşımı", sources["H-007"]["Erişim tarihi ve durumu"])
        self.assertEqual(stage_3.ids(sources["H-007"]["Güncellik ve açık kayıt"], "E"), {"E-004"})
        gazette = sources["H-008"]
        self.assertIn("32487", gazette["Sürüm veya yürürlük"])
        self.assertIn("26.11.2026", gazette["İşlem tarihi karşılaştırması"])
        self.assertIn("H-005", stage_3.ids(gazette["İşlem tarihi karşılaştırması"], "H"))
        findings = self.report_table(sample, FINDINGS)
        self.assertTrue(any("E-004" in stage_3.ids(row["Durum, gerekçe ve açık kayıt"], "E") for row in findings))
        self.assertTrue(all("H-007" not in stage_3.ids(row["Hukuki kaynak"], "H") for row in findings))

    def test_policy_and_observed_visibility_leave_method_selection_and_roles_open(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        methods = self.report_table(sample, METHODS)
        self.assertEqual(len(methods), 3)
        for row in methods:
            self.assertTrue(row["Seçim, seçen taraf ve tarih"].startswith("Belirlenemedi"))
            self.assertIn("E-009", stage_3.ids(row["Durum ve K/E/H kayıtları"], "E"))
        management, support = self.report_table(sample, ACCESS)
        self.assertEqual(management["Ortam no."], "1")
        self.assertEqual(support["Ortam no."], "3")
        self.assertEqual(stage_3.ids(management["İlgili kullanıcı kapsamı, kanıt ve açık kayıt"]), {"K-003", "E-002"})
        self.assertEqual(stage_3.ids(support["İlgili kullanıcı kapsamı, kanıt ve açık kayıt"]), {"K-004", "E-005"})

    def test_method_reason_delivery_and_recipient_disposal_are_independent(self):
        sample = (SAMPLES / "disposal-method-stage-6-draft.md").read_text(encoding="utf-8")
        automatic, requested = self.report_table(sample, METHODS)
        explanation = "İlgili kişiye yöntem açıklaması ve kanıtı"
        self.assertIn("Yok etme", automatic["Seçim, seçen taraf ve tarih"])
        self.assertEqual(stage_3.ids(automatic[explanation], "K"), set())
        self.assertIn("Yok etme", requested["Talep edilen yöntem"])
        self.assertIn("Silme", requested["Seçim, seçen taraf ve tarih"])
        self.assertEqual(stage_3.ids(requested[explanation], "K"), {"K-013"})
        request, = self.report_table(sample, SCHEDULE)
        self.assertEqual(stage_3.ids(request["Üçüncü kişiye bildirim"], "K"), {"K-014"})
        self.assertEqual(stage_3.ids(request["Üçüncü kişi işlemi ve takip"]), {"E-011"})
        self.assertIn("30 gün", request["Uygulanacak süre ve son tarih"])
