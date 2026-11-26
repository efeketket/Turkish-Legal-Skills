# Roadmap

## Phase 0 · Repository foundation

Ship the portable layout, the `turkish-kvkk` scope preview, validation, contributor guides and distribution instructions. Record evidence for every install, activation or listing claim.

## Phase 1 · KVKK evidence and source review

Phase 1.1 implements [Stage 1 business discovery](../skills/turkish-kvkk/references/stage-1-business-discovery.md) as a read-only review. It produces five linked outputs, including preliminary data flows, preliminary roles and open items. [Synthetic scenarios](../tests/stage-1/README.md) cover the Stage 1 workflow.

Phase 1.2 adds a Stage 1 Markdown checker, a bilingual skill-routing matrix and synthetic checks for provenance, disclosure and trust boundaries. The [evaluation guide](../tests/stage-1/README.md) describes the procedure for testing additional clients, and the [compatibility guide](compatibility.md) records client observations.

Phase 1.3 integrates Stage 2 processing activity identification in `turkish-kvkk` `0.3.0`. Stage 2 reuses the Stage 1 record IDs and produces a preliminary master inventory with linked data categories, purposes, operations, lifecycle and open items. The methodology is under renewed legal review. [Stage 2 methodology](../skills/turkish-kvkk/references/stage-2-processing-activities.md) · [Evaluation](../tests/stage-2/README.md)

Phase 1.4 adds a draft Stage 3 preview for activity-level role assessment. It connects six report outputs to the Stage 2 inventory and records separate factual and legal statuses, sources and scoped handoffs. The legal team will review the methodology and source findings before a version is approved. Stages 4–8 remain planned. [Stage 3 methodology](../skills/turkish-kvkk/references/stage-3-legal-roles.md) · [Source review](stage-3-source-review.md) · [Evaluation](../tests/stage-3/README.md)

Phase 1.5 prepares `turkish-kvkk` `0.4.0` for legal review. It applies the nine Stage 2 corrections, distinguishes the Stage 1 starting threshold from the Stage 2 handoff, records evidence limits by environment and preserves dated revisions across activity splits or mergers. Stage 3 uses the revised handoff. [Acceptance evidence](../tests/stage-2/README.md#phase-15-acceptance-evidence) · [Legal review brief](küb-docs/history/phase-1.5-hukuk-inceleme-promptu.md)

Phase 1.6 closes Stage 3 legal review on 26 November 2026. Counsel approved the role methodology, report template and activity-level handoff and confirmed the existing Stage 2 approval. Live Codex CLI validation remains open for technical release and live-use acceptance. [Counsel decision](küb-docs/history/asama3-kapanıs.md) · [Verification record](../tests/stage-3/README.md)

Stage 4 closed legal review on 26 November 2026. Counsel found all seven corrections satisfied and approved the `turkish-kvkk` `0.5.0` methodology and template for draft candidate assessment in scopes with matching Stage 2 and Stage 3 decisions. The template tracks element-level evidence, legitimate interest indicators, Article 6(4) evidence status and documented counsel decisions. Natural and explicit Codex CLI runs verified the blocked handoff on the current synthetic chain. [Closure decision](küb-docs/history/asama4-kapanıs.md) · [Counsel-approved methodology](../skills/turkish-kvkk/references/stage-4-processing-conditions.md) · [Live verification](../tests/stage-3/README.md#live-stage-4-and-stage-5-checks)

Stage 5 closed legal review on 26 November 2026 for real-case intake and preparation and synthetic methodology review in unreleased `turkish-kvkk` `0.6.0`. The `0.7.0` preview implements the conditions from that decision for candidate drafts submitted to counsel. It requires matched Stage 2 and Stage 3 handoffs, an operation-specific Stage 4 record and sufficient transfer facts. Standard contract controls include the default notifier, text integrity and signatures on the Turkish text. [Closure decision](küb-docs/history/asama5-kapanis.md) · [Stage 5 intake](../skills/turkish-kvkk/references/stage-5-intake.md) · [Masked intake scenario](../tests/stage-5/fixtures/masked-stage-5-input.md) · [Remote support example](../tests/stage-5/samples/remote-support-stage-5-intake.md)

Stage 6 is ready for counsel review as a draft on retention, disposal and data security. Its proposed handoff links the current activity and scope to the Stage 2 and Stage 3 decisions, with Stage 4 and Stage 5 dependencies recorded where they affect a finding. Counsel will decide the intake threshold, the minimum evidence and the scope for real-case use before Stage 6 is routed by the skill. [Counsel brief](küb-docs/asama-6-hukuk-inceleme-promptu.md) · [Deferred handoff example](../tests/stage-6/samples/phase-1.5-stage-6-intake.md) · [Backup and restore example](../tests/stage-6/samples/backup-stage-6-draft.md)

Further Phase 1 work includes the following.

1. Complete Stage 3 live report validation. Capture skill and reference reads, validator results, project file snapshots and trace safety checks.
2. Apply the Stage 6 legal review findings and validate the approved scope with synthetic fixtures before enabling the route.
3. Compare observed system behavior with corresponding statements in privacy notices and other documentation. Give each finding a source, observed evidence, confidence level and open questions. Route legal conclusions and draft documents to human review.
4. Test install and removal, explicit invocation and automatic selection across named client versions. Evaluate Turkish and English prompts, including cases outside the skill's scope. After publication, check catalog results independently.

## Later

Expand the KVKK workflow to cover risk assessment, document drafting and audit report templates with review. Consider separate skills for Turkish legal research, contracts, consumer law and e-commerce law as their scopes and maintainers become clear.
