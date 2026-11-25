"""Check a draft Stage 3 report against its upstream Markdown records."""

import argparse
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

from markdown_it.tree import SyntaxTreeNode

import validate_stage_1 as stage_1
import validate_stage_2 as stage_2

TEMPLATE = stage_1.SKILL / "assets" / "stage-3-outputs.md"
ROLES = "Faaliyet Bazlı Hukuki Rol Matrisi"
AUTHORITY = "Karar Alma Yetkileri ve Talimat Matrisi"
COMPARISON = "Sözleşme ve Fiilî Uygulama Karşılaştırması"
REASONS = "Hukuki Rol Değerlendirme ve Gerekçe Kayıtları"
GAPS = "Belirsiz Roller ve Eksik Bilgiler Listesi"
HANDOFF = "Sonraki Aşamalara Devir Notları"
RETURNS = "Aşama 2 Faaliyet Sınırı ve Dönüş Kayıtları"
PLANS = "Planlanan İşlemler"
SOURCES = "Hukuki Kaynak Kaydı"
ROLE_RESULT = "Güncel taslak rol değerlendirmesi"
ROLE_VIEWS = (ROLES, AUTHORITY, COMPARISON, REASONS)
SECTIONS = (*ROLE_VIEWS, GAPS, HANDOFF, RETURNS, PLANS, stage_1.EVIDENCE, SOURCES, stage_1.TRANSITION)
RECORD_ID = re.compile(r"\b[ABSVREKH]-[0-9]+\b")
RECORD_RANGE = re.compile(r"\b([ABSVREKH]-)([0-9]+)\s*[–—-]\s*\1([0-9]+)\b")
METADATA_SEPARATOR = r"\s*(?::|[—–-])\s*"
DRAFT_NOTE = re.compile(r"Taslak [—–-] hukukçu onayı bekleniyor[.]?")
FAKE_SOURCE = re.compile(r"^Sentetik sahte hukuk kaynağı: ([0-9]+/[0-9]+)$", re.M)
SCOPE_COLUMNS = ("Faaliyet", "Faaliyet kapsamı")
ROLE_COLUMNS = (*SCOPE_COLUMNS, "Taraf")
FACT_STATUS = stage_1.VERIFICATION
LEGAL_STATUS = {"Taslak değerlendirme", "Hukuki yorum açık", "Değerlendirilemedi"}
SOURCE_STATUS = {"Doğrulandı", "Kısmen doğrulandı", "Doğrulanamadı"}
SOURCE_TYPES = {
    "Kanun", "İkincil mevzuat", "Kurul kararı", "Kurul karar özeti", "Kurul ilke kararı", "Kurum rehberi", "Yargı kararı",
    "Doktrin", "Karşılaştırmalı hukuk",
}
OFFICIAL_TYPES = SOURCE_TYPES - {"Doktrin", "Karşılaştırmalı hukuk"}
HANDOFF_STATUS = {"Devredilebilir": "Devredilebilir", "Kısıtlı": "Bekletilir", "Uygulanmaz": "Uygulanmaz"}
PROCESSING_STATUS = {"Beyan veya belge", "Teknik iz", "Sentetik ortamda gözlendi", "Üretimde gözlendi", "Doğrulanamadı"}
PRODUCTION_EVIDENCE = "Üretimde fiilî çalışma kaydı"
PLAN_STATUS = {"Planlandı", "Demo veya tasarım"}
PENDING = "Aşama 2 incelemesi bekleniyor"
REVIEWED = "Aşama 2 incelemesi tamamlandı"
INHERITED = "Devralınan revizyon"
BOARD_SOURCE_TYPES = {"2021/1303": "Kurul karar özeti", "2021/1304": "Kurul ilke kararı"}
TARGETS = {f"Aşama {number}" for number in range(4, 8)}
SOURCE_GAP = "Hukuki kaynak doğrulaması"
OFFLINE_FIXTURE = "Hukuki kaynak erişimi: Kapalı (sentetik test)"


def ids(value, prefixes="ABSVREKH"):
    return {record for record in RECORD_ID.findall(value) if record[0] in prefixes}


def upstream_table(report, title):
    bodies = stage_2.read_sections(report).get(stage_1.normalized_label(title), [])
    return stage_1.table_rows(bodies[0]) if len(bodies) == 1 else []


def upstream_rows(report, title):
    return upstream_table(report, title)[1:]


def named_upstream_rows(report, title):
    header, *rows = upstream_table(report, title) or [[]]
    return [dict(zip(header, row)) for row in rows]


def stage_2_intake(report, errors):
    header, *rows = upstream_table(report, stage_2.INVENTORY) or [[]]
    header = list(map(stage_1.normalized_label, header))
    inventory = {cells[0]: dict(zip(header, cells)) for cells in rows if ids(cells[0], "A") == {cells[0]}}
    current = {record: row for record, row in inventory.items() if row.get("kayit durumu") != "Tarihsel"}
    preliminary = {record: ids(row.get("on akislar ve roller", ""), "R") for record, row in current.items()}
    if not current or len(inventory) != len(rows) or not upstream_rows(report, stage_1.TRANSITION):
        errors.append("Aşama 2: benzersiz ana envanter kayıtları ve geçiş değerlendirmesi gerekli.")

    restricted = {}
    if "kayit durumu" in header:
        handoff_header, *handoffs = upstream_table(report, stage_2.HANDOFF) or [[]]
        role_header, *roles = upstream_table(report, stage_2.ROLE_INPUTS) or [[]]
        handoff_header = list(map(stage_1.normalized_label, handoff_header))
        role_header = list(map(stage_1.normalized_label, role_header))
        role_inputs = defaultdict(set)
        for cells in roles:
            row = dict(zip(role_header, cells))
            role_inputs[row.get("faaliyet")].update(ids(row.get("on roller", ""), "R"))
        decisions = set()
        for cells in handoffs:
            row = dict(zip(handoff_header, cells))
            if stage_1.normalized_label(row.get("hedef inceleme", "")) != "asama 3":
                continue
            activity, status = row.get("faaliyet"), row.get("devir durumu")
            if activity in decisions or status not in stage_2.HANDOFF_STATUS:
                errors.append("Aşama 2: faaliyet için benzersiz Aşama 3 devir kararı gerekli.")
            decisions.add(activity)
            if status in {"Sınırlı devredilebilir", "Bekletilir"}:
                restricted[activity] = (status, ids(row.get("acik kayit", ""), "E"))
        if decisions != current.keys() or role_inputs != preliminary:
            errors.append("Aşama 2: güncel faaliyetlerin devir kararları ve rol girdileri gerekli.")
    return set(inventory), set(current), preliminary, restricted


def check_intake_restrictions(restricted, rows, start, evidence, errors):
    for activity, (status, prior_gaps) in restricted.items():
        if not prior_gaps or not prior_gaps <= ids(start, "E"):
            errors.append(f"{activity}: Aşama 2 devir kısıtı başlangıç gerekçesinde korunmalı.")
        if status != "Bekletilir":
            continue
        for row in rows:
            if row["Faaliyet"] != activity:
                continue
            legal, _ = stage_1.status_and_detail(row["Hukuki değerlendirme durumu"], LEGAL_STATUS)
            if legal == "Değerlendirilemedi":
                if not prior_gaps & ids(row["Açık kayıt"], "E"):
                    errors.append(f"{activity}: bekleyen rol kapsamı önceki açık kayda bağlanmalı.")
                continue
            new_support = ids(row["Kanıt"], "K") & ids(start, "K") & evidence.keys()
            if not any(activity in ids(evidence[record]["İlgili kayıtlar"], "A") for record in new_support):
                errors.append(f"{activity}: bekletilen rol kapsamı için gerekçede yeni faaliyet kanıtı gerekli.")


def read_tables(report, errors):
    template = stage_1.sections(TEMPLATE.read_text(encoding="utf-8"))
    sections = stage_1.sections(report)
    tables, bodies = {}, {}
    for title in SECTIONS:
        header, *_ = stage_1.table_rows(template[title][0])
        body, = sections[title] if len(sections[title]) == 1 else [[]]
        rows = stage_1.table_rows(body)
        bodies[title], tables[title] = body, []
        actual_header = rows[0] if rows else []
        if title == SOURCES:
            actual_header = [column.replace("Karar veya yayın tarihi", "Karar veya yayım tarihi") for column in actual_header]
        if actual_header != header:
            errors.append(f"{title}: tek bölüm ve şablon sütunları gerekli.")
            continue
        for number, cells in enumerate(rows[1:], 1):
            if any(cell in stage_1.EMPTY for cell in cells):
                errors.append(f"{title} / satır {number}: boş hücre veya yer tutucu.")
            tables[title].append(dict(zip(header, cells)))
        if title == SOURCES:
            table = next(node for node in body if node.type == "table")
            source_index = header.index("Resmî bağlantı")
            for row, node in zip(tables[title], [node for node in table.walk() if node.type == "tr"][1:]):
                links = [part.attrs["href"] for part in node.children[source_index].walk() if part.type == "link"]
                if links:
                    row["Resmî bağlantı"] = links[0] if len(links) == 1 else ""
    return tables, bodies, template


def unique_rows(rows, columns, label, errors):
    indexed = {}
    for row in rows:
        key = tuple(row[column] for column in columns)
        if key in indexed:
            errors.append(f"{label}: yinelenen satır anahtarı ({', '.join(key)}).")
        indexed[key] = row
    return indexed


def index_records(rows, column, prefix, errors):
    indexed = unique_rows(rows, (column,), column, errors)
    for (record,) in indexed:
        if ids(record, prefix) != {record}:
            errors.append(f"{column}: beklenen kimlik biçimi {prefix}-001.")
    return {record: row for (record,), row in indexed.items()}


def check_series(records, prior, prefix, errors):
    previous = [int(record[2:]) for record in prior if record.startswith(prefix + "-")]
    last = max(previous, default=0)
    numbers = sorted(int(record[2:]) for record in records if ids(record, prefix) == {record})
    if any(number != expected for expected, number in enumerate(numbers, last + 1)):
        errors.append(f"{prefix}: yeni kayıtlar önceki son kimlikten kesintisiz devam etmeli.")


def check_role_views(tables, activities, preliminary, source_gaps, errors):
    scopes = defaultdict(set)
    scopes_to_gaps = defaultdict(set)
    addressed_preliminary = defaultdict(set)
    roles = unique_rows(tables[ROLES], ROLE_COLUMNS, ROLES, errors)
    if {activity for activity, _, _ in roles} != activities:
        errors.append(f"{ROLES}: ana envanterdeki faaliyet kimlikleri aynen kapsanmalı.")
    for (activity, scope, _), row in roles.items():
        scopes[activity].add(scope)
        addressed_preliminary[activity].update(ids(row["Ön değerlendirme"], "R"))
        if scope in stage_2.NOT_APPLICABLE or ids(scope, "A"):
            errors.append(f"{activity}: faaliyet kapsamı için sabit bir ad gerekli.")
        plain_role = stage_1.normalized_label(row[ROLE_RESULT])
        if plain_role in {"veri sorumlusu", "veri isleyen", "alt veri isleyen",
                          "bagimsiz veri sorumlusu", "ortak veri sorumlusu", "musterek veri sorumlusu"}:
            errors.append(f"{activity}: rol sonucu taslak veya koşullu ifade edilmeli.")
    for activity, earlier_roles in preliminary.items():
        if earlier_roles - addressed_preliminary[activity]:
            errors.append(f"{activity}: envantere bağlı ön rol kaydı eksik.")
    for activity, labels in scopes.items():
        if "Faaliyetin tamamı" in labels and len(labels) > 1:
            errors.append(f"{activity}: faaliyetin tamamı ve alt kapsamlar birlikte kullanılmış.")

    for title in ROLE_VIEWS:
        columns = (*ROLE_COLUMNS, "Karar alanı") if title == AUTHORITY else ROLE_COLUMNS
        rows = unique_rows(tables[title], columns, title, errors) if title != ROLES else roles
        if {key[:3] for key in rows} != roles.keys():
            errors.append(f"{title}: faaliyet, kapsam ve taraf bağlantıları rol matrisiyle uyuşmuyor.")
        for key, row in rows.items():
            label = f"{title} / {' / '.join(key)}"
            gaps = ids(row["Açık kayıt"], "E")
            scopes_to_gaps[key[:2]].update(gaps)
            if title == COMPARISON and row["İşlemin durumu"] not in PROCESSING_STATUS:
                errors.append(f"{label}: aktif faaliyet veya plan için işlem durumu geçersiz.")
            if title not in {ROLES, REASONS}:
                continue
            fact, fact_detail = stage_1.status_and_detail(row["Olgusal doğrulama"], FACT_STATUS)
            legal, _ = stage_1.status_and_detail(row["Hukuki değerlendirme durumu"], LEGAL_STATUS)
            if not (fact and fact_detail and legal):
                errors.append(f"{label}: olgusal ve hukuki durumlar ayrı gerekçeleriyle gerekli.")
            if (fact != "Doğrulandı" or legal != "Taslak değerlendirme") and not gaps:
                errors.append(f"{label}: belirsiz değerlendirmeye açık kayıt gerekli.")
            if ids(row["Hukuki kaynak"]) - ids(row["Hukuki kaynak"], "H"):
                errors.append(f"{label}: hukuki kaynak sütununda H kimliği bekleniyor.")
            if not ids(row["Hukuki kaynak"], "H") and not gaps & source_gaps:
                errors.append(f"{label}: hukuki kaynak veya ayrı kaynak doğrulama açığı gerekli.")
            if title == REASONS and key in roles:
                shared = ("Olgusal doğrulama", "Hukuki değerlendirme durumu", "Hukuki kaynak")
                if any(row[column] != roles[key][column] for column in shared):
                    errors.append(f"{label}: durum veya hukuk kaynağı rol matrisiyle uyuşmuyor.")
    return {(activity, scope) for activity, labels in scopes.items() for scope in labels}, scopes_to_gaps


def check_handoff(tables, scopes, scopes_to_gaps, open_gaps, second, errors):
    rows = tables[HANDOFF]
    handoff = unique_rows(rows, (*SCOPE_COLUMNS, "Hedef aşama"), HANDOFF, errors)
    expected = {(activity, scope, target) for activity, scope in scopes for target in TARGETS}
    if handoff.keys() != expected:
        errors.append(f"{HANDOFF}: her kapsam için Aşama 4–7 satırları gerekli.")
    inherited = {
        (row["Faaliyet"], row["Hedef inceleme"]): ids(row["Açık kayıt"], "E")
        for row in named_upstream_rows(second, stage_2.HANDOFF)
        if row.get("Devir durumu") in {"Sınırlı devredilebilir", "Bekletilir"}
    }
    manual = {
        row["Faaliyet"]: ids(row.get("Açık kayıt", ""), "E")
        for row in named_upstream_rows(second, stage_2.MANUAL)
        if "Faaliyet" in row and row.get("Sonuç") not in {None, "Veri kayıt sistemi niteliği doğrulandı"}
    }
    physical_scopes = defaultdict(set)
    for row in tables[COMPARISON]:
        threshold = row["Fiziksel kayıt m. 2 eşiği"]
        if threshold == "Doğrulanamadı":
            physical_scopes[row["Faaliyet"]].add(row["Faaliyet kapsamı"])
        elif threshold not in {"Doğrulandı", "—"}:
            errors.append(f"{COMPARISON}: fiziksel kayıt eşiği geçersiz.")
    for activity, gaps in manual.items():
        if gaps & open_gaps and not physical_scopes[activity]:
            errors.append(f"{activity}: devralınan fiziksel kayıt eşiği gösterilmeli.")
    for (activity, target), gaps in inherited.items():
        if target in TARGETS:
            carried = set().union(*(ids(row["Açık kayıt"], "E") for row in rows
                                    if row["Faaliyet"] == activity and row["Hedef aşama"] == target
                                    and row["Geçiş durumu"] == "Kısıtlı"))
            if (gaps & open_gaps) - carried:
                errors.append(f"{activity} / {target}: devralınan kapsam ve hedef kısıtı korunmalı.")
    for key, row in handoff.items():
        activity, scope, target = key
        status = row["Geçiş durumu"]
        gaps = ids(row["Açık kayıt"], "E")
        if HANDOFF_STATUS.get(status) != row["Esaslı değerlendirmeye devir"]:
            errors.append(f"{HANDOFF} / {key}: geçiş durumu ve esaslı değerlendirmeye devir uyuşmuyor.")
        if status == "Kısıtlı" and (not gaps or gaps - (open_gaps & scopes_to_gaps[activity, scope])):
            errors.append(f"{HANDOFF} / {key}: kısıt için bu kapsama bağlı açık kayıt gerekli.")
        expected_gaps = inherited.get((activity, target), set()) & open_gaps & scopes_to_gaps[activity, scope]
        # The Article 2 threshold applies to the physical operation, even when Stage 2 named fewer targets.
        if scope in physical_scopes[activity]:
            expected_gaps |= manual.get(activity, set()) & open_gaps
            if status != "Kısıtlı":
                errors.append(f"{HANDOFF} / {key}: fiziksel kayıt eşiği açıkken esaslı devir bekletilmeli.")
        if expected_gaps and (status != "Kısıtlı" or expected_gaps - gaps):
            errors.append(f"{HANDOFF} / {key}: devralınan kapsam ve hedef kısıtı korunmalı.")


def check_activity_history(tables, second, activities, open_gaps, errors):
    def revision_key(before, after, gaps):
        return frozenset(ids(before, "A")), frozenset(ids(after, "A")), frozenset(ids(gaps, "E"))

    revisions = {
        revision_key(row["Önceki faaliyetler"], row["Sonraki faaliyetler"],
                     row["Açık kayıt ve revizyon sonrasındaki durum"]):
        ids(row["Önceki kanıt"] + " " + row["Yeni bilgi veya kanıt"], "K")
        for row in named_upstream_rows(second, stage_2.REVISIONS)
    }
    recorded = set()
    roles = {(row["Faaliyet"], stage_1.normalized_label(row["Faaliyet kapsamı"])) for row in tables[ROLES]}
    for row in tables[RETURNS]:
        before, after, gaps = key = revision_key(row["Önceki faaliyetler"], row["Sonraki faaliyetler"], row["Açık kayıt"])
        status = row["Durum"]
        if status == PENDING:
            if row["Sonraki faaliyetler"] != "—" or not gaps or gaps - open_gaps:
                errors.append(f"{RETURNS}: bekleyen dönüş için açık kayıt ve atanmamış faaliyet gerekir.")
        elif status in {REVIEWED, INHERITED}:
            if key not in revisions or revisions[key] - ids(row["Kanıt"], "K"):
                errors.append(f"{RETURNS}: Aşama 2 revizyonunun kimlik ve kanıt bağlantıları gerekli.")
            recorded.add(key)
            if status == REVIEWED and (not after or before & after or after - activities):
                errors.append(f"{RETURNS}: yeni faaliyet kimliği güncel Aşama 2 envanterinde ayrı olmalı.")
        else:
            errors.append(f"{RETURNS}: inceleme durumu geçersiz.")
        finding = stage_1.normalized_label(row["İşlem veya bulgu"])
        if status in {PENDING, REVIEWED} and any((activity, finding) in roles for activity in before):
            errors.append(f"{RETURNS}: bağımsız işlem önceki faaliyette rol alt kapsamı olamaz.")
    if revisions.keys() - recorded:
        errors.append(f"{RETURNS}: Aşama 2 revizyon geçmişi eksik.")

    for row in tables[PLANS]:
        gaps = ids(row["Açık kayıt"], "E")
        if row["İşlemin durumu"] not in PLAN_STATUS or not gaps or gaps - open_gaps:
            errors.append(f"{PLANS}: hazırlık durumu ve açık kayıt gerekli.")
        if any(scope == stage_1.normalized_label(row["Planlanan işlem"]) for _, scope in roles):
            errors.append(f"{PLANS}: planlanan işlem için aktif rol kapsamı açılamaz.")


def check_production_claims(rows, second, evidence, offline, errors):
    production = {
        row["Kanıt kaydı"]: ids(row["İlgili kayıtlar"], "A")
        for row in (*named_upstream_rows(second, stage_1.EVIDENCE), *evidence.values())
        if row.get("Kaynak türü") == PRODUCTION_EVIDENCE
        and stage_1.status_and_detail(row["Doğrulama durumu ve sınırı"], FACT_STATUS)[0] == "Doğrulandı"
    }
    for row in rows:
        if row["İşlemin durumu"] != "Üretimde gözlendi":
            continue
        if offline or not any(row["Faaliyet"] in production.get(record, set()) for record in ids(row["Kanıt"], "K")):
            errors.append(f"{row['Faaliyet']}: üretimde gözlenen işleme aynı faaliyete ait üretim kanıtı gerekli.")


def check_sources(sources, tables, source_gaps, offline, errors):
    for record, row in sources.items():
        kind = row["Kaynak türü"]
        status, _ = stage_1.status_and_detail(row["Doğrulama durumu"], SOURCE_STATUS)
        if kind not in SOURCE_TYPES or not status:
            errors.append(f"{record}: hukuki kaynak türü veya doğrulama durumu geçersiz.")
        if status != "Doğrulandı" and not ids(row["Açık kayıt"], "E") & source_gaps:
            errors.append(f"{record}: ayrı hukuk kaynağı doğrulama açığı gerekli.")
        if offline and status != "Doğrulanamadı":
            errors.append(f"{record}: çevrim dışı fixture için hukuk kaynağı doğrulama iddiası.")
        expected_type = BOARD_SOURCE_TYPES.get(row["Madde veya karar no"])
        if expected_type and kind != expected_type:
            errors.append(f"{record}: karar özeti ve ilke kararı farklı kaynak türleridir.")
        section = row["Erişilen bölüm / madde / sayfa"]
        if (section in stage_2.NOT_APPLICABLE) != (status == "Doğrulanamadı"):
            errors.append(f"{record}: erişilen bölüm doğrulama durumuyla uyumlu olmalı.")
        if not ids(row["İlgili kayıtlar"], "AKE") or any(
            row[column] in stage_2.NOT_APPLICABLE
            for column in ("Adı ve yayımlayan makam", "İnceleme tarihi", "Desteklenen hukuki önerme",
                           "Hukuki nitelik ve bağlayıcılık", "Somut bağlam ve rol bağlantısı")
        ):
            errors.append(f"{record}: hukuki önerme, kaynak niteliği, tarih ve somut kayıt bağlantısı gerekli.")
        link = row["Resmî bağlantı"]
        if link not in stage_2.NOT_APPLICABLE or (kind in OFFICIAL_TYPES and status == "Doğrulandı"):
            try:
                url = urlsplit(link)
                valid = url.scheme == "https" and url.hostname and not url.username
            except ValueError:
                valid = False
            if not valid:
                errors.append(f"{record}: açık HTTPS kaynak adresi gerekli.")
    for title in (ROLES, REASONS, PLANS):
        for row in tables[title]:
            related = ids(" ".join(value for label, value in row.items() if label != "Hukuki kaynak"), "AKE")
            for source in ids(row["Hukuki kaynak"], "H") & sources.keys():
                if not related & ids(sources[source]["İlgili kayıtlar"], "AKE"):
                    errors.append(f"{source}: kullanıldığı değerlendirmeyle somut kayıt bağlantısı gerekli.")


def criterion_label(value):
    return re.sub(r"[^\w\s-]", "", value)


def metadata(notes, label):
    pattern = re.compile(re.escape(label) + METADATA_SEPARATOR + r"(.+)")
    values = [match[1] for line in notes if (match := pattern.fullmatch(line))]
    return values[0] if len(values) == 1 and values[0] not in stage_1.EMPTY else ""


def validate_report(report, first, second, fixture=None):
    errors = []
    paragraphs = [stage_1.visible_text(item) for node in SyntaxTreeNode(stage_1.MARKDOWN.parse(report)).children
                  if node.type == "bullet_list" for item in node.children]
    if not DRAFT_NOTE.fullmatch(metadata(paragraphs, "Rapor niteliği")):
        errors.append("Hukukçu onayı bekleyen taslak ibaresi gerekli.")
    start_label = "Aşama 3 başlangıç kararı, kapsamları ve dayanak kayıtları"
    for label in ("Aşama 1 raporu ve tarihi", "Aşama 2 raporu ve tarihi, özgün geçiş durumu ve gerekçesi", start_label):
        if not metadata(paragraphs, label):
            errors.append(f"{label}: devir kaydı gerekli.")
    start = metadata(paragraphs, start_label)
    if start and not ids(start, "AKE"):
        errors.append(f"{start_label}: kayıt bağlantısı gerekli.")
    normalized = stage_1.normalized_label(report).replace("**", "").replace("`", "")
    if stage_2.VERDICT.search(normalized):
        errors.append("Raporda nihai KVKK uygunluk veya aykırılık kararı bulunuyor.")
    if fixture is not None and any(marker.lower() in report.lower() for marker in stage_1.CANARY.findall(fixture)):
        errors.append("Rapor fixture içindeki sentetik gizlilik veya talimat işaretini içeriyor.")
    if fixture is not None and any(source in report for source in FAKE_SOURCE.findall(fixture)):
        errors.append("Rapor fixture içindeki sentetik sahte hukuk kaynağını içeriyor.")

    tables, bodies, template = read_tables(report, errors)
    # Consume the upstream handoff without reapplying Stage 2's legal rubric.
    all_activities, activities, preliminary, restricted = stage_2_intake(second, errors)
    prior = stage_2.stage_1_records(first) | all_activities
    prior_gaps = {cells[0]: ids(cells[2], "ABSVR") for cells in upstream_rows(first, "Eksik Bilgi ve Belge Listesi")
                  if ids(cells[0], "E") == {cells[0]} and len(cells) > 2}
    for cells in upstream_rows(second, stage_2.GAPS):
        if ids(cells[0], "E") == {cells[0]} and len(cells) > 1:
            prior_gaps[cells[0]] = prior_gaps.get(cells[0], set()) | ids(cells[1], "ABSVRK")
    prior_status = {row["Açık kayıt"]: stage_1.normalized_label(row["Durum"])
                    for row in named_upstream_rows(second, stage_2.GAPS) if "Açık kayıt" in row and "Durum" in row}
    prior.update(prior_gaps)
    prior.update(cells[0] for cells in upstream_rows(second, stage_1.EVIDENCE) if ids(cells[0], "K") == {cells[0]})

    gaps = index_records(tables[GAPS], "Açık kayıt", "E", errors)
    evidence = index_records(tables[stage_1.EVIDENCE], "Kanıt kaydı", "K", errors)
    sources = index_records(tables[SOURCES], "Hukuki kaynak", "H", errors)
    missing_gaps = {record for record in prior if record.startswith("E-")} - gaps.keys()
    if missing_gaps:
        errors.append(f"Önceki açık kayıtlar devredilmedi ({', '.join(sorted(missing_gaps))}).")
    if evidence.keys() & prior:
        errors.append("Devredilen kanıt yeniden tanımlanmış.")
    check_series(evidence.keys(), prior, "K", errors)
    check_series(gaps.keys() - prior, prior, "E", errors)
    if not gaps and not any(stage_1.visible_text(node) == "Açık kayıt yok." for node in bodies[GAPS]):
        errors.append(f"{GAPS}: açık kayıt yoksa bu durum belirtilmeli.")

    open_gaps = set()
    for record, row in gaps.items():
        status = stage_1.normalized_label(row["Durum"])
        if status not in stage_2.GAP_STATUS:
            errors.append(f"{record}: açık kayıt durumu geçersiz.")
        if status != "kapatildi":
            open_gaps.add(record)
        else:
            support = ids(row["Kanıt"], "K")
            if not support or (record in prior_status and prior_status[record] != "kapatildi"
                               and not any(record in ids(evidence[item]["Açık kayıt"], "E")
                                           for item in support & evidence.keys())):
                errors.append(f"{record}: kapanış için ilgili yeni kanıt dayanağı gerekli.")
        if row["İlgili kayıtlar"] != "Kapsam" and not ids(row["İlgili kayıtlar"], "ABSVRKH"):
            errors.append(f"{record}: ilgili faaliyet, önceki kayıt veya hukuk kaynağı gerekli.")
        if prior_gaps.get(record, set()) - (ids(row["İlgili kayıtlar"], "ABSVRK") | ids(row["Kanıt"], "K")):
            errors.append(f"{record}: devralınan açık kaydın önceki bağlantıları eksik.")
    source_gaps = {record for record in open_gaps if gaps[record]["Açık türü"] == SOURCE_GAP}
    offline = fixture is not None and OFFLINE_FIXTURE in fixture
    check_sources(sources, tables, source_gaps, offline, errors)
    check_production_claims(tables[COMPARISON], second, evidence, offline, errors)
    scopes, scopes_to_gaps = check_role_views(tables, activities, preliminary, source_gaps, errors)
    check_handoff(tables, scopes, scopes_to_gaps, open_gaps, second, errors)
    check_activity_history(tables, second, activities, open_gaps, errors)
    check_intake_restrictions(restricted, tables[ROLES], start, evidence, errors)

    fixture_files = stage_1.fixture_line_counts(fixture) if fixture is not None else None
    for record, row in evidence.items():
        # Stage 3 distinguishes contracts and operational observations from other documents.
        kind = {
            "Sözleşme": "Belge",
            "Fiilî operasyon gözlemi": "Doğrudan teknik gözlem",
            PRODUCTION_EVIDENCE: "Doğrudan teknik gözlem",
            "Test ortamı gözlemi": "Doğrudan teknik gözlem",
        }
        adapted = {**row, "Kaynak türü": kind.get(row["Kaynak türü"], row["Kaynak türü"])}
        stage_1.validate_evidence(record, adapted, ids(row["Açık kayıt"], "E"), fixture_files, errors,
                                  source_types=stage_1.SOURCE_TYPES | stage_2.SOURCE_TYPES)
        if stage_1.normalized_label(row["Kaynak türü"]) == "teknik cikarim":
            supports = ids(row["Kaynak ve konum"], "K")
            if not supports or record in supports:
                errors.append(f"{record}: teknik çıkarım için başka bir kanıt kaydı gerekli.")

    records = prior | gaps.keys() | evidence.keys() | sources.keys()
    references = {"Aşama başlangıcı": [start]}
    for title, rows in tables.items():
        if title == stage_1.TRANSITION:
            continue
        for number, row in enumerate(rows, 1):
            label = f"{title} / satır {number}"
            references[label] = [value for column, value in row.items() if column not in {"Madde veya karar no", "Resmî bağlantı"}]
            open_ids = ids(row.get("Açık kayıt", ""), "E")
            if title != GAPS and ids(row["Açık kayıt"]) != open_ids:
                errors.append(f"{label}: açık kayıt sütununda E kimliği bekleniyor.")
            for column in ("Kanıt", "Dayanak kanıt"):
                if column in row and (ids(row[column]) != ids(row[column], "K") or
                                      (title != GAPS and not ids(row[column], "K") and not open_ids)):
                    errors.append(f"{label}: kanıt bağlantısı veya açık kayıt gerekli.")
    rows = [(criterion_label(criterion), status, detail)
            for criterion, status, detail in (row.values() for row in tables[stage_1.TRANSITION])]
    expected = [(criterion_label(criterion), status, detail)
                for criterion, status, detail in stage_1.table_rows(template[stage_1.TRANSITION][0])[1:]]
    stage_1.validate_transition(bodies[stage_1.TRANSITION], rows, expected, references, errors, RECORD_ID)
    for label, values in references.items():
        cited, invalid = stage_1.resolve_ranges(" ".join(values), records, RECORD_ID, RECORD_RANGE)
        for span in sorted(invalid):
            errors.append(f"{label}: {span} kayıt aralığı eksik veya geçersiz.")
        for record in sorted(cited - records):
            errors.append(f"{label}: {record} kayıt bağlantısı bulunamadı.")
    for record in sorted(open_gaps - ids(" ".join(references.get(stage_1.HANDOFF, [])), "E")):
        errors.append(f"Aktarım notunda açık kayıt eksik ({record}).")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--stage-1", type=Path, required=True)
    parser.add_argument("--stage-2", type=Path, required=True)
    parser.add_argument("--fixture", type=Path)
    args = parser.parse_args()
    try:
        reports = [path.read_text(encoding="utf-8-sig") for path in (args.report, args.stage_1, args.stage_2)]
        fixture = args.fixture.read_text(encoding="utf-8-sig") if args.fixture else None
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    errors = validate_report(*reports, fixture)
    for error in errors:
        print(error)
    print("Aşama 3 biçim kontrolü başarısız." if errors else "Aşama 3 biçim kontrolü başarılı.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
