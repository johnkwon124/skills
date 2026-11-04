---
name: premeeting-notes
description: "Builds a pre-meeting company brief (v1.1). Works without any meeting record (transcript, recording, memo): given a company name or domain and an upcoming meeting, it opens and verifies public primary sources (PitchBook is used only for lead investors, total funding, latest round date and Series; Harmonic AI is not used), picks one canonical value per metric, and produces an English note DOCX, a Korean note DOCX (each with a matching PDF), and inline Key Questions (in Korean). Quick mode is the speed-optimized default; Full mode is for investment decisions. Use this skill whenever the user says: \"pre-meeting notes\", \"meeting prep\", \"brief me before I meet X\", \"pre-meeting brief\", \"here is a company name, research it before the meeting\", follow-up prep based on earlier meeting notes, or the Korean equivalents (\"프리미팅 노트\", \"미팅 전 준비\", \"미팅 prep\", \"X 만나기 전에 정리해줘\"). If the meeting already happened and a transcript, recording or memo exists, use meeting-notes instead; review of an existing note is meeting-notes MODE R. VC, LP and conference prep are out of scope.\n"
---

# Pre-Meeting Notes (v1.1)

## Overview

A note that gets you up to speed on a company before a meeting. Because it is written with no meeting record, the reader must immediately see "what is publicly confirmed about this company, what is unconfirmed, and what to ask in the meeting."

**Reader test**: someone who knows nothing about the company should be able to read only the note and understand what the technology is, how the company makes money, which problem it can solve and why, where it sits in the competitive landscape, and how much commercial progress is confirmed.

**This note delivers facts the author has decided.** A note that lays out conflicting figures and leaves the reader to choose is a failure. First define what each number measures, pick one canonical value per metric, and leave the selection process in the private Source Record (`references/source-resolution.md`).

**Deliverables**
1. English note DOCX
2. Korean note DOCX
3. Key Questions (Korean, inline chat preview only, no file)

Produce both DOCX files and, per the user's standing instruction, matching PDFs of the same content (from v1.1; v1.0 made PDFs only on request). Markdown files are delivered only when the user explicitly asks.

During the work, also maintain a private Source Record (a .md in the working directory). It is a work record, not a deliverable: do not count it among delivered files and do not copy its contents into the note or the chat. Deliver it only on request.

## 0. Routing (so the two skills never overlap)

| Situation | Skill |
|---|---|
| Turn a finished meeting's record into a note (at least one of transcript, recording, detailed memo) | meeting-notes |
| Check or review an existing note or briefing DOCX | meeting-notes MODE R |
| Prepare for an upcoming company meeting (name only, no meeting record) | **premeeting-notes** (this skill) |
| A past transcript or note exists and an upcoming follow-up meeting needs prep | **premeeting-notes** (past records are input material) |
| Prep for VC, LP or conference sessions | Out of scope for both skills. Proceed as general research or confirm with the user |

The dividing line is the note's subject. Recording a meeting that already happened is meeting-notes; preparing for an upcoming meeting is premeeting-notes. Even when a past transcript is attached, if the request is prep for the next meeting it is this skill; if the request is a record of that meeting, it is meeting-notes.

**Ambiguous case** ("make me a note for the X meeting", nothing attached): ask exactly one thing. "Has the meeting already happened, and do you have a transcript or notes?" If there is no answer, or the run is unattended, treat it as no record and proceed with this skill if the request is company prep. If the request is VC, LP or conference prep, do not produce a note; only report that it is out of scope. This skill never writes as if a meeting has taken place.

**One-line start confirmation**: when the company and routing are clear, post the line below and proceed immediately. Wait for a user reply only when company identification or routing is ambiguous.
`Proceeding with premeeting-notes - [company], meeting on [date or TBD], inputs: [domain, prior notes, deck, etc.]. Deliverables: English DOCX, Korean DOCX, Key Questions (Korean).`

## 0.5 Execution modes (v1.1)

**Quick mode** is the default. Run **Full mode** (section 2) when the user says "full mode", "for IC", "for an investment decision" or "precision", or says valuation, revenue, headcount or cap table is needed. If the user has not chosen a mode, proceed in Quick and state the mode in the start confirmation. Per-mode differences and detailed procedures are in `references/quick-mode.md`.

- **Harmonic AI is not used in either mode.**
- **Quick reads only 4 items from PitchBook**: lead investors, total funding, latest funding date, and that round's Series. The purpose is to check for a recent round that public sources missed and to reconcile total funding against the sum of public rounds. Round amounts and dates are anchored to public primary sources.
- **Quick writes only from the ledger**: record a URL and an under-15-word verbatim snippet for every claim as you research; every figure, date and proper noun in the note comes from a ledger row. Never write a fact that is not in the ledger.
- Regardless of mode, the common principles (section 1), English structure (section 3), Key Questions (section 4), format (section 5) and completion checklist (section 7) are identical. The only differences are in sections 2Q and 6.

## 1. Common principles

- **No guessing, sourced values only.** Give a source for figures from public sources. Write values from PitchBook as bare values, with no source name or classifying phrase such as "deal database". Reason: the user has a standing instruction to use PitchBook data without attributing it in the note, and that instruction is limited to PitchBook. Public sources follow the note's existing attribution format, and every source's name and retrieval date go into the private Source Record.
- **Decisive writing.** Never show two or more candidate values for one metric. Never compare different metrics in one sentence (e.g. an amount and a valuation). Procedure: `references/source-resolution.md`.
- **Unresolved items go into the note only when they change a judgment or a meeting question.** When included, say in one sentence what is unknown and why it matters, and move the same item into Key Questions. Everything else stays in the Source Record.
- **Delete obvious observations.** Do not write a sentence that a reader with the numbers can see immediately and that changes no judgment or question.
- **Undisclosed is not zero.** Distinguish "nothing is public (search complete)" from "not found (list of sources searched)". Never assert there are no grants, debt, customers or revenue.
- **Single-Statement Rule.** State each fact, claim or insight exactly once in the body. At a Glance is the only exception, and it must be an independently compressed sentence, not a copy of a body sentence.
- **Mixed prose and bullets.** Each section opens with a 1-2 sentence prose lead; enumerable facts go in bullets, causation and judgment in prose. Company Snapshot is the only all-bullet section allowed.
- **Insights are woven into the body.** Move from fact to judgment with no separate label, italics or color. Do not mechanically attach hedging phrases to every section.
- **Never narrate the writing process.** No sentences like "originally X, but recheck shows Y" or "excluded in this revision". State confirmed facts directly. Never grade yourself ("the most accurate", etc.).
- **No investment opinion and no Next Steps.** This note is prep material, not a recommendation.
- **Author anonymization.** No author real names and no first person ("I", "we", "my", "our", "나", "저희", "우리"). If attribution is unavoidable, use your organization's short name or a neutral expression.
- **No internal signals.** Skill mode names, internal agent or tool names, and labels like [UNVERIFIED], [f/u], [footnote], [VC insight] go into no deliverable.
- **Keep your own firm's name and firm-internal content out of deliverables.**
- **Never write as if the meeting has happened.** No "the founder said" or "during the meeting". Attribution forms: "company materials", "press release (date)", outlet names, "earlier meeting notes (date)". State facts from earlier meeting notes directly with a date, and send open items from prior conversations to Key Questions.
- **Language.** English: short, plain sentences; explain jargon in one phrase at first use; ban signpost words like "notably", "importantly", "significantly", "furthermore", "moreover", "cutting-edge"; vary sentence openings and lengths. Writing standards (including the AI-detection target) follow the existing meeting-notes standards unchanged. Korean: natural prose with sentence endings unified to ~임/함/됨/있음/없음/필요함; avoid literal translation; write "투자 thesis" and do not use Korean transliteration for it. Never use an em dash (U+2014).
- **Dates are absolute.** Month and year instead of "recently" or "this year". Attach an as-of date to current-state claims.
- **Reporting honesty.** Do not report completion just because a tool returned "saved" or "opened". Re-extract a file's text to verify it, and write "opened" only after reading on-screen text. Report what you could not verify as "could not verify".
- **Length.** English target 700-1,100 words (2-3 Letter pages), lint cap 1,200 words (R19, `--max-words 1200`). Quick mode per-section budgets are in `references/quick-mode.md` section 6. Korean runs 60-70% of the original; Key Questions 5-8 items.

## 2Q. Quick mode workflow (default, fixed order)

```
0. One-line start confirmation (mode included). No content pre-approval wait
1. Batch 1 (parallel in one turn): official site, press-release search, patent search, PitchBook 4 items -> Identity Lock
2. Batch 2 (4 parallel tracks): A funding/team, B technology, C competition, D traction -> return ledger rows only
3. Merge and resolve canonical values (public primary sources win, source-resolution.md section 6)
4. English draft (from the ledger only, section word budgets) + inline preview
5. Machine checks: lint --max-words 1200, check_ledger.py (do not advance before these pass)
6. Risk-based verification: one fresh-context verifier pass (H rows plus legal, contract and trial-status sentences, ~30 call cap) -> reopen flagged URLs -> fix (max 2 rounds)
7. Korean draft + check_drift.py + lint, Key Questions + lint
8. Build DOCX and PDF, VERIFY OK, checklist -> deliver
```

Research caps: ~25 WebFetch calls, ~10 WebSearch calls, 2 attempts per item. Skip secondary aggregators and sources already confirmed blocked. Per-track instructions, ledger format and the verifier brief are in `references/quick-mode.md`. The stop-after-2-attempts rule for blocked sources (2.2) and the rule against filling values from inaccessible sources apply to Quick unchanged.

## 2. Workflow (Full mode, fixed order)

```
1. Entity Identity Lock + domain confirmation  -> create Source Record
2. Access Check (verify real access per source)
3. Capture + Resolve (references/source-resolution.md S3-S7)
4. Deep research (technology mechanism, independent evidence for the problem, competitive axes)
5. Content pre-approval outline -> user approval
6. English markdown draft + inline preview + lint
7. First-pass review: independent verifier call
8. Korean markdown + EN->KR drift check + Key Questions
9. DOCX build + rendering integrity check
10. Second-pass review: completion checklist -> deliver
```

### 2.1 Entity Identity Lock
Do not trust the name the user gave as-is. Confirm the legal name and spelling on the official domain, and cross-check that each database profile's website, legal name, founding year, HQ and founders are the same company. Exclude same-name entities by industry and domain and record the basis in the Source Record. Names in older internal documents are context, never naming evidence. All deliverables use only the confirmed name.

### 2.2 Access Check
Follow `references/source-resolution.md` section 3. Summary: verify existence with the available tool list before claiming a source exists; use only browser sessions the user is already logged into or source text the user pasted; when blocked, stop after 2 attempts and ask the user for the access you need; never fill values from sources you could not access. Failure reports state what was tried and what access is needed.

### 2.3 Capture + Resolve
Open originals, not summary boxes. Funding by round (date, instrument, amount, currency, status, lead, participants); separate equity, grants and debt, with totals per class; valuation with pre/post, as-of date, basis and the round it belongs to; investors split deal-level vs company-level; team backgrounds and headcount (with date); data the company has actually published (specs, papers, patents, benchmarks, customer facts) collected separately from claims. Label checks, cross-checking important numbers against two or more independent sources, and per-metric canonical selection are in the reference's sections 5-6. Results go into a Source Record in the `references/source-record-template.md` format.

### 2.4 Deep research
Pick 8-12 sources from `references/sector-source-map.md` for the sector. Skip low-signal sources. Research the technology section until you can explain the causal chain of "what is implemented how, and why the performance claim holds". When sources explain a mechanism differently, that changes judgment, so record it once. For the problem section, collect independently verifiable evidence (market data, regulation, competitor funding) separately from company claims. When the same entity is spelled differently across sources, run a cross-source consistency check: if it is a typo or rebrand, unify on the most reliable source; if you cannot be sure it is the same entity and the difference affects judgment, state it once in the note and send it to Key Questions. For comparable companies, run a separate search for valuations or financings announced within 6 months of the meeting date.

### 2.5 Content pre-approval (Full mode)
Before writing, show the user the outline below and wait for approval. If the user instructed to skip it or the run is unattended, skip it and record that in the Source Record.
```
Section plan for approval:
 1. At a Glance - [open question in 1 line]
 2. Company Snapshot - [stage, team, canonical-choice summary per key figure]
 3. The Problem - [pain in 1 line, count of independent evidence]
 4. Technology - [component count, mechanism explainable?, Claimed vs Verified item count, any company-published data]
 5. Business Model & GTM - [disclosed or not]
 6. Commercial Traction - [any public traction]
 7. Competitive Landscape - [axis count, competitor count]
 8. Key Considerations - [strength count, risk count, unresolved items elevated to the note]
 Access status: [per source opened / not accessible]
```

## 3. English note structure (8 sections, fixed headings)

Title: `[Company Name] Pre-Meeting Notes`. No divider under the title. Dates are absolute.

1. **At a Glance** (4 bullets, 1 sentence each, no copying body sentences)
   - **What**: what the company does, for someone who knows nothing about it
   - **Why now**: why this problem matters now
   - **Stage**: stage, team size, latest round compressed
   - **Open question**: the single most important question to resolve in this meeting
2. **Company Snapshot** (Type A bullets only)
   - **Founded / HQ**, **Team** (headcount with date, founder names and key backgrounds), **Product status**
   - **Funding**: one line per round (date, type, amount and currency, lead, participants). Grants on a separate line. Totals split between equity and non-dilutive
   - **Valuation**: "post-money $X at [round, date]". Never in the same sentence as an amount line. If the basis is weak, mark it only as "a value the company has not confirmed"
   - **History**: pivots, name changes (when applicable)
3. **The Problem** (1-2 sentence prose lead + 2-4 evidence bullets): distinguish facts verified independently of company claims. A claim with no independent evidence is marked "company claim, no independent evidence found".
4. **Technology: What It Is & How It Works** (the section to invest the most in)
   - 4a lead prose, 2-3 sentences: what the product physically is, and where and how it is used
   - 4b **System Components** (Type A bullets): components and their roles
   - 4c operating mechanism (2-4 sentences of prose): the causal chain for why the performance claim holds. If a claim cannot be explained, say so. If sources explain the mechanism differently, state it once and note what it means for judgment
   - 4d **Claimed vs Verified** (Type A bullets): performance, durability and cost claims with verification status. The only place verification needs are mentioned. The **Published data** line lists specs, papers, patents, project records and benchmarks the company has actually published
   - 4e **Manufacturing & Deployment** (hardware companies only): manufacturing method, partners, deployment lead time
5. **Business Model & Go-to-Market** (prose lead + bullets): pricing model, sales channel, partner structure. If undisclosed, write "Not disclosed" for exactly what is undisclosed; do not fill the gap with rephrasing. These items feed Key Questions.
6. **Commercial Traction** (prose lead + bullets): only confirmed customers, pilots, LOIs, partnerships and revenue signals. If none: "No customers, pilots or LOIs have been disclosed as of [date]". A database classification tag is not traction evidence.
7. **Competitive Landscape** (prose lead + bullets per axis): define how many approaches exist, and for each competitor state on which axis it competes, with what, and at what scale. Close with 1-2 prose sentences on the target company's position and the funding gap (only in this section).
8. **Key Considerations Going Into the Meeting** (4-6 sentences of prose, no bullets): synthesize 2-3 strengths and 2-3 risks with their basis, and explain why the unresolved items elevated to the note matter for judgment. Only briefly reference facts already stated in the body. No investment opinion, no Next Steps.

Not in this note: meeting timeline, Follow-up Items, post-meeting agreements, red highlighting, a closing paragraph, transcript-error-pattern checks. Post-meeting work belongs to meeting-notes.

## 4. Key Questions (Korean, inline preview)

Categories: technology validation / business validation / team & execution / market & competition / funding & exit. 5-8 questions. Each must be specific (no "what do you think?" types), and must include items the note handled as "Not disclosed" and unresolved items elevated to the note. Never make a question about an item resolved as a definitional difference. Open items from earlier meetings land here.

## 5. Format (fixed, no ad-hoc changes)

| Item | Value |
|---|---|
| English font | Calibri 11pt, title Bold 13pt, section headers Bold 11pt, all black |
| Bullets | Round bullets (•), 0.25 inch indent, 2pt between bullets |
| Bullet Type A | `• **Bold Label**: content` |
| Page | Letter, margins 1 inch (EN), 1.1 inch (KR) |
| Korean font | NanumGothic 11pt, title 13pt Bold |
| Divider | None (EN); KR DOCX has a 0.5pt line under the title |
| Company name | Bold once at first mention |
| Filenames | `[Company]_Premeeting_Notes_[MMDDYYYY].docx`, `KR_[Company]_Premeeting_Notes_[MMDDYYYY].docx` |
| Save location | The same folder used for meeting-notes output. If no connected computer tool exists in the session, create the files in-session and deliver them as files; do not claim they were saved to a folder |

Korean note section names: 1. 한눈에 보기 / 2. 회사 개요 / 3. 문제 정의 / 4. 기술 및 작동 원리 / 5. 비즈니스 모델 / 6. 상업적 트랙션 / 7. 경쟁 구도 / 8. 미팅 전 핵심 고려사항 (following the meeting-notes MODE A Korean structure).

Build: complete the markdown first, show it as an inline preview, then convert. Run the commands below from the skill folder (python-docx and LibreOffice required, system install assumed).
```
python3 -I scripts/build_docx.py --lang en --title "[Company] Pre-Meeting Notes" --date MMDDYYYY --md note_en.md --out OUT.docx --pdf
python3 -I scripts/build_docx.py --lang kr --title "[Company] - 프리미팅 노트" --date MMDDYYYY --md note_kr.md --out KR_OUT.docx --pdf
```
Markdown convention: `##` section headers, `###` subheaders, `- ` bullets (`- **Label**: text` allowed), everything else prose. After conversion, re-extract text from the DOCX and compare it against the markdown (`scripts/build_docx.py --verify`).

## 6. Verification

- **lint (English markdown, Korean markdown, Key Questions markdown, each)**: from the skill folder, `python3 -I scripts/lint_note.py --mode pre note.md` (add `--max-words 1200` for English). Key Questions are chat output, but database source names, first person and firm references leak easily through that channel, so save them to a temp file and lint it. Proceed only at 0 FAILs. WARN is a human decision; never auto-fix.
- **Quick mode machine checks (v1.1)**: right after the English draft, `python3 -I scripts/check_ledger.py --note note_en.md --ledger SourceRecord_X.md` must show 0 numbers missing from the ledger. Right after the Korean draft, `python3 -I scripts/check_drift.py --en note_en.md --kr note_kr.md` must show 0 FAILs (the script also serves Full mode's EN->KR comparison).
- **First-pass review (independent verifier call)** (Quick mode: the risk-based scope of `references/quick-mode.md` section 8 with a ~30 call cap; Full mode: all claims): the context that wrote the note never verifies it. Call an independent verification skill or agent and pass the calling skill's name (premeeting-notes) and the company name. Give the verifier the English note markdown, the Source Record, the source URL list, the as-of date and `references/known-error-patterns.md`. If the verifier's tier table has no premeeting-notes entry, treat it as Tier 1, same as meeting-notes, and report that fact. The verifier's CONTRADICTED and UNSUPPORTED are recheck targets, not final verdicts: reopen the URL in question and confirm.
- **EN->KR drift check**: right after the Korean markdown, mechanically compare figures, dates and proper nouns against the finalized English version.
- **DOCX integrity**: `build_docx.py` re-extracts text from the DOCX right after saving and compares it with the markdown. Report completion only after seeing VERIFY OK in the output. Add `--pdf` to also build the PDF and confirm PDF VERIFY OK.
- **Failure loop**: at most 2 rework rounds when a review fails. If it still fails, stop and report which item failed, why, and what was tried, then wait for instructions. Tag a cause category: `identity-mismatch` / `cross-source-conflict` / `unverifiable-claim` / `stale-info` / `format-drift` / `metric-mismatch` / `other`. For recurring types, propose adding them to `known-error-patterns.md` but do not add them before user confirmation.

## 7. Completion checklist

```
Source
[ ] Domain and legal name confirmed, DB profiles cross-checked as the same company, same-name exclusions recorded
[ ] Per-source Access Log written. "opened" only when on-screen text was actually read. Inaccessible sources and their impact recorded
[ ] No values from inaccessible sources in the note (0 values filled from memory or guesses)
[ ] Funding organized by round (date, instrument, amount, currency, lead, participants). Equity, grants, debt separated, totals per class
[ ] Valuation tied to a round and an as-of date
[ ] Investors split deal-level vs company-level
[ ] Key figures cross-checked with 2+ independent sources, or single-source status recorded
Writing
[ ] One value per metric. 0 candidate-value lists. 0 cross-metric comparisons
[ ] Only unresolved items that affect judgment or meeting questions are in the note, each feeding a Key Question
[ ] 0 obvious observations
[ ] 0 places writing the undisclosed as zero or absent
[ ] 0 PitchBook source names or "deal database"-type phrases (lint R03). Public sources use the existing attribution format. 0 Harmonic AI values
[ ] 8 sections present, prose lead per section, Single-Statement Rule kept, At a Glance not a body copy
[ ] Technology has mechanism causality, Claimed vs Verified, Published data. 0 technology repetition, tautology, or unfounded adjectives
[ ] 0 expressions written as if the meeting happened (lint R13)
[ ] 0 writing-process narration or self-grading (lint R06, R17)
[ ] No investment opinion, no Next Steps. No firm-related content. No internal signals. No real names, no first person
Output
[ ] lint 0 FAILs (English with --max-words 1200, Korean, Key Questions)
[ ] Quick: check_ledger unsourced 0, check_drift 0 FAIL, every ledger row has URL and snippet, verifier within ~30 calls
[ ] Independent first-pass review complete, verifier verdicts rechecked
[ ] Korean note's figures, dates and proper nouns match the finalized English version
[ ] 2 DOCX and 2 matching PDFs delivered (markdown files only on explicit request). Text re-extracted from DOCX and PDF and compared with markdown
[ ] Key Questions: 5-8, Korean, specific, including Not disclosed items and unresolved items
[ ] Source Record sits in the working directory and its content is exposed in neither the note nor the chat
[ ] Save location reported as it actually is (if not saved to a computer folder, say so)
```

## 8. Reference files

- `references/quick-mode.md`: Quick mode details (PitchBook 4 items, ledger format, 4 parallel tracks, word budgets, risk-based verification)
- `references/source-resolution.md`: PitchBook, public-primary-source verification and canonical-value selection procedure (core. Harmonic AI phrasing is not used from v1.1)
- `references/source-record-template.md`: private Source Record template
- `references/examples-good-bad.md`: good and bad examples
- `references/sector-source-map.md`: per-sector source mapping (for choosing 8-12)
- `references/known-error-patterns.md`: running log of recurring errors (skim before review)
- `references/CHANGELOG.md`: version history
- `scripts/build_docx.py`, `scripts/lint_note.py`: DOCX/PDF conversion and text lint (length cap R19)
- `scripts/check_ledger.py`, `scripts/check_drift.py`: note figures vs ledger, EN-KR figure drift
- `tests/`: lint fixtures and script regression tests
