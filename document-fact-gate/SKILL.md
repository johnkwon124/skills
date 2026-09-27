---
name: document-fact-gate
description: Puts a document (docx, md, or txt) through a four-stage fact-check pipeline, covering mechanical lint, fresh-context claim verification, fail-closed merge, and a writing-standard gate. Use it before sharing any report, memo, or brief with factual claims, or when another workflow needs a shared QA step.
---

# document-fact-gate

## Why it exists

Self-review by the same model in the same context lets hallucinations survive. This pipeline counters that in three ways.

1. **Use code for anything checkable by code.** Deterministic checks cannot hallucinate and cost almost no tokens.
2. **Verify in a fresh context.** The verifier sees only the document and its original sources, never the drafting history. Seeing the history anchors the verifier and removes its independence.
3. **Fail closed.** A claim the verifier cannot confirm is removed or flagged by default. Unverified content never survives silently.

The verifier does not judge whether a claim is plausible. It finds the claim in a source, or reports that it could not.

## Step 0: Inputs

Required:
- Path to the document (.docx, .md, .txt).
- Original sources: transcripts, notes, URL list, or a claims ledger if one exists (prefer the ledger).

Optional:
- Reference date for date checks (for example the meeting date).
- Voice: `first-person` (default for emails, posts, notes) or `anonymized-third-person` (documents shared externally with the author removed).

If there are no sources, run only Step 1 and Step 3.5, and state in the QA report that claim-level verification was skipped for lack of sources.

## Step 1: Mechanical lint

```bash
pip install python-docx        # only for .docx input, once
python3 scripts/lint.py "<document>" --json [--require-section "Summary" ...]
```

Checks, all regex based:
- **REL_DATE (FAIL):** relative dates such as "this year", "next summer", "by year-end", "in the coming months". Replace with absolute dates.
- **EM_DASH (FAIL):** the long dash character. Use a period or comma.
- **PROCESS_NARRATION (WARN):** phrases such as "originally I wrote", "on re-check", "revision history", "after several passes". The lint only finds candidates. Step 3.5 makes the final call.
- **UNSOURCED_FIGURE (WARN):** a line with a currency amount, percentage, large number, or unit quantity and no source marker. These become the verifier's must-resolve list.
- **MISSING_SECTION (FAIL):** for each `--require-section` heading not found.
- Tag counts for "(unverified)" and "(stated by company)".

Any FAIL blocks Step 2. Fix, then lint again.

## Step 2: Fresh-context verification

Start a sub-agent with a mid-tier model. Claim verification is easier than generation, so a smaller model is enough. Use a stronger model only when a wrong paraphrase would be costly.

Pass: the full document text, source file paths, the URL list, the reference date, and the Step 1 WARN list.
Never pass: the drafting conversation, reasoning, outlines, or intermediate drafts. No exceptions.

Prompt template:

```
You are a document verifier. You did not write this document and do not know how it was written.

[Document] ...
[Sources] <file paths> / <URLs>
[Reference date] YYYY-MM-DD
[Lint warnings] ...

Tasks:
1. Extract every atomic factual claim: numbers, dates, names, titles,
   affiliations, announcements, contracts, partnerships, technical specs.
2. Classify each claim. Do not judge plausibility. Find it in a source.
   - VERIFIED: found in a source. Quote the passage or show the re-fetched page content.
   - UNSUPPORTED: not found in any source.
   - CONTRADICTED: conflicts with a source. Quote the source and state the mismatch.
   - SYNTHESIS: interpretation, comparison, or implication that no single source can verify.
3. For each person, re-check current role. Treat person data older than two years as UNSUPPORTED.
4. For each cited URL, fetch it again and confirm the content matches.
5. Catch strength drift: "in discussions" becoming "signed" is CONTRADICTED.
   Quote the original wording.

Output a table of claims with classification and evidence.
```

## Step 3: Fail-closed merge

Apply these rules without exceptions.

| Class | Action |
| --- | --- |
| CONTRADICTED | Must fix to match the source. If it cannot be fixed, delete the claim. |
| UNSUPPORTED | Delete, or tag "(unverified)". Default is delete. Keep with a tag only if the user told you in advance to keep it. |
| SYNTHESIS | Move out of the facts section into an analysis block, or reword so it is clearly analysis. Never mix fact and analysis in one sentence. |
| VERIFIED | Keep. |

Re-run Step 1 after edits, since edits can introduce new violations.

## Step 3.5: Writing-standard gate

Independent of accuracy, check these rules. Use the Step 1 results as input, then judge in context. Fix violations, then re-run from Step 1.

1. **Voice.** For `first-person`, write as the person who did the research. No surface traces of the tool that did the work ("I analyzed with AI", "the model found"). For `anonymized-third-person`, remove author identity and first person entirely.
2. **No process narration.** Do not describe how the research was done, how many revisions occurred, or why something was dropped. State corrected facts as plain facts. If process information matters, put it in the QA report, not the document.
3. **Style rules.** Zero long dashes. No invented or estimated figures. Every number has a source or is removed.
4. **Machine-sounding prose.** Reduce over-smooth openings, stock transitions, repeated parallel structures, and any sentence that grades the document's own accuracy. Use an AI-detector target only if the caller sets one.

Pass means zero violations. Record fixes only in the QA report.

## Step 4: QA report

Attach one summary to the delivery:

```
QA: N claims checked. VERIFIED X, corrected Y, deleted Z, kept as (unverified) W, SYNTHESIS moved V.
Lint: REL_DATE fixed N, EM_DASH fixed N.
Writing standard: passed / passed after N fixes (voice: first-person | anonymized-third-person).
Residual risk: [number of SYNTHESIS sentences, or none]
```

Provide the full claim table only on request.

## Calling this from another workflow

Add one step to any document-producing workflow:

```
## Step N: fact-gate
After drafting, run document-fact-gate with: document path, sources, reference date, voice.
Deliver only the file that passed the merge, the writing-standard gate, and the QA report.
```

Do not maintain a separate fact-checking checklist in the caller. Keep only format and length checks there. Route fact checks and writing rules here so there is one place to maintain.
