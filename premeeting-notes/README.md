# premeeting-notes

A Claude skill that prepares an investor-grade company brief before a meeting, with no meeting record required. Give it a company name or domain and an upcoming meeting; it opens and verifies public primary sources, picks one canonical value per metric, and delivers an English note DOCX, a Korean note DOCX (each with a matching PDF), and inline Key Questions in Korean.

Version 1.1 (2026-11-03). See `references/CHANGELOG.md`.

## Modes

- **Quick (default)**: speed-optimized. A claims ledger is written during research, the note is written only from the ledger, and verification is risk-based. PitchBook is used for 4 items only (lead investors, total funding, latest round date, Series).
- **Full**: the complete research-and-verification procedure for investment decisions (valuation, revenue, headcount, cap table).

## Layout

- `SKILL.md` - routing, principles, workflows (Quick and Full), the 8-section note structure, Key Questions, format, verification, completion checklist
- `references/` - quick-mode spec, source-resolution protocol, Source Record template, good/bad examples, per-sector source map, known error patterns, changelog
- `scripts/` - `build_docx.py` (markdown to DOCX/PDF for EN and KR, with text round-trip verification), `lint_note.py` (deterministic text lint, R01-R19), `check_ledger.py` (every note figure must exist in the claims ledger), `check_drift.py` (EN-KR figure and proper-noun drift)
- `tests/` - lint fixtures and script regression tests (`python3 -I tests/run_lint_fixtures.py`, `python3 -I tests/run_script_tests.py`)

## Requirements

Python 3 with python-docx; LibreOffice and pdftotext for the PDF step. Korean PDF rendering needs a NanumGothic font (the script tries to fetch it and only warns if it cannot).

## Private-watch configuration

Two lint rules fail a note that leaks private names. Both are inactive until you create their token file next to `scripts/lint_note.py` (one token per line, `#` for comments; keep the real files out of git):

- `lint_private_tokens.txt` -> R09 PRIVATE_TOKEN: your firm's name and abbreviations, codenames, affiliations. Template: `lint_private_tokens.example.txt`
- `lint_internal_names.txt` -> R08 INTERNAL_NAME: internal agent, tool and project names. Template: `lint_internal_names.example.txt`

The public package ships no real tokens. The test suite exercises both rules with fictional tokens (TestFirm, TestAgent) through temporary token files, so the fixtures pass on a fresh clone.

## Notes

- The English note, Korean note and Key Questions are all linted; Key Questions are chat output but go through the same checks via a temp file.
- This public mirror omits the `evals/` folder from the original package (a skill-creator eval harness with Korean prompts). Everything needed to use the skill is included.
