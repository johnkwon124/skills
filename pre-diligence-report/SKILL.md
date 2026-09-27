---
name: pre-diligence-report
description: Written just before formal diligence, this report covers a single company in depth, with footnoted sources, a SWOT, funding and deal dynamics, structural debates framed as competing hypotheses, and a diligence checklist. Use it once a company has cleared early screening and you need to decide what to verify before committing diligence resources.
---

# Pre-Diligence Report

## Purpose

An early pitch memo answers "is this worth a look". This report answers "should we start formal diligence, and what must we verify independently first". It covers one company only and ends with a conditional recommendation.

| | Early pitch memo | Pre-diligence report |
|---|---|---|
| Stage | Sourcing and first review | Just before formal diligence |
| Scope | One target, a few comparables | One company in depth |
| Structure | Seven chapters | Eleven chapters plus primer, executive summary, conclusion |
| Sourcing | Inline tags | Inline tags plus numbered footnotes |
| Unique parts | None | SWOT, funding and deal dynamics, structural debates, diligence checklist, catalyst calendar |
| Output | Document | Document plus a PDF copy |

## Input modes

- **Mode A, company name only**: research from zero.
- **Mode B, deepen existing material**: an earlier memo, meeting notes, or other files exist. Treat them as the source of truth and research only the gaps.

If the mode is unclear, ask once.

## Roles

Coordinator (talks to the user, holds gates, runs verification), researcher (sources and tables, answers questions), writer (drafts with footnotes, asks clarifying questions, produces the document and PDF). Keep researcher and writer contexts separate.

## Workflow

Gate 1, Phase 1, Gate 2, Phase 2, Phase 3, Phase 4, Phase 5, Phase 6.

**Gate 1 (user approves).** In one or two paragraphs state the target, the input mode, three key investment questions (for example: can the performance figures be independently verified, how visible is revenue, how large is the capital gap to competitors), and two or three candidate structural debates. No research before approval.

**Phase 1: research.** Follow `references/research-prompts.md`. Every figure gets a source, date, and URL. Tags: `company-stated`, `estimate` (hypothesis from public information), `analysis` (your own interpretation), `unavailable, reason`. Never fill a gap with an estimate presented as fact.

**Gate 2 (user approves).** Before drafting, present the eleven-chapter outline: thesis per chapter, the topic of the variable chapter 3, three or four structural debates for chapter 10, and candidate items for the diligence checklist. Approval first avoids rerunning the question loop.

**Phase 2: writer questions.** Five to seven questions, only about gaps that change the investment view: independent verification of performance figures, nature of contracts, revenue split, regulatory exposure, competitor capital, valuation comparables. No questions the research already answers.

**Phase 3: researcher answers.** Web-verified answers with URLs, or "no public information, reason". Merge Phase 1, questions, and answers into one research file.

**Phase 4: drafting.** Read `references/chapter-structure.md` and `references/document-generation.md`, then write the report and convert it to PDF. Always deliver the document and PDF as a matched pair.

**Phase 5: verification (required).**
1. Check document structure.
2. Have a reviewer with no drafting history re-check claims against sources: re-fetch the origin of each figure, person, contract, and market size; check for missing `company-stated` or `unverified` tags; check for drift where a vendor claim gets stronger in the report than in the source.
3. Fail closed: remove or tag anything unconfirmed. At most two rework loops, then report what remains unresolved.
4. If the document changed, regenerate the PDF so both files match.

**Phase 6: report to the user.** One-line QA summary (claims checked, confirmed, corrected, removed, tagged), file paths and sizes, two or three lines per chapter, and a summary of the checks to complete before formal diligence.

## Analysis standards

Never:
- Present company-stated figures as fact without verification.
- Use promotional adjectives.
- Give a market size without a source.
- Combine products that differ by orders of magnitude (for example a pilot-scale line and a commercial-scale line) to make the company look stronger.

Always:
- Use three steps for each claim: company says, third parties confirm or not, our interpretation.
- Footnote every key figure, contract, and quotation.
- Separate `estimate` from `analysis`.
- State the TRL.
- Close chapter 11 with a checklist of items to confirm before formal diligence.

Style: continuous prose, tables only for comparison and summary, no bullets in body text. Open with a plain-language primer so a non-specialist can follow. Wording should read as written by a person.
