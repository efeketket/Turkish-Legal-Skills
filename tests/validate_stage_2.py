"""Check a Stage 2 Markdown report and its Stage 1 handoff."""

import argparse
import re
from datetime import date
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

from markdown_it.tree import SyntaxTreeNode

import validate_stage_1 as stage_1

TEMPLATE = stage_1.SKILL / "assets" / "stage-2-outputs.md"
INVENTORY = "Kişisel Veri İşleme Faaliyetleri Envanteri"
CATEGORIES = "Kişisel Veri Kategorileri ve İlgili Kişi Grupları Matrisi"
LIFECYCLE = "Veri Akış ve Yaşam Döngüsü Haritası"
PURPOSES = "İşleme Amaçları Matrisi"
OPERATIONS = "Teknik Sistem ve İşleme Operasyonları Eşleştirme Tablosu"
GAPS = "Doğrulanamayan Faaliyetler ve Eksik Bilgiler Listesi"
COVERAGE = "Aşama 1 Süreç Kapsamı"
VIEWS = (CATEGORIES, LIFECYCLE, PURPOSES, OPERATIONS)
MANUAL = "Manuel ve Fiziksel Kayıt İncelemesi"
AUTOMATION = "Otomatik Analiz ve Sonuç İncelemesi"
REVISIONS = "Gerekçeli Revizyon Geçmişi"
INHERITED_SCOPE = "Devralınan Kanıt Kapsamı"
START = "Aşama 1 → 2 Başlangıç Eşiği"
ACTIVITY_CRITERIA = "Faaliyet Bazlı Geçiş Ölçütleri"
HANDOFF = "Faaliyet Bazlı Devir Kararları"
ROLE_INPUTS = "Aşama 3 Rol İncelemesi Girdileri"
SUBSECTIONS = (MANUAL, AUTOMATION, REVISIONS, INHERITED_SCOPE, START, ACTIVITY_CRITERIA, HANDOFF, ROLE_INPUTS)
REPORT_SECTIONS = (
    INVENTORY, *VIEWS, GAPS, COVERAGE, stage_1.EVIDENCE, stage_1.TRANSITION, *SUBSECTIONS,
)
RECORD_ID = re.compile(r"\b[ABSVREK]-[0-9]+\b")
RECORD_RANGE = re.compile(r"\b([ABSVREK]-)([0-9]+)\s*[–—-]\s*\1([0-9]+)\b")
GAP_STATUS = {"eksik", "dogrulanamadi", "celiskili", "kapatildi"}
NOT_APPLICABLE = {"—", "–", "-", "yok", "none"}
HANDOFF_STATUS = {"Devredilebilir", "Sınırlı devredilebilir", "Bekletilir"}
OPERATION_SOURCES = {
    "Beyan": {"İşletme beyanı"},
    "Belge": {"Belge", "Sözleşme veya politika belgesi"},
    "Kod olasılığı": {"Kaynak kod incelemesi", "Doğrudan teknik gözlem / Kaynak kod"},
    "Yapılandırma": {"Yapılandırma incelemesi", "Doğrudan teknik gözlem / Teknik yapılandırma"},
    "Testte gözlendi": {"Test ortamı gözlemi"},
    "Üretim yapılandırması": {"Üretim ortamı yapılandırması"},
    "Üretimde gözlendi": {"Üretimde fiilî çalışma kaydı"},
    "Çıkarım": {"Teknik çıkarım"},
}
SOURCE_TYPES = {kind for kinds in OPERATION_SOURCES.values() for kind in kinds
                if not kind.startswith("Doğrudan teknik gözlem")}
RUNTIME_OPERATIONS = {"Testte gözlendi", "Üretim yapılandırması", "Üretimde gözlendi"}
SCOPE_FIELDS = ("Ortam veya sistem", "İnceleme kapsamı", "Doğruladığı husus", "Tek başına doğrulamadığı husus")
MANUAL_RESULTS = {
    "Veri kayıt sistemi niteliği doğrulandı",
    "Veri kayıt sistemi niteliği doğrulanamadı",
    "Veri kayıt sistemi niteliği konusunda değerlendirme için ek bilgi gerekiyor",
}
SPECIAL_STATUS = {"İhtimal", "Doğrulandı", "Gösterge yok", "Değerlendirilemedi"}
SCOPE_NOTE = re.compile(
    r"^\s*[-*]\s*rapor niteligi\s*[:–—-]\s*(?:on calisma|preliminary (?:review|work|report))[.]?\s*$", re.M,
)
INVENTORY_LIMIT = re.compile(
    r"(?:nihai mevzuat envanteri (?:veya|ya da) kvkk uyum karari degildir"
    r"|does not (?:constitute|replace) (?:a |the )?final (?:statutory |legal )?inventory or (?:a )?kvkk compliance decision)"
)
# Catch common standalone verdicts. Legal substance remains a reviewer task.
VERDICT = re.compile(
    r"^\s*(?:[-*#]+\s*|\d+[.)]\s*)?(?:nihai (?:karar|sonuc):\s*)?"
    r"(?:(?:(?:isletme|uygulama|platform) )?kvkk['’]?ya (?:tam )?"
    r"(?:uygundur|aykiridir|uyumludur|uyumsuzdur|uygun degildir)"
    r"|(?:the (?:business|application|platform) is )?(?:not |fully )?"
    r"(?:compliant|non[- ]?compliant) with (?:the )?kvkk)[.!]?\s*$",
    re.M,
)


def ids(text, prefixes="ABSVREK"):
    return {record for record in RECORD_ID.findall(text) if record[0] in prefixes}


def read_sections(markdown):
    by_label = {}
    subsection_titles = {stage_1.normalized_label(title) for title in SUBSECTIONS}
    body = None
    for node in SyntaxTreeNode(stage_1.MARKDOWN.parse(markdown)).children:
        if node.type == "heading":
            title = stage_1.normalized_label(stage_1.visible_text(node))
            if node.tag == "h2" or (node.tag == "h3" and title in subsection_titles):
                body = []
                by_label.setdefault(title, []).append(body)
                continue
        if body is not None:
            body.append(node)
    return by_label


def read_tables(report, errors):
    template = read_sections(TEMPLATE.read_text(encoding="utf-8"))
    actual = read_sections(report)
    tables, bodies, template_rows = {}, {}, {}
    for title in REPORT_SECTIONS:
        label = stage_1.normalized_label(title)
        header, *template_rows[title] = stage_1.table_rows(template[label][0])
        instances = actual.get(label, [])
        if len(instances) != 1:
            errors.append(f"{title}: başlık bir kez bulunmalı.")
            tables[title], bodies[title] = [], []
            continue
        bodies[title] = instances[0]
        rows = stage_1.table_rows(instances[0])
        if not rows or list(map(stage_1.normalized_label, rows[0])) != list(map(stage_1.normalized_label, header)):
            errors.append(f"{title}: şablondaki sütunlarla tek bir tablo bulunmalı.")
            tables[title] = []
            continue
        tables[title] = [dict(zip(header, cells)) for cells in rows[1:]]
        for number, cells in enumerate(rows[1:], 1):
            if any(cell in stage_1.EMPTY for cell in cells):
                errors.append(f"{title} / satır {number}: boş hücre veya yer tutucu bulunuyor.")
    return tables, bodies, template_rows


def index_rows(rows, prefix, title, errors):
    index = {}
    for row in rows:
        record = next(iter(row.values()))
        if ids(record, prefix) != {record}:
            errors.append(f"{title}: beklenen kimlik biçimi {prefix}-001.")
        elif record in index:
            errors.append(f"{title}: yinelenen kayıt kimliği {record}.")
        else:
            index[record] = row
    return index


def stage_1_records(report):
    actual = read_sections(report)
    records = set()
    for title, prefix in {**stage_1.OUTPUTS, stage_1.EVIDENCE: "K"}.items():
        bodies = actual.get(stage_1.normalized_label(title), [])
        if len(bodies) == 1:
            for cells in stage_1.table_rows(bodies[0])[1:]:
                records.update(ids(cells[0], prefix))
    return records


def inherited_evidence(report):
    actual = read_sections(report)
    bodies = actual.get(stage_1.normalized_label(stage_1.EVIDENCE), [])
    if len(bodies) != 1:
        return {}
    rows = stage_1.table_rows(bodies[0])
    header = list(map(stage_1.normalized_label, rows[0])) if rows else []
    if "kaynak turu" not in header:
        return {}
    source_column = header.index("kaynak turu")
    return {cells[0]: cells[source_column] for cells in rows[1:]}


def typed_references(value, prefixes, label, errors, required=False):
    cited = ids(value)
    if cited - ids(value, prefixes) or (required and not cited):
        errors.append(f"{label}: kayıt bağlantısı eksik veya yanlış türde.")
    return cited


def check_activities(tables, bodies, activities, coverage, gaps, errors):
    expected_by_process = {process: set() for process in coverage}
    for activity, row in activities.items():
        processes = typed_references(row["Aşama 1 süreçleri"], "S", activity, errors)
        typed_references(row["Ön akışlar ve roller"], "VR", activity, errors)
        if not processes and not stage_1.has_detail(row["Aşama 1 süreçleri"], RECORD_ID):
            errors.append(f"{activity}: Aşama 1 süreç bağlantısı veya gerekçesi gerekli.")
        for process in processes & coverage.keys():
            expected_by_process[process].add(activity)
    for process, row in coverage.items():
        linked = typed_references(row["Faaliyetler"], "A", process, errors)
        if linked != expected_by_process[process]:
            errors.append(f"{process}: süreç kapsamı ve ana envanter bağlantıları uyuşmuyor.")

    for title in (INVENTORY, *VIEWS):
        rows = tables[title]
        if not rows:
            notes = [stage_1.visible_text(node) for node in bodies[title] if node.type == "paragraph"]
            if not any(note.startswith("Açık kayıt: ") and ids(note, "E") & gaps.keys() for note in notes):
                errors.append(f"{title}: boş tabloda geçerli açık kayıt açıklaması gerekli.")
        if title in VIEWS and {row["Faaliyet"] for row in rows} != set(activities):
            errors.append(f"{title}: her faaliyet ana envanterde bulunmalı ve bu tabloda yer almalı.")

    def field_keys(rows):
        return {
            (row["Faaliyet"], row["İlgili kişi grubu"], row["Veri alanı"], row["Somut işleme amacı"])
            for row in rows
        }

    if field_keys(tables[CATEGORIES]) != field_keys(tables[PURPOSES]):
        errors.append(f"{PURPOSES}: faaliyet, kişi grubu, amaç ve alan bağlantıları kategori matrisiyle uyuşmuyor.")


def valid_date(value):
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def check_evidence_scope(record, row, errors):
    if not valid_date(row["İnceleme tarihi"]):
        errors.append(f"{record}: ISO inceleme tarihi gerekli.")
    if any(not stage_1.has_detail(row[field], RECORD_ID) for field in SCOPE_FIELDS):
        errors.append(f"{record}: ortam, kapsam ve iki doğrulama sınırı gerekli.")
    if stage_1.normalized_label(row[SCOPE_FIELDS[-2]]) == stage_1.normalized_label(row[SCOPE_FIELDS[-1]]):
        errors.append(f"{record}: olumlu ve olumsuz doğrulama sınırları ayrı yazılmalı.")


def check_operations(rows, activities, evidence, inherited, inherited_scope, errors):
    for row in rows:
        activity = row["Faaliyet"]
        basis = row["Operasyon dayanağı"]
        if basis == "Doğrulanamadı":
            if not ids(row["Açık kayıt"], "E"):
                errors.append(f"{activity}: doğrulanamayan operasyon için açık kayıt gerekli.")
            continue
        if basis not in OPERATION_SOURCES:
            errors.append(f"{activity}: operasyon dayanağı geçersiz.")
            continue
        candidates = ids(row["Kanıt kaydı"], "K")
        if (candidates & inherited.keys()) - inherited_scope.keys():
            errors.append(f"{activity}: devralınan operasyon kanıtı için kapsam notu gerekli.")
        allowed = {stage_1.normalized_label(kind) for kind in OPERATION_SOURCES[basis]}
        processes = ids(activities.get(activity, {}).get("Aşama 1 süreçleri", ""), "S")
        for record in candidates:
            source = evidence.get(record)
            kind = stage_1.normalized_label(source["Kaynak türü"] if source else inherited.get(record, ""))
            if kind not in allowed:
                continue
            if source:
                linked = ids(source["İlgili kayıtlar"], "AS")
                if activity not in linked and (ids(source["İlgili kayıtlar"], "A") or not linked & processes):
                    continue
            if basis in RUNTIME_OPERATIONS:
                if not source or stage_1.normalized_label(source["Ortam veya sistem"]) != stage_1.normalized_label(row["Ortam"]):
                    continue
                if stage_1.status_and_detail(source["Doğrulama durumu ve sınırı"], stage_1.VERIFICATION)[0] not in {"Doğrulandı", "Kısmen doğrulandı"}:
                    continue
            break
        else:
            errors.append(f"{activity}: {basis} için faaliyet ve ortamla uyumlu kanıt türü gerekli.")


def check_special_reviews(tables, activities, errors):
    for row in tables[CATEGORIES]:
        activity = row["Faaliyet"]
        if any(stage_1.normalized_label(row[field]) == "pazarlama"
               for field in ("Temel kategori", "İşletmeye özgü alt kategori")):
            errors.append(f"{activity}: pazarlama veri kategorisi olarak kullanılamaz.")
        status = row["Özel nitelik durumu"]
        note = row["Özel nitelik inceleme notu"]
        if status not in SPECIAL_STATUS or not stage_1.has_detail(note, RECORD_ID):
            errors.append(f"{activity}: özel nitelik durumu ve tarama gerekçesi gerekli.")
        if status == "Doğrulandı" and not ids(row["Kanıt kaydı"], "K"):
            errors.append(f"{activity}: doğrulanmış özel nitelik için kanıt gerekli.")
        if status in {"İhtimal", "Değerlendirilemedi"} and not ids(row["Açık kayıt"], "E"):
            errors.append(f"{activity}: özel nitelik belirsizliği açık kayda bağlanmalı.")

    for title in (MANUAL, AUTOMATION):
        for row in tables[title]:
            activity = row["Faaliyet"]
            if activity not in activities:
                errors.append(f"{title}: güncel faaliyet kimliği gerekli.")
            if title == MANUAL:
                result = row["Sonuç"]
                if result not in MANUAL_RESULTS:
                    errors.append(f"{activity}: veri kayıt sistemi sonucu geçersiz.")
                elif result == "Veri kayıt sistemi niteliği doğrulandı":
                    fields = ("Düzen ve sınıflandırma", "Geçmiş kayda erişim", "Düzenli süreç kullanımı")
                    if not ids(row["Kanıt kaydı"], "K") or any(
                        stage_1.normalized_label(row[field]) in NOT_APPLICABLE or row[field] in stage_1.UNKNOWN
                        for field in fields
                    ):
                        errors.append(f"{activity}: doğrulanan veri kayıt sistemi için yapı ve erişim dayanağı gerekli.")
                elif not ids(row["Açık kayıt"], "E"):
                    errors.append(f"{activity}: belirsiz veri kayıt sistemi için açık kayıt gerekli.")
            elif any(not stage_1.has_detail(row[field], RECORD_ID) for field in (
                "Otomatik analiz veya profilleme", "Fiilî insan incelemesi ve yetkisi",
                "İnsan müdahalesi olmadan sonuç ve etkisi", "Ortam ve kapsam",
            )):
                errors.append(f"{activity}: otomatik analiz, insan incelemesi ve otomatik sonuç ayrı gerekçelendirilmeli.")


def check_revisions(rows, activities, historical, gaps, errors):
    replacements = {}
    for row in rows:
        revision_date, operation = row["Revizyon tarihi"], row["İşlem"]
        before = typed_references(row["Önceki faaliyetler"], "A", REVISIONS, errors)
        after = typed_references(row["Sonraki faaliyetler"], "A", REVISIONS, errors)
        for field in ("Önceki kanıt", "Yeni bilgi veya kanıt"):
            cited = ids(row[field], "K")
            if (field == "Önceki kanıt" or not stage_1.has_detail(row[field], RECORD_ID)) and not cited:
                errors.append(f"{REVISIONS}: {field} için dayanak gerekli.")
        for field in ("Önceki tespit", "Önceki kapsam", "Yeni tespit", "Gerekçe", "Etkilenen faaliyet ve çıktı"):
            if not stage_1.has_detail(row[field], RECORD_ID):
                errors.append(f"{REVISIONS}: {field} için açıklama gerekli.")
        gap, _, status = row["Açık kayıt ve revizyon sonrasındaki durum"].partition(" / ")
        if gap not in gaps or stage_1.normalized_label(status) not in GAP_STATUS:
            errors.append(f"{REVISIONS}: açık kaydın revizyon sonrası durumu gerekli.")
        previous_date = row["Önceki tespit tarihi"]
        if not (valid_date(revision_date) and valid_date(previous_date) and previous_date <= revision_date):
            errors.append(f"{REVISIONS}: önceki tespit ve revizyon tarihleri kronolojik olmalı.")
        if (before | after) - activities.keys():
            errors.append(f"{REVISIONS}: önceki ve sonraki faaliyetler ana envanterde korunmalı.")
        if operation == "Düzeltme" and before == after:
            continue
        if operation == "Yeni faaliyet":
            if not before or len(after) != 1 or before & after or not ids(row["Yeni bilgi veya kanıt"], "K"):
                errors.append(f"{REVISIONS}: yeni faaliyet eski kapsamdan ayrı kimlik ve yeni kanıt gerektirir.")
            continue
        split = operation == "Bölme" and len(before) == 1 and len(after) >= 2
        merge = operation == "Birleştirme" and len(before) >= 2 and len(after) == 1
        if not (split or merge) or before & after or before - historical:
            errors.append(f"{REVISIONS}: bölme veya birleştirme eski tarihsel ve yeni farklı kimlikleri gerektirir.")
            continue
        for activity in before:
            if activity in replacements:
                errors.append(f"{REVISIONS}: {activity} için birden çok kimlik değişikliği var.")
            replacements[activity] = (revision_date, after)
    if historical - replacements.keys():
        errors.append(f"{REVISIONS}: her tarihsel faaliyet gerekçeli eski-yeni ilişkiye bağlanmalı.")
    for revision_date, targets in replacements.values():
        if any(target in replacements and replacements[target][0] < revision_date for target in targets):
            errors.append(f"{REVISIONS}: ardışık kimlik değişiklikleri kronolojik olmalı.")
    try:
        TopologicalSorter({record: targets for record, (_, targets) in replacements.items()}).prepare()
    except CycleError:
        errors.append(f"{REVISIONS}: eski-yeni faaliyet bağlantıları döngü oluşturamaz.")


def check_criterion_rows(rows, expected, label, errors):
    expected_labels = {stage_1.normalized_label(row[0]) for row in expected}
    criteria = {stage_1.normalized_label(row["Geçiş ölçütü"]) for row in rows}
    if len(rows) != len(expected_labels) or criteria != expected_labels:
        errors.append(f"{label}: her ölçüt bir kez bulunmalı.")
    for row in rows:
        status, _ = stage_1.status_and_detail(row["Durum"], stage_1.TRANSITION_STATUS)
        detail = row["Gerekçe ve ilgili kayıtlar"]
        if not status or not ids(detail) or not stage_1.has_detail(detail, RECORD_ID):
            errors.append(f"{label}: geçerli durum, gerekçe ve kayıt bağlantısı gerekli.")
        elif status == "Karşılandı" and not ids(detail, "ABSVRK") and stage_1.normalized_label(
            RECORD_ID.sub("", detail).strip(" ().")
        ) in {"acildi", "acik kayit acildi", "eksik kaydi acildi"}:
            errors.append(f"{label}: açık kayıt tek başına karşılanma gerekçesi olamaz.")


def check_handoff(tables, template, activities, gaps, open_gaps, errors):
    check_criterion_rows(tables[START], template[START], START, errors)
    criteria_by_activity = {activity: [] for activity in activities}
    for row in tables[ACTIVITY_CRITERIA]:
        activity = row["Faaliyet"]
        if activity in criteria_by_activity:
            criteria_by_activity[activity].append(row)
        else:
            errors.append(f"{ACTIVITY_CRITERIA}: güncel faaliyet kimliği gerekli.")
    for activity, rows in criteria_by_activity.items():
        check_criterion_rows(rows, template[stage_1.TRANSITION], f"{ACTIVITY_CRITERIA} / {activity}", errors)

    decisions = set()
    for row in tables[HANDOFF]:
        activity, target, status = row["Faaliyet"], row["Hedef inceleme"], row["Devir durumu"]
        key = (activity, stage_1.normalized_label(target))
        if activity not in activities or key in decisions or not stage_1.has_detail(target, RECORD_ID):
            errors.append(f"{HANDOFF}: benzersiz güncel faaliyet ve hedef gerekli.")
        decisions.add(key)
        if status not in HANDOFF_STATUS or not stage_1.has_detail(row["Gerekçe ve devir kapsamı"], RECORD_ID):
            errors.append(f"{HANDOFF} / {activity}: geçerli devir durumu ve gerekçe gerekli.")
        if status in {"Sınırlı devredilebilir", "Bekletilir"}:
            activity_scope = {activity} | ids(activities.get(activity, {}).get("Aşama 1 süreçleri", ""), "S")
            linked = {gap for gap in ids(row["Açık kayıt"], "E") & open_gaps
                      if ids(gaps[gap]["İlgili kayıtlar"], "AS") & activity_scope}
            if not linked or not stage_1.has_detail(row["Sınır veya devam koşulu"], RECORD_ID):
                errors.append(f"{HANDOFF} / {activity}: ilgili açık kayıt ve devam koşulu gerekli.")
        if activity in activities and key[1] == "asama 3" and status != "Bekletilir" and any(
            activities[activity][field] in stage_1.UNKNOWN for field in ("Operasyonel işlev", "Somut amaç özeti")
        ):
            errors.append(f"{HANDOFF} / {activity}: amacı veya temel operasyonu belirsiz rol incelemesi bekletilmeli.")

    roles = {activity: set() for activity in activities}
    for row in tables[ROLE_INPUTS]:
        activity = row["Faaliyet"]
        if activity not in roles:
            errors.append(f"{ROLE_INPUTS}: güncel faaliyet kimliği gerekli.")
            continue
        typed_references(row["Ön roller"], "R", f"{ROLE_INPUTS} / {activity}", errors)
        roles[activity].update(ids(row["Ön roller"], "R"))
    if {row["Faaliyet"] for row in tables[ROLE_INPUTS]} != activities.keys() or any(
        roles[activity] != ids(row["Ön akışlar ve roller"], "R") for activity, row in activities.items()
    ):
        errors.append(f"{ROLE_INPUTS}: tüm güncel faaliyetler ve ilgili ön rol kimlikleri korunmalı.")
    if any((activity, "asama 3") not in decisions for activity in activities):
        errors.append(f"{HANDOFF}: her güncel faaliyet için Aşama 3 kararı gerekli.")


def validate_report(report: str, prior_report: str, fixture: str | None = None) -> list[str]:
    errors = [f"Aşama 1: {error}" for error in stage_1.validate_report(prior_report)]
    prior = stage_1_records(prior_report)
    inherited = inherited_evidence(prior_report)
    fixture_files = stage_1.fixture_line_counts(fixture) if fixture is not None else None
    tables, bodies, template = read_tables(report, errors)
    normalized = stage_1.normalized_label(report).replace("**", "").replace("`", "")
    if not SCOPE_NOTE.search(normalized):
        errors.append("Ön çalışma kapsamı belirtilmeli.")
    inventory_note = stage_1.normalized_label(" ".join(
        stage_1.visible_text(node) for node in bodies[INVENTORY] if node.type == "paragraph"
    ))
    if not ("on calisma" in inventory_note or "preliminary" in inventory_note) or not INVENTORY_LIMIT.search(inventory_note):
        errors.append(f"{INVENTORY}: ön çalışma, nihai envanter ve uyum kararı sınırı belirtilmeli.")
    if VERDICT.search(normalized):
        errors.append("Raporda nihai KVKK uygunluk veya aykırılık kararı bulunuyor.")
    if fixture is not None and any(marker.lower() in report.lower() for marker in stage_1.CANARY.findall(fixture)):
        errors.append("Rapor fixture içindeki sentetik gizlilik veya talimat işaretini içeriyor.")

    activities = index_rows(tables[INVENTORY], "A", INVENTORY, errors)
    historical = {activity for activity, row in activities.items() if row["Kayıt durumu"] == "Tarihsel"}
    current = {activity: row for activity, row in activities.items() if activity not in historical}
    for activity, row in activities.items():
        if row["Kayıt durumu"] not in {"Güncel", "Tarihsel"} or not stage_1.has_detail(
            row["Faaliyet sınırı ve karar alanı"], RECORD_ID
        ):
            errors.append(f"{activity}: kayıt durumu ve faaliyet sınırı gerekçesi gerekli.")
    gaps = index_rows(tables[GAPS], "E", GAPS, errors)
    coverage = index_rows(tables[COVERAGE], "S", COVERAGE, errors)
    evidence = index_rows(tables[stage_1.EVIDENCE], "K", stage_1.EVIDENCE, errors)
    inherited_scope = index_rows(tables[INHERITED_SCOPE], "K", INHERITED_SCOPE, errors)

    if set(coverage) != {record for record in prior if record.startswith("S-")}:
        errors.append(f"{COVERAGE}: önceki süreç kimliklerinin tümü aynı biçimde bulunmalı.")
    for record in sorted(prior - gaps.keys()):
        if record.startswith("E-"):
            errors.append(f"{GAPS}: önceki açık kayıt devredilmedi ({record}).")
    for duplicate in sorted(evidence.keys() & prior):
        errors.append(f"{stage_1.EVIDENCE}: devredilen kanıt yeniden tanımlanmış ({duplicate}).")
    if not gaps and not any(
        stage_1.visible_text(node) == "Açık kayıt yok." for node in bodies[GAPS] if node.type == "paragraph"
    ):
        errors.append(f"{GAPS}: açık kayıt yoksa bu durum belirtilmeli.")
    check_activities(tables, bodies, current, coverage, gaps, errors)
    check_special_reviews(tables, current, errors)
    check_revisions(tables[REVISIONS], activities, historical, gaps, errors)

    records = prior | activities.keys() | gaps.keys() | evidence.keys()
    references = {}
    for title, rows in tables.items():
        if title == stage_1.TRANSITION:
            continue
        for number, row in enumerate(rows, 1):
            label = f"{title} / satır {number}"
            references[label] = [value for column, value in row.items() if column != "Kaynak ve konum"]
            open_ids = typed_references(row.get("Açık kayıt", ""), "E", label, errors)
            if "Kanıt kaydı" in row and title not in {stage_1.EVIDENCE, INHERITED_SCOPE}:
                typed_references(row["Kanıt kaydı"], "K", label, errors, title != GAPS and not open_ids)

    open_gaps = set()
    for gap, row in gaps.items():
        status = stage_1.normalized_label(row["Durum"])
        typed_references(row["İlgili kayıtlar"], "ABSVRK", gap, errors, row["İlgili kayıtlar"] != "Kapsam")
        if status not in GAP_STATUS:
            errors.append(f"{gap}: açık kayıt durumu geçersiz.")
        if status == "kapatildi":
            typed_references(row["Kanıt kaydı"], "K", gap, errors, required=True)
        else:
            open_gaps.add(gap)
            if row["Sonraki aşama notu"] == "—":
                errors.append(f"{gap}: sonraki aşamaya aktarım notu gerekli.")

    for record, row in evidence.items():
        typed_references(row["İlgili kayıtlar"], "ABSVR", record, errors, row["İlgili kayıtlar"] != "Kapsam")
        stage_1.validate_evidence(record, row, ids(row["Açık kayıt"], "E"), fixture_files, errors,
                                  source_types=SOURCE_TYPES)
        check_evidence_scope(record, row, errors)
        if stage_1.normalized_label(row["Kaynak türü"]) == "teknik cikarim":
            supports = ids(row["Kaynak ve konum"], "K")
            if not supports or record in supports:
                errors.append(f"{record}: teknik çıkarım için başka bir kanıt kaydı gerekli.")
            references[record] = list(supports)
    for record, row in inherited_scope.items():
        if record not in inherited:
            errors.append(f"{record}: kapsam notu Aşama 1 kanıtına bağlanmalı.")
        check_evidence_scope(record, row, errors)
    check_operations(tables[OPERATIONS], current, evidence, inherited, inherited_scope, errors)
    check_handoff(tables, template, current, gaps, open_gaps, errors)

    transition_rows = []
    for number, row in enumerate(tables[stage_1.TRANSITION], 1):
        criterion, status, detail, missing, blockers, note = row.values()
        transition_rows.append((criterion, status, detail))
        label = f"{stage_1.TRANSITION} / ek alanlar {number}"
        references[label] = [missing, blockers, note]
        has_blockers = stage_1.normalized_label(blockers) not in NOT_APPLICABLE
        typed_references(missing, "E", label, errors, stage_1.normalized_label(missing) not in NOT_APPLICABLE)
        typed_references(blockers, "E", label, errors, has_blockers)
        if has_blockers and stage_1.status_and_detail(status, stage_1.TRANSITION_STATUS)[0] == "Karşılandı":
            errors.append(f"{label}: devam engeli bulunan ölçüt karşılanmış gösterilemez.")

    check_criterion_rows(tables[stage_1.TRANSITION], template[stage_1.TRANSITION], stage_1.TRANSITION, errors)
    stage_1.validate_transition(bodies[stage_1.TRANSITION], transition_rows,
                                template[stage_1.TRANSITION], references, errors, RECORD_ID)
    for label, values in references.items():
        cited, invalid = stage_1.resolve_ranges(" ".join(values), records, RECORD_ID, RECORD_RANGE)
        for span in sorted(invalid):
            errors.append(f"{label}: {span} kayıt aralığı eksik veya geçersiz.")
        for missing in sorted(cited - records):
            errors.append(f"{label}: {missing} kayıt bağlantısı bulunamadı.")
    handoff, _ = stage_1.resolve_ranges(
        " ".join(references.get(stage_1.HANDOFF, [])), records, RECORD_ID, RECORD_RANGE,
    )
    for missing in sorted(open_gaps - handoff):
        errors.append(f"{stage_1.TRANSITION}: aktarım notunda açık kayıt eksik ({missing}).")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="completed Stage 2 Markdown report")
    parser.add_argument("--stage-1", type=Path, required=True, help="prior Stage 1 Markdown report")
    parser.add_argument("--fixture", type=Path, help="optional synthetic excerpts for new evidence and marker checks")
    args = parser.parse_args()
    try:
        report = args.report.read_text(encoding="utf-8-sig")
        prior_report = args.stage_1.read_text(encoding="utf-8-sig")
        fixture = args.fixture.read_text(encoding="utf-8-sig") if args.fixture else None
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    errors = validate_report(report, prior_report, fixture)
    for error in errors:
        print(error)
    print("Aşama 2 biçim kontrolü başarısız." if errors else "Aşama 2 biçim kontrolü başarılı.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
