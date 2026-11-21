"""Check a Stage 2 Markdown report and its Stage 1 handoff."""

import argparse
import re
from pathlib import Path

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
REPORT_SECTIONS = (INVENTORY, *VIEWS, GAPS, COVERAGE, stage_1.EVIDENCE, stage_1.TRANSITION)
RECORD_ID = re.compile(r"\b[ABSVREK]-[0-9]+\b")
RECORD_RANGE = re.compile(r"\b([ABSVREK]-)([0-9]+)\s*[–—-]\s*\1([0-9]+)\b")
GAP_STATUS = {"eksik", "dogrulanamadi", "celiskili", "kapatildi"}
NOT_APPLICABLE = {"—", "–", "-", "yok", "none"}
SCOPE_NOTE = re.compile(
    r"^\s*[-*]\s*rapor niteligi\s*[:–—-]\s*(?:on calisma|preliminary (?:review|work|report))[.]?\s*$", re.M,
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
    for title, bodies in stage_1.sections(markdown).items():
        by_label.setdefault(stage_1.normalized_label(title), []).extend(bodies)
    return by_label


def read_tables(report, errors):
    template = stage_1.sections(TEMPLATE.read_text(encoding="utf-8"))
    actual = read_sections(report)
    tables, bodies = {}, {}
    for title in REPORT_SECTIONS:
        header, *_ = stage_1.table_rows(template[title][0])
        instances = actual.get(stage_1.normalized_label(title), [])
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
    return tables, bodies, template


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
            (row["Faaliyet"], row["İlgili kişi grubu"], row["Veri alanı"])
            for row in rows
        }

    if field_keys(tables[CATEGORIES]) != field_keys(tables[PURPOSES]):
        errors.append(f"{PURPOSES}: faaliyet, kişi grubu ve alan bağlantıları kategori matrisiyle uyuşmuyor.")


def validate_report(report: str, prior_report: str, fixture: str | None = None) -> list[str]:
    errors = [f"Aşama 1: {error}" for error in stage_1.validate_report(prior_report)]
    prior = stage_1_records(prior_report)
    fixture_files = stage_1.fixture_line_counts(fixture) if fixture is not None else None
    tables, bodies, template = read_tables(report, errors)
    normalized = stage_1.normalized_label(report).replace("**", "").replace("`", "")
    if not SCOPE_NOTE.search(normalized):
        errors.append("Ön çalışma kapsamı belirtilmeli.")
    if VERDICT.search(normalized):
        errors.append("Raporda nihai KVKK uygunluk veya aykırılık kararı bulunuyor.")
    if fixture is not None and any(marker.lower() in report.lower() for marker in stage_1.CANARY.findall(fixture)):
        errors.append("Rapor fixture içindeki sentetik gizlilik veya talimat işaretini içeriyor.")

    activities = index_rows(tables[INVENTORY], "A", INVENTORY, errors)
    gaps = index_rows(tables[GAPS], "E", GAPS, errors)
    coverage = index_rows(tables[COVERAGE], "S", COVERAGE, errors)
    evidence = index_rows(tables[stage_1.EVIDENCE], "K", stage_1.EVIDENCE, errors)

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
    check_activities(tables, bodies, activities, coverage, gaps, errors)

    records = prior | activities.keys() | gaps.keys() | evidence.keys()
    references = {}
    for title, rows in tables.items():
        if title == stage_1.TRANSITION:
            continue
        for number, row in enumerate(rows, 1):
            label = f"{title} / satır {number}"
            references[label] = [value for column, value in row.items() if column != "Kaynak ve konum"]
            open_ids = typed_references(row.get("Açık kayıt", ""), "E", label, errors)
            if "Kanıt kaydı" in row and title != stage_1.EVIDENCE:
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
        stage_1.validate_evidence(record, row, ids(row["Açık kayıt"], "E"), fixture_files, errors)
        if stage_1.normalized_label(row["Kaynak türü"]) == "teknik cikarim":
            supports = ids(row["Kaynak ve konum"], "K")
            if not supports or record in supports:
                errors.append(f"{record}: teknik çıkarım için başka bir kanıt kaydı gerekli.")
            references[record] = list(supports)

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

    stage_1.validate_transition(
        bodies[stage_1.TRANSITION], transition_rows,
        stage_1.table_rows(template[stage_1.TRANSITION][0])[1:], references, errors, RECORD_ID,
    )
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
