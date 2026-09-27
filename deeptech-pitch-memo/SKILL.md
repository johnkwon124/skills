---
name: deeptech-pitch-memo
description: An early-stage investment memo on a single company or a single technology bet, built through a research pass, a writer pass, and a question-and-answer loop between the two. Use it after screening and before a deeper pre-diligence report, when the question is whether the target deserves more time.
---

# Deeptech Pitch Memo

## Scope

One company or one technology bet per memo. If the request is a full sector landscape, this is the wrong tool. If the target already deserves a formal diligence write-up, use the pre-diligence report instead.

Position in the pipeline: sourcing, then screening, then this memo, then a deeper single-company report.

## Roles

Run the work as three roles. They can be separate subagents or separate passes in one session. Keep the researcher and writer contexts apart so the writer can challenge the research.

- **Coordinator**: talks to the user, holds the approval gates, relays results, checks the final output.
- **Researcher**: web search and source collection. Records every figure in structured tables with a source and a tag. Answers the writer's questions.
- **Writer**: drafts the memo in prose, asks the researcher five follow-up questions, and finishes the document.

## Workflow

Gate 1, Phase 1, Gate 2, Phase 2, Phase 3, Phase 4, Phase 5.

### Gate 1: target and brief (user approves)

If no target is named, propose three to five candidates that are investable, not already covered by earlier work, and tied to current industry themes. Once the target is fixed, write a one or two paragraph research brief: why this target, and three key questions the memo must answer. Do not start research before approval.

### Phase 1: initial research

Collect:
- Technology status and readiness level (TRL 1 to 9).
- The target company, plus a few direct competitors for positioning only.
- Funding rounds and investor profiles.
- Market size figures, each with a named source.
- Competitive position of the target, not a sector map.
- Technical constraints and open debates.

Quality rules:
- Every number carries a source (filing, press report, market study) and a date.
- Tag each item: `verified`, `estimate`, `company-stated`, or `unavailable`.
- Company claims and independently verified facts go in separate rows.
- Never fill a gap with a guess. Write `unavailable` and the reason.

Save the result as structured tables: sector overview (TAM, SAM, TRL, growth drivers), one profile table per company (founding year, HQ, latest round, total raised, investors, core technology, TRL, customers, claimed differentiation, verified differentiation), competitor table, and a debates table (skeptic view, counterargument, source).

### Gate 2: outline (user approves)

Before drafting, present a seven-chapter outline: one or two sentences of thesis per chapter, the key data points to be used, and three expected points of differentiation. Do not start Phase 2 until approved. This prevents rerunning the question loop after a direction change.

### Phase 2: writer questions

The writer reads the research and asks exactly five questions, each about a data gap that changes the investment view. Good questions target company-stated numbers that need independent confirmation, unclear market-size methods, missing competitive dynamics, or unverified timing claims. Do not ask what the tables already answer, vague "tell me more" questions, or questions about information that is private by nature. Format: question, then one line on why it matters.

### Phase 3: researcher answers

The researcher searches and answers each question with a source and tag. If nothing is public, answer "no public information" and say why. Flag any answer that conflicts with Phase 1. Merge Phase 1 tables, the questions, and the answers into one research file.

### Phase 4: drafting

Start from the merged research file, ideally in a fresh session to keep noise out. Write the memo following `references/chapter-structure.md`. Produce a Word document (or your preferred format) with a cover, headings, and page numbers.

### Phase 5: verification

Check document structure first. Then have a reviewer who did not take part in drafting re-check every claim against sources:
- Re-fetch the source for each number, person, and market figure.
- Look for missing `company-stated` or `unverified` tags.
- Look for drift, where a vendor claim becomes stronger in the memo than in the source.
- Remove or tag anything that cannot be confirmed. Allow at most two rework loops, then report what is unresolved.

Report to the user: a one-line QA summary (claims checked, confirmed, corrected, removed, tagged), file size, and two or three lines of insight per chapter.

## Writing standards

Never:
- Present a company-stated number as fact without verification.
- Use promotional adjectives such as "revolutionary" or "game-changing".
- Cite a market size without a source.
- Use another company's success as evidence without noting business model differences.

Always:
- Structure each claim as: company says X, independent evidence says Y, investor implication Z.
- Mark self-reported figures "(company-stated)" or "(unverified)".
- State the TRL.
- End with due diligence checkpoints.

Style: continuous prose, no bullets in body text, tables only where they help. Each chapter at least the length in the chapter guide. Plain numerals with units. Natural wording that does not read as machine-written.
