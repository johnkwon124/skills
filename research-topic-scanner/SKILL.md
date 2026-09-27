---
name: research-topic-scanner
description: Reviews recent reading and signal sources on a daily or weekly schedule, scores topic candidates, and returns a ranked shortlist of about ten deep-research topics with rationale and supporting company facts. Use it to decide what to research next. It stops at the shortlist and does not write the research itself.
---

# Research Topic Scanner

Scan recent inputs, pick the ten strongest research topics, present them as a shortlist, and stop. The scanner never performs the research itself. When you pick a topic, hand it to a deep-research or report-writing workflow.

## Run frequency

Daily or weekly, whichever suits your reading volume. Before each run, check whether a shortlist for the current period already exists. If it does, stop and report that a duplicate was avoided.

## Step 1. Collect candidates

Read three kinds of input from the last 7 days:

- **A. Signal scans.** Notes or digests that flag weak signals. Extract topics that recur or are strongly flagged.
- **B. News and sourcing digests.** Weekly news summaries, company-sourcing lists, and startup-scouting notes. Extract topics inside your focus sectors.
- **C. Direct requests.** A file or note where you list topics you want researched. Treat these as high priority.

If no source is readable, pick ten candidates from the sector trends you follow and mark all company facts "N/A".

**Extract company facts while reading.** For every startup cited as evidence for a topic, copy these fields only if they already appear in the source text:

- HQ location
- Latest round (type, date, amount, valuation if stated)
- Total funding
- Key investors (lead investor first)

Do not run new searches for these fields. Anything missing from the source is written "N/A". Never estimate or invent.

## Step 2. Select the top ten

Score each candidate on three criteria and keep the ten best:

1. **Cross-source repetition.** Appearing in several sources beats appearing in one.
2. **Fit with your focus sectors.** Define a short list of sectors you cover (for example battery storage, industrial robotics, developer tools) and tag each topic with exactly one.
3. **Timeliness.** A new inflection in the last two to four weeks: a rule change, a large financing, a technical release.

Prepare four items for each topic:

- **Topic name** (short, about 20 characters or fewer) and one sector tag.
- **Why now** (3 to 4 sentences): the signals behind it and the market or technical context.
- **Research direction** (2 to 3 sentences): the question to dig into and the data you would need.
- **Supporting startups:** company, HQ, latest round, total funding, key investors, using source values only, else "N/A". List every supporting startup.

## Step 3. Produce the shortlist

Format as a message or email with:

- A header line: number of topics, number of sources scanned, generation time.
- An index table: number, topic, sector tag, one-line background.
- A detail block per topic with the four items above.
- A footer: reply with the numbers to research; multiple picks are allowed; nothing is researched automatically without a pick.

Use inline styles only if you send it as HTML, because many mail clients strip style blocks. Send or save it with whatever delivery tool you use. If delivery fails, report the reason and do not retry silently.

Then stop. Do not begin the research.

## Handoff after a pick

When a topic is chosen, pass the topic name, sector tag, rationale, research direction, and supporting startup facts to the next workflow:

- A whole sector or technology goes to a sector deep-dive report.
- A single company or single bet goes to a company memo.

The scanner does not write the report or send a second message.

## Checklist

- [ ] Checked for an existing shortlist this period
- [ ] Collected all three input types
- [ ] Extracted company facts from source text only
- [ ] Selected ten topics with name, sector tag, why now, direction, and supporting startups
- [ ] Every value not in a source is "N/A"
- [ ] Delivered the shortlist and stopped

## Error handling

- Source tool unavailable: scan recent local files or ask the user for topics directly.
- Delivery fails: report the reason. Do not retry automatically.
- Local save fails: save to a backup output folder and report the path.
