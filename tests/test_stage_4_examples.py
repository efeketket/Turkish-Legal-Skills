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
        for row, expected_gaps in zip(
            handoffs,
            ({"E-002"}, {"E-009"}, {"E-009", "E-016"}, {"E-011"}, {"E-012"}, {"E-012"}),
            strict=True,
        ):
            self.assertEqual(row[3], "Bekletilir")
            self.assertTrue(all(cell and cell != "—" for cell in row[5:10]))
            self.assertEqual(stage_3.ids(row[9], "E"), expected_gaps)
            self.assertLessEqual(expected_gaps, stage_3.ids(row[10], "E"))
        for section in ("İşleme şartı adayları", "Hukuki kaynak kaydı"):
            self.assertEqual(table(sample, section), table(TEMPLATE, section))

    def test_open_chain_links_candidates_to_distinct_evidence_and_legal_sources(self):
        sample = SAMPLES / "booking-stage-4-draft.md"
        _, *decisions = table(sample, "Sentetik devir girdileri")
        _, *evidence = table(sample, "Sentetik kanıt")
        handoff_header, handoff = table(sample, "Devir ve hazırlık")
        self.assertEqual(handoff_header, table(INTAKE, "Devir ve hazırlık notu")[0])
        self.assertEqual(handoff[3], "Devredilebilir")
        self.assertEqual({row[0] for row in decisions}, {"Aşama 2", "Aşama 3"})
        self.assertTrue(all(row[1:4] == [handoff[0], "Aşama 4", "Devredilebilir"] for row in decisions))

        source_header, *sources = table(sample, "Hukuki kaynak kaydı")
        self.assertEqual(source_header, table(TEMPLATE, "Hukuki kaynak kaydı")[0])
        header, contract, legitimate_interest = table(sample, "İşleme şartı adayları")
        self.assertEqual(header, table(TEMPLATE, "İşleme şartı adayları")[0])
        self.assertEqual(contract[1:4], legitimate_interest[1:4])
        self.assertEqual(handoff[0], contract[1])
        self.assertNotEqual(contract[0], legitimate_interest[0])
        self.assertIn("m. 5/2-c", contract[4])
        self.assertIn("m. 5/2-f", legitimate_interest[4])
        self.assertTrue(contract[7].startswith("Hukukçu değerlendirmesi gerekli ·"))
        self.assertTrue(legitimate_interest[7].startswith("Ek kanıt gerekli ·"))
        source_ids = {item[0] for item in sources}
        evidence_ids = {item[0] for item in evidence}
        _, *gaps = table(sample, "Açık kayıtlar")
        gap_ids = {item[0] for item in gaps}
        for row in (contract, legitimate_interest):
            self.assertEqual(stage_3.ids(row[5], "K"), evidence_ids)
            self.assertLessEqual(stage_3.ids(row[6], "H"), source_ids)
            self.assertLessEqual(stage_3.ids(row[8], "E"), gap_ids)
        self.assertEqual(stage_3.ids(contract[6], "H"), {"H-001"})
        self.assertEqual(stage_3.ids(legitimate_interest[6], "H"), {"H-001", "H-002"})
        self.assertEqual(stage_3.ids(contract[8], "E"), {"E-001"})
        self.assertEqual(stage_3.ids(legitimate_interest[8], "E"), {"E-001", "E-002"})

        section = "Adayın kurucu unsurları"
        element_header, *elements = table(sample, section)
        self.assertEqual(element_header, table(TEMPLATE, section)[0])
        self.assertCountEqual(
            [(row[0], row[1]) for row in elements],
            [(contract[0], label) for label in (
                "Sözleşmeyle doğrudan bağlantı", "Sözleşme tarafının verisi", "Veri ve işlem gerekliliği"
            )] + [(legitimate_interest[0], label) for label in ("Amaç ve meşru menfaat", "Zorunluluk", "Denge")],
        )
        for row in elements:
            self.assertLessEqual(stage_3.ids(row[3], "K"), evidence_ids)
            self.assertLessEqual(stage_3.ids(row[4], "E"), gap_ids)
            if "K-002" in stage_3.ids(row[3], "K"):
                self.assertRegex(row[3].casefold(), r"sentetik|test")

        principles_header, *principles = table(sample, "m. 4 genel ilkeler kontrolü")
        self.assertEqual(principles_header, table(TEMPLATE, "m. 4 genel ilkeler kontrolü")[0])
        self.assertEqual(len({row[2] for row in principles}), 5)
        self.assertTrue(all(row[0] == handoff[0] for row in principles))
        decision_header, decision = table(sample, "Adaylar ve hukukçu kararı")
        self.assertEqual(decision_header, table(TEMPLATE, "Adaylar ve hukukçu kararı")[0])
        self.assertEqual(decision[3:], ["Hukukçu kararı bekleniyor", "—"])
