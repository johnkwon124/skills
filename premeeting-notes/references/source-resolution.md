# Source Resolution Protocol (v1.1, Full mode baseline. Quick mode: quick-mode.md)

Maintenance note: through v1.0 this file shipped with identical contents in both meeting-notes and premeeting-notes. In v1.1 the premeeting-notes copy dropped the Harmonic AI phrasing, so the two copies now differ at that spot. The meeting-notes copy was not changed without a user instruction.

The procedure for collecting company data from PitchBook and public primary sources and deciding "the value the note will use". Two purposes: the note hands the reader already-decided facts, and the basis for each decision is kept separately with dates.

## 1. Four principles

1. **Define what each number measures first.** Amount and valuation, announced and closed, equity and grants, cumulative and single round are different metrics. Different metrics cannot conflict, so they are never compared; each sits under its own label.
2. **Pick one canonical value per metric.** Never show the reader two or three figures and leave the choice to them. The author's choosing is the value of this note.
3. **The reconciliation process goes in the Source Record; the note carries only the conclusion.** Candidate values, sources, dates and reasons for differences stay in the private record.
4. **Write the unknown as unknown.** Never turn "undisclosed" into zero or absent, and never dress an unverified value in confidence.

## 2. Procedure (fixed order)

| Step | What to do | Recorded where |
|---|---|---|
| S1 Identity | Confirm the official domain and legal name; cross-check each DB profile's website, legal name, founding year, HQ and founders for the same company. Record the basis for excluding same-name entities | Source Record > Identity |
| S2 Access | Verify the sources you plan to use are actually accessible (section 3) | Source Record > Access Log |
| S3 Open originals | Open originals, not summary boxes. For DBs the round-detail (Deals) tab and deal pages; for public sources the original press releases, regulatory filings (SEC Form D etc.), government grant records, official sites | Access Log |
| S4 Capture | Capture values per the section 4 checklist. Attach source, retrieval date and as-of date to every value | Source Record > Metrics, Rounds |
| S5 Label check | Verify what a field name actually measures (section 5) | Source Record > Label notes |
| S6 Cross-check | Confirm important numbers from two or more independent source classes | Metrics > Confidence |
| S7 Resolve | Pick the canonical value per metric by the section 6 rules | Metrics > Canonical |
| S8 Reflect | Only canonical values go in the note. Only unresolved items past the section 7 bar go into the note and Key Questions | Metrics > In note |

## 3. Access verification (S2)

- **Verify before claiming existence.** Before saying a PitchBook connector exists, actually check with the connector or tool listing available in this session (if tools load lazily, load them first). If there is none, record that there is none.
- **Use only paths you may legally use.** The range readable in a browser session the user is already logged into, or source text the user pasted or attached. No credential guessing, no login bypass, no caches or mirrors, no paywall circumvention.
- **When blocked, try at most twice and stop.** On a login screen, insufficient permission or a paywall, report to the user what was tried and what access is needed (which source, which screen), then wait for instructions. Meanwhile proceed with public sources where possible, recording "not accessible" and the affected items in the Access Log.
- **Never fill values for inaccessible sources from memory or guesses.** Text the user pasted is recorded as "user-provided extract, date" and never written as if opened directly.
- **Report completion only after actually reading on-screen text.** A tool returning "opened" is not evidence.

## 4. Capture checklist (S4)

**Funding.** One line per round: date, round type and instrument (priced equity, SAFE, convertible note, grant, debt, accelerator, etc.), amount, currency, status (announced, closed, additional closing), lead and participants.

**Separate equity, grants and debt.** Compute cumulative funding per class too. Check which classes the DB's "total raised" includes (section 5) and reconcile it against your own sum from the round list.

**Valuation.** pre-money, post-money, as-of date, basis (priced round, cap, implied value, estimate), and which round it belongs to. Never use a valuation not tied to a round.

**Investors.** Record deal-level (participants in that round) and company-level (cumulative investor list) separately.

**Team.** Founder and key-executive backgrounds, headcount (value, as-of date, whether the source is a company announcement or a DB aggregate).

**Data the company has actually published.** Collected separately from claims: product specs and datasheets, papers, patents, benchmarks, customer and pilot facts, open-source repositories, government project records. "What the company said" and "what the company published as material" are different evidence grades.

## 5. Label check (S5)

Do not trust field names at face value. Below are pairs that repeatedly mislead.

| Field | What to check |
|---|---|
| Last deal amount vs Total raised | Is the last deal amount included in the cumulative? Do grants count toward the cumulative? |
| Post valuation | Which round's value is it? Is the as-of date the same as the last deal date? |
| Deal amount | Same as the announced amount in the press release? Does it fold in an additional closing or extension? |
| Pre/Post valuation vs Deal amount | Verify they come from the same deal record. post-money should be pre-money plus that deal's new money. If the announced amount and the DB deal amount differ, tie the valuation to the round only ("post-money at the seed"); never pair it with the announced amount as if they were arithmetically related |
| Investors (company level) | The cumulative list to date. Not the participants of a specific round |
| Investors (deal level) | That deal's lead and participants. Round attribution comes only from this list or a press release |
| Business status (e.g. generating revenue) | A classification tag. Not revenue data, so never traction evidence |
| Employees | Company-announced or aggregated? What is the as-of date? |
| Currency | Display currency vs original currency. If converted, record the date and the exchange-rate source |

## 6. Per-metric resolution rules (S7)

**A. Are they measuring the same thing?** If not, there is no conflict. Each goes under its own label. (Example: a round amount of $8M and a post-money valuation of $22.6M.)

**B. Same metric, different values: look for an explainable reason first.** Announced vs closed, additional closing, currency, tranche, rounding, grant inclusion, as-of date differences. Once explained, the value matching the metric's definition is canonical.

**C. Source priority (within one metric).**
1. Original announcements by the company or lead investor, regulatory filings, government records
2. Credible media citing the press release
3. DB fields (items not confirmed in public sources are marked only as "a value the company has not confirmed" where needed)

If an investor's own materials and the company press release phrase things differently, use the company press release (the round-lead case in known-error-patterns). Never add precision the source does not have to an amount.

**D. If B and C still do not narrow it to one**, use the value with the strongest basis and mark its nature ("company-reported", "press-reported"). Never list candidate values side by side. Record the unresolved fact in the Source Record.

**E. Canonical choice per metric.**

| Metric | Canonical | Notes |
|---|---|---|
| Round amount | The round's announced amount. If an additional closing is documented, the summed amount with dates | Even when the announced amount and DB amount differ for an unconfirmed reason, the note carries only the announced amount |
| Round date | Announcement date. If a closing date is confirmed, mention that fact once | |
| Valuation | The form "post-money $X at [round, date]" | Never compared with an amount metric in one sentence |
| Total funding | Per-class sums ("equity $X, non-dilutive grants $Y") | If not reconstructable from the round list, write "at least $X" |
| Round participants | The deal-level list | The company-level list is used only as "existing investors" |
| Headcount | A dated company-announced value, else a dated aggregated value | Use one value only. Undated site copy (e.g. team-intro sentences) is auxiliary, and role-group counts (e.g. number of engineers) are a different metric from total headcount |

## 7. The bar for elevating unresolved items to the note

An unresolved item goes into the note only when one of these holds:
- It changes an investment judgment: runway, valuation step-up, dilution, reliability of company claims, plausibility of the technology mechanism.
- It changes a question to ask in the meeting.

When elevating, write **one sentence on what is unknown and why it matters**, and put the same item as a question in Key Questions (Korean). Never list candidate values. Exception: when the gap between a company claim and a verified value is itself the finding, write it in the Claimed vs Verified format. Those are two values with different roles.

Items below the bar - resolved as definitional differences, a few heads of headcount difference, a day of date difference - do not go in the note.

## 8. Deleting obvious observations

After writing a sentence, ask two things. Could a reader with the numbers see this immediately on their own? Does this sentence change an investment judgment or a meeting question? If both are no, delete it. Example: a sentence stating that this round's new investors were absent from the earlier seed announcement. New investors are by definition absent from earlier announcements. Conversely, the fact that existing investors sat out a follow-on round can bear on judgment, so state the fact once without a conclusion and handle it as a question.

## 9. Source attribution rules (note body)

- Values from PitchBook are written as bare values, with no source name or classifying phrase like "deal database" or "database lists". Leaving PitchBook unattributed in the note is the user's standing instruction and is limited to PitchBook.
- Harmonic AI is not used from v1.1. Even if the user pastes Harmonic text, its values do not go in the note; confirm the same facts through public primary sources.
- Every source's name, retrieval date and as-of date (PitchBook and public alike) stays in the private Source Record.
- Public sources are attributed in the existing format: "company materials", "press release (2026-10-21)", outlet names, report names. Core figures like rounds and amounts should point to the original press release or regulatory filing where possible. For other data services' citation styles (Crunchbase, LinkedIn, etc.), there is no user instruction, so do not change them; but if the same fact exists in a press release, cite the press release.
- A value's nature is expressed by the kind of value, not the source name: announced, closed, filed, company-reported, estimated.
- If a DB field is a classification tag (e.g. generating revenue), it is never traction evidence.

## 10. Honesty

- Every row in the Source Record is a value from a screen or document actually opened. Sources that could not be opened are written as not opened.
- For unconfirmed items, distinguish "not found (list of sources searched)" from "nothing is public". The latter only after a sufficient search.
- A tool's completion response is never evidence of completion. Re-extract text from saved files to verify.
