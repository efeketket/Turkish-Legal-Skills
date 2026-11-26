import unittest
from pathlib import Path

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2
import validate_stage_3 as stage_3


TESTS = Path(__file__).parent
SAMPLES = TESTS / "stage-5" / "samples"
MASKED_INPUT = TESTS / "stage-5" / "fixtures" / "masked-stage-5-input.md"
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
        self.assertIn("Yurt içi", domestic["Aktarım hedefi ve yön"])
        self.assertIn("Yurt dışı", foreign["Aktarım hedefi ve yön"])
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
        self.assertIn("Aşama 4 aday 1", domestic_candidate["Aşama 4 kayıt kimliği ve kapsam eşleşmesi"])
        self.assertIn("Aşama 4 aday 2", foreign_candidate["Aşama 4 kayıt kimliği ve kapsam eşleşmesi"])
        self.assertEqual(stage_3.ids(domestic_candidate["Açık kayıt ve istenecek kanıt"], "E"), {"E-001", "E-011"})
        self.assertEqual(stage_3.ids(foreign_candidate["Açık kayıt ve istenecek kanıt"], "E"),
                         {"E-002", "E-003", "E-004", "E-011"})
        sources = {row["Kaynak kimliği"] for row in self.report_table(sample, "Hukuki kaynak kaydı")}
        open_records = set().union(*(stage_3.ids(row["Açık kayıt ve kaynak"], "E")
                                     for row in self.report_table(sample, "Açık kayıtlar")))
        for row in candidates.values():
            self.assertTrue(row["Taslak durum ve gerekçe"].startswith("Ek kanıt gerekli"))
            references = stage_3.ids(row["Hukuki kaynak"], "H")
            self.assertTrue(references)
            self.assertLessEqual(references, sources)
            self.assertLessEqual(stage_3.ids(row["Açık kayıt ve istenecek kanıt"], "E"), open_records)

    def test_hosting_keeps_country_law_contract_signature_notification_and_use_open(self):
        sample = SAMPLES / "hosting-stage-5-draft.md"
        domestic, = self.report_table(sample, "Yurt içi aktarım kontrolleri")
        self.assertIn("E-001", domestic["m. 8/2-a bendin kurucu unsurları"])
        foreign, = self.report_table(sample, "Yurt dışı aktarım yolları")
        rights, = self.report_table(sample, "m. 9/4 hak ve başvuru yolları")
        occasional, = self.report_table(sample, "m. 9/6 arızilik ve bent incelemesi")
        self.assertEqual({foreign["Akış no."], rights["Akış no."], occasional["Akış no."]}, {"2"})
        self.assertTrue(foreign["m. 9/1 yeterlilik durumu ve kapsamı"].startswith("Araştırılıyor"))
        self.assertTrue(rights["Durum, kaynak ve açık kayıt"].startswith("Ek kanıt gerekli"))
        self.assertEqual(occasional["m. 9/6 bendi ve kurucu koşulları"], "—")
        self.assertIn("K-003", occasional["Sıklık ve süreklilik"])

        contract_records = {
            row["İncelenen kayıt"]: row for row in self.report_table(sample, "Standart sözleşme ve bildirim kayıtları")
        }
        expected_open_records = {
            "Taraf, rol ve Kurul metni": "E-005", "Temsil ve imzalar": "E-006",
            "Nihai metin ve ekler": "E-007", "m. 9/5 bildirimi": "E-008", "Fiilî uygulama": "E-009",
        }
        self.assertEqual(set(contract_records), set(expected_open_records))
        for name, gap in expected_open_records.items():
            row = contract_records[name]
            self.assertEqual(row["Akış no."], "2")
            self.assertEqual(stage_3.ids(row["Açık kayıt ve istenecek kanıt"], "E"), {gap})
            self.assertTrue(row["Durum ve gerekçe"].startswith("Ek kanıt gerekli"))
        self.assertIn("metin bütünlüğü", contract_records["Taraf, rol ve Kurul metni"]["Durum ve gerekçe"])
        self.assertIn("Türkçe metindeki imzalar",
                      contract_records["Temsil ve imzalar"]["Açık kayıt ve istenecek kanıt"])
        notification = contract_records["m. 9/5 bildirimi"]
        self.assertIn("belirlenip belirlenmediği açık", notification["Durum ve gerekçe"])
        self.assertIn("belirleme yapılmamışsa veri aktaran", notification["Durum ve gerekçe"])
        self.assertIn("H-007", stage_3.ids(notification["Kanıt, tarih ve sürüm"], "H"))
        sources = {row["Kaynak kimliği"]: row for row in self.report_table(sample, "Hukuki kaynak kaydı")}
        for source_id, issue in (("H-005", "29677"), ("H-006", "32487"), ("H-007", "32598")):
            self.assertIn(issue, sources[source_id]["Erişilen bölüm"])
            self.assertIn("E-011", stage_3.ids(sources[source_id]["Güncellik kontrolü ve açık kayıt"], "E"))
        self.assertEqual(self.report_table(sample, "Hukukçu karar ve onay kaydı"), [])

    def test_remote_access_and_onward_transfer_are_mapped_while_stage_four_linkage_is_open(self):
        sample = SAMPLES / "remote-support-stage-5-intake.md"
        domestic, remote_access, onward = self.report_table(sample, FLOWS)
        self.assertEqual(domestic["Barındırma ülkesi"], remote_access["Barındırma ülkesi"])
        self.assertEqual(remote_access["Barındırma ülkesi"], "Türkiye")
        self.assertEqual(remote_access["Erişim yetkisi ülkeleri"], "Almanya")
        self.assertEqual(remote_access["Fiilî erişim ülkeleri"], "Almanya")
        self.assertIn("İndirme belirsiz", remote_access["Fiilî erişim ve indirme"])
        self.assertEqual(onward["Önceki akış no."], remote_access["Akış no."])
        chain, = self.report_table(sample, "Sonraki aktarım ve güvence bağlantısı")
        self.assertEqual(chain["İlk akış no."], remote_access["Akış no."])
        self.assertEqual(chain["Önceki akış no."], remote_access["Akış no."])
        self.assertEqual(chain["Sonraki akış no."], onward["Akış no."])
        self.assertIn("E-004", stage_3.ids(chain["Kanıt ve açık kayıt"], "E"))

        handoffs = self.report_table(sample, HANDOFF)
        self.assertTrue(all(row["Esaslı incelemeye devir"] == "Devredilebilir" for row in handoffs))
        self.assertIn("Kapsam uyuşmuyor", handoffs[0]["Aşama 4 işleme şartı bağlantısı"])
        for flow in (domestic, remote_access, onward):
            self.assertTrue(flow["Mekanizma inceleme durumu"].startswith("Ek kanıt gerekli"))
        self.assertEqual(self.report_table(sample, MECHANISMS), [])

    def test_masked_intake_limits_candidate_drafts_to_matched_and_identified_flows(self):
        sample = SAMPLES / "masked-stage-5-draft.md"
        self.check_masked_intake_report(sample)

    def check_masked_intake_report(self, sample):
        scope_column = "Faaliyet ve aktarım kapsamı"
        _, *upstream = table(MASKED_INPUT, "Aşama 2 · Envanter ve devredilen kapsam")
        handoffs = {row[scope_column]: row for row in self.report_table(sample, HANDOFF)}
        self.assertCountEqual(handoffs.keys(), [row[0] for row in upstream])

        domestic = "A-010 · TR barındırma"
        foreign = "A-010 · DE yedekleme"
        missing_stage_four = "A-010 · TR test kurtarma"
        unknown_country = "A-013 · Arşiv kopyası"
        mapped = {domestic, foreign, missing_stage_four, unknown_country}
        for scope, row in handoffs.items():
            with self.subTest(scope=scope):
                expected = "Devredilebilir" if scope in mapped else "Bekletilir"
                self.assertEqual(row["Esaslı incelemeye devir"], expected)
        self.assertIn("Aşama 4", handoffs[missing_stage_four]["Hazırlık işi, engel ve devam koşulu"])

        flow_rows = self.report_table(sample, FLOWS)
        flows = {row[scope_column]: row for row in flow_rows}
        self.assertCountEqual([row[scope_column] for row in flow_rows], mapped)
        self.assertEqual(len({row["Akış no."] for row in flow_rows}), len(mapped))
        self.assertIn("test", flows[missing_stage_four]["İletim veya erişim, ortam ve sıklık"].lower())
        self.assertIn("Belirsiz", flows[unknown_country]["Barındırma ülkesi"])
        for scope in (missing_stage_four, unknown_country):
            self.assertTrue(flows[scope]["Mekanizma inceleme durumu"].startswith("Ek kanıt gerekli"))

        rows = self.report_table(sample, MECHANISMS)
        candidates = {row["Akış no."]: row for row in rows}
        self.assertCountEqual([row["Akış no."] for row in rows],
                              [flows[domestic]["Akış no."], flows[foreign]["Akış no."]])
        expected_candidates = [
            (domestic, "m. 8/2-a", "21", "E-021"),
            (foreign, "m. 9/4-c", "22", "E-025"),
        ]
        sources = {row["Kaynak kimliği"] for row in self.report_table(sample, "Hukuki kaynak kaydı")}
        for scope, article, stage_four_id, inherited_gap in expected_candidates:
            with self.subTest(scope=scope):
                candidate = candidates[flows[scope]["Akış no."]]
                self.assertIn(article, candidate["Aday hüküm ve mekanizma"])
                self.assertIn(stage_four_id, candidate["Aşama 4 kayıt kimliği ve kapsam eşleşmesi"])
                self.assertTrue(candidate["Taslak durum ve gerekçe"].startswith("Ek kanıt gerekli"))
                self.assertIn(inherited_gap, stage_3.ids(candidate["Açık kayıt ve istenecek kanıt"], "E"))
                references = stage_3.ids(candidate["Hukuki kaynak"], "H")
                self.assertTrue(references)
                self.assertLessEqual(references, sources)
        self.assertIn("koşullu", candidates[flows[foreign]["Akış no."]]["Aday hüküm ve mekanizma"].lower())
        self.assertEqual(self.report_table(sample, "Hukukçu karar ve onay kaydı"), [])
