# premeeting-notes: Update History

## v1.1 (2026-11-03)
Speed-improvement release. Basis: a real pre-meeting note run had gotten slow; the goal was to cut the causes (resolving DB value conflicts, 118 verification calls, over-length rework, oversized Source Records) while keeping verification reliability. User-approved 2026-11-03.

Changed
- Added Quick mode as the default. Full mode (the v1.0 procedure) runs when the user says full mode, for IC, for an investment decision, or precision, or when valuation, revenue, headcount or cap table is needed. Details in `references/quick-mode.md`
- Harmonic AI discontinued (both modes)
- Quick mode reads only 4 PitchBook items: lead investors, total funding, latest funding date, Series. Round amounts and dates are anchored to public primary sources
- Claims ledger written during research: every claim gets a URL, an under-15-word verbatim snippet, a materiality grade (H/N) and a class. The note is written only from the ledger
- 4-track parallel research (funding & team / technology / competition / traction), research caps ~25 WebFetch and ~10 WebSearch calls
- Secondary aggregators and sources with confirmed blocking are not called
- Per-section word budgets for English, lint cap 1,200 words (new rule R19)
- Two machine checks added: `scripts/check_ledger.py` (fails on any note figure missing from the ledger), `scripts/check_drift.py` (EN-KR figure comparison)
- Risk-based verification: the verifier re-confirms H rows and legal, contract and trial-status sentences against their ledger URLs, ~30 call cap, returns CONTRADICTED and UNSUPPORTED only. Full mode keeps all-claim verification
- Deliverables always include PDFs (user standing instruction). Use `build_docx.py --pdf`
- Harmonic AI phrasing removed from source-resolution.md, source-record-template.md, sector-source-map.md, examples-good-bad.md and the access eval

Unchanged
- 8-section structure, writing principles, the PitchBook no-attribution rule, Key Questions rules, format, the 2-round rework loop, existing lint rules R01-R18 and the 24 fixtures

Assumptions and open items
- In Quick mode, valuation, headcount and revenue stay "Not disclosed" unless confirmed in public sources. Rerun in Full mode when needed.
- Risk-based verification checks N rows by sample only. This risk is reduced, not eliminated, by check_ledger.py and the ledger-only writing rule.
- The speed gain is not yet measured. Record duration and call counts on the next real run.
- Eval cases have not been verified by model runs. Scripts were verified on a real note run (English 1,498 words, R19 failure confirmed) and by unit tests.
- source-resolution.md now differs from the meeting-notes copy (Harmonic phrasing).
- If the verifier's tier table has no premeeting-notes entry, treat it as Tier 1 (same as v1.0). The verifier itself was not modified.

## v1.0 (2026-11-03)
New skill. Split MODE A Source Mode W (web-research notes with no meeting record) out of meeting-notes v3.8, reflecting feedback from a real pre-meeting note run.

Scope
- Pre-meeting company prep notes. Works with no meeting record. Earlier meeting notes are usable as input material
- English DOCX, Korean DOCX, Key Questions (Korean inline). Per the existing output requirement only DOCX is produced, and PDFs are made only on explicit user request
- Meeting-record notes belong to meeting-notes (the routing table is identical in both SKILL.md files)

Taken from meeting-notes
- The 8-section structure and headings (At a Glance, Company Snapshot, The Problem, Technology, Business Model & GTM, Commercial Traction, Competitive Landscape, with only the last section renamed "Key Considerations Going Into the Meeting")
- Entity Identity Lock, cross-source consistency check, Single-Statement Rule, prose+bullet mixing, insight integration, no investment opinion or Next Steps, author anonymization, exclusion of internal signals and firm-related content, the fixed format table, the Korean ~임/함 style, the Key Questions format
- Content pre-approval step, independent first-pass review, EN->KR drift check, DOCX integrity check, the 2-round rework loop with failure-category tagging, reporting-honesty principles
- The per-sector source mapping (unchanged) and the prep-relevant entries of known-error-patterns

Not taken (post-meeting only)
- Transcription-error patterns, transcript attribution rules, red highlighting, Follow-up Items, meeting timeline, closing paragraph, review mode, verifier-misjudgment and spoken-utterance cases

Added
- `references/source-resolution.md`: PitchBook and public-primary-source verification procedure (identity, access check, opening originals, capture, label check, cross-check, per-metric canonical selection)
- `references/source-record-template.md`: the private Source Record
- `references/examples-good-bad.md`: 14 good and bad examples
- Published data line in Technology 4d, Valuation line in Company Snapshot
- `scripts/build_docx.py` (EN/KR DOCX conversion with text comparison; --pdf on explicit request), `scripts/lint_note.py`
- `tests/` (lint fixtures), `evals/` (10 skill-creator cases)

Assumptions and open items
- The no-attribution instruction is limited to PitchBook. All other sources follow the existing attribution format, and every source's name and retrieval date stays in the private Source Record.
- The verifier's tier table may lack premeeting-notes. When absent, treat as Tier 1. The verifier itself was not modified.
- Output saves to the same folder as meeting-notes, distinguished by filename (`_Premeeting_Notes_`).
- Eval cases were not verified by model runs. Only the lint fixtures were executed and confirmed passing.
- Writing and verification standards follow the existing meeting-notes standards. No new AI-detection targets were introduced.
