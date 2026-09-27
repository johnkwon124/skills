---
name: startup-screening-scorecard
description: Rates one startup or a batch of startups on a 100-point rubric (investor quality, founding team, notable backers, strategic fit, traction), assigns an A-to-D grade, and recommends a next action. Use it to decide whether a company deserves outreach, or to rank a batch of sourced companies.
---

# Startup Screening Scorecard

A structured screening tool to decide whether a startup is worth your time. It gives a quantitative score, qualitative comments, and a recommended next step. The core question: is this worth meeting, and if so, how fast and through which channel.

## 1. Modes

| Input | Mode | Output |
|---|---|---|
| One company | Quick | Chat markdown |
| Five or more companies | Batch | Table document |
| "deep" or "detailed" requested | Deep | Chat markdown, optional document |

Fewer than five companies: run Quick for each and do not produce a document.

## 2. Inputs

Required: company name. Optional, and if given, skip web search: round details, lead investor, other investors, founder names, one-line product summary.

If information is missing, run at most one web search per company with a combined query for funding, investors, and founders.

## 3. Rubric (100 points)

Each dimension is capped at its maximum. If a fact cannot be verified, score that item zero and flag it as unverified. Never estimate.

### 3.1 Investor quality (30)

Add up the items below, then cap at 30.
- Lead investor is a top-tier venture firm: up to 15
- Participation by a well-known corporate venture arm: up to 10
- Direct strategic investment from a large technology company (more than a passive fund): up to 10
- Top specialist firm in the company's sector: up to 8
- Second-tier venture firm as lead: up to 7

Define your own tier lists in advance and keep them stable across runs. If investors cannot be confirmed: zero points and "Investor info unverified".

### 3.2 Founding team (25)

Add up, then cap at 25. Items can stack.
- Repeat founder with a prior exit: 15 (prior founding without an exit: 5)
- Founder from a leading research lab in the field: 10
- Senior leadership at a top technology company (director level or above): 8
- Recognized domain expert for the sector (for example a former senior engineer or lab lead): up to 10
- Relevant PhD from a top program: 5

If background cannot be confirmed: zero points and "Founder background unverified".

### 3.3 Notable angels and backers (15)

Cap at 15.
- Notable angels or scouts with a strong track record: 5 each, up to 10
- Backers who are operator-founders of large companies: 8
- An industry leader as advisor or investor: 5

### 3.4 Strategic fit (20)

Define the mandate once (sectors, stage, geography, any partner or customer relationships that matter to you) and score against it. Cap at 20.
- Sector matches the core thesis: 10
- Adjacent sector: 5
- Stage fit (for example Series A to C): 5. Pre-seed, seed, or late growth: 0
- A specific, named synergy with a partner, customer, or acquirer you can reach: 5. If you cannot name it: 0
- Based in, or expanding into, your target geography: 2. Outside it with no plans: minus 3

### 3.5 Traction and round quality (10)

Cap at 10. Negative totals are allowed.
- Disclosed ARR that is reasonable for the stage: 5 (not disclosed: 0). Define stage benchmarks in advance.
- Notable customer logos (large enterprises, cloud providers, government): 3
- Round freshness: last round within 6 months plus 2; 12 months neutral; more than 18 months minus 2 (down-round risk)

## 4. Rating

| Rating | Score | Action |
|---|---|---|
| A | 85 to 100 | Reach out immediately, within one to two days. Warm introduction first, cold contact otherwise |
| B | 70 to 84 | Reach out within one week |
| C | 55 to 69 | Monitor. Add to a watchlist and act on the next funding signal |
| D | below 55 | Pass. Log it for pattern tracking only |

## 5. Output formats

### Quick

```markdown
## [Company] | Rating: B (76/100)

**Basics**
- Sector, stage and round size, lead and participants, founders

**Score breakdown**
| Dimension | Score | Comment |
|---|---|---|
| Investor quality | 25/30 | one line |
| Founding team | 18/25 | one line |
| Angels and backers | 8/15 | one line |
| Strategic fit | 17/20 | one line |
| Traction | 8/10 | one line |
| Total | 76/100 | |

**Positive signals**
**Negative signals and risks**
**Recommended next action** (channel, parallel steps, logging, what to do if a meeting is set)
```

### Batch

A table with columns: Company, Sector, Stage, Lead investor, Key founders, Score, Rating, Recommended action. For A and B companies add a three to five line summary.

### Deep

Quick output plus three to five lines of reasoning per dimension, a comparison with three competitors, two strategic synergy scenarios, and a suggested outreach angle. Offer a document once and create it only if the user says yes.

## 6. Validation rules

1. Never guess investor names. Missing means unverified and zero.
2. Never guess founder backgrounds.
3. Never estimate ARR or traction. No "expected $5M".
4. Name a synergy only if it is clearly identifiable. Otherwise "synergy unclear" and zero.
5. No promotional adjectives. State facts: "led by a top-tier firm", "founder previously at a research lab".
6. For competitors, state funding and product facts only. Compare on objective metrics such as ARR or customer count.

## 7. Efficiency rules

- Documents are off by default. Quick never creates one.
- At most one web search per company. Skip search if the input already has the facts.
- Do not trigger other workflows automatically. Recommend the next step and wait.
- Warn before batches larger than ten companies, since cost grows.
- If the same company is requested again, ask once whether an earlier result exists.

## 8. Workflow

1. Parse input, pick the mode, and check whether the input is enough to score.
2. Search once per company only if needed.
3. Score each dimension, apply caps, compute the total, assign the rating.
4. Output in the mode's format, with positive and negative signals separate and a recommended next action.
5. Stop and wait for the user.

## 9. Edge cases

- Nothing found (stealth company, name clash): stop scoring and ask for a URL or more detail.
- User input conflicts with search results: show both and ask which to trust.
- Already met the company: ask whether to run a follow-up evaluation instead.
- Possible conflict of interest (for example a competitor of an existing holding): flag it and leave the judgment to the user.

## Example (fictional)

Lumina Inference, Series A of $30M, led by a top-tier firm, with a large chip company and a corporate venture arm participating. Founders: an ex-research-lab engineer and a former chip architect with a relevant PhD. Score: investor quality 30/30 (capped), founding team 23/25, backers 10/15, strategic fit 17/20, traction 8/10, total 88, rating A. Risks: several well-funded competitors in the same category, and ARR that is low for a Series A.
