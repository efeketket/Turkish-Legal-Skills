import unittest
from pathlib import Path

import validate_stage_1 as stage_1
import validate_stage_3 as stage_3


SAMPLES = Path(__file__).with_name("stage-4") / "samples"
TEMPLATE = stage_1.SKILL / "assets/stage-4-outputs.md"
INTAKE = stage_1.SKILL / "references/stage-4-intake.md"


def table(path, section):
    body, = stage_1.sections(path.read_text(encoding="utf-8"))[section]
    return stage_1.table_rows(body)


class StageFourExamples(unittest.TestCase):
    def test_blocked_chain_keeps_preparation_without_condition_candidates(self):
        sample = SAMPLES / "phase-1.5-stage-4-intake.md"
        header, *handoffs = table(sample, "Devir ve hazırlık")
        self.assertEqual(header, table(INTAKE, "Devir ve hazırlık notu")[0])
        self.assertEqual(len(handoffs), 6)
        self.assertTrue(all(row[3] == "Bekletilir" and row[5] != "—" for row in handoffs))
        for section in ("İşleme şartı adayları", "Hukuki kaynak kaydı"):
            self.assertEqual(table(sample, section), table(TEMPLATE, section))

    def test_open_chain_links_candidates_to_distinct_evidence_and_legal_sources(self):
        sample = SAMPLES / "booking-stage-4-draft.md"
        _, *decisions = table(sample, "Sentetik devir girdileri")
        _, *evidence = table(sample, "Sentetik kanıt")
        _, handoff = table(sample, "Devir ve hazırlık")
        self.assertEqual(handoff[3], "Devredilebilir")
        self.assertEqual({row[0] for row in decisions}, {"Aşama 2", "Aşama 3"})
        self.assertTrue(all(row[1:4] == [handoff[0], "Aşama 4", "Devredilebilir"] for row in decisions))

        source_header, source = table(sample, "Hukuki kaynak kaydı")
        self.assertEqual(source_header, table(TEMPLATE, "Hukuki kaynak kaydı")[0])
        header, primary, alternate = table(sample, "İşleme şartı adayları")
        self.assertEqual(header, table(TEMPLATE, "İşleme şartı adayları")[0])
        self.assertEqual(primary[:3], alternate[:3])
        self.assertEqual(handoff[0], primary[0])
        self.assertNotEqual(primary[3], alternate[3])
        self.assertEqual(primary[6], "Hukukçu değerlendirmesi gerekli")
        self.assertEqual(alternate[6], "Ek kanıt gerekli")
        for row in (primary, alternate):
            self.assertEqual(stage_3.ids(row[4], "K"), {item[0] for item in evidence})
            self.assertEqual(row[5], source[0])
            self.assertIn("E-001", stage_3.ids(row[7], "E"))
        self.assertEqual(stage_3.ids(alternate[7], "E") - stage_3.ids(primary[7], "E"), {"E-002"})
