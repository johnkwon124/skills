---
name: weekly-vc-news-curation
description: Scans five tiers of public sources across three configurable focus areas, selects the top items per sector, and produces a table document plus short insight notes for the items you pick. Use it for a weekly news digest or for insight notes on curated articles.
---

# Weekly VC News Curation

A two-phase workflow. First you curate a weekly digest. Then, after the user picks items, you write short insight notes. The user's selection is a required gate between the phases.

## Rules

- **Verifiable only.** Report confirmed, public information. Never invent or estimate funding amounts, valuations, or statistics. If the source does not say it, you do not say it.
- **Neutral tone.** No positive or negative adjectives or adverbs. Describe what happened and what it implies.
- **No paid sources.** If a link is paywalled, find another source for the same story.
- **Working languages.** Write in plain English by default. If the user wants a second language, produce both versions in natural wording, not stiff or machine-sounding.
- **Gate.** After saving the digest, stop and wait for the user's selection.

## Phase 1: Scan sources

Aim to surface the most significant developments of the current week. Read several articles per source, not just headlines. The full source list is in `references/sources.md`, which is an example set to swap for sources in your own sectors. The five tiers are:

1. **General news:** funding, deals, market moves, policy.
2. **Sector publications:** trade press for each of your focus areas.
3. **Funding and deal trackers:** confirmed rounds and notable early deals.
4. **Fund blogs and newsletters:** sector theses, portfolio spotlights, commentary from relevant venture funds.
5. **Institutional research:** public reports and briefings from consulting firms and bank research groups.

Define each focus area to include the enabling technology and suppliers, not just the headline companies. Funding, partnerships, and supply chain shifts in those layers are in scope.

## Phase 2: Select

Pick up to 10 items per focus area. Use three areas, for example software and AI, physical infrastructure, and energy (merge two if they overlap heavily).

Use this slot structure for each area:

| Slot | Count | Criteria |
|---|---|---|
| Large company (late stage, public, or unicorn) | 4 | News that changes market structure. Skip routine product updates and press releases. |
| Mid-stage startup (Series A to C) | 4 | Real technical differentiation, a notable contract or partnership, or backing from a leading fund. |
| Early stage (seed to pre-A) | 2 | A new category signal or a directional indicator for the sector. |

Extra filters:
- Large-company items must reflect infrastructure spending, M&A, a major partnership structure, or entry into a new category that affects startups.
- For startups, weight confirmed participation of leading funds, large customer contracts, and approaches that differ from incumbents.
- Check that every link opens without a login or paywall.

Keep a separate section, **Perspectives**, for notable fund blog posts and institutional research. These are analytical pieces, not news, and they do not count toward the 10.

## Phase 3: Weekly document

Create a formatted Word document.

- **File name:** `weekly_MMDDYYYY.docx`, using today's date.
- **Title:** Weekly VC News Digest, followed by the full date.
- **Body:** one section per focus area with this table:

| # | Title | Source | Category | Link |
|---|---|---|---|---|
| 1 | Article headline | Publication | Large company | https://... |

Categories are Large company, Mid-stage startup, and Early stage.

- **Perspectives section**, after the three areas:

| # | Title | Author or fund | Type | Link |
|---|---|---|---|---|
| 1 | Post or report title | Fund name | Fund blog | https://... |

After saving:
1. Give the user the file location.
2. Ask them to name the items they want insights on, by section and number, for example "Software #3, Energy #7".
3. Stop. Do not start Phase 4 until they answer.

## Phase 4: Insight notes

For each selected item:

1. Reread the source article to confirm the facts.
2. Write a short summary plus one investor-relevant point.

Format:

```
[Article title], [Source]

[2 to 4 sentences of key facts, then 1 to 2 sentences on what it signals for the sector, what competitive dynamic it reflects, or what investors should watch.]
```

If a second language was requested, add a matching version under its own label.

Limits and tone:
- At most 100 words per language per item.
- Read like a sharp analyst wrote it, not a press release.
- Say what happened and what it implies, not whether it is good or bad.
- Point out competitive dynamics, market structure, or technical direction where relevant.

Save as `insight_MMDDYYYY.docx` with the same date format.

### Verification pass

Before you present the insight file, run an independent check. Reopen each cited article and compare every number, name, and date in your notes against the source. Remove or fix anything you cannot confirm. If something remains uncertain, flag it next to the item instead of leaving it in silently.

Then give the user the file location.

## Edge cases

- **Paywall or dead link:** skip it and find another source for the same story. Never include a link you could not open.
- **Duplicate stories:** count once and cite the highest-tier source.
- **Slow week:** if fewer than 10 items meet the criteria, list only those. Do not pad with low-signal items.
- **Fund post timing:** a post from before the current week may be included if it directly relates to a story in the digest. Note its date.
