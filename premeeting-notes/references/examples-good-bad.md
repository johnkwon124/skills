# Good and Bad Examples (v1.0)

All company names, investor names and figures are illustrative fictional values (ExampleCo). Take only the format and the judgment criteria.

---

## 1. Amount and valuation are different metrics

**Bad**
> The 2024 seed was announced at $8M, while the post-money valuation of $22.6M differs from the announced amount.

Problem: a round amount and a post-money valuation measure different things. Writing that they "differ" manufactures a conflict that does not exist and hands interpretation to the reader. (lint R04)

**Good**
> - **Seed (May 2024)**: $8M, led by Alpha Ventures (press release).
> - **Valuation**: $22.6M post-money at the seed.

Each value sits under its own label, and the valuation is tied to a round and a point in time. No comparison, and no pairing with the announced amount as if they were arithmetically related. The valuation record may have been based on a deal amount different from the announced one, so run the pre/post check of source-resolution.md section 5 first.

---

## 2. Same metric, different values across sources

**Bad**
> The seed was $8M in the announcement but $9.1M in another record. (lint R05)

**Good (note)**
> Seed: $8M, announced May 2024.

**Good (Source Record row)**
> Seed round size | announced round amount | $8M | 2024-05 | company press release | $9.1M, funding database deals tab, retrieved 2026-11-03 | extra closing not announced (unconfirmed) | medium | Y, single figure only

One announced amount in the note. The reconciliation lives only in the record. If the difference is large enough to change an investment judgment and the reason is unknowable, elevate it as one sentence and a question per the section 7 bar.

---

## 3. Never write obvious observations

**Bad**
> The three follow-on investors were absent from the 2024 seed announcement.

New investors are by definition absent from an earlier announcement. It changes no judgment and no question. Delete it. (lint R15 flags this shape as WARN)

**The opposite case, worth keeping**
> The 2024 seed investors Beta Capital and Gamma Angels did not take part in the October 2026 round.

State the fact once and attach no conclusion. If it bears on judgment, move it to a Key Question: "기존 시드 투자자 Beta Capital과 Gamma Angels가 2026년 10월 라운드에 참여하지 않은 배경은 무엇인지?" (Key Questions are written in Korean.)

---

## 4. Unresolved items are elevated only when they change a judgment or a question

**Bad (a judgment-irrelevant difference elevated to the note)**
> Headcount is 16 in one record and the company site mentions a team of 12 engineers.

**Good**
> 16 employees as of September 2026.

Use one dated value only. Undated site copy and role-group counts are different metrics and change no judgment.

**Good (elevated because it affects judgment)**
> The valuation of the October 2026 round is not disclosed, so the step-up from the 2024 seed cannot be assessed.

And in Key Questions: "2026년 10월 라운드의 밸류에이션과 2024년 시드 대비 step-up은 어느 수준인지?" Write only what is unknown and why it matters; never list candidate values.

---

## 5. Never mix equity, grants and totals

**Bad**
> Total funding is $17.3M.

The composition is invisible. Equity and grants may be mixed.

**Good**
> - **Equity**: $16.5M across two rounds (May 2024 seed, October 2026 round).
> - **Non-dilutive**: $0.84M in grants (October 2026).

A total that cannot be reconstructed from the round list is written as "at least $X".

---

## 6. Never turn the undisclosed into absence

**Bad**
> The company has no debt and no grants. Revenue is zero. (lint R12)

**Good**
> No debt financing is disclosed. No grants were found in the sources checked (company site, press releases, public grant records). Revenue is not disclosed.

"Nothing is public" is written only after a sufficient search. When the search is insufficient, write "not found" with the list of sources searched.

---

## 7. Database sourcing and classification tags

**Bad**
> Per PitchBook, the company has 16 employees. ExampleCo is listed as revenue-generating in deal databases. (lint R03, R16)

**Good**
> 16 employees as of September 2026. Revenue is not disclosed.

Use the values but never the source name or a classifying phrase like "deal database". "generating revenue" is a DB classification tag, not revenue data, so it is not traction evidence. Sourcing lives in the Source Record's Access Log and Claims table.

---

## 8. Round participants come only from the deal-level list

**Bad**
> The October 2026 round included Delta Partners, Alpha Ventures, Epsilon Fund, Beta Capital and Zeta Foundation.

Beta Capital and Zeta Foundation are names pulled from the company-level cumulative investor list.

**Good**
> The October 2026 round was led by Delta Partners, with Alpha Ventures and Epsilon Fund participating. Beta Capital is an existing investor.

---

## 9. Sources you could not access

**Bad (chat or record)**
> I pulled the figures from PitchBook.
(The connector or logged-in session was never checked, and no screen was ever read)

**Good (Access Log row)**
> PitchBook | not accessible | logged-in browser check, login page, 2 attempts | 2026-11-03 | round amounts, valuation and headcount taken from the company press release and the company site only

**Good (chat report)**
> PitchBook would not open in this session (login screen, 2 attempts). I proceeded with public sources; the deal-level investor list and the latest-round reconciliation are left empty. If you open a logged-in browser session or paste the Deals tab text, I will fill them in.

---

## 10. Tautology, unfounded adjectives, writing-process narration

**Bad**
> The pilot is a pilot with a beverage maker, and the beverage maker is the pilot customer. The industry-leading approach was originally listed as a prototype but on recheck it is a pilot.

**Good**
> Pilot with a multinational beverage manufacturer. The customer is not named.

---

## 11. When sources explain the technology mechanism differently (an unresolved item that affects judgment)

**Good (format example, content fictional)**
> The patent describes a reversible phase change in the solid. The press account describes gas molecules transferring energy to the pore walls. Public materials do not say which applies to the current product.

It changes both the technology-plausibility judgment and the meeting questions, so state it once and send it to a Key Question: "특허의 상변화 설명과 보도의 기공 흡착 설명 중 어느 쪽이 현재 제품의 작동 원리인지?" Do not assert which is right, and do not infer beyond what the sources support about what it means for judgment.

---

## 12. When using an earlier meeting note as input (premeeting-notes)

**Bad**
> The founder said pricing is still open. (lint R13)

That is quotational, as if the meeting just happened. This note is not a meeting record.

**Good**
> Pricing was open as of the August 5, 2026 meeting.

State it directly as a dated fact, and send open items to Key Questions: "2026년 8월 미팅 시점에 열려 있던 가격 체계가 현재 확정됐는지, 확정이라면 과금 단위는 무엇인지?"

---

## 13. A section with nothing public (premeeting-notes)

**Bad**
> The company is expected to monetize through a mix of hardware sales and services as it scales.

An empty section filled with groundless generality.

**Good**
> Not disclosed: pricing, sales channel, and whether the company will sell equipment, supply modules or license the technology.

And in Key Questions: "장비 판매, 모듈 공급, 라이선스 중 어느 모델을 우선하는지, 첫 파일럿의 과금 구조는 어떠한지?"

---

## 14. Data the company has actually published (the Published data line in Technology 4d)

**Bad**
> The company has strong technical documentation and a robust IP position.

**Good**
> **Published data**: one granted patent (priority October 2022, granted January 2026, university as assignee); a government project record listing durability testing as a planned task; no datasheet or third-party test report found.

List available data by kind and date, and bound what is absent by the scope searched ("found"), never as absence.
