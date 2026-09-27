---
name: vc-news-digest
description: Sorts items from Google Alerts and similar feeds by sector, flags relevance as HIGH or MEDIUM, and delivers one daily or twice-daily digest email, optionally in a second language. Use it when setting up or running a recurring deal-flow and market news digest.
---

# VC News Digest

Turns a stream of alert emails into a short, ranked digest organized by investment sector. The value is in the curation: what to keep, what to skip, and why an item matters.

## Inputs

- A mailbox that receives alert emails (Google Alerts or newsletters) you have chosen to follow.
- A sector list with keywords. Defaults are in `references/sectors.md`. Edit them to match your focus.
- A delivery address and a schedule (for example one morning run, one evening run). Configure these in your own environment.

## Workflow

1. **Collect.** Search the mailbox for alert and newsletter emails from the last 24 hours (use the last 12 hours for the evening run). For each email, extract the article title, publisher, URL, and snippet.
2. **Deduplicate.** If several alerts cover the same event, keep the one with the best primary source and drop the rest. Prefer the original announcement or reporting over aggregators.
3. **Assign a sector.** Use the decision tree in `references/sectors.md`. Each item gets one primary sector. Add a cross-reference only when an item clearly belongs to two.
4. **Rate relevance.**
   - HIGH: a direct deal or market signal for the sectors you track (a funding round, a fund close, an exit, a major product or policy change).
   - MEDIUM: adjacent signal (a trend piece, a seed round in a neighboring field, an incumbent's expansion).
   - Skip: generic opinion, consumer news, repeated coverage, anything with no business or investment angle.
5. **Write each entry.** Title, publisher, one or two sentences that state what happened with the key number, company, and date, and the link. State only what the source says. If a funding amount or investor list is unconfirmed, mark it "as reported".
6. **Cap the volume.** Aim for 20 to 25 items in total, with three to five per sector. Fewer strong items beat a long list. If a sector has nothing strong that day, say so in one line.
7. **Assemble the email.**
   - Header with date and run time.
   - One section per sector, in your priority order, each item marked HIGH or MEDIUM.
   - Subject line pattern: `VC News Digest, {Month Day, Year}, Morning` (or Evening).
8. **Optional second language.** If you read the digest in another language, produce a second email with identical items and the same order, translated. Send it as a separate message with its own subject line. Do not merge languages in one email.
9. **Send** through your email tool and confirm delivery. Before sending, check for an existing digest with the same subject on the same day to avoid duplicates.

## Quality checks before sending

- Every summary matches its own source. Nothing from another article is mixed in.
- Company names, currency, and units (M, B, GW) are correct.
- Every link goes to the specific article, not a site homepage.
- No adjective inflation ("revolutionary", "game-changing"). State facts and let the reader judge.
- No item appears twice across sectors unless it is a labeled cross-reference.

## Tuning

- Change sectors or keywords by editing `references/sectors.md`.
- Add or remove alert queries to change what enters the pipeline. Suggested starting queries are listed in `references/sectors.md`.
- For a quieter digest, raise the bar so only HIGH items are included.
- Run the digest on any schedule your tooling supports. Two runs a day is a reasonable default; one is enough for most people.
