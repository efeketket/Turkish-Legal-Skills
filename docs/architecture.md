# Architecture

Each immediate child of `skills/` is an independently installable package with its own `SKILL.md`. Its frontmatter follows the [Agent Skills specification](https://agentskills.io/specification). The folder name is the skill name, and this collection uses lowercase ASCII letters, digits and single hyphens for portable names. Agents can use the description to select a skill, read its body when needed and open bundled files on demand.

```text
.github/                 Pull request validation and contribution templates
docs/                    Maintainer and user guides
skills/<skill-name>/
  SKILL.md               Metadata and agent instructions
  LICENSE                License notice shipped with the skill
  references/            Optional supporting material
  scripts/               Optional runnable helpers
  assets/                Optional resources or templates
tests/                   Repository validation and validator tests
```

The source directory is the distribution unit. Consumers can copy one folder or install it through a supported CLI. Platform-specific install paths belong in [the compatibility guide](compatibility.md). Maintainer docs and validation tools live at the repository root and are outside skill packages. The GitHub owner and repository name appear in distribution instructions where a source is required. A repository transfer calls for updating those instructions and rechecking catalog entries.

## References and shared work

Use skill-relative Markdown links for bundled files and forward slashes in paths. CI checks local links and images in each `SKILL.md` and in bundled Markdown. Reference definitions are checked when used. Keep runtime files in the same skill directory, including any common resource or helper that a single-skill install needs.

Keep shared contributor guidance in `docs/`. If multiple skills eventually need the same runtime material, bundle a reviewed copy in each consumer and record its source and revision. A future maintainer tool can check or synchronize those copies before release. Installations receive the bundled copies and require only explicitly documented runtime prerequisites.

## KVKK review stages

The [KVKK entrypoint](../skills/turkish-kvkk/SKILL.md) routes preparation and discovery to the [Stage 1 reference](../skills/turkish-kvkk/references/stage-1-business-discovery.md) and loads the [Stage 1 template](../skills/turkish-kvkk/assets/stage-1-outputs.md) for a discovery report. For a broader review it uses the existing Stage 1 report or prepares one first. The [Stage 2 reference](../skills/turkish-kvkk/references/stage-2-processing-activities.md) contains the legal team's complete methodology and a technical implementation section. The handoff uses the five outputs, shared evidence and transition assessment. The Stage 2 start decision records whether the business, parties and general flow are sufficiently understood and identifies any blockers.

Stage 1 puts five outputs in one Markdown document so that processes, flows, preliminary roles and open items can refer to the same evidence. The [Stage 2 template](../skills/turkish-kvkk/assets/stage-2-outputs.md) puts six outputs and the handoff into one preliminary Markdown report. The master inventory defines one stable `A-…` ID per activity. The organization represented, decision authority, concrete purpose, operation and systems guide activity boundaries. The category matrix has separate fields for base category, business-specific subcategory and purpose. The purpose matrix retains each field–purpose relationship. Lifecycle, operations, evidence and open items link to the master activity IDs. The process coverage table links the Stage 1 `S-…` records to resulting activities.

Keep the Stage 1 report accessible so Stage 2 references to `B-…`, `S-…`, `V-…`, `R-…` and existing `K-…` records can be resolved. Record later evidence with its own `K-…` ID, date, source type, environment and affirmative and negative verification limits. The Stage 1 → 2 threshold assesses whether inventory research can begin. Stage 2 evaluates its eleven criteria for the report and for each current activity. A separate decision per activity and target review records any limits or blockers. The revision history preserves previous findings, dates, both sources and affected `E-…` items. A split or merger retains historical `A-…` records and links them to the current ones.

Stage 3 supports full KVKK reviews and requests for activity-level role assessment. Routing checks the prior reports through the [technical handoff](../skills/turkish-kvkk/references/stage-3-integration.md). For scopes with a sufficient basis, the agent loads the [counsel-approved role methodology](../skills/turkish-kvkk/references/stage-3-legal-roles.md) and [Stage 3 template](../skills/turkish-kvkk/assets/stage-3-outputs.md). The draft report uses the existing Stage 2 activity IDs. An activity, operational scope and party link the role, decision authority, contract comparison and rationale views. Each comparison distinguishes statements, contract terms, technical observations and operational evidence. Legal sources have report-local `H-…` IDs. Findings keep factual verification and legal assessment in separate fields, and source access gaps have their own `E-…` records.

Stage 3 records the Stage 2 report version or date and original transition decision. Its validator reads the upstream inventory, role inputs, decisions and record IDs. For an activity deferred at Stage 2, a Stage 3 assessment requires new evidence cited in the reassessment. Historical IDs remain available as references. Earlier reports are supported through their inventory and transition record. Stage 3 records proposed activity boundary changes in linked open items. It assesses its 15 criteria separately and scopes Stage 4–7 role dependencies to activities, operational scopes and target stages.

Stage 4 intake joins the current Stage 2 activity and its Stage 4 decision with the matching Stage 3 scope and target row. The preparation note records blockers, the effect of new evidence and any required update to the upstream decisions. In both real and synthetic cases the matching handoffs allow draft candidate assessment for counsel. Each candidate links to its legal elements, evidence limits and open items. Special-category classification and Article 6(4) measures have dedicated fields. Only documented counsel decisions provide the final choice for an assessed operation. [Stage 4 intake](../skills/turkish-kvkk/references/stage-4-intake.md) · [Counsel-approved methodology](../skills/turkish-kvkk/references/stage-4-processing-conditions.md) · [Worked assessment](../tests/stage-4/samples/booking-stage-4-draft.md)

Stage 5 joins the current activity with the Stage 2 and Stage 3 decisions for the requested transfer scope and the Stage 5 target. The intake links Stage 4 findings at the operation level and carries any open evidence limits. In the synthetic assessment draft, each flow has a report-local number shared by the flow and mechanism tables. The template records recipients, location, access and onward transfers, with dedicated fields for the legal condition, safeguards and missing evidence. [Stage 5 intake](../skills/turkish-kvkk/references/stage-5-intake.md) · [Transfer assessment draft](../skills/turkish-kvkk/references/stage-5-transfers.md) · [Output template](../skills/turkish-kvkk/assets/stage-5-outputs.md)

## Versioning

Track each skill's maturity in its instructions and its independent version in `metadata.version`. The preview starts at `0.1.0`. Use patch increments for corrections, minor increments for new behavior and major increments for breaking workflow or output changes once stable. During `0.x`, describe breaking changes explicitly in the pull request. A change to one skill requires reviewing that skill's version only. For now, pull requests record changes. If release tags become useful, use names such as `turkish-kvkk-v0.1.0` to identify the skill and the repository snapshot.

## Validation

Pull requests run the [Agent Skills reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) and local checks for exact filenames, Markdown bodies and paths to bundled references. The same job exercises the Markdown checkers. Stage 2 checks the six outputs, stable IDs, links across tables and stages, handoff and transition structure. Stage 3 adds checks for the six role outputs, scope and party links, continued IDs, source access states and scoped restrictions. Synthetic fixture modes also check file-backed source locations and disclosure markers. The validation job requires no agent credentials.

The scenario guides describe agent evaluation with synthetic inputs. Review the cited sources and legal substance independently of automated report checks. [Stage 1](../tests/stage-1/README.md) · [Stage 2](../tests/stage-2/README.md) · [Stage 3](../tests/stage-3/README.md)
