---
name: pitch-day-sourcing
description: Extracts the startup list from a shared pitch-day or demo-day deck link, enriches each company with web research, filters by target region, and ranks them into priority tiers against your investment focus before writing a formatted Excel sourcing list. Use it whenever a pitch-day document needs to be analyzed, listed, tiered, or turned into an outreach plan.
---

# Pitch-Day Sourcing

Turns a public pitch-day document (accelerator batch list, university demo day, corporate innovation program) into a tiered sourcing spreadsheet.

Before starting, ask for two inputs if they were not given:
- **Focus areas.** The sectors you invest in, used as the thesis test for tiering. Example: industrial software, robotics, battery technology.
- **Target regions.** The region to keep and any preference order inside it. Example: United States first, then Canada.

The steps below assume that example. Substitute your own.

## Phase 1: Extract the list

Open the link in a browser. Confirm what the document looks like.

- **Table layout.** Note the page count. Scroll to the last row of each page and capture every row.
- **Slide layout.** Step through each slide and capture company name, description, country, and funding.

Fields to capture: row number, company, brief summary, amount raised, country, university (if shown).

Read the event metadata at the top of the document for the file title: event name, date, audience or cohort, host organization.

If the link asks for an email to view, tell the user and skip that link.

## Phase 2: Filter by region

Keep companies whose country is in the target regions. Drop the rest. If country is missing, infer it from the summary or mark it "to confirm".

Regional priority is a tie-break only. If two companies are otherwise equal, the one in the higher-priority region ranks higher. Never lower a tier because of region alone.

Record the counts: total companies, kept, and a split by region.

## Phase 3: Web research (three axes)

Research the kept companies in batches of three in parallel.

**Axis 1: Technology and differentiation.** Search the company name plus technology or product keywords. What problem does it solve and how? Is the difference from competitors clear?

**Axis 2: Investor profile.** Search funding, investors, seed round. List investors and judge signal strength: well-known top-tier venture firms or strategic corporate investors versus angels and unknown small funds. If the deck's raised amount differs from search results, use the deck number and note "(per deck)".

**Axis 3: Founding team.** Search the CEO name plus previous company, co-founder, PhD. Look for prior founding or exits, large technology company or top research lab background, and domain expertise.

Quality rules:
- Add one or two technology keywords from the summary to the query to avoid same-name companies.
- Prefer funding databases, professional profiles, and official sites.
- If nothing is found, write "N/A". Never guess.
- After two failed searches, write "N/A" and move on. Place the company in tier 3 (limited information).

## Phase 4: Sector labels and key bullets

Assign one sector label from a fixed list, for example: Agentic or Enterprise AI, Healthcare AI, Biotech, Regulatory or Life Sciences AI, Sales AI, AI Infrastructure or Developer Tools, Cybersecurity, Data and Analytics, FinTech, Education, Supply Chain, Energy and Climate, Defense or Hardware, Space, Blockchain, Government Technology, Mining or Critical Minerals.

Write two to four bullets per company:
1. Core business and differentiation.
2. Investor signal.
3. Founding team.
4. Optional: what is unusual about the approach or business model, with specific evidence. No unsupported enthusiasm.

Bullets should carry analysis, not a list of facts. Use only verified information. Mark inference with "likely" or "estimated". Avoid loaded adjectives.

## Phase 5: Tiers

Give each company a tier and a one or two line rationale. The rationale must state at least one of: focus-area fit, team or investor signal, differentiation.

| Tier | Criteria |
|------|----------|
| Top | Fits your focus areas, has a proven team or investor signal (top-tier investor, meaningful exit, major lab or company background), and has a clear technical or business difference |
| 2nd | Fits the focus but signal is weak or the company is very early; or signal is strong but fit is weak |
| 3rd | Adjacent sector, or too little information to place |
| Others | Does not fit, or outreach is unlikely to be worth it. State the reason |

## Phase 6: Excel file

File name: `<Host>_<EventShortName>_<MMDDYYYY>_<Region>_Startups.xlsx`

Layout:
- Row 1: merged title, `<Host> | <Event> - <Region> Startup Sourcing List`. Dark navy fill (#0D2137), white bold Arial 13.
- Row 2: merged subtitle, `<audience> | <date> | <N> companies in region | Top X / 2nd Y / 3rd Z / Others W`. Same fill, white Arial 10.
- Row 3: column headers on #1F3864, white bold Arial 10.
  `# | Company | Tier | Sector | Key Bullets | Tier Rationale | Website | CEO Name | CEO LinkedIn | Raised | Investors | University | Country`
- Row 4 onward: data. Alternate white and light gray (#EEF2F7). Sort by tier (Top, 2nd, 3rd, Others), then by region priority.
- Tier cell fill: Top #E2F0D9, 2nd #FFF2CC, 3rd #F2F2F2, Others #FCE4E4.
- Column widths: #:4, Company:20, Tier:8, Sector:26, Key Bullets:55, Rationale:32, Website:25, CEO:22, LinkedIn:42, Raised:12, Investors:38, University:10, Country:8.
- Arial, headers 10 pt bold, data 9 pt, data row height 65. Thin gray borders (#CCCCCC). Center: #, Tier, Raised, University, Country. Freeze panes at A4 and put an auto filter on row 3.

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
num_cols = 13
TIER_FILL = {t: PatternFill("solid", start_color=c, end_color=c)
             for t, c in {"Top": "E2F0D9", "2nd": "FFF2CC",
                          "3rd": "F2F2F2", "Others": "FCE4E4"}.items()}

ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=num_cols)
t1 = ws.cell(row=1, column=1, value="<Host> | <Event> - Startup Sourcing List")
t1.font = Font(name="Arial", bold=True, color="FFFFFF", size=13)
t1.fill = PatternFill("solid", start_color="0D2137", end_color="0D2137")
t1.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 30
# Row 2 subtitle, row 3 headers, rows 4+ data (apply TIER_FILL[tier] to the tier cell)
ws.freeze_panes = "A4"
ws.auto_filter.ref = f"A3:{get_column_letter(num_cols)}3"
output_path = "sourcing_list.xlsx"  # set to your real file name
wb.save(output_path)
```

## Phase 7: Fact check

- No invented or guessed numbers.
- The CEO named is the actual CEO or founder (watch title confusion).
- The website is the company's official site, not a same-name company.
- The LinkedIn URL belongs to that person.
- Any difference between deck and search amounts is marked "(per deck)".
- The region filter has no misclassified rows.
- Missing data is "N/A".
- Each tier rationale cites specific evidence.
- Every "Others" row has a stated reason.

## Phase 8: Report

Save the file in the workspace folder the user names. Report:

```
[Event] sourcing complete
- Companies: N total | in region: M (split by region, K excluded)
- Tiers: Top X / 2nd Y / 3rd Z / Others W
- CEO LinkedIn found: X of M | websites: Y of M | investors: Z of M

Top tier:
- [Company]: [one-line rationale]

[file link]
```

Then ask whether to draft outreach for the Top tier. Include 2nd tier only if the user asks.

## Phase 9: Outreach handoff (optional)

This skill does not send messages. If the user approves, hand each Top tier company to your outreach drafting step with: company, target person and profile URL, key bullets, and tier rationale. Every message needs the user's approval before it is sent.

Avoid duplicates. Compare against earlier sourcing files in the same folder. If a company appeared before, check whether outreach already happened. Mark it "contacted in earlier batch" and skip resending. You may still refresh its research.

## Multiple links

Process each link in turn through Phases 1 to 9 and create one file per event. Reuse earlier research when a company reappears, but recheck its tier rationale. Finish with a summary: links processed, unique companies, and overall tier counts.

## Error handling

| Situation | Action |
|-----------|--------|
| Link needs email verification | Tell the user, skip the link |
| Two failed searches for a company | "N/A", tier 3 |
| Slow page load | Wait 3 seconds, retry once |
| Possible same-name confusion | Mark the bullet "(to confirm)" |
