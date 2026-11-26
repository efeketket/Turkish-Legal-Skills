# Turkish-Legal-Skills

Turkish-Legal-Skills is an early-stage, open-source collection of [Agent Skills](https://agentskills.io/specification) for work involving Türkiye's legal system. The project aims to help agents research law, verify current legal sources, inspect software and data practices, assess risks from evidence, draft documentation and compare public or internal statements with observed system behavior.

The project provides research and review workflows for human oversight. Legal advice and compliance determinations are outside the project's scope.

## Skills

| Skill | Status |
| --- | --- |
| [`turkish-kvkk`](skills/turkish-kvkk/SKILL.md) | Unreleased `0.8.2`. Counsel approved the Stage 2–4 methodologies and the Stage 5 intake and preparation scope. Stage 5 supports candidate drafts for counsel under its intake conditions. The Stage 6 `0.8.1` closing review accepted limited real-case intake and factual preparation. [Stage 4 counsel decision](docs/küb-docs/history/asama4-kapanıs.md) · [Stage 5 counsel decision](docs/küb-docs/history/asama5-kapanis.md) · [Stage 6 closing decision](docs/küb-docs/history/asama6-kapanisimsibisey.md) · [Live CLI verification record](tests/stage-3/README.md) |
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

For a full KVKK review or role assessment by processing activity, Stage 3 uses the Stage 2 master inventory, activity-level decisions and role inputs to prepare a draft report for counsel. An open item can defer the affected scope. Requests limited to discovery or inventory end at the requested stage. Stage 4 records the handoff for each requested scope and prepares draft candidates for counsel only where the current activity has matching Stage 2 and Stage 3 decisions for that scope and Stage 4. [Stage 3 examples and checks](tests/stage-3/README.md) · [Stage 4 intake example](tests/stage-4/samples/phase-1.5-stage-4-intake.md) · [Stage 4 assessment example](tests/stage-4/samples/booking-stage-4-draft.md)

Stage 5 records recipients, transfer paths and matching Stage 2 and Stage 3 handoffs. Factual mapping can continue while the operation-specific Stage 4 record is pending. When transfer assessment is requested, each candidate draft requires a matching Stage 4 record and evidence that establishes the relevant transfer facts. Final mechanism choices require a documented decision by counsel. [Candidate conditions](skills/turkish-kvkk/references/stage-5-intake.md#aday-taslağı-koşulları) · [Masked intake example](tests/stage-5/samples/masked-stage-5-draft.md) · [Deferred transfer example](tests/stage-5/samples/phase-1.5-stage-5-intake.md) · [Remote support example](tests/stage-5/samples/remote-support-stage-5-intake.md)

Stage 6 records matching handoffs, storage environments and copies, policy statements, settings, observed operations and evidence gaps. Real-case routing covers intake and factual preparation, including documented disposal choices and explanations. Substantive methodology is demonstrated on synthetic examples. Substantive real-case drafts require approval for a future version. [Stage 6 verification](tests/stage-6/README.md)

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
