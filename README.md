# Turkish-Legal-Skills

Turkish-Legal-Skills is an early-stage, open-source collection of [Agent Skills](https://agentskills.io/specification) for work involving Türkiye's legal system. The project aims to help agents research law, verify current legal sources, inspect software and data practices, assess risks from evidence, draft documentation and compare public or internal statements with observed system behavior.

The project provides research and review workflows for human oversight. Legal advice and compliance determinations are outside the project's scope.

## Skills

| Skill | Status |
| --- | --- |
| [`turkish-kvkk`](skills/turkish-kvkk/SKILL.md) | Unreleased `0.4.0`. Counsel approved the Phase 1.5 [Stage 2 methodology](tests/stage-2/README.md). The Phase 1.6 [Stage 3 role assessment](tests/stage-3/README.md) is a `draft-preview` awaiting counsel review. |
| `turkish-legal-research`, `turkish-contracts`, `turkish-consumer-law`, `turkish-ecommerce-law` | Planned. |

## Install

Use Node.js 22.20 or later for the current Skills CLI. Run the command from the project that will use the skill. The GitHub commands require the skill to be available on the remote's default branch.

```bash
# Install from the GitHub collection
npx skills add efeketket/Turkish-Legal-Skills

# Install a single skill for Codex in the current project
npx skills add efeketket/Turkish-Legal-Skills --skill turkish-kvkk -a codex

# Install the skill from a local copy of this repository
npx skills add "<path-to-Turkish-Legal-Skills>" --skill turkish-kvkk -a codex --copy
```

Use `--list` with `add` to see the available skills before installing. Use `-g` for a user-wide installation. Use `--copy` when symlinks are unavailable or you want a standalone copy. See the [Skills CLI command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

For manual installation, copy the entire `skills/turkish-kvkk/` folder into a [skill directory for your agent](docs/compatibility.md#manual-installation), such as `.agents/skills/` at the target project's root for Codex. Open a new session if the agent does not pick up the change. Ask for a KVKK review to start with business discovery and continue to the preliminary inventory when the evidence supports it. A review limited to Stage 1 produces the five discovery outputs and a transition assessment. To resume, provide the existing Stage 1 report. See the [Stage 1 scenarios](tests/stage-1/README.md) and the [Stage 2 example report and checks](tests/stage-2/README.md).

For a full KVKK review or role assessment by processing activity, the preview uses the Stage 2 master inventory, activity-level decisions and role inputs to prepare a draft for counsel. An open item can defer the affected activity while review proceeds for others. Requests limited to business discovery or the inventory end at the requested stage. [Stage 3 example and checks](tests/stage-3/README.md)

For CLI-managed installs, use `npx skills list` to find the installed copy. For GitHub installs, use `npx skills check` to check for updates and `npx skills update turkish-kvkk` to update it from its recorded source. For a local-path install, rerun the original add command when the source changes. Use `npx skills remove turkish-kvkk` from the project to remove it, adding `-g` for a global install. For a manual install, replace the installed folder to update it or remove that folder to uninstall it.

## Discover

Supported clients can select a skill already installed in a location they scan. For an external search, use [skills.sh](https://skills.sh) or the Skills CLI.

```bash
npx skills find "KVKK"
npx skills find "Turkish data protection"
npx skills find "KVKK uyumluluk denetimi"
```

These searches illustrate how to look for a skill. A catalog listing is pending verification after publication. An agent without external search needs a source or an installed copy. See [Discovery and distribution](docs/discovery.md) for catalog entry paths and post-publication checks.

## Agent compatibility

Codex, Claude Code, Cursor, GitHub Copilot and Gemini CLI document Agent Skills support on specific surfaces. See the [compatibility matrix](docs/compatibility.md) for installation paths, surface limits and observed client test results.

## Contribute

Start with [CONTRIBUTING.md](CONTRIBUTING.md), the [architecture](docs/architecture.md) and the [roadmap](docs/roadmap.md). For a security issue or possible exposure of private data, follow [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE).
