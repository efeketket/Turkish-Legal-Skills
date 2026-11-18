"""Validate the format and bundled file references of each skill package."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import strictyaml
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
from skills_ref.validator import validate_metadata

SKILLS_DIRECTORY = Path(__file__).resolve().parents[1] / "skills"
MARKDOWN = MarkdownIt("commonmark")
# Inspect file: URLs too. The validator reads link destinations without rendering.
MARKDOWN.validateLink = lambda _destination: True
PORTABLE_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK_ATTRIBUTES = {"link": "href", "image": "src"}


def reference_error(destination: str, source: Path, skill: Path) -> str | None:
    """Return a diagnostic for a local link that cannot ship with the skill."""
    try:
        url = urlsplit(destination)
    except ValueError:
        return f"Invalid link destination: {destination}"
    if url.scheme == "file" or len(url.scheme) == 1:
        return f"Use a relative file reference: {destination}"
    if url.scheme or url.netloc or not url.path:
        return None

    path = unquote(url.path)
    if path.startswith("/") or "\\" in path or "\0" in path:
        return f"Use a relative file reference: {destination}"

    target = (source.parent / path).resolve()
    if not target.is_relative_to(skill):
        return f"Reference leaves the skill directory: {destination}"
    if not target.is_file():
        return f"Referenced file does not exist: {destination}"
    return None


def validate_skill(skill: Path) -> list[str]:
    """Check a single skill independently of the other packages."""
    entrypoint = skill / "SKILL.md"
    if skill.is_symlink() or entrypoint.is_symlink():
        return ["The skill directory and SKILL.md must be bundled directly."]
    if not entrypoint.is_file() or not any(path.name == "SKILL.md" for path in skill.iterdir()):
        return ["Missing SKILL.md with the required filename."]

    lines = entrypoint.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return ["SKILL.md must start with YAML frontmatter between two --- lines."]

    closing_line = lines.index("---", 1)
    try:
        metadata = strictyaml.load("\n".join(lines[1:closing_line])).data
    except strictyaml.YAMLError as error:
        return [f"Invalid YAML frontmatter: {error}"]
    if not isinstance(metadata, dict):
        return ["YAML frontmatter must be a mapping."]

    errors = validate_metadata(metadata, skill)
    if not PORTABLE_NAME.fullmatch(skill.name):
        errors.append("Use lowercase ASCII letters, digits and single hyphens in skill names.")

    extra_metadata = metadata.get("metadata", {})
    if not isinstance(extra_metadata, dict) or any(
        not isinstance(value, str) for value in extra_metadata.values()
    ):
        errors.append("The optional metadata field must map keys to scalar strings.")
    for field in ("license", "allowed-tools"):
        if field in metadata and not isinstance(metadata[field], str):
            errors.append(f"The optional {field} field must be a string.")

    body = "\n".join(lines[closing_line + 1 :])
    if not body.strip():
        errors.append("SKILL.md must contain a Markdown body.")

    skill_root = skill.resolve()
    for source in sorted(skill.rglob("*")):
        if source.suffix.lower() != ".md" or not source.is_file():
            continue
        if not source.resolve().is_relative_to(skill_root):
            errors.append(f"{source.relative_to(skill)}: Markdown file leaves the skill directory.")
            continue
        markdown = body if source == entrypoint else source.read_text(encoding="utf-8")
        for node in SyntaxTreeNode(MARKDOWN.parse(markdown)).walk():
            attribute = LINK_ATTRIBUTES.get(node.type)
            if attribute is None:
                continue
            error = reference_error(node.attrs[attribute], source, skill_root)
            if error:
                errors.append(f"{source.relative_to(skill)}: {error}")
    return errors


def main() -> int:
    skills = sorted(path for path in SKILLS_DIRECTORY.iterdir() if path.is_dir())
    if not skills:
        print("No skill directories found.")
        return 1

    failed = 0
    for skill in skills:
        errors = validate_skill(skill)
        if errors:
            failed += 1
            for error in errors:
                print(f"{skill.name}: {error}")
        else:
            print(f"{skill.name}: valid")
    print(f"{len(skills) - failed}/{len(skills)} skills passed validation.")
    return int(failed > 0)


if __name__ == "__main__":
    raise SystemExit(main())
