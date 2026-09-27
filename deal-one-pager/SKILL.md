---
name: deal-one-pager
description: Turns web research and an optional meeting transcript into a one-page company introduction for a pipeline or investment-committee meeting, with every fact tied to a source in a claims ledger. Use it when a new deal joins a pipeline agenda or a shareable company summary is needed.
---

# Deal One-Pager

A structured company introduction prepared before a meeting or when a deal enters the pipeline. The structure is fixed. The main goal is to block date and people errors and to keep every claim traceable.

Difference from meeting notes: notes are an after-the-fact record that reproduces the transcript. The one-pager is a forward-looking, shareable summary.

Principles:
- Length: one to one and a half Letter pages, with room to breathe.
- Language: English, concise prose mixed with bullets.
- Every figure has a source or a "(Company-stated)" tag. Never invent numbers.
- Convert relative dates ("this summer", "next year") to absolute years using the meeting date.
- Drop any person whose information was last verified more than two years ago, except co-founders.
- Source-locked writing: a factual claim not in the ledger cannot appear. If it cannot be sourced, omit it.

## Step 0: inputs

Required: company name and meeting date. Without the meeting date, stop and ask for it, because date checks depend on it.
Optional: transcript or meeting notes, sector hint.

## Step 1: research and claims ledger

Sources beyond the usual company materials: founder profiles (recent roles, current employment confirmed), funding announcements (prefer the last six months), and official customer or partner announcements. If a transcript exists, extract every figure and date said aloud, flag every relative date, and confirm titles and names against a current public profile.

Record every factual claim in a ledger before writing:

```
| ID | Claim (original wording, no strength change) | Source | Source date | Note |
|----|----------------------------------------------|--------|-------------|------|
| S1 | Series A of $30M closed 2025-11               | press URL | 2025-11 | |
| S2 | "We're in discussions with two large buyers"  | transcript 12:40 | meeting date | discussions, not a contract |
| S3 | CEO Jane Doe, formerly on a battery team      | profile URL | confirmed 2026-05 | current role confirmed |
```

Ledger rules:
- Preserve the strength of the source. "In discussions" never becomes "partnership".
- Company statements get a "(Company-stated)" note.
- Person information older than two years is marked [STALE] and cannot be used.
- Relative dates are converted to absolute years, with the original wording kept in the note.

## Step 2: outline check

Before drafting, list the planned sections with counts: number of pain points, the one-line value proposition, number of process steps, number of funding rounds and the total, which people are included and the source year, and the year range of milestones. Also list ledger size, date conversions, and people kept or removed. Get approval if a reviewer is involved.

## Step 3: draft

Every fact (figure, date, person, contract, technical spec) must come from the ledger. If a needed fact is missing, either go back to Step 1 or omit it. Do not mix interpretation with fact in one sentence.

Fixed structure:

```
Title: Company Name
Subtitle: one-line tagline in italics
Meta row: HQ | Founded | Stage | Website
1. Market Pain Points
2. Solution
3. How It Works
4. Funding
5. Founders & Key Team
6. Key Milestones to Watch
Footer: "Prepared by <your organization> | Sources: ..."
```

- **Pain points**: three to five plain bullets. Structural problems with concrete numbers or examples. No generalities such as "X is a growing market".
- **Solution**: one or two sentences with the company name in bold, then three to five bullets in the form "**Label**: description". Separate revenue streams, customer segments, and deployment models if they exist.
- **How it works**: bullets in order (input, process, output). Explain jargon in brackets.
- **Funding**: total raised on the first line, then rounds with amount, date, and main investors. Offtake or revenue agreements in their own bullet, at the ledger's strength (discussion is not a signed contract).
- **Founders**: co-founders only by default. Others only if the transcript confirms them. Never use [STALE] people. Format: "**Name, title**: prior affiliation and one line of relevant experience".
- **Milestones**: "**Year or quarter**: milestone". Absolute dates only. Add "(Company-stated)" where applicable.

Format: Calibri. Title 18 pt bold, left aligned. Subtitle 11 pt italic. Meta row 9.5 pt with bold labels. Section headers 11 pt bold with a thin bottom border. Bullets 10 pt, round bullet, hanging indent, small spacing. Footer 8 pt italic gray with a top border. Letter paper, 0.75 inch margins. Wrap document generation in error handling and check that the output directory exists.

File name: `<Company Name> One Pager.docx`.

## Step 4: independent verification (required)

Do not self-review. Hand the document to a reviewer with no drafting history, together with the ledger, the transcript if any, the source URLs, and the meeting date.

1. **Mechanical lint**: relative date expressions, unsourced figures, presence of all six sections and the footer.
2. **Fresh-context check**: re-ground each claim against the ledger and sources. Re-confirm people against a current public profile, re-fetch cited URLs, and look for drift in wording strength.
3. **Fail-closed merge**: fix contradicted claims, delete unsupported ones by default, separate interpretation from fact, then lint again.

Allow at most two rework loops. If issues remain, stop and report them. For documents with many contract or partnership claims, use a stronger model for the reviewer.

Final message on success: company name, number of claims verified, counts of confirmed, corrected, removed, and kept-as-unverified claims, date conversions made, and people removed. On failure: the unresolved items, and stop.
