import unittest
from pathlib import Path

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2
import validate_stage_3 as stage_3


TESTS = Path(__file__).parent
SAMPLES = TESTS / "stage-5" / "samples"
TEMPLATE = stage_1.SKILL / "assets/stage-5-outputs.md"
HANDOFF = "Devir ve hazırlık"
FLOWS = "Aktarım akışları"
MECHANISMS = "Aktarım şartı ve mekanizma adayları"


def table(path, section):
    body, = stage_1.sections(path.read_text(encoding="utf-8"))[section]
    return stage_1.table_rows(body)


class StageFiveExamples(unittest.TestCase):
    def report_table(self, sample, section):
        header, *rows = table(sample, section)
        self.assertEqual(header, table(TEMPLATE, section)[0])
        return [dict(zip(header, row, strict=True)) for row in rows]

    def test_deferred_transfer_keeps_upstream_target_decisions_and_evidence(self):
        sample = SAMPLES / "phase-1.5-stage-5-intake.md"
        second = (TESTS / "stage-2/samples/manual-and-incomplete-stage-2.md").read_text(encoding="utf-8")
        third = (TESTS / "stage-3/samples/phase-1.5-to-stage-3.md").read_text(encoding="utf-8")
        fourth = (TESTS / "stage-4/samples/phase-1.5-stage-4-intake.md").read_text(encoding="utf-8")
        stage_two_decisions = {
            row["Faaliyet"]: row["Devir durumu"]
            for row in stage_3.named_upstream_rows(second, stage_2.HANDOFF)
            if row["Hedef inceleme"] == "Aşama 5"
        }
        stage_three_decisions = {
            (row["Faaliyet"], row["Faaliyet kapsamı"]): row
            for row in stage_3.named_upstream_rows(third, stage_3.HANDOFF)
            if row["Hedef aşama"] == "Aşama 5"
        }
        stage_four_handoffs = {
            row["Faaliyet ve kapsam"]: row for row in stage_3.named_upstream_rows(fourth, HANDOFF)
        }
        handoffs = self.report_table(sample, HANDOFF)
        scopes = [tuple(row["Faaliyet ve aktarım kapsamı"].split(" · ", 1)) for row in handoffs]
        self.assertEqual(len(scopes), 6)
        self.assertCountEqual(scopes, stage_three_decisions.keys())
        for (activity, scope), row in zip(scopes, handoffs, strict=True):
            with self.subTest(activity=activity, scope=scope):
                previous = stage_three_decisions[activity, scope]
                decision = row["Aşama 2 kararı"].split(" · ", 1)[0]
                self.assertEqual(decision, stage_two_decisions.get(activity, "Aşama 5 için karar yok"))
                self.assertEqual(row["Aşama 3 devir durumu"].split(" / "),
                                 [previous["Geçiş durumu"], previous["Esaslı değerlendirmeye devir"]])
                self.assertEqual(row["Esaslı incelemeye devir"], "Bekletilir")
                self.assertTrue(row["Hazırlık işi, engel ve devam koşulu"])
                self.assertEqual(stage_3.ids(row["Kanıt ve açık kayıt"]),
                                 stage_3.ids(previous["Kanıt"] + " " + previous["Açık kayıt"]))
                stage_four_scope = stage_four_handoffs[row["Faaliyet ve aktarım kapsamı"]]
                self.assertEqual(stage_four_scope["Esaslı incelemeye devir"], "Bekletilir")
                self.assertEqual(stage_3.ids(row["Aşama 4 işleme şartı bağlantısı"], "E"),
                                 stage_3.ids(stage_four_scope["Engelleyen açık ve devam koşulu"], "E"))
        for section in (FLOWS, MECHANISMS, "Hukuki kaynak kaydı"):
            self.assertEqual(self.report_table(sample, section), [])

    def test_domestic_and_foreign_flows_keep_separate_mechanisms_and_open_records(self):
        sample = SAMPLES / "hosting-stage-5-draft.md"
        _, *decisions = table(sample, "Sentetik devir girdileri")
        self.assertTrue(all(row[2:4] == ["Aşama 5", "Devredilebilir"] for row in decisions))
        handoffs = self.report_table(sample, HANDOFF)
        self.assertTrue(all(row["Esaslı incelemeye devir"] == "Devredilebilir" for row in handoffs))
        self.assertCountEqual([row[1] for row in decisions if row[0] == "Aşama 3"],
                              [row["Faaliyet ve aktarım kapsamı"] for row in handoffs])
        domestic, foreign = self.report_table(sample, FLOWS)
        self.assertCountEqual([row["Faaliyet ve aktarım kapsamı"] for row in (domestic, foreign)],
                              [row["Faaliyet ve aktarım kapsamı"] for row in handoffs])
        self.assertNotEqual(domestic["Akış no."], foreign["Akış no."])
        self.assertNotEqual(domestic["Alıcı ve rol"], foreign["Alıcı ve rol"])
        self.assertTrue(domestic["Yön ve sonraki aktarım"].startswith("Yurt içi"))
        self.assertTrue(foreign["Yön ve sonraki aktarım"].startswith("Yurt dışı"))
        for flow in (domestic, foreign):
            self.assertIn("sentetik", flow["İletim veya erişim, ortam ve sıklık"])

        mechanism_rows = self.report_table(sample, MECHANISMS)
        self.assertEqual(len(mechanism_rows), 2)
        candidates = {row["Akış no."]: row for row in mechanism_rows}
        self.assertEqual(set(candidates), {domestic["Akış no."], foreign["Akış no."]})
        domestic_candidate = candidates[domestic["Akış no."]]
        foreign_candidate = candidates[foreign["Akış no."]]
        self.assertIn("m. 8/2-a", domestic_candidate["Aday hüküm ve mekanizma"])
        self.assertIn("m. 9/4-c", foreign_candidate["Aday hüküm ve mekanizma"])
        self.assertIn("Koşullu", foreign_candidate["Aday hüküm ve mekanizma"])
        self.assertIn("m. 9/1", foreign_candidate["Mekanizma koşulları ve kanıt sınırı"])
        self.assertIn("m. 9/5", foreign_candidate["Güvence, izin, bildirim ve önlemler"])
        self.assertCountEqual(stage_3.ids(domestic_candidate["Açık kayıt ve istenecek kanıt"], "E"), {"E-001"})
        self.assertCountEqual(stage_3.ids(foreign_candidate["Açık kayıt ve istenecek kanıt"], "E"),
                              {"E-002", "E-003", "E-004"})
        sources = {row["Kaynak kimliği"] for row in self.report_table(sample, "Hukuki kaynak kaydı")}
        open_records = set().union(*(stage_3.ids(row["Açık kayıt ve kaynak"], "E")
                                     for row in self.report_table(sample, "Açık kayıtlar")))
        for row in candidates.values():
            self.assertTrue(row["Taslak durum ve gerekçe"].startswith("Ek kanıt gerekli"))
            references = stage_3.ids(row["Hukuki kaynak"], "H")
            self.assertTrue(references)
            self.assertLessEqual(references, sources)
            self.assertLessEqual(stage_3.ids(row["Açık kayıt ve istenecek kanıt"], "E"), open_records)
