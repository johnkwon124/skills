---
name: deliverable-trust-scoring
description: Layers tiered verification gates, a document-level confidence score, a persistent verification audit log, and a periodic consistency sweep on top of a fact-check pipeline. Use it when decision-driving deliverables must clear a measurable accuracy bar before they go out, or when accuracy needs to be tracked over time.
---

# deliverable-trust-scoring

## What it adds

A fact-check pipeline (for example `document-fact-gate`) verifies one document and then forgets. This skill wraps that pipeline and adds four things. It does not reimplement verification.

1. **Tiered gates.** Higher-stakes documents must pass a threshold. Lower-stakes ones only get a warning.
2. **A confidence score** per document, weighted by how much each claim matters.
3. **An audit log** that persists across sessions and can be queried before writing.
4. **A periodic sweep** that finds contradictions across documents and tracks accuracy trends per workflow.

Run this as an independent check. The person or workflow that produced the document should not be the one deciding whether it passes.

## Step 0: Inputs and tier

Required: document path, name of the workflow that produced it, original sources.
Optional: entity (the company, project, or topic the document is about). It keys the log. If missing, extract it from the document.

Pick the tier from the workflow name using `references/tiering-and-gating.md`.

- **Tier 0** (daily digests, link roundups): do not run this skill. The lint stage alone is enough.
- **Tier 1** (periodic or sector reports): compute the score, log it, warn below the threshold, never block.
- **Tier 2** (documents that drive a decision): run everything and block below the threshold.

If the tier is unclear, use Tier 2.

## Step 1: Look up prior records

Before verifying, query the log for the entity.

```bash
python3 scripts/ledger.py lookup --entity "<entity>" --ledger "<ledger path>"
```

Compare key figures in the new document (funding amount, valuation, headcount, dates) with what was verified before. If a value differs, add "This differs from the earlier record: ..." to the verifier prompt so it checks that item first. Skip this step if the log is empty or the entity is new.

## Step 2: Run the fact-check pipeline

Run the pipeline as documented, without changing its prompts or rules. Append one extra output request to the verifier prompt:

```
Also output each atomic claim as a JSON array. Mark materiality "high" for claims
that would change a decision if wrong (financial figures, valuations, funding rounds,
contract terms, dates). Mark everything else "normal".

[{"id": "c1", "category": "VERIFIED|UNSUPPORTED|CONTRADICTED|SYNTHESIS",
  "materiality": "high|normal", "text": "short restatement of the claim"}]
```

Let the pipeline finish its merge, writing-standard gate, and QA report. You receive the corrected file and the JSON array.

## Step 3: Score

Score the original classification, before the fail-closed merge. If you score after the merge, deleting risky claims raises the score. Scoring the original measures how accurate the draft was.

```bash
python3 scripts/score.py --claims claims.json --tier <0|1|2>
```

The score is VERIFIED weight divided by (VERIFIED + UNSUPPORTED + CONTRADICTED) weight. High-materiality claims weigh 2, normal claims 1. SYNTHESIS is excluded. The output includes a `verdict`: `not_gated`, `pass`, `warn`, or `block`.

## Step 4: Disposition by tier

| Tier | Threshold | If below |
| --- | --- | --- |
| 1 | 0.90 | Do not block. Report the score as a warning. |
| 2 | 0.95 | Block. Return "confidence below threshold, rework needed". The document may not go to send or filing steps. |

Act on the `verdict` value directly. Only an explicit instruction from the document's owner can override a Tier 2 block, and the override must be written to the log and the QA report.

If any claim was CONTRADICTED, note it in the QA report even when the document passes after correction. Such documents get priority in the next sweep.

## Step 5: Extra checks

- If Step 1 found a value that differs from the log and the verifier marked it VERIFIED, require the verifier to cite the evidence that the newer value is correct (for example a later funding round). With no evidence, downgrade it to UNSUPPORTED.
- If the document cites a URL that was not in the source list given to the verifier, mark it FAIL. It may be an invented source.

### Step 5b: Record repeated mistakes

If the same workflow has made the same kind of mistake before (misreading dates on one site, inventing URLs in one field), log a pattern keyed to the workflow, not the entity.

```bash
python3 scripts/ledger.py flag-pattern --ledger "<ledger path>" \
  --skill "<workflow>" --entity "<entity>" --pattern "<one-sentence pattern>"
```

Before drafting, a Tier 2 workflow can run `ledger.py lookup-patterns --skill "<workflow>"` and take extra care on those points. Patterns are never auto-resolved. A person decides during the sweep whether one has stopped occurring.

## Step 6: Write the audit log

```bash
python3 scripts/ledger.py append --ledger "<ledger path>" \
  --entity "<entity>" --skill "<workflow>" --skill-version "<workflow version>" \
  --tier <0|1|2> --score <score> --verified N --unsupported N --contradicted N --synthesis N \
  --blocked <true|false> --claims claims.json
```

Record the workflow version so you can tell whether a revision actually improved accuracy. Scores without versions show the average but not the effect of changes.

The ledger is a JSON Lines file. Store it somewhere that persists between sessions and fetch the latest copy before appending.

## Step 7: Periodic sweep

Run monthly, or on demand.

```bash
python3 scripts/ledger.py sweep --ledger "<ledger path>"
```

The sweep shows three things and does not judge them automatically:

1. **Entity cross-check.** High-materiality claims for the same entity, side by side across documents. A person decides whether a difference is an error or a real change over time.
2. **Score trend per workflow.** Latest score, average, and direction (improving, declining, flat), with version history.
3. **Open patterns.** Repeated mistakes logged in Step 5b that nobody has closed.

Send the result to the owner of the deliverables.

## Wiring into workflows

Add these steps to each Tier 1 and Tier 2 workflow as required steps, not suggestions. A step that runs only when someone remembers to ask is not a gate.

```
## Step 0: Pattern lookup
Run ledger.py lookup-patterns for this workflow and take extra care on any open pattern.

## Step N: Trust scoring (required)
After drafting and before delivery, run deliverable-trust-scoring with the document path,
sources, workflow name, and entity. Tier 2 documents proceed to send or filing steps only
with a pass. Tier 1 documents always run it, and any warning is shown with the deliverable.
```

For Tier 2, also check the log at the send or filing step for a passing record. That second gate catches a workflow that skipped the first one.
