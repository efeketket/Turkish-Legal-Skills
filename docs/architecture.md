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

The [KVKK entrypoint](../skills/turkish-kvkk/SKILL.md) routes discovery requests to the [Stage 1 reference](../skills/turkish-kvkk/references/stage-1-business-discovery.md) and loads the [output template](../skills/turkish-kvkk/assets/stage-1-outputs.md) for a Stage 1 review. Keep each implemented stage in its own skill-bundled reference with its inputs, outputs and transition criteria. Add routing as stages become available.

Stage 1 puts five outputs in one Markdown document so that processes, flows, preliminary roles and open items can refer to the same evidence. Subsequent stages can consume the scope, stable record IDs, source locations, verification status, open items and transition assessment. Keep record IDs when updating the evidence so later stages can follow prior findings. The stage transition records each criterion and its supporting evidence in Markdown.

## Versioning

Track each skill's maturity in its instructions and its independent version in `metadata.version`. The preview starts at `0.1.0`. Use patch increments for corrections, minor increments for new behavior and major increments for breaking workflow or output changes once stable. During `0.x`, describe breaking changes explicitly in the pull request. A change to one skill requires reviewing that skill's version only. For now, pull requests record changes. If release tags become useful, use names such as `turkish-kvkk-v0.1.0` to identify the skill and the repository snapshot.

## Validation

Pull requests run the [Agent Skills reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) and local checks for exact filenames, Markdown bodies and paths to bundled references. The validation job runs without agent credentials and checks package structure. Agent activation, catalog indexing and legal content review have separate evidence requirements.

The [Stage 1 scenario guide](../tests/stage-1/README.md) describes behavioral evaluation with synthetic inputs. Record agent behavior separately from automated package validation.
