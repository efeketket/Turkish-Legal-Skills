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

Client activation is unverified. The local Codex CLI could not resolve a home directory in the test environment. Explicit invocation, automatic selection and hosted behavior are pending tests for the listed clients.
