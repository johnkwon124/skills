---
name: daily-tech-news-digest
description: Assembles a daily, sector-first tech news digest as a styled HTML email, with curated sources, per-item investment insight, a funding table, and a pre-send QA gate. Use it for a scannable morning briefing across a fixed set of investment sectors.
---

# Daily Tech News Digest

A morning briefing for an investor covering a handful of tech and energy sectors. The digest should be read in a few minutes and let the reader see the day's volume and the top three items at a glance.

Example sectors: Enterprise Software, Semiconductors, Cloud Infrastructure, Energy, Health Tech. Replace them with your own list. Keep the total to five or six so each has a distinct color.

## Principle

The email is about the news. Never show how many sources were scanned, how many checks passed, or which sources failed. Those are internal. Report only the content and the send status.

## Step 1. Gather sources (last 24 hours)

- Newsletters and alerts in your mailbox from senders you follow.
- A short list of analyst-grade publications for your sectors (semiconductors, energy, AI research, and so on).
- Tech press for fill-in: a front-page aggregator, a launch feed, and a venture news section.

If a source fails to load, skip it quietly and continue.

## Step 2. Curate

1. Dedupe. One primary source per event. Note other coverage in brackets.
2. Assign one primary sector per item. Add a cross-reference only when needed.
3. Rank with stars:
   - three stars: the top three of the day, the ones that may trigger action
   - two stars: must-read within the sector
   - one star: meaningful event
   - no star: context
4. Volume: 6 to 10 items for the larger sectors, 4 to 8 for the smaller. 25 to 40 in total, counting new and cross-referenced items.
5. Build a separate funding table for every round announced in the last 24 hours.
6. Links must be article-level links to the primary source. Never a site homepage or an aggregator. If only an aggregator is available, label it "(aggregator, primary source not found)".

## Step 3. Write the email

Subject: `Daily Tech Digest, {Month Day, Year}, Morning`. Keep this format fixed, because the duplicate check in Step 5 searches for it.

Layout, top to bottom:

1. **Header.** Title, date, run time.
2. **Ticker bar.** One dot and count per sector (new plus cross-referenced items).
3. **At-a-glance row.** Four tiles: total items, new items, funding rounds, number of sectors.
4. **Top 3.** A card per item with sector tag, headline, source and link, two to three sentence summary, and a dashed insight box labeled with your firm or role prefix.
5. **Sector sections.** A header line with the sector name and `NEW:{n} REF:{m}`. Cross-referenced items get a headline and "see Top 3 #n" only. New items get source, headline, link, a summary of two or more sentences with the key number, actor, and date, and one arrow-prefixed line on market or investment implication that does not repeat the facts.
6. **Funding table.** Columns: company, round, amount, investors (as reported), sector.
7. **Footer.** Totals only.

### Rendering rules

- Use real HTML `<table>`, `<tr>`, `<td>` markup for every table. No markdown pipes, no ASCII dividers, no flexbox pseudo-tables.
- Use inline styles only. No `<style>` block and no class attributes, because many email clients strip or ignore them.
- Use a monospace font stack, a dark page background, and light text.
- Give each sector a fixed color and use it on the sector header, the left border of Top 3 cards, and the sector column of the funding table. See `references/color-palette.md`.
- Always set bold weight on headlines, so they remain readable if a client ignores the dark background.
- After the first send with a new template, look at it once in a web mail client and once on a phone.

### Writing rules

- Objective, analytical, plain prose. No adjective inflation.
- Verify funding amounts, investor names, and round stages against the source. If unsure, write "as reported".
- Say so when a valuation or round terms look stretched.
- No em dashes.

## Step 4. QA gate (internal, required before sending)

Check in this order. Fix and recheck any failure. Do not proceed until all pass.

1. **Source match.** Each summary and insight contains only what its own source says. If a sentence has no clear source, delete it or cite one.
2. **Names and units.** Company and product names are spelled correctly. Units (B, M, $, GW) are correct.
3. **HTML validity.** Search the body for `|` used as table syntax and for runs of `=` or box-drawing characters. Confirm the funding table is a real table, no flexbox layout remains, and there is no `<style>` block or `class=` attribute. Confirm section headers use the fixed sector colors.
4. **Counts.** Each section's NEW and REF numbers equal its item count. The ticker, tiles, and footer totals all agree.
5. **Links.** Every link is an article-level primary source, or is labeled as an aggregator.
6. **Tone.** No inflated adjectives, no em dashes, and "as reported" on any unconfirmed figure.

Never mention QA results in the email or in the send report.

## Step 5. Deliver

1. **Duplicate check.** Search your mailbox, sent and drafts, for today's subject. If one exists, stop and report that today's digest already exists.
2. **Send** the HTML body through your email tool to your own address. Send HTML only, with no plain-text alternative that contradicts it.
3. **Verify** the send status. Treat it as success only when the tool confirms a message ID.
4. **Report** in one line: sent status, then counts of new items, cross-referenced items, and funding rounds. If sending failed, report the reason and stop.

## Optional archive and chat copy

- Save a plain-text copy of the digest to a dated file if you keep an archive.
- If you use a chat channel, send the Top 3 headlines, the sector counts, and a completion note.
