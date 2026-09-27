---
name: sector-market-map
description: Scores startups across an investment sector on investors, founders, and partnerships, then outputs a workbook and a sector overview report. Use it to map a sector, find companies worth watching, or produce a spreadsheet and report on a theme.
---

# Sector Market Map

Research a sector from public sources and produce two deliverables:

1. **Excel market map**: every company found, three-axis scores, value-chain layers, and an A-grade shortlist.
2. **Word sector report**: an eight-section overview for investors.

All company names in this skill and its script are fictional placeholders (Acme Grid, Example Robotics, and so on). Replace them with real findings.

## Workflow

```
Step 0  Define the sector and scope
Step 1  Web research, find 6 to 12 companies
Step 2  Score each company on three axes and assign a grade
Step 3  Build the Excel market map
Step 4  Build the Word sector report
Step 5  Review and deliver
```

## Step 0. Define the sector

Confirm: sector name, sub-theme (which layer to focus on), stage limits (default: any stage), and geography (default: global). If the user gives only a sector name, start researching and ask follow-up questions after the first deliverable.

## Step 1. Research

Use public information only. Data integrity comes first. Do not write a number you cannot confirm.

1. Search recent news and funding announcements for the sector.
2. Search each company separately for investors, founder background, and partnerships.
3. Include companies that have already exited (acquired or public), marked separately, as benchmarks.

Collect per company: name, founding year, HQ; stage and total funding (latest round); core product and differentiator; key investors; founder background; announced partnerships only; value-chain position.

## Step 2. Three-axis scoring

Rules: score from public facts only, put estimates in the notes, apply the same rubric at every stage, and score low with a stated reason when information is thin.

### Axis 1: Investor profile (1 to 5)

Define your own tier list before scoring and keep it fixed across the map. Example structure: Tier 1 is the most sought-after generalist and sector-leading funds, Tier 2 is strong growth and crossover funds, Tier 3 is respected specialist and early-stage funds.

| Score | Criteria |
|---|---|
| 5 | Two or more Tier 1 funds, or one Tier 1 plus a major strategic investor |
| 4 | One Tier 1 plus a Tier 2, or two or more funds from the tier list |
| 3 | Mostly Tier 2, or a recognized sector-specialist fund outside the list |
| 2 | Recognized institution outside the list, or mainly PE or corporate investors |
| 1 | Unknown, angel-only, or small seed funds only |

### Axis 2: Founder background (1 to 5)

| Score | Criteria |
|---|---|
| 5 | Big-tech or top research lab experience plus a prior company built, or 15+ years of domain expertise |
| 4 | Top-tier tech background or a relevant PhD, plus startup experience |
| 3 | Solid relevant industry career, first-time founder |
| 2 | Technical background only loosely tied to the sector |
| 1 | Insufficient information or domain experience not verifiable |

### Axis 3: Partnerships (1 to 5)

| Score | Criteria |
|---|---|
| 5 | Publicly announced contract with a market-leading customer or platform in the sector |
| 4 | Formal collaboration with a large enterprise or major industry platform |
| 3 | Verifiable collaboration with a recognized startup or institution |
| 2 | Pilot stage, or a partnership of limited scale or credibility |
| 1 | No public partnerships |

### Grades

| Total (of 15) | Grade | Action |
|---|---|---|
| 13 to 15 | A | Prioritize for outreach |
| 9 to 12 | B | Add to a monitoring queue, re-score at the next round or milestone |
| 5 to 8 | C | Hold, keep tracking the sector |
| 4 or less | Pass | Exclude |
| n/a | EXITED | Acquired or public, kept as a benchmark |

## Step 3. Excel market map

Use Python with `openpyxl`. See `scripts/build_market_map.py` for a runnable template with placeholder data. It computes totals and grades from the three scores.

**Sheet 1, Long List.** Title block (sector, date, source note). Columns: Company, Founded, HQ, Stage, Total Funding, Value Chain Position, Customer Segment, Business Model, Core Product and Differentiator, Key Investors, Investor Score, Founder Background, Founder Score, Key Partnerships, Partnership Score, Total Score, Rating, Evaluation Notes. Row colors by grade: A green, B yellow, C gray, Pass red, EXITED mid-gray.

**Sheet 2, Competitive Landscape.** Group companies by value-chain layer. For each layer: players, core approach, main customers, competitive relationships, funding, key investors. Below, a "Key Structural Observations" block with five or six investor-level points, including open questions for diligence.

**Sheet 3, A-Grade Shortlist.** Only A-grade companies. Columns: Company, Score, Stage and Funding, Why A-Grade, Key Risks, Recommended Next Step. List B-grade names in a note row as the monitoring queue.

Style: Arial throughout, gridlines hidden, freeze panes below the header row, per-column widths, thin borders on all cells.

## Step 4. Word sector report

Use a document library (Node `docx` or Python `python-docx`). Structure:

```
Cover: sector name, "Investor Overview", date, coverage list
1. Why this sector: the structural problem, with key figures and sources
2. Core technology and approaches: three or four technology layers
3. What separates good companies: four or five criteria
4. Why now: technology maturity, regulation, large-player moves
5. Investor activity: 8 to 10 active VC, corporate, and PE investors
6. Competitive landscape: layer, players, approach, customers, competition, funding, investors
7. Structural risks: five sector-wide risks with content and impact level
8. Investment view: where value is captured, key validation points, exit paths, priorities
```

Mark public companies with their exchange. Write in the language the user asks for, keep company, product, and investor names in their original form, and cite a source for every figure.

## Step 5. Independent check and delivery

Before delivery, have the finished report checked against the research sources (a separate review pass is best). Then save both files and summarize: number of companies found, grade distribution, A-grade names, and one or two key observations.

File names: `{Sector}_MarketMap.xlsx` and `{Sector}_Sector_Overview.docx`.

## Data integrity rules

1. Cite only public sources: agency data, sector regulators, funding databases, press releases, filings.
2. No estimates. Write "N/A" where a number cannot be confirmed.
3. Prefer recent data. Use funding announced in the last 12 months.
4. Stay neutral. Avoid promotional adjectives. Write facts.
