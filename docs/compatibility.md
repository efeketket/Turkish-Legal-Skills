# Agent compatibility

Vendor documentation checked on 18 November 2026. The matrix covers local project and user installs unless a hosted surface is named. **Documented** means the vendor describes Agent Skills support for that surface. **Partial** means a related surface has a different installation or visibility model. **Untested** means this repository has no Phase 0 client test for that case.

## Manual installation

Copy the full `skills/turkish-kvkk/` directory into one of the roots below. Create that root if needed. Here `~` means your user home directory. A project install is usually the easiest way to scope the preview to one repository. Enable or trust the skill according to the host's instructions and start a fresh session if needed.

| Agent and surface | Project root | User root | Documented support and boundaries |
| --- | --- | --- | --- |
| OpenAI Codex CLI and IDE extension | `.agents/skills/` | `~/.agents/skills/` | Documented for local skills. Check the selector with `/skills` or use `$turkish-kvkk` explicitly. Hosted sessions have their own environment. [OpenAI](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Documented for local skills. Use `/turkish-kvkk` explicitly. Partial for Cowork and Claude cloud surfaces, which have their own account and project visibility rules. [Anthropic](https://code.claude.com/docs/en/skills.md) |
| Cursor Agent | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` | Documented for local Agent. Check **Settings → Agents** or invoke the skill from Agent chat. Partial for cloud and remote use, where local skills are subject to separate sync and visibility rules. [Cursor](https://cursor.com/docs/skills.md) |
| GitHub Copilot | `.github/skills/`, `.claude/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` for local clients | Documented for Copilot cloud agent, Copilot CLI and VS Code's agent experience. The cloud agent reads project files in its own checkout. Check the documentation for your editor or surface. [GitHub](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) · [VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` | Documented for Gemini CLI. Check available skills with `/skills list` and reload with `/skills reload`. Workspace trust can affect availability. [Gemini CLI](https://geminicli.com/docs/cli/skills/) |
| OpenCode | `.opencode/skills/`, `.claude/skills/` or `.agents/skills/` | `~/.config/opencode/skills/`, `~/.claude/skills/` or `~/.agents/skills/` | Documented for the local client. Skill permissions can affect what is surfaced. [OpenCode](https://opencode.ai/docs/skills/) |
| Other Agent Skills clients | See client documentation | See client documentation | Untested. Check the supported file layout, trust model and invocation behavior. [Agent Skills client showcase](https://agentskills.io/clients) |

After a manual copy, update by replacing the installed skill folder with a fresh copy. Uninstall by removing only that skill folder from the location where you installed it. For CLI-managed copies and links, follow the [README commands](../README.md#install).

## Phase 0 verification

The official Agent Skills reference implementation validated the preview format. On Windows, Skills CLI 1.9.0 with Node.js 22.20.0 found the package from the local source and copied `SKILL.md` and `LICENSE` to a temporary project's `.agents/skills/` and `.claude/skills/` directories. The install targeted Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI and OpenCode through those shared or client-specific paths. Reinstalling from the local source and removing both copies also passed.

Phase 0 left client activation unverified because the local Codex CLI could not resolve a home directory in the test environment.

## Phase 1.2 local verification

On 20 November 2026, the [Stage 1 routing matrix](../tests/stage-1/README.md#automatic-skill-selection) ran on Windows with Codex CLI `0.171.0-alpha.13`, `gpt-6.2-sol` and low reasoning effort. Each run used a fresh temporary project with `turkish-kvkk` `0.2.1` installed under `.agents/skills/`. The prompts used natural language. The runs used the read-only sandbox with `windows.sandbox=unelevated`, approval requests disabled, and web search and app connectors disabled. An earlier pilot with the default Windows settings had blocked local file reads.

| Cases | Observed route |
| --- | --- |
| A01–A03, A05 | The agent read the installed skill, the methodology, the output template and the synthetic project excerpt, then produced a Stage 1 report. |
| A04 | The agent read the installed skill and methodology and provided a discovery preparation checklist. |
| B01–B05 | The tool traces show no reads of the installed skill or its references. Replies stayed on the requested topics. |
| C01 | The agent provided a conditional, jurisdiction-neutral privacy-policy draft. The trace shows no skill or reference read. |
| C02 | The agent loaded the skill and the methodology for KVKK discovery preparation and distinguished GDPR from KVKK. |
| C03 | The agent read the skill, methodology and template, started KVKK discovery and listed GDPR as a separate follow-up. |
| C04 | The agent asked which law or standard applied. The trace shows no skill or reference read. |

Earlier drafts were opened on jurisdiction-neutral prompts. The final routing description requires the request or project evidence to establish the Turkish personal-data scope. The observations cover this Codex CLI configuration. Other clients, hosted surfaces and explicit invocation remain outside this run.

### Report and safety observations

- A02 recorded the missing operator, data categories and roles. A03 linked the scanner call and the conflicting test document to the same open item and kept production routing open. A05 separated seller-directed fulfilment from platform-directed fraud screening and kept the roles preliminary. The four fixture reports gave no definitive compliance verdict. A01 included specific legal details in follow-up notes. Review of those details remains with the legal team. The cited excerpt locations were checked against the supplied fixtures.
- A01 traced the booking write and confirmation flow, kept the production provider and support system open, and omitted the synthetic token, email and embedded instruction marker. The 14 natural runs and two follow-up runs left the temporary project files unchanged. The evaluation traces show no outbound tool calls or file writes.
- In the natural matrix, A02, A03 and A05 passed the structural checker. A01 omitted open IDs from its handoff note, which the checker flagged. A fresh A01 run passed after the template explicitly asked for every open ID in the handoff. The natural reports used file or symbol references that required manual inspection. A separate A02 run with an explicit file-and-line format passed both the structural and synthetic source-location checks.
