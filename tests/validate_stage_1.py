"""Check the structure of a completed Stage 1 Markdown report."""

import argparse
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

SKILL = Path(__file__).resolve().parents[1] / "skills" / "turkish-kvkk"
TEMPLATE = SKILL / "assets" / "stage-1-outputs.md"
MARKDOWN = MarkdownIt("commonmark").enable("table")

OUTPUTS = {
    "İşletme Tanıma Dosyası": "B",
    "İş Süreçleri Haritası": "S",
    "Ön Veri Akış Haritası": "V",
    "Ön Hukuki Rol Tablosu": "R",
    "Eksik Bilgi ve Belge Listesi": "E",
}
EVIDENCE = "Ortak Kanıt Kaydı"
TRANSITION = "Aşama Geçiş Değerlendirmesi"
RECORD_ID = re.compile(r"\b[BSVREK]-[0-9]+\b")
RECORD_RANGE = re.compile(r"\b([BSVREK]-)([0-9]+)\s*[–—-]\s*\1([0-9]+)\b")
SOURCE_TYPES = {
    "İşletme beyanı",
    "Belge",
    "Doğrudan teknik gözlem",
    "Doğrudan teknik gözlem / Kaynak kod",
    "Doğrudan teknik gözlem / Teknik yapılandırma",
    "Teknik çıkarım",
}
VERIFICATION = {"Doğrulandı", "Kısmen doğrulandı", "Doğrulanamadı", "Çelişkili"}
TRANSITION_STATUS = {"Karşılandı", "Karşılanmadı", "Değerlendirilemedi"}
EMPTY = {"", "…", "..."}
UNKNOWN = {"Bilinmiyor", "Belirlenemedi"}
GAP_NOTE = "Açık kayıt / sonraki aşama notu"
OVERALL = "Geçiş durumu ve gerekçesi"
HANDOFF = "Açık kayıtlar ve sonraki aşamaya aktarılacak notlar"
FILE_LOCATION = re.compile(r"Dosya: ([^#\s]+)(?:#L([1-9][0-9]*)(?:-L([1-9][0-9]*))?)?")
CANARY = re.compile(r"SYNTHETIC_(?:CANARY|PERSON|INSTRUCTION)_[A-Z0-9_]+", re.I)


def normalized_label(value):
    # Preserve the canonical labels while allowing typographic and ASCII variants.
    text = unicodedata.normalize("NFKD", value.casefold().replace("ı", "i"))
    return "".join(character for character in text if not unicodedata.combining(character))


def status_and_detail(value, allowed):
    status, *details = re.split(r"\s*(?:[.:–—]| - )\s*", value, maxsplit=1)
    status = next((label for label in allowed if normalized_label(label) == normalized_label(status)), None)
    return status, details[0] if details else ""


def visible_text(node):
    return "".join(
        part.content for part in node.walk() if part.type in {"text", "code_inline"}
    ).strip()


def sections(markdown):
    result = defaultdict(list)
    body = None
    for node in SyntaxTreeNode(MARKDOWN.parse(markdown)).children:
        if node.type == "heading" and node.tag == "h2":
            body = []
            result[visible_text(node)].append(body)
        elif body is not None:
            body.append(node)
    return result


def table_rows(body):
    tables = [node for node in body if node.type == "table"]
    if len(tables) != 1:
        return []
    return [
        [visible_text(cell) for cell in row.children]
        for row in tables[0].walk() if row.type == "tr"
    ]


def record_ids(text, prefixes="BSVREK"):
    return {record for record in RECORD_ID.findall(text) if record[0] in prefixes}


def resolve_ranges(text, records):
    cited = record_ids(text)
    invalid = set()
    for prefix, first, last in RECORD_RANGE.findall(text):
        span = f"{prefix}{first}–{prefix}{last}"
        try:
            start, end = int(first), int(last)
        except ValueError:
            invalid.add(span)
            continue
        matching = {
            record for record in records if record.startswith(prefix)
            and len(record) - len(prefix) == len(first) and start <= int(record[len(prefix):]) <= end
        }
        if start >= end or len(first) != len(last) or len(matching) != end - start + 1:
            invalid.add(span)
        cited.update(matching)
    return cited, invalid


def has_detail(text):
    return bool(re.search(r"\w", RECORD_ID.sub("", text)))


def fixture_line_counts(fixture):
    counts = {}
    for title, bodies in sections(fixture).items():
        if len(bodies) != 1 or not bodies[0]:
            continue
        body = bodies[0]
        # The supplied Markdown fixtures use one excerpt per file heading.
        if len(body) == 1 and body[0].type == "fence":
            counts[title] = len(body[0].content.splitlines())
        else:
            counts[title] = body[-1].map[1] - body[0].map[0]
    return counts


def validate_source(record, row, fixture_files, errors):
    if fixture_files is None:
        return
    location = row["Kaynak ve konum"]
    kind = normalized_label(row["Kaynak türü"])
    file_backed = kind == "belge" or kind.startswith("dogrudan teknik gozlem")
    if not file_backed and not location.startswith("Dosya:"):
        return
    match = FILE_LOCATION.fullmatch(location)
    if not match:
        errors.append(f"{record}: beklenen kaynak konumu Dosya: yol[#L1-L2].")
        return
    path, first, last = match.groups()
    if path not in fixture_files:
        errors.append(f"{record}: kaynak dosya başlığı fixture içinde bulunamadı.")
    elif first is not None:
        last = last or first
        line_count = fixture_files[path]
        max_digits = len(str(line_count))
        if max(len(first), len(last)) > max_digits or not (int(first) <= int(last) <= line_count):
            errors.append(f"{record}: kaynak satır aralığı fixture dışında.")
    elif kind.endswith("/ kaynak kod"):
        errors.append(f"{record}: kaynak kod atfı fixture satırı içermeli.")


def validate_report(report: str, fixture: str | None = None) -> list[str]:
    errors = []
    records = set()
    references = {}
    fixture_files = fixture_line_counts(fixture) if fixture is not None else None
    template = sections(TEMPLATE.read_text(encoding="utf-8"))
    actual = defaultdict(list)
    for title, bodies in sections(report).items():
        actual[normalized_label(title)].extend(bodies)

    report_lower = report.lower()
    if fixture is not None and any(marker.lower() in report_lower for marker in CANARY.findall(fixture)):
        errors.append("Rapor fixture içindeki sentetik gizlilik veya talimat işaretini içeriyor.")

    for section, prefix in {**OUTPUTS, EVIDENCE: "K", TRANSITION: None}.items():
        bodies = actual.get(normalized_label(section), [])
        if len(bodies) != 1:
            errors.append(f"{section}: başlık bir kez bulunmalı.")
            continue
        body = bodies[0]
        paragraphs = [visible_text(node) for node in body if node.type == "paragraph"]
        template_bodies = template.get(section, [])
        template_rows = table_rows(template_bodies[0]) if len(template_bodies) == 1 else []
        if not template_rows:
            errors.append(f"{section}: şablon tablosu okunamadı.")
            continue
        header, *sample_rows = template_rows
        rows = table_rows(body)
        if not rows or list(map(normalized_label, rows[0])) != list(map(normalized_label, header)):
            errors.append(f"{section}: şablondaki sütunlarla tek bir tablo bulunmalı.")
            continue
        if prefix is None:
            validate_transition(body, rows[1:], sample_rows, references, errors)
            continue
        if len(rows) == 1:
            gap_note = " ".join(text for text in paragraphs if normalized_label(text).startswith("acik kayit: "))
            if prefix == "E" and any(normalized_label(text) == "acik kayit yok." for text in paragraphs):
                continue
            if prefix != "E" and record_ids(gap_note, "E"):
                references[section] = [gap_note]
                continue
            errors.append(f"{section}: kayıt veya açık kayıt açıklaması bulunmalı.")

        for number, cells in enumerate(rows[1:], 1):
            record = cells[0]
            label = f"{section} / satır {number}"
            if not RECORD_ID.fullmatch(record) or record[0] != prefix:
                errors.append(f"{label}: beklenen kimlik biçimi {prefix}-001.")
                continue
            if record in records:
                errors.append(f"{label}: yinelenen kayıt kimliği.")
                continue
            records.add(record)
            row = dict(zip(header, cells))
            if any(cell in EMPTY for cell in cells):
                errors.append(f"{record}: boş hücre veya yer tutucu bulunuyor.")
            references[record] = [value for column, value in row.items() if column not in {header[0], "Kaynak ve konum"}]
            gaps = record_ids(row.get(GAP_NOTE, ""), "E")
            if prefix in "BSVR":
                check_record_field(record, row, "Kanıt kaydı", "K", gaps, errors)
                findings = (value for column, value in row.items() if column != "Kanıt kaydı")
                if not gaps and UNKNOWN.intersection(findings):
                    errors.append(f"{record}: bilinmeyen bilgi bir açık kayda bağlanmalı.")
            if prefix == "V":
                check_record_field(record, row, "Süreç", "S", gaps, errors)
            if prefix == "R":
                check_record_field(record, row, "Faaliyet ve bağlantılı süreç / akış", "SV", gaps, errors)
            if prefix == "E":
                if normalized_label(row[header[1]]) not in {"eksik", "celiskili", "dogrulanamadi"}:
                    errors.append(f"{record}: açık kayıt durumu geçersiz.")
                check_record_field(record, row, "İlgili kayıtlar", "BSVRK", row["İlgili kayıtlar"] == "Kapsam", errors)
            if prefix == "K":
                location = row["Kaynak ve konum"]
                location_ids = record_ids(location, "K")
                inference = normalized_label(row["Kaynak türü"]) == "teknik cikarim"
                if location.startswith("Dayanak:") or (inference and location_ids):
                    if not location_ids or record in location_ids:
                        errors.append(f"{record}: başka bir kanıt kaydı dayanak olarak gerekli.")
                    references[record].append(location)
                validate_evidence(record, row, gaps, fixture_files, errors)

    for label, locations in references.items():
        cited, invalid = resolve_ranges(" | ".join(locations), records)
        for span in sorted(invalid):
            errors.append(f"{label}: {span} kayıt aralığı eksik veya geçersiz.")
        for missing in sorted(cited - records):
            errors.append(f"{label}: {missing} kayıt bağlantısı bulunamadı.")
        if label == HANDOFF and any(record.startswith("E-") for record in records - cited):
            errors.append(f"{TRANSITION}: aktarım notunda eksik açık kayıt bağlantısı var.")
    return errors


def check_record_field(record, row, column, prefixes, has_open_item, errors):
    cited = record_ids(row[column])
    if (not cited and not has_open_item) or any(value[0] not in prefixes for value in cited):
        errors.append(f"{record}: {column} alanındaki kayıt bağlantısı eksik veya yanlış türde.")


def validate_evidence(record, row, gaps, fixture_files, errors):
    if normalized_label(row["Kaynak türü"]) not in {normalized_label(label) for label in SOURCE_TYPES}:
        errors.append(f"{record}: kaynak türü geçersiz.")
    status, boundary = status_and_detail(row["Doğrulama durumu ve sınırı"], VERIFICATION)
    location = row["Kaynak ve konum"]
    if not has_detail(location) and not record_ids(location, "K"):
        errors.append(f"{record}: kaynak konumu gerekli.")
    if status not in VERIFICATION or not has_detail(boundary):
        errors.append(f"{record}: doğrulama durumu ve sınırı gerekli.")
    if status in {"Doğrulanamadı", "Çelişkili"} and not gaps:
        errors.append(f"{record}: doğrulanamayan veya çelişkili kanıta açık kayıt gerekli.")
    validate_source(record, row, fixture_files, errors)


def validate_transition(body, rows, sample_rows, references, errors):
    expected = {normalized_label(row[0]) for row in sample_rows}
    if len(rows) != len(expected) or {normalized_label(row[0]) for row in rows} != expected:
        errors.append(f"{TRANSITION}: her şablon ölçütü bir kez bulunmalı.")
    statuses = set()
    for number, (_, status, detail) in enumerate(rows, 1):
        label = f"{TRANSITION} / ölçüt {number}"
        status, _ = status_and_detail(status, TRANSITION_STATUS)
        statuses.add(status)
        references[label] = [detail]
        if not status or not record_ids(detail) or not has_detail(detail):
            errors.append(f"{label}: geçerli durum, gerekçe ve kayıt bağlantısı gerekli.")

    notes = [
        visible_text(node) for block in body if block.type == "bullet_list"
        for node in block.children
    ]
    overall = [note[len(OVERALL):].lstrip(" .:–—-") for note in notes
               if normalized_label(note).startswith(normalized_label(OVERALL))]
    handoff = [note[len(HANDOFF):].lstrip(" .:–—-") for note in notes
               if normalized_label(note).startswith(normalized_label(HANDOFF))]
    if len(overall) != 1 or len(handoff) != 1 or not has_detail(handoff[0]):
        errors.append(f"{TRANSITION}: tek genel durum ve tek aktarım notu gerekli.")
        return
    status, reason = status_and_detail(overall[0], TRANSITION_STATUS)
    combined = "Değerlendirilemedi"
    if "Karşılanmadı" in statuses:
        combined = "Karşılanmadı"
    elif statuses == {"Karşılandı"}:
        combined = "Karşılandı"
    if status != combined or not has_detail(reason):
        errors.append(f"{TRANSITION}: genel durum ölçütlerle tutarlı ve gerekçeli olmalı.")
    references[OVERALL] = [reason]
    references[HANDOFF] = handoff


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="completed report in UTF-8 Markdown")
    parser.add_argument("--fixture", type=Path, help="optional synthetic excerpt file")
    args = parser.parse_args()
    try:
        report = args.report.read_text(encoding="utf-8")
        fixture = args.fixture.read_text(encoding="utf-8") if args.fixture else None
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    errors = validate_report(report, fixture)
    for error in errors:
        print(error)
    print("Aşama 1 biçim kontrolü başarısız." if errors else "Aşama 1 biçim kontrolü başarılı.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
