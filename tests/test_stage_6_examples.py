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
DISPOSAL = "İmha ve doğrulama"
CONTROLS = "Teknik ve idari tedbirler"
FINDINGS = "Taslak değerlendirme"
GAPS = "Açık kayıtlar ve sonraki aşamaya devir"
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
        for section in (STORAGE, DISPOSAL, CONTROLS, FINDINGS, DECISIONS):
            self.assertEqual(stage_3.upstream_rows(sample, section), [])

    def test_backup_expiry_and_restored_copy_access_keep_separate_evidence_gaps(self):
        sample = (SAMPLES / "backup-stage-6-draft.md").read_text(encoding="utf-8")
        storage = self.report_table(sample, STORAGE)
        disposal = self.report_table(sample, DISPOSAL)
        controls = self.report_table(sample, CONTROLS)
        self.assertCountEqual([row["Ortam no."] for row in storage], ["1", "2", "3"])
        self.assertCountEqual([row["Ortam no."] for row in disposal], ["1", "2", "3"])
        self.assertEqual([row["Ortam no."] for row in controls], ["3"])

        disposal_by_copy = {row["Ortam no."]: row for row in disposal}
        for copy, evidence, gap in (("1", "K-003", "E-002"),
                                    ("2", "K-004", "E-003"), ("3", "K-004", "E-005")):
            self.assertEqual(stage_3.ids(disposal_by_copy[copy]["Olgusal durum, kanıt ve açık kayıt"], "E"), {gap})
            self.assertIn(evidence, stage_3.ids(disposal_by_copy[copy]["Olgusal durum, kanıt ve açık kayıt"], "K"))

        gaps = self.report_table(sample, GAPS)
        open_ids = stage_3.ids(" ".join(row["Açık kayıt ve kaynak"] for row in gaps), "E")
        sources = {row["Kaynak kimliği"] for row in self.report_table(sample, SOURCES)}
        handoff, = self.report_table(sample, HANDOFF)
        self.assertIn("E-001", stage_3.ids(handoff["Kanıt ve açık kayıt"], "E"))
        for row in self.report_table(sample, FINDINGS):
            status = row["Durum, gerekçe ve açık kayıt"]
            self.assertEqual(status.split(" · ", 1)[0], "Ek kanıt gerekli")
            self.assertLessEqual(stage_3.ids(status, "E"), open_ids)
            self.assertLessEqual(stage_3.ids(row["Hukuki kaynak"], "H"), sources)
        self.assertEqual(self.report_table(sample, DECISIONS), [])
