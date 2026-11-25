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

    def assert_row_change_fails(self, prefix, old, new, expected):
        row = next(line for line in self.report.splitlines() if line.startswith(prefix))
        self.assertIn(old, row)
        self.assert_change_fails(row, row.replace(old, new, 1), expected)

    def reviewed_tables(self):
        errors = []
        tables, _, _ = stage_2.read_tables(self.report, errors)
        self.assertEqual(errors, [])
        return tables

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
        self.assert_change_fails("\n\nBu envanter faaliyetleri ve operasyonları belirlemeye yönelik ön çalışmadır. "
                                 "Tek başına nihai mevzuat envanteri veya KVKK uyum kararı değildir.",
                                 "\n\nBu envanter ön çalışmadır. Nihai mevzuat envanteri veya KVKK uyum kararı oluşturur.",
                                 "nihai envanter ve uyum kararı sınırı")
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

    def test_shared_platform_separates_independent_businesses_and_groups_one_operation(self):
        tables = self.reviewed_tables()
        inventory = {row["Faaliyet"]: row for row in tables[stage_2.INVENTORY]}
        self.assertIn("Alfa", inventory["A-004"]["Somut amaç özeti"])
        self.assertIn("Beta", inventory["A-005"]["Somut amaç özeti"])
        for activity in ("A-004", "A-005"):
            self.assertIn("KurguPlatform", inventory[activity]["Faaliyet sınırı ve karar alanı"])
        operations = {row["Sistem veya kayıt ortamı"] for row in tables[stage_2.OPERATIONS] if row["Faaliyet"] == "A-004"}
        self.assertIn("Alfa katılım formu, depo ve kuyruk", operations)
        self.assertIn("Nöbetçi defteri", operations)
        self.assertNotIn("A-003", {row["Faaliyet"] for row in tables[stage_2.OPERATIONS]})

    def test_purpose_is_linked_and_sensitive_signal_stays_distinct_from_classification(self):
        categories = {row["Veri alanı"]: row for row in self.reviewed_tables()[stage_2.CATEGORIES]}
        health = categories["accessAccommodation"]
        self.assertEqual(health["Özel nitelik durumu"], "Doğrulandı")
        self.assertEqual(health["Kanıt kaydı"], "K-025")
        image = categories["profilePhoto"]
        self.assertEqual(image["Özel nitelik durumu"], "İhtimal")
        self.assertEqual(image["Açık kayıt"], "E-012")
        self.assert_change_fails("| Sağlık bilgileri | Hareket kısıtlılığı", "| Pazarlama | Hareket kısıtlılığı", "pazarlama veri kategorisi")
        self.assert_change_fails("| Katılımcı formu | AlfaAtölye atölye katılımını yönetmek |",
                                 "| Katılımcı formu | Pazarlama |", "alan bağlantıları kategori matrisiyle uyuşmuyor")
        self.assert_change_fails("| K-025 | E-011 |\n| A-004 | Atölye katılımcıları | İşlem Güvenliği",
                                 "| — | E-011 |\n| A-004 | Atölye katılımcıları | İşlem Güvenliği", "doğrulanmış özel nitelik için kanıt")

    def test_manual_record_presence_has_three_possible_system_outcomes(self):
        manual = {row["Faaliyet"]: row for row in self.reviewed_tables()[stage_2.MANUAL]}
        self.assertEqual(manual["A-001"]["Sonuç"], "Veri kayıt sistemi niteliği konusunda değerlendirme için ek bilgi gerekiyor")
        self.assertEqual(manual["A-004"]["Sonuç"], "Veri kayıt sistemi niteliği doğrulandı")
        self.assertEqual(manual["A-005"]["Sonuç"], "Veri kayıt sistemi niteliği doğrulanamadı")
        self.assert_row_change_fails("| A-004 | Maskelenmiş örnekte", "Bu iki ölçütle geçmiş kayıt bulunur",
                                     "Bilinmiyor", "yapı ve erişim dayanağı")

    def test_automatic_score_review_and_automatic_refusal_behave_differently(self):
        first, second, third = self.reviewed_tables()[stage_2.AUTOMATION]
        result = "İnsan müdahalesi olmadan sonuç ve etkisi"
        review = "Fiilî insan incelemesi ve yetkisi"
        self.assertIn("kararı oluşmadı", first[result])
        self.assertIn("puanı geçersiz kılabildi", second[review])
        self.assertIn("görevlinin esaslı kararı", second[result])
        self.assertIn("insan incelemesi yok", third[review])
        self.assertIn("otomatik reddetti", third[result])
        self.assert_row_change_fails("| A-004 | Yol 3", third[result], "—", "otomatik sonuç ayrı gerekçelendirilmeli")

    def test_start_and_handoff_differ_and_missing_activity_does_not_stop_others(self):
        tables = self.reviewed_tables()
        self.assertTrue(all(row["Durum"] == "Karşılandı" for row in tables[stage_2.START]))
        decisions = {(row["Faaliyet"], row["Hedef inceleme"]): row for row in tables[stage_2.HANDOFF]}
        self.assertEqual(decisions["A-001", "Aşama 3"]["Devir durumu"], "Sınırlı devredilebilir")
        self.assertEqual(decisions["A-002", "Aşama 3"]["Devir durumu"], "Bekletilir")
        self.assertEqual(decisions["A-002", "Aşama 3"]["Açık kayıt"], "E-009")
        self.assertEqual({row["Durum"] for row in tables[stage_2.ACTIVITY_CRITERIA]}, stage_1.TRANSITION_STATUS)
        self.assert_row_change_fails("| A-002 | Aşama 3 |", "Bekletilir", "Devredilebilir", "rol incelemesi bekletilmeli")
        self.assert_row_change_fails("| A-002 | Aşama 3 |", "E-009", "E-002", "ilgili açık kayıt ve devam koşulu")
        self.assert_row_change_fails("| A-001 | Manuel ve yazılım dışı", "Fiziksel defter araştırmaya alındı, düzeni teyit edilecek (K-011).",
                                     "Açık kayıt açıldı (E-002).", "açık kayıt tek başına karşılanma gerekçesi")

    def test_old_sample_transition_does_not_infer_conflict_or_sensitive_data_from_scope(self):
        tables = self.reviewed_tables()
        global_rows = {row["Geçiş ölçütü"]: row for row in tables[stage_1.TRANSITION]}
        conflict = global_rows["Teknik bulgular ile işletme beyanları arasındaki önemli çelişkiler belirlendi"]
        sensitive = global_rows["Özel nitelikli veriler ve özel inceleme gerektiren faaliyetler işaretlendi"]
        self.assertEqual(conflict["Durum"], "Değerlendirilemedi")
        self.assertIn("ayrı faaliyet ve sistemleri", conflict["Gerekçe ve ilgili kayıtlar"])
        self.assertEqual(sensitive["Durum"], "Değerlendirilemedi")
        self.assertIn("kişi bağlantısı incelenemedi", sensitive["Gerekçe ve ilgili kayıtlar"])

    def test_test_runtime_and_production_configuration_do_not_prove_production_use(self):
        self.assert_row_change_fails("| A-002 | Bellek içi olay deposu |", "Testte gözlendi", "Üretimde gözlendi",
                                     "Üretimde gözlendi için faaliyet ve ortamla uyumlu kanıt türü")
        self.assert_row_change_fails("| A-004 | Alfa formu ve katılım deposu |", "Üretim yapılandırması |", "Üretimde gözlendi |",
                                     "Üretimde gözlendi için faaliyet ve ortamla uyumlu kanıt türü")
        self.assert_row_change_fails("| A-002 | Bellek içi olay deposu |", "K-022", "K-026", "faaliyet ve ortamla uyumlu kanıt türü")
        self.assert_row_change_fails("| A-002 | Bellek içi olay deposu |", "Sentetik olay testi", "Başka test ortamı",
                                     "faaliyet ve ortamla uyumlu kanıt türü")
        self.assert_row_change_fails("| K-022 | A-002", "Üretim etkinliği, fiilî kullanım, gerçek üst kaynak ve amaç", "—",
                                     "iki doğrulama sınırı gerekli")

    def test_role_input_keeps_preliminary_roles_and_evidence_by_activity(self):
        roles = {row["Faaliyet"]: row for row in self.reviewed_tables()[stage_2.ROLE_INPUTS]}
        self.assertEqual(roles["A-001"]["Ön roller"], "R-006")
        self.assertEqual(roles["A-002"]["Ön roller"], "R-019")
        self.assertIn("Alfa talimatına", roles["A-004"]["Sözleşme, protokol, talimat ve hizmet"])
        self.assertIn("Alfa alan, erişim ve sonuç", roles["A-004"]["Temel vasıta kararı"])
        self.assertIn("teknik bağlantı", roles["A-004"]["Erişim, kullanım ve paylaşım"])
        self.assert_row_change_fails("| A-001 | Müşteri ofisi ve iç resepsiyon", "R-006", "R-019", "ilgili ön rol kimlikleri korunmalı")

    def test_revision_keeps_previous_facts_and_split_ids_with_dated_evidence_and_gap(self):
        tables = self.reviewed_tables()
        revision, = tables[stage_2.REVISIONS]
        self.assertEqual(revision["Önceki faaliyetler"], "A-003")
        self.assertEqual(revision["Sonraki faaliyetler"], "A-004, A-005")
        self.assertEqual(revision["Önceki kanıt"], "K-023")
        self.assertIn("K-024", revision["Yeni bilgi veya kanıt"])
        self.assertEqual(revision["Açık kayıt ve revizyon sonrasındaki durum"], "E-010 / Kapatıldı")
        gap = next(row for row in tables[stage_2.GAPS] if row["Açık kayıt"] == "E-010")
        self.assertEqual(gap["Durum"], "Kapatıldı")
        self.assert_row_change_fails("| 2026-11-22 | Bölme", "2026-11-20", "2026-11-24", "tespit ve revizyon tarihleri kronolojik")
        self.assert_row_change_fails("| 2026-11-22 | Bölme", "A-004, A-005", "A-004", "bölme veya birleştirme")
        self.assert_row_change_fails("| 2026-11-22 | Bölme", "E-010 / Kapatıldı", "—", "açık kaydın revizyon sonrası durumu")
        self.assert_row_change_fails("| A-003 | KurguPlatform", "Tarihsel", "Güncel", "eski tarihsel ve yeni farklı kimlikleri")
