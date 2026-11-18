import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from validate_skills import validate_skill


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.skill = Path(temporary.name) / "test-skill"
        self.skill.mkdir()

    def write(self, path: str, contents: str):
        file_path = self.skill / path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(contents, encoding="utf-8")

    def write_skill(self, body: str):
        self.write(
            "SKILL.md",
            "---\nname: test-skill\ndescription: >-\n"
            "  Turkish privacy review preview — Türkiye\n"
            'metadata:\n  version: "0.1.0"\n---\n' + body,
        )

    def test_checks_reference_links_and_images_in_bundled_markdown(self):
        self.write_skill("[Guide][guide]\n\n[guide]: references/review%20guide.md#scope")
        self.write("references/review guide.md", "![Diagram](../assets/flow.svg)")
        self.write("assets/flow.svg", "<svg/>")
        self.assertEqual(validate_skill(self.skill), [])

    def test_rejects_missing_references_in_bundled_markdown(self):
        self.write_skill("[Guide](references/guide.md)")
        self.write("references/guide.md", "[Missing](missing.md)")
        self.assertIn(
            "references/guide.md: Referenced file does not exist: missing.md",
            [error.replace("\\", "/") for error in validate_skill(self.skill)],
        )

    def test_rejects_paths_to_neighboring_packages_even_if_they_exist(self):
        self.write_skill("[Neighbor](%2e%2e/other/SKILL.md)")
        other = self.skill.parent / "other"
        other.mkdir()
        (other / "SKILL.md").touch()
        errors = validate_skill(self.skill)
        self.assertTrue(any("leaves the skill directory" in error for error in errors))

    def test_ignores_external_urls_fragments_and_examples(self):
        self.write_skill(
            "[External](https://example.org/guide) [Section](#scope)\n\n"
            "```md\n[Example](missing.md)\n```\n\n## Scope"
        )
        self.assertEqual(validate_skill(self.skill), [])

    def test_rejects_absolute_local_references(self):
        self.write_skill("[File](file:///tmp/guide.md) [Windows](C:/guide.md) [Root](/guide.md)")
        errors = validate_skill(self.skill)
        self.assertEqual(len(errors), 3)
        self.assertTrue(all("Use a relative file reference" in error for error in errors))

    def test_rejects_invalid_yaml(self):
        self.write("SKILL.md", "---\nname: test-skill\nname: duplicate\n---\n# Skill")
        self.assertTrue(any("Invalid YAML" in error for error in validate_skill(self.skill)))

    def test_rejects_missing_description_and_name_mismatch(self):
        self.write("SKILL.md", "---\nname: other-skill\n---\n# Skill")
        errors = validate_skill(self.skill)
        self.assertTrue(any("description" in error for error in errors))
        self.assertTrue(any("must match" in error for error in errors))

    def test_rejects_missing_markdown_body(self):
        self.write_skill("")
        self.assertIn("SKILL.md must contain a Markdown body.", validate_skill(self.skill))

    def test_requires_exact_entrypoint_case(self):
        self.write("skill.md", "---\nname: test-skill\ndescription: Preview\n---\n# Skill")
        self.assertIn("Missing SKILL.md with the required filename.", validate_skill(self.skill))
