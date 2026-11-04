# Source Record Template (v1.1, Full mode. Quick mode: the ledger format in quick-mode.md section 3)

A **private work record** created once per company. Its contents are never copied into the note (DOCX), Key Questions, or the chat body. The PitchBook source name exists only inside this file. Every source's name and retrieval date (PitchBook and public alike) is kept here.

- Filename: `SourceRecord_[Company]_[MMDDYYYY].md` (stored in the working directory, not counted as a deliverable)
- Delivered as-is if the user asks. Without a request, the chat gets a one-line summary only: "Source Record: N metrics resolved, M unresolved (K reflected in the note)"
- The Claims table (section 8) maps the note body's figures and proper nouns to sources 1:1. It replaces the older "light claims ledger" from meeting-notes.

---

```
# Source Record: [Company] ([MMDDYYYY])
Prepared for: [premeeting-notes | meeting-notes MODE A/B]

## 1. Identity
- Legal / working name:
- Official domain:            (how confirmed: site visit, domain match)
- Profile IDs:                (DB profile IDs, if any)
- Same-company checks:        (website, legal name, founding year, HQ, founders match?)
- Excluded same-name entities:(names, basis for exclusion)

## 2. Access Log
| Source | Access status | Method | Date | Limits / impact |
|---|---|---|---|---|
| PitchBook | opened / not accessible / user-provided extract | logged-in browser / connector / pasted | | |
| Company site, press releases | | | | |
| Regulatory / grant records | | | | |
(Status is "opened" only when on-screen text was actually read. For inaccessible sources, record the affected items)

## 3. Rounds (original basis, one deal per line)
| Date | Type / instrument | Amount | Currency | Pre-val | Post-val | Status | Lead | Participants | Class (equity / grant / debt) | Source class | Retrieved |
|---|---|---|---|---|---|---|---|---|---|---|---|
(Pre-val and Post-val come only from the same deal record as the Amount in that row. Check post = pre + that deal's new money; if it does not hold, note it under "Likely reason" in Metrics)

## 4. Metrics and resolution
| Metric | What it measures | Canonical value | As-of | Basis for choice | Alternates seen (value, source, date) | Likely reason for difference | Confidence | In note? (Y/N + why) |
|---|---|---|---|---|---|---|---|---|
(Example: Seed round size | announced round amount | $8M | 2024-05 | company press release | $9.1M, funding database deals tab, 2026-11-03 | possible extra closing (unconfirmed) | medium | Y, single figure only)

## 5. Investors
| Name | Deal-level (round) | Company-level only | Source |
|---|---|---|---|

## 6. Team and headcount
| Person / metric | Value | As-of | Source class |
|---|---|---|---|

## 7. Company-published data inventory
| Item (spec, paper, patent, benchmark, customer fact, repo) | What it shows | Date | Link or location | Claim or published data? |
|---|---|---|---|---|

## 8. Claims ledger (note-body figures and proper nouns 1:1)
| Claim in note | Value | Source class (public / db / transcript / user-provided) | URL or record | Published or retrieved |
|---|---|---|---|---|

## 9. Unresolved
| Item | Why unresolved | Changes judgment or meeting question? (Y/N) | Where handled (note sentence / Key Question / record only) |
|---|---|---|---|
```

Writing rules: value cells carry exactly what the source showed. Interpretation goes only in "Basis for choice" and "Likely reason", and unconfirmed reasons are tagged "unconfirmed".
