# Contributing

Issues and pull requests are welcome in English or Turkish. The main README and maintainer guides use English. Skill instructions and legal terminology can use Turkish where it improves accuracy.

## Propose or improve a skill

- Use the skill proposal issue template for a new skill. Describe the audience, task, expected output, overlap with existing skills and how a reviewer could evaluate it.
- For a new package, create `skills/<name>/SKILL.md` with the standard `name` and `description` fields. Add `metadata.version`, write a focused workflow, and include the applicable license notice. Add `references/`, `scripts/` or `assets/` when the workflow needs them.
- For an improvement, describe the behavior or source being corrected. Keep the description aligned with shipped behavior, document relevant dependencies and update the skill's version as appropriate.
- Format files as UTF-8. Keep entrypoints brief, use relative Markdown links for bundled files and use synthetic or redacted data in examples and tests.

## Add or correct legal sources

Prefer primary sources such as official legislation, publications of public authorities and official copies of decisions. Record the title, issuing authority, relevant article or decision identifier, publication or effective date when known, source URL and date checked. Distinguish official text from interpretation, and distinguish proposed changes from measures already in force. Verify quoted text against the source and check reuse terms before bundling copies.

Use the legal content issue template to report an error. Include the affected file or passage, the issue you see and the best available official source. Mark uncertain sources or interpretations for review. Contributions that state legal obligations, interpret decisions or supply legal document templates may require review by a qualified Turkish legal professional before merge.

## Pull requests

Keep changes scoped to one skill or infrastructure purpose and link the relevant issue when available. Summarize the behavior changed, how it was verified, and any agent surfaces or legal claims that still need review. Use the [architecture guide](docs/architecture.md) for package and version conventions.

With Python 3.11 or later, run the same validation commands as CI from the repository root. Use the Python interpreter for your development environment.

```bash
python -m pip install -r tests/requirements.txt
python -X utf8 tests/validate_skills.py
python -X utf8 -m unittest discover -s tests
```

Submit material you have the right to contribute under the [project license](LICENSE). Disclose third-party material and its terms. Use the [private reporting process](SECURITY.md) for security issues or possible exposure of sensitive data.
