import hashlib
import re
import unittest
from pathlib import Path

from markdown_it.tree import SyntaxTreeNode

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2
from validate_skills import validate_skill

SCENARIOS = Path(__file__).resolve().parent / "stage-2"
REFERENCE = stage_1.SKILL / "references" / "stage-2-processing-activities.md"


class StageTwoValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prior, cls.report = [
            (SCENARIOS / "samples" / f"manual-and-incomplete-stage-{number}.md").read_text(encoding="utf-8")
            for number in (1, 2)
        ]
        cls.fixture = (SCENARIOS / "fixtures" / "manual-and-incomplete.md").read_text(encoding="utf-8")

    def assert_change_fails(self, old, new, expected):
        self.assertIn(old, self.report)
        errors = stage_2.validate_report(self.report.replace(old, new, 1), self.prior, self.fixture)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_package_links_route_to_reference_and_template(self):
        self.assertEqual(validate_skill(stage_1.SKILL), [])
        entrypoint = (stage_1.SKILL / "SKILL.md").read_text(encoding="utf-8")
        link_sets = [
            {
                node.attrs["href"].split("#")[0]
                for node in SyntaxTreeNode(stage_1.MARKDOWN.parse(text)).walk() if node.type == "link"
            }
            for text in (entrypoint, REFERENCE.read_text(encoding="utf-8"))
        ]
        self.assertLessEqual(
            {"references/stage-2-processing-activities.md", "assets/stage-2-outputs.md"}, link_sets[0]
        )
        self.assertIn("../assets/stage-2-outputs.md", link_sets[1])

    def test_supplied_methodology_and_output_titles_are_preserved(self):
        reference = REFERENCE.read_text(encoding="utf-8")
        source = reference.split("\n", 1)[1].split("<!-- Hukuk ekibi kaynak metni sonu -->", 1)[0].rstrip("\n")
        self.assertEqual(
            hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "9b435f74cb365cdc9530c8695f001f585f6a1b40c9d4757dfeb293166a0dfef9",
        )
        outputs = source.split("4. Aşama çıktıları", 1)[1].split("5. Aşama geçiş kriteri", 1)[0]
        self.assertEqual(re.findall(r"(?m)^\d+\. (.+)$", outputs), list(stage_2.REPORT_SECTIONS[:6]))

    def test_accepts_linked_report_in_both_modes(self):
        self.assertEqual(stage_1.validate_report(self.prior, self.fixture), [])
        self.assertEqual(stage_2.validate_report(self.report, self.prior), [])
        self.assertEqual(stage_2.validate_report(self.report, self.prior, self.fixture), [])

    def test_accepts_equivalent_scope_and_absent_blockers_notation(self):
        report = self.report.replace("- Rapor niteliği: Ön çalışma", "- **Rapor niteligi** — On calisma")
        report = report.replace(" | — | Kapsamı koru", " | - | Kapsamı koru")
        self.assertEqual(stage_2.validate_report(report, self.prior), [])

    def test_requires_all_six_sections_and_transition(self):
        for title in (*stage_2.REPORT_SECTIONS[:6], stage_1.TRANSITION):
            with self.subTest(title=title):
                self.assert_change_fails(f"## {title}", "## Başka Başlık", f"{title}: başlık")

    def test_rejects_duplicate_inventory_id(self):
        self.assert_change_fails("| A-002 | KurguZiyaret", "| A-001 | KurguZiyaret", "yinelenen kayıt kimliği")

    def test_checks_view_ids_and_person_field_links(self):
        self.assert_change_fails("| A-001 | Kâğıt ziyaretçi", "| A-040 | Kâğıt ziyaretçi", "bu tabloda yer almalı")
        self.assert_change_fails(
            "| Olası ziyaretçiler | visitRef | Belirlenemedi",
            "| Olası ziyaretçiler | visitref | Belirlenemedi",
            "alan bağlantıları kategori matrisiyle uyuşmuyor",
        )

    def test_resolves_inherited_and_new_evidence_links(self):
        self.assert_change_fails("| K-020, K-021 | E-009", "| K-020, K-090 | E-009", "K-090 kayıt bağlantısı")
        self.assert_change_fails("| K-021 | A-002,", "| K-020 | A-002,", "devredilen kanıt yeniden tanımlanmış")
        self.assert_change_fails("docs/event-schema.md#L1", "docs/event-schema.md#L90", "fixture dışında")

    def test_checks_integration_with_prior_processes_flows_roles_and_gaps(self):
        self.assert_change_fails("| S-013 | A-001", "| S-001 | A-001", "önceki süreç kimliklerinin tümü")
        self.assert_change_fails("| S-013 | A-001", "| S-013 | A-002", "ana envanter bağlantıları uyuşmuyor")
        self.assert_change_fails("V-005, R-006 |", "V-001, R-001 |", "R-001 kayıt bağlantısı")
        self.assert_change_fails("| E-002 | A-001,", "| E-025 | A-001,", "önceki açık kayıt devredilmedi")

    def test_checks_record_ids_inside_a_range(self):
        self.assert_change_fails("K-020, K-021 | E-009", "K-011–K-021 | E-009", "kayıt aralığı eksik veya geçersiz")

    def test_checks_transition_and_handoff(self):
        self.assert_change_fails(
            "Olay girdisinin üst kaynağı belirsiz (A-002, K-020)",
            "Olay girdisinin üst kaynağı belirsiz",
            "geçerli durum, gerekçe ve kayıt bağlantısı gerekli",
        )
        self.assert_change_fails("Geçiş durumu ve gerekçesi: Değerlendirilemedi", "Geçiş durumu ve gerekçesi: Karşılandı",
                                 "genel durum ölçütlerle tutarlı")
        self.assert_change_fails(
            "E-002 ve A-001 için Aşama 6'ya", "A-001 için Aşama 6'ya", "aktarım notunda açık kayıt eksik (E-002)"
        )
        self.assert_change_fails(
            "| E-009 | E-009 | Olay tetikleyicisini", "| E-009 | Engelliyor | Olay tetikleyicisini",
            "kayıt bağlantısı eksik veya yanlış türde",
        )

    def test_keeps_preliminary_scope_and_flags_common_verdicts(self):
        self.assert_change_fails("Rapor niteliği: Ön çalışma", "Nihai rapor", "Ön çalışma kapsamı")
        for verdict in ("**İşletme KVKK’ya uygundur.**", "KVKK'ya aykırıdır.", "The platform is non-compliant with KVKK."):
            with self.subTest(verdict=verdict):
                errors = stage_2.validate_report(self.report + "\n" + verdict + "\n", self.prior)
                self.assertTrue(any("nihai KVKK uygunluk veya aykırılık kararı" in error for error in errors), errors)

    def test_flags_fixture_markers_without_echoing_them(self):
        fixture = (SCENARIOS.parent / "stage-1/fixtures/small-saas.md").read_text(encoding="utf-8")
        for marker in stage_1.CANARY.findall(fixture):
            with self.subTest(marker_type=marker.split("_")[1]):
                errors = stage_2.validate_report(self.report + f"\n{marker}\n", self.prior, fixture)
                self.assertTrue(any("sentetik gizlilik veya talimat işaretini" in error for error in errors), errors)
                self.assertNotIn(marker, "\n".join(errors))
