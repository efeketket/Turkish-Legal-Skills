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

Stage 1 puts five outputs in one Markdown document so that processes, flows, preliminary roles and open items can refer to the same evidence. The [Stage 2 template](../skills/turkish-kvkk/assets/stage-2-outputs.md) puts six outputs and the handoff into one separate Markdown report. The master inventory defines one stable `A-…` ID per activity. Operational function and concrete purpose guide activity separation, with system boundaries supporting the decision. The category matrix combines reusable category names and optional business-specific subcategories with actual field names, groups and sources. The purpose matrix retains each field–purpose relationship. Lifecycle, operations, evidence and open items link to the master activity IDs. The process coverage table links the Stage 1 `S-…` records to any resulting activities.

Keep the Stage 1 report accessible so Stage 2 references to `B-…`, `S-…`, `V-…`, `R-…` and existing `K-…` records can be resolved. Record later evidence under a new `K-…` ID with its date and scope. Preserve the original evidence and link both sources to the same `E-…` item when resolving a gap or recording a discrepancy. Record the current status and new evidence link in the handoff. Each Stage 2 transition criterion has its own status, supporting records, gaps, blockers and follow-up. The connected Markdown reports carry this history and support later legal review without a separate store.

## Versioning

Track each skill's maturity in its instructions and its independent version in `metadata.version`. The preview starts at `0.1.0`. Use patch increments for corrections, minor increments for new behavior and major increments for breaking workflow or output changes once stable. During `0.x`, describe breaking changes explicitly in the pull request. A change to one skill requires reviewing that skill's version only. For now, pull requests record changes. If release tags become useful, use names such as `turkish-kvkk-v0.1.0` to identify the skill and the repository snapshot.

## Validation

Pull requests run the [Agent Skills reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) and local checks for exact filenames, Markdown bodies and paths to bundled references. The same job exercises both Markdown checkers. Stage 2 checks the six outputs, stable IDs, links across tables and stages, handoff and transition structure. Its optional synthetic fixture mode also checks new file-backed source locations and disclosure markers. The validation job requires no agent credentials.

The [Stage 1](../tests/stage-1/README.md) and [Stage 2](../tests/stage-2/README.md) scenario guides describe agent evaluation with synthetic inputs. Review the cited sources and legal substance independently of automated report checks.
