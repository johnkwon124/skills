---
name: conference-report
description: For a conference you just attended, assembles a DOCX report covering sector theme diagnosis, session deep dives with analysis, briefs for sessions missed, meeting cards for startups and investors met, and a conclusion with investment implications. Use it whenever an internal write-up of a conference is needed.
---

# Conference Report

## Overview

The report gives analysis, not a relay of what speakers said. Each session gets a critical read.

Tone: write as the attendee, in first-person observation. It should read like notes from someone who was in the room, not a third-party summary. Avoid uniform closers such as "it appears that" or "it is assessed that". Use plain personal phrasing: "What struck me was...", "I came away thinking...", "The most concrete story came from...". Keep the register professional. No slang, no emoji.

The first-person voice must not distort facts. Do not flip a speaker's meaning to sound natural. If two remarks may or may not come from the same person, keep that uncertainty in the sentence.

Load input files one type at a time, not all at once. Respect the web search caps below.

## Report structure

| Part | Title | Content | Omit when |
|------|-------|---------|-----------|
| I | Sector Theme Diagnosis | Direction of the sector as seen at the conference, investment lens | Never |
| II | Session Deep Dive | Sessions attended: recap, gap fill, analytical insight | No sessions attended |
| III | Sessions Not Attended | Key message and recent developments | None to cover |
| IV | Meeting Notes | Cards for startups and investors met | No meetings |
| V | Conclusion | Investment implications, follow-ups | Never |

Length has no fixed target. A rough guide: 1.5 pages per attended session, 2 pages for Part I, half a page per meeting, 1 page for Part V.

If the user asks to drop a part (not-attended sessions, follow-up actions, long-term watch points, a priority column), follow the request. Renumber later parts. The structure is a default, not a requirement.

## Web search caps

| Section | Purpose | Cap |
|---------|---------|-----|
| Part II | Verify uncertain claims, fill background | 2 per session |
| Part III | Last 12 months of developments on the topic | 1 per session |
| Part IV | Funding status, investor portfolio | 1 per meeting |
| Parts I and V | Synthesis of what is collected | none |
| Total | | sessions x 2 + meetings x 1 + 5 |

## Phase 0: Inputs

Ask only for what is missing:
- Conference name, dates, location.
- Organization name and attendee name and title for the header, if the user wants them shown.
- Report language (default English).
- Workspace folder.

List the files and ask the user to assign each a type:
- A: transcript of a session attended (Part II)
- B: notes on a session not attended (Part III)
- C: meeting notes with investors or startups (Part IV)
- D: agenda or reference (Parts I and III)
- E: exclude

Also ask for the list of startups and investors met, and which companies are already tracked or held (mark these on their cards). Do not read files until types are confirmed.

## Phase 1: Read files

Read by type, one file once. Use python-docx for DOCX and a PDF text extractor for PDFs. Do not re-read a file.

## Phase 2: Content

### Part I: Sector Theme Diagnosis
Use only what you already collected. Cover:
- The direction the conference signals for the sector (1 to 2 pages).
- Three to five recurring themes, each with evidence.
- What changed from last year, if agenda data allows.
- Investment implications: where attention is concentrating.

### Part II: Session Deep Dive
Three blocks per session.

**Session Recap.** Follow the session's logic, not a list. Cover the speaker's main claims, data and cases shown, and the useful Q&A. Refer to speakers by name with a natural verb ("Ms. Lee argued that...").

**Gap Fill.** Only when needed. Use web search (max 2) for weak or unsupported claims and missing background. Cite the source. If search contradicts the speaker, show both.

**Analytical Insight.** A critical assessment from an investor's view:
- Strengths and weaknesses of the argument.
- Gaps between the claim and market reality.
- Points or risks worth watching.
- How the session connects to the sector direction.

Stay objective and avoid loaded adjectives. Mark inference as inference ("this suggests", "one possible reading"). Objectivity of the basis and the personal voice of the delivery do not conflict.

### Part III: Sessions Not Attended
For each session: title and speaker from the agenda, a summary of the last year's key developments (one search), and one or two sentences on why it matters to an investor. Stick to sourced facts. No speculation about what was said.

### Part IV: Meeting Notes
Startup card fields: CEO (name and background), Core Technology, Differentiation, Funding (round, amount, year, lead), Investors, Discussion, Next Step. Add a marker on the card if the company is already tracked or held.

Investor card fields: Firm, contact and title, one line with AUM or size, stage, focus, recent portfolio, Discussion, Next step.

One search per card at most, for funding or portfolio confirmation. Remove any field with no public data. No placeholders.

For companies seen only at booths or exhibits, replace cards with a short table: company, what it does, funding status, fit with your focus. Do not add priority rankings unless the user asks. Work priorities into the conclusion in prose.

If you keep a deal list or CRM, check exhibitor names against it and leave out companies that already have an exact-match record.

### Part V: Conclusion
Use only what you collected. Cover investment implications by sector, near-term follow-ups (meetings, further review), and longer-term watch points. Follow-ups and watch points can be dropped on request.

## Phase 3: Structure gate

Before writing content, show the user the planned structure and wait for approval:

```
Conference: [name]
Parts: I (about 2 pages); II ([N] sessions); III ([N] sessions); IV ([N] startups, [N] investors); V (about 1 page)
Omitted: [none / list]
Estimated length: [N] pages | Language: [English]
```

Revise if asked. Do not generate the DOCX before approval.

## Phase 4: Build the DOCX

Use the `docx` npm package, or python-docx if you prefer. Define helpers once: h1 to h4, body, bullet, callout, startup card, investor card, page setup. Insert real paths. Leave no placeholder paths in the final script.

Common errors:

| Error | Cause | Fix |
|-------|-------|-----|
| `Cannot read properties of undefined (reading 'cells')` | An undefined array element (double comma) | Remove the double comma |
| `SyntaxError: Unexpected identifier` | Apostrophe inside a single-quoted string | Use double quotes |
| Broken shading | Package version | Use `ShadingType.CLEAR` |
| Unstable table width | Percentage widths | Use `WidthType.DXA` |

Check syntax before running (`node --check script.js`).

## Phase 5: Verification

### 5-A. Page estimate
Extract text from the DOCX and estimate pages as characters divided by about 2,500. Report the count of tables and non-empty paragraphs.

### 5-B. Mechanical scan
Search the DOCX text for banned phrases and count hits: "transcript", "the speaker said", "as an AI", "this report", "groundbreaking", "revolutionary". Count em dash characters. All counts must be zero.

### 5-C. Independent check
The author of the report should not be the only verifier. Have a separate pass, ideally a fresh-context reviewer, that receives only the report and the raw sources (transcripts, notes, cited URLs) plus the conference date. It re-grounds claim by claim:
1. People. Re-check speaker names, titles, and affiliations against the conference site, company pages, or professional profiles. Watch for speech-to-text distortions of names.
2. Numbers. Each must be traceable to a primary source, clearly attributed to a speaker, or deleted. Recheck quotes of institutions (energy agencies, consultancies, banks) against the actual publication.
3. Source conflicts. Where a speaker and a web source disagree, both should appear.
4. Paraphrase drift. Speaker statements must not be strengthened ("under discussion" to "decided"). The first-person rewrite must not reverse a speaker's meaning.
5. Speaker identity. When transcripts label speakers only by number, do not merge different remarks into one person. If unsure, say it is unclear whether they are the same person.

Merge findings fail-closed: unverified claims are removed or flagged. Rerun 5-A afterward. Loop at most twice, then stop and report what is unresolved.

## Writing principles

1. No placeholders. Remove any item you cannot confirm.
2. Numbers need public sources and citations.
3. Objective tone with no loaded adjectives.
4. Mark inference as inference.
5. Use the confirmed report language (English by default).
6. Each part reads on its own.
7. Insight is required. Close each session with one or two sentences of critical comment.
8. Keep the personal observation tone from the Overview.

### Style and banned phrases
- Target a low AI-detection score: plain English, no ornate adjectives. Do not start every paragraph the same way ("First...", "Second...", "Finally..."). Mix short and long sentences.
- Do not refer to the source material: "according to the transcript", "based on the recording", "from the audio".
- No AI self-reference: "this report was generated", "as an AI", "based on the input provided".
- No meta-narration: "in this section we will discuss", "this report covers".
- No cliches: "in today's rapidly evolving landscape", "navigating complexity".
- No hype: "groundbreaking", "game-changing", "revolutionary".
- No em dashes. Use commas, periods, or parentheses.
- Give numbers context ("a 40 GW build-out, about forty reactors of 1 GW each").

## Quick recap mode

If the user asks for a "quick recap", "short version", or "2 to 3 pages", skip the structure gate and use one flow: Sector Takeaway, Session Briefs, Implications. Each session is one paragraph of 80 to 120 words with a one-line critical remark. The search cap is one per session. Tone rules and Phase 5 checks still apply.

## Checklist

- [ ] Files typed and confirmed before reading
- [ ] Meeting list and tracked companies confirmed
- [ ] Files read once, by type
- [ ] Search caps respected
- [ ] Structure approved (skip for quick recap)
- [ ] Real paths in script, syntax check passed
- [ ] Page estimate done
- [ ] Mechanical scan clean, independent check done
- [ ] Tone check: banned phrases zero, first-person observation voice present
- [ ] File saved in the workspace
