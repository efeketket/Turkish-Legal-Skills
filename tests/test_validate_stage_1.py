import re
import unittest
from pathlib import Path

from markdown_it.tree import SyntaxTreeNode

from validate_stage_1 import (
    EVIDENCE,
    MARKDOWN,
    OUTPUTS,
    SKILL,
    TEMPLATE,
    TRANSITION,
    TRANSITION_STATUS,
    VERIFICATION,
    sections,
    table_rows,
    validate_report,
    visible_text,
)

SCENARIOS = Path(__file__).resolve().parent / "stage-1"


class StageOneValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = (SCENARIOS / "samples/incomplete-business-report.md").read_text(encoding="utf-8")
        cls.fixture = (SCENARIOS / "fixtures/incomplete-business.md").read_text(encoding="utf-8")

    def assert_has_error(self, report, message):
        errors = validate_report(report, self.fixture)
        self.assertTrue(any(message in error for error in errors), errors)

    def test_methodology_outputs_and_status_labels_match_template_contract(self):
        methodology = (SKILL / "references/stage-1-business-discovery.md").read_text(encoding="utf-8")
        tree = SyntaxTreeNode(MARKDOWN.parse(methodology))
        marker = next(i for i, node in enumerate(tree.children)
                      if node.type == "paragraph" and visible_text(node) == "Aşama çıktıları")
        declared_outputs = tree.children[marker + 1]
        self.assertEqual(declared_outputs.type, "bullet_list")
        self.assertEqual([visible_text(node) for node in declared_outputs.children], list(OUTPUTS))
        inline_labels = {node.content for node in tree.walk() if not node.is_root and node.type == "code_inline"}
        self.assertLessEqual(VERIFICATION | TRANSITION_STATUS, inline_labels)

        template = sections(TEMPLATE.read_text(encoding="utf-8"))
        for title in [*OUTPUTS, EVIDENCE, TRANSITION]:
            with self.subTest(section=title):
                self.assertEqual(len(template[title]), 1)
                self.assertTrue(table_rows(template[title][0]))

    def test_accepts_completed_report_in_both_modes(self):
        self.assertEqual(validate_report(self.report), [])
        self.assertEqual(validate_report(self.report, self.fixture), [])

    def test_accepts_equivalent_typography_without_changing_report_labels(self):
        report = self.report.replace("İşletme Tanıma Dosyası", "Isletme Tanima Dosyasi")
        report = report.replace("| Kayıt |", "| Kayit |")
        report = report.replace("Doğrulandı —", "Dogrulandi.")
        report = report.replace("Değerlendirilemedi", "Degerlendirilemedi")
        report = report.replace("Geçiş durumu ve gerekçesi: ", "**Gecis durumu ve gerekcesi.** – ")
        self.assertEqual(validate_report(report, self.fixture), [])

    def test_requires_real_headings_and_tables(self):
        for title in [*OUTPUTS, EVIDENCE, TRANSITION]:
            with self.subTest(section=title):
                report = self.report.replace(f"## {title}", f"```md\n## {title}\n```")
                self.assert_has_error(report, f"{title}: başlık")
        self.assert_has_error(self.report.replace("| Rol kaydı |", "| Başka sütun |"), "şablondaki sütunlarla")

    def test_checks_unique_typed_ids_and_references(self):
        for old, new, message in (
            ("| K-003 |", "| K-002 |", "yinelenen kayıt kimliği"),
            ("| K-003 |", "| S-003 |", "beklenen kimlik biçimi K-001"),
            ("| K-003 |", "| K-030 |", "K-003 kayıt bağlantısı bulunamadı"),
            ("| V-001 | S-001 |", "| V-001 | E-002 |", "Süreç alanındaki kayıt bağlantısı"),
            ("| K-001 | E-001 |", "| E-001 | E-001 |", "Kanıt kaydı alanındaki kayıt bağlantısı"),
        ):
            with self.subTest(old=old, new=new):
                self.assert_has_error(self.report.replace(old, new), message)

    def test_requires_explicit_gaps_and_verification_scope(self):
        for old, new, message in (
            ("| İşletme kimliği ve gelir modeli |", "| … |", "yer tutucu"),
            ("| K-001 | E-001 |", "| K-001 | — |", "bilinmeyen bilgi bir açık kayda"),
            ("| E-001 | eksik |", "| E-001 | ? |", "açık kayıt durumu geçersiz"),
            ("Doğrulandı — README metni kapsamında", "Doğrulandı", "doğrulama durumu ve sınırı"),
            ("Doğrulandı — README metni kapsamında | E-001", "Çelişkili — belge kapsamında | —", "çelişkili kanıta açık kayıt"),
        ):
            with self.subTest(old=old, new=new):
                self.assertIn(old, self.report)
                self.assert_has_error(self.report.replace(old, new), message)

    def test_accepts_only_linked_explanations_for_empty_output_sections(self):
        report = re.sub(r"(?m)^\| R-001 .*\n", "\nAçık kayıt: E-001\n", self.report)
        report = report.replace(" / R-001", "").replace("(R-001, E-001)", "(E-001)")
        self.assertEqual(validate_report(report, self.fixture), [])
        self.assert_has_error(report.replace("Açık kayıt: E-001", "Açık kayıt: E-010"), "E-010 kayıt bağlantısı")
        self.assert_has_error(report.replace("Açık kayıt: E-001", "Eksik"), "açık kayıt açıklaması")

    def test_requires_transition_criteria_reasons_status_and_handoff(self):
        for old, new, message in (
            ("Temel faaliyetler anlaşıldı", "Başka ölçüt", "her şablon ölçütü"),
            ("Prototip işlevi biliniyor, işletme kapsamı açık (B-001, E-001)", "B-001", "geçerli durum, gerekçe"),
            ("Değerlendirilemedi — işletme", "Karşılandı — işletme", "genel durum ölçütlerle tutarlı"),
            ("E-002 CSV kategorileri", "CSV kategorileri", "aktarım notunda eksik açık kayıt"),
        ):
            with self.subTest(old=old, new=new):
                self.assertIn(old, self.report)
                self.assert_has_error(self.report.replace(old, new), message)

    def test_aggregates_all_met_and_any_unmet_transition_criteria(self):
        all_met = self.report.replace("Değerlendirilemedi", "Karşılandı")
        self.assertEqual(validate_report(all_met, self.fixture), [])

        one_unmet = self.report.replace("anlaşıldı | Değerlendirilemedi", "anlaşıldı | Karşılanmadı", 1)
        self.assert_has_error(one_unmet, "genel durum ölçütlerle tutarlı")
        self.assertEqual(validate_report(one_unmet.replace("Değerlendirilemedi —", "Karşılanmadı —"), self.fixture), [])

    def test_checks_every_record_in_a_range(self):
        report = self.report.replace("E-001 işletme kapsamı ve E-002 CSV kategorileri", "E-001–E-002 aralığındaki açıklar")
        item = next(line for line in report.splitlines() if line.startswith("| E-002 |"))
        report = report.replace(item, item + "\n" + item.replace("| E-002 |", "| E-003 |"))
        report = report.replace("E-001–E-002 aralığındaki", "E-001–E-003 aralığındaki")
        self.assertEqual(validate_report(report, self.fixture), [])
        self.assert_has_error(report.replace(item + "\n", ""), "E-001–E-003 kayıt aralığı eksik")

    def test_checks_fixture_file_and_line_range_without_echoing_source(self):
        for old, new, message in (
            ("src/import.ts#L1-L4", "src/missing.ts#L1-L4", "kaynak dosya başlığı"),
            ("src/import.ts#L1-L4", "src/import.ts#L1-L40", "kaynak satır aralığı"),
            ("src/import.ts#L1-L4", "src/import.ts#L4-L1", "kaynak satır aralığı"),
            ("src/import.ts#L1-L4", "src/import.ts", "kaynak kod atfı fixture satırı"),
        ):
            with self.subTest(new=new):
                errors = validate_report(self.report.replace(old, new), self.fixture)
                self.assertTrue(any(message in error for error in errors), errors)
                self.assertNotIn(new, "\n".join(errors))

    def test_flags_each_synthetic_marker_without_echoing_it(self):
        fixture = (SCENARIOS / "fixtures/small-saas.md").read_text(encoding="utf-8")
        for marker in ("SYNTHETIC_CANARY_1807_DO_NOT_COPY", "SYNTHETIC_PERSON_1807", "SYNTHETIC_INSTRUCTION_1807"):
            with self.subTest(marker_kind=marker.split("_")[1]):
                self.assertIn(marker, fixture)
                errors = validate_report(self.report + f"\n{marker.lower()}\n", fixture)
                self.assertTrue(any("sentetik gizlilik veya talimat işaretini" in error for error in errors), errors)
                self.assertNotIn(marker.lower(), "\n".join(errors).lower())
