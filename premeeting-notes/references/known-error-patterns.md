# Known Error Patterns (running log)

Recurring error types premeeting-notes has hit while collecting and writing company data. Skim this list before starting source verification and actively watch for these patterns in the current note. This file also ships with the verification brief sent to the independent first-pass verifier.

**Addition rule**: new entries are added only when the user has confirmed a real error. Never added on the skill's own judgment alone. Format: date / error-type category / what was wrong and how / how it was caught, in one or two lines. Entries shared with the same file in meeting-notes are kept in sync.

Categories: identity-mismatch / cross-source-conflict / unverifiable-claim / stale-info / format-drift / metric-mismatch / other

(Company and person names below are anonymized; the dates and lessons are real.)

---

## 2026-08 - identity-mismatch
An older internal meeting-note file (written 2025-08) carried a typo of the company's official name. Had a follow-up note used that internal document as a naming source, the typo would have propagated. It was caught because a separate web check (official domain, Crunchbase) confirmed the correct spelling. Lesson: use internal legacy documents for context only; always re-confirm names and spellings against external authoritative sources (see SKILL.md 2.1 Entity Identity Lock).

## 2026-08 - cross-source-conflict
Coverage of one company's large deal: a November 2025 press release named the counterparty one way, and a separate March 2026 source (an article quoting a conference talk) named the counterparty of a similar-sized deal differently. The session could not confirm whether it was a misreport of the same deal or two separate deals, so the note stated the uncertainty once and left a confirmation question in Key Questions. Lesson: when the name of a key counterparty differs across sources, never pick one arbitrarily. If verification resolves it, resolve it in the Source Record; if it stays unresolved and the deal's existence or counterparty affects judgment, state it once in the note and elevate it as a question (see the cross-source consistency check).

## 2026-09 - cross-source-conflict (round-lead inflation)
A briefing described a 2019 Series C as "co-led by Investor A alongside two others, $54.7M". The company's press release (2019-04-08) said "$54M, led by Investor B", with Investor A and the third party as participants. Only Investor A's own materials and an award article said "co-led". Caught by re-calling the primary source. Lesson: when an investor's self-description ("co-led") and the company press release ("led by") differ, the body uses only the press-release phrasing and the investor's phrasing stays in the Source Record. Never add precision the source does not have to an amount.

## 2026-09 - stale-info (missed comparable valuation)
A 2026-09-16 briefing carried a comparable company's valuation only as of 2025-08. A newer financing had in fact been announced in 2026-06, nearly doubling the figure. The document's own claim was not wrong, but the missed recent event weakened the category-valuation logic. Caught by a "is there a newer announcement" search. Lesson: for comparable companies' valuations and financings, run a separate search for announcements within 6 months of the writing date.

## 2026-09 - cross-source-conflict (title mismatch inside one firm)
A deck gave an investor's title as "co-founder and Managing Director"; the firm's team page and an award body said "Managing Partner"; the firm's own January 2025 press release said "Managing Director". The briefing wrote it as if only the deck was wrong and cited unchecked sources as support. Lesson: even a firm's own materials can disagree. Record only the sources actually checked, use one title from the firm's own materials, keep per-source differences in the Source Record, and elevate only when they affect judgment or diligence questions.

## 2026-09 - other (date arithmetic)
A note wrote "about 7 months before" for an interval between a January and an August event. Computing from the actual dates (January 29 to August 7) gives about 6 months. Lesson: compute month-level intervals from dates.

## 2026-11 - metric-mismatch (comparing an amount with a valuation)
A pre-meeting note draft wrote, in effect, "the post-money $22.6M differs from the announced $8M". A round amount and a post-money valuation are different metrics; there is no conflict. Confirmed by user feedback (2026-11-03). Lesson: define what each number measures first, write different metrics under their own labels, and never compare them (see source-resolution.md section 6 A).

## 2026-11 - metric-mismatch (listing candidate values for one metric)
When sources disagreed on one metric, the draft listed two or three values in the body and left the choice to the reader. User feedback (2026-11-03). Lesson: the author picks one canonical value, and candidate values with reasons for differences stay in the Source Record. The only unresolved item that goes into the note is a single sentence on one that changes an investment judgment or a meeting question (see source-resolution.md sections 6 D, 7).

## 2026-11 - other (obvious observation)
A sentence like "the three follow-on investors were absent from the 2024 seed announcement", trivially true by definition, made it into a note. User feedback (2026-11-03). Lesson: delete sentences a reader with the numbers can see immediately and that change no judgment or question (see source-resolution.md section 8).

## 2026-11 - other (source-label leak risk)
A pre-meeting note draft contained a sentence to the effect of "listed as revenue-generating in deal databases". What the user confirmed is the standing preference (2026-11-03) that PitchBook data is used but never attributed in the note; whether this sentence itself was flagged is unconfirmed. Lesson: write PitchBook values as bare values, with no PitchBook source name or classifying phrase. A classification tag (generating revenue, etc.) is not revenue data, so it is never traction evidence (see source-resolution.md section 9, lint R03 R16).
