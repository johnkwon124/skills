# Quick Mode Spec (v1.1)

The default execution mode of premeeting-notes. The goal is to cut time while keeping reliability. Time comes from (1) creating fewer conflicting values in the first place, (2) recording evidence in a ledger at research time, (3) concentrating verification on items where an error would change a judgment, and (4) handing every check a machine can do to a script. Review is never skipped.

## 1. Choosing a mode

| | Quick (default) | Full |
|---|---|---|
| When | Ordinary meeting prep | The user said "full mode", "for IC", "for an investment decision" or "precision", or said valuation, revenue, headcount or cap table is needed |
| Rounds, amounts, dates | Anchored to public primary sources (press releases, regulatory filings, government records) | The original v1.0 procedure (source-resolution.md) |
| PitchBook | 4 items only (section 2 below) | Round details, valuation, headcount, cap table |
| Harmonic AI | Not used | Not used |
| Valuation, headcount, revenue | Only when confirmed by the company or credible press. Otherwise "Not disclosed" | PitchBook values may be used, marked "a value the company has not confirmed" |
| Content pre-approval | None (one-line start confirmation) | Yes (skipped on unattended runs) |
| Verification | Risk-based, ~30 call cap | All claims |

If the user has not chosen a mode, proceed in Quick and state the mode in the first line.

## 2. The 4 PitchBook items (Quick)

What is read: (1) lead investors (deal-level lead and participants where possible), (2) total funding, (3) latest funding date, (4) that round's Series (type).

Purpose
- To check for a **more recent round** that public-source searching missed. If PitchBook's latest round date is later than the public record, run one search aimed at that round; if it cannot be confirmed, record it in the Source Record only.
- Total funding is reconciled against the sum of public rounds. The sum is canonical. If the PitchBook value differs, leave the difference in the Source Record. Only when the total cannot be reconstructed from public rounds, write the PitchBook value as "at least $X".
- Access rules follow source-resolution.md section 3 as-is (pasted text or a logged-in session only; stop after 2 attempts when blocked). If there is no access, note it in the Access Log and proceed with public sources.
- The note never carries the PitchBook source name or a classifying phrase (lint R03).

Not read: valuation, revenue, headcount, cap table, business-status tags, similar-company lists.

## 3. Claims ledger format

Record one row per claim the moment you research it. The note is written only from this ledger. The ledger is the "Claims ledger" section inside the Source Record, and check_ledger.py reads this table.

```
## 3. Claims ledger
| ID | Claim | Value | As-of | Source URL | Snippet (15 words max) | Mat (H/N) | Class |
|---|---|---|---|---|---|---|---|
| C01 | Series B amount | $60M | 2024-07-31 | https://... | "raised $60 million" | H | public |
```

- **Snippet**: under 15 words of verbatim text read from the page. Not a summary, the original. This column eliminates the verifier's re-search cost.
- **Class**: public / company / competitor / sponsored / db / user-provided.
- **Mat**: H means an error here would change an investment judgment or a meeting question.
  - H: amounts, dates, round types and leads, participants, valuation, contract terms, patent and litigation facts, trial and certification status, government grants, customers and orders, competitor funding, performance figures
  - N: background, titles, secondary figures, general engineering explanation
- When sources disagree on one metric, keep only the canonical row in the ledger and put alternate values in the "4. Canonical values" section (source, reason for the difference).
- Items with no value found get no row; they go to "9. Unresolved".

Quick Record layout: 1 Identity (3 lines) / 2 Access Log / 3 Claims ledger / 4 Canonical values (only metrics that had conflicts) / 5 Unresolved / 6 Verification log. The investor, team and published-data inventory tables are absorbed into ledger rows.

## 4. Four parallel research tracks

If your environment has an agent tool, launch one subagent per track in a single turn. Otherwise call WebFetch and WebSearch in parallel within one turn. Each track returns ledger rows only (no narrative summaries).

| Track | Scope | Priority sources |
|---|---|---|
| A funding & team | Per-round dates, amounts, leads, participants, government grants, founder and CEO backgrounds, headcount (company-announced only) | Press releases, regulatory filings, government records, media |
| B technology | Components, mechanism, company claims, trial and certification status, patents, company-published data, cross-source explanation differences | Official site, company materials, patent DBs, certification bodies |
| C competition | Approach-axis definition, scale and latest funding of 3-4 competitors | Competitor official materials, press releases |
| D traction | Customers, pilots, LOIs, partners, deployments, revenue signals, business-model disclosure | Company announcements, exchange filings, media |

Shared instructions (include in every track prompt):
1. Return ledger-row format only. Values exactly as read from the page, snippets verbatim under 15 words.
2. Never invent values for pages you could not open. When blocked, try at most 2 times and record "not accessible". No workarounds.
3. Mark company claims, competitor claims and sponsored articles as such in Class.
4. Attach an as-of date to time-sensitive values.

Research caps (total): ~25 WebFetch calls, ~10 WebSearch calls, 2 attempts per item. If a cap is hit while an H item is still empty, research only that item further and record the reason in the Source Record.

## 5. Sources to skip

- Do not use secondary aggregators (CB Insights, Tracxn, LeadIQ, Preqin, etc.). Only when a public round cannot be confirmed through press releases, check one as a last resort and mark the value as "unverified aggregator value".
- Sources with confirmed robots blocking in this environment (SEC EDGAR search UI, CourtListener) are not called; record "not accessible (known)" in the Access Log. Environments change, so if the user names such a source, try it once.
- Skip revisiting pages already read and reposts of the same press release.

## 6. Section word budgets (English)

Target total 1,100 words, lint cap 1,200 words (`--max-words 1200`).

| Section | Budget |
|---|---|
| At a Glance | 90 |
| Company Snapshot | 220 |
| The Problem | 90 |
| Technology | 330 |
| Business Model & Go-to-Market | 90 |
| Commercial Traction | 110 |
| Competitive Landscape | 120 |
| Key Considerations | 120 |

Cut over-budget sentences first by the Single-Statement Rule and the obvious-observation test (source-resolution.md section 8). If information must go, drop N rows with the least judgment impact first.

## 7. Machine checks

| Check | Command (from the skill folder) | Pass bar |
|---|---|---|
| Rules and length | `python3 -I scripts/lint_note.py --mode pre note_en.md --max-words 1200` | 0 FAIL |
| Note figures vs ledger | `python3 -I scripts/check_ledger.py --note note_en.md --ledger SourceRecord_X.md` | unsourced=0 |
| EN-KR figure drift | `python3 -I scripts/check_drift.py --en note_en.md --kr note_kr.md` | 0 FAIL, WARN is a human call |

check_ledger.py catches numbers with no source. Whether a number is attached to the right claim is the verifier's job.

## 8. Risk-based verification

1. What the (fresh-context) verifier gets: the English note, the ledger's H rows (URLs and snippets included), the as-of date, known-error-patterns.md. The verifier reopens the URLs directly. It does not search for new sources beyond the ledger.
2. Additional sentences the verifier checks: litigation, contract terms, trial and certification status, items the note handled as "Not disclosed" (whether anything is actually public), and places in the technology mechanism paragraph where company statements and general engineering explanation are mixed.
3. ~30 call cap. If all H rows are checked before the cap, stop. Check only about 5 N rows as a sample.
4. Return CONTRADICTED and UNSUPPORTED items only (note sentence, what the source says, URL opened). No VERIFIED list.
5. The author reopens each flagged URL, confirms, and fixes. At most 2 rework rounds. If the verifier's tier table has no premeeting-notes entry, treat it as Tier 1.
6. Full mode verifies all claims, as in v1.0.

## 9. What Quick mode gives up

- Valuation, headcount and revenue stay "Not disclosed" unless confirmed in public sources. Rerun in Full mode when they are needed.
- With parallel research, cross-source naming inconsistencies first surface at the merge step.
- N rows are sample-verified, so low-materiality errors can survive. The ledger-only writing rule and check_ledger.py reduce this risk.
