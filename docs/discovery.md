# Discovery and distribution

Agent Skills standardizes package structure and describes how a client can enumerate skills, offer their descriptions to the model and load instructions on demand. External search depends on an agent, integration or separate CLI. [Agent Skills client implementation guide](https://agentskills.io/client-implementation/adding-skills-support)

| Situation | How the skill reaches the agent |
| --- | --- |
| Installed and recognized | The client can offer it for explicit selection or select it for a relevant request, subject to its scope, permissions and invocation behavior. |
| Uninstalled, external search available | A configured integration or an explicit search command can surface a matching result. Preview the source and install it in the relevant scope. |
| Uninstalled, external search unavailable | Provide a repository link or install the skill manually. Automatic discovery cannot be guaranteed in this environment. |

Agents with a terminal can use `npx skills find` when the user requests a search and the environment allows it. Vercel's optional `find-skills` skill can give an agent a workflow for that search. [find-skills source](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)

## Search metadata

The canonical metadata lives in each `SKILL.md`. Keep a stable skill name and use concise Turkish and English descriptions of tasks the package actually supports. The Phase 0 preview covers scoping a software review under Türkiye's personal data protection framework. Its description uses KVKK, Turkish privacy law, Turkish data protection and KVKK uyumluluk denetimi in that context. A broader collection description can describe Turkish legal research as a project goal.

Use the following as search and selection probes. A search match and an agent deciding to load an installed skill are separate results.

| Search intent | Probe examples |
| --- | --- |
| Direct KVKK need | `KVKK`, `KVKK compliance`, `KVKK uyumluluk denetimi` |
| Türkiye-specific privacy | `Turkish data protection`, `Turkish privacy law`, `Türkiye kişisel veri koruma` |
| Broad or ambiguous | `Turkish law`, `Turkish legal research`, `GDPR Turkey`, `SaaS legal audit` |

Broad prompts may indicate another jurisdiction, an EU GDPR question or a general legal task. Use them to check relevance and scope. Search probes do not belong in frontmatter solely to influence ranking. [Agent Skills guidance on descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)

## Catalogs and publication routes

- **skills.sh and Skills CLI.** The CLI finds installable packages in standard folders such as `skills/<name>/` from a known repository source. The skills.sh leaderboard uses anonymous install telemetry. Vercel describes a public Git repository and normal installations with telemetry enabled as the automatic route for a skill to appear. Its documentation provides no mandatory submission form or guaranteed indexing time or rank. Users can opt out with `DISABLE_TELEMETRY=1`. [Vercel publishing guide](https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context#theres-no-special-publish-command-for-skills.sh) · [skills.sh documentation](https://www.skills.sh/docs)
- **GitHub CLI.** The preview command `gh skill search` uses GitHub Code Search across public repositories. GitHub CLI 2.90 or later also offers `gh skill preview` and `gh skill install`. The optional `gh skill publish --dry-run` validates a local tree. Running `gh skill publish` without that flag guides maintainers through adding the `agent-skills` topic, choosing a tag and creating a GitHub release. A release is a separate publishing choice. [Search command](https://cli.github.com/manual/gh_skill_search) · [Publish command](https://cli.github.com/manual/gh_skill_publish)
- **VoltAgent Awesome Agent Skills.** This open-source curated list accepts proposed external repository links through a pull request. It asks for a direct skill link, a short description and the appropriate category. Maintainers review additions. Consider a submission once the skill carries a useful, reviewable workflow. [Contribution guide](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md)
- **Awesome GitHub Copilot.** This open-source collection accepts individual skill contributions to its own catalog and has a separate review process. Review its current criteria if upstream contribution is useful. [Contribution guide](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md)
- **Domain-hosted discovery.** Cloudflare's draft defines `/.well-known/agent-skills/index.json` for clients that implement that protocol. Consider it if a project domain and compatible clients justify hosting an index. Phase 0 uses GitHub distribution. [Discovery RFC](https://github.com/cloudflare/agent-skills-discovery-rfc)

## GitHub listing

Suggested repository description

> Open-source Agent Skills for Turkish legal research, KVKK review, and evidence-based software compliance workflows.

Suggested topics

`agent-skills`, `turkish-law`, `legal-research`, `kvkk`, `data-protection`, `legal-tech`, `ai-agents`, `open-source`, `compliance`

1. Review the first GitHub publication, add the description and topics, and confirm that the default branch serves the public skill directory. Enable private vulnerability reporting if available.
2. From a clean test project, run `npx skills add efeketket/Turkish-Legal-Skills --list` and a named install. Verify the version, license and file placement. Check that the selected client can open the skill.
3. Check skills.sh in the browser and through `npx skills find "turkish-kvkk" --owner efeketket`. Repeat the domain searches above. Where available, compare `gh skill search turkish-kvkk --owner efeketket`. Record the date, query and result before claiming a catalog listing.
4. Consider a reviewed directory submission once the skill meets that directory's criteria. Track each listing independently.

## Phase 0 status

The GitHub repository was public and empty at the Phase 0 check. On 18 November 2026, the owner-scoped Skills CLI search returned no exact entry, and the `KVKK`, `Turkish data protection` and `KVKK uyumluluk denetimi` searches returned other results without this preview. Remote installation and catalog visibility can be checked once the local files are published.
