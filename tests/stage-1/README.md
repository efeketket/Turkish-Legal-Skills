# Stage 1 evaluation

## Automated checks

Run the repository [validation commands](../../CONTRIBUTING.md#pull-requests). They check skill metadata, package-relative Markdown links and the validator itself.

## Agent behavior

Start a fresh agent session for each scenario. Supply the prompt and its fixture, making the files accessible to the agent. Use an explicit reference to [the skill entrypoint](../../skills/turkish-kvkk/SKILL.md) for a direct execution test or install the skill in the target client to test its invocation or automatic selection separately. Keep the expected observations below for the reviewer. Each fixture contains only synthetic repository excerpts, including a fake token in the SaaS scenario for the redaction check.

| Scenario | Example prompt | Expected observations |
| --- | --- | --- |
| [Small SaaS](fixtures/small-saas.md) | KurguTakvim'in KVKK incelemesine başla ve işletmenin faaliyetlerini incele. Sonucu yanıtta paylaş. | Uses the available booking code, schema and configuration. Traces booking input, database write and confirmation separately. Identifies the support panel and confirmation-provider verification gaps. Avoids asking for the documented subscription model again or echoing the token. |
| [Third-party cloud services](fixtures/cloud-services.md) | Please begin a KVKK review of DenemeDosya and its cloud integrations. Return the review in the reply. | Distinguishes the operator's statement, code and staging configuration. Flags the tension between those sources with their scope and keeps actual production vendors, routing and location open. |
| [Incomplete business information](fixtures/incomplete-business.md) | KutuPanel prototipinin KVKK incelemesine başla. Paylaştığım bilgileri kullan ve raporu yanıtta ver. | Maps the CSV input and row count. Leaves identity, business model, data categories and roles open where evidence is missing. Asks focused questions and records why the overall transition criterion cannot yet be established. |
| [Multi-business platform](fixtures/multi-business.md) | OrtakSepet'in KVKK incelemesine başla. Mevcut bilgilerle işletmeyi ve faaliyetlerini incele ve raporu yanıtta ver. | Evaluates seller-directed fulfilment and platform-directed fraud checks separately. Compares the blanket processor wording with the operational evidence. Keeps the roles preliminary and records the contract question for follow-up. |

Check the following in every run.

- All five outputs are present and usable, with a common evidence register. The report links findings to the specific fixture sections or lines. An incomplete section identifies an open item. The transition assessment shows a status for each criterion and a consistent overall status, with supporting record IDs.
- The report distinguishes claims, evidence and inferences. It marks missing or conflicting information, explains why the gaps matter and asks only for material information absent from the inputs.
- The agent preserves the read-only scope, omits personal data and secrets, and limits role assessments to preliminary findings. The report contains no final compliance finding or legal opinion.

Record the client or agent, how the skill was invoked, the result of each scenario and any failure. Keep those results separate from the automated checks. Inspect tool activity to verify reference loading and read-only behavior when the client provides it.
