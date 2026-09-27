---
name: investor-meeting-notes
description: Converts a meeting transcript, raw notes, or just a company name into an analytical meeting note, covering four meeting types, a first startup meeting, a startup follow-up, an investor or LP meeting, and a conference session. Use it whenever a meeting needs to be written up, summarized, or recorded.
---

# Investor Meeting Notes

## Goal

Produce a meeting note that adds analysis to the record. It should not just relay what was said.

Reader test: someone who has never heard of the company should finish the note knowing what the technology is, how the company makes money, why the problem is solvable, where the company sits among competitors, and how far commercial progress has gone.

Deliverables:
1. An English note as a DOCX file (about 600 to 900 words for a first meeting).
2. A short list of 5 to 8 follow-up questions, shown in chat only.

Do not create PDF or markdown files unless asked.

## Step 0: Pick the meeting type and source mode

Ask for confirmation of both choices before starting.

```
Transcript or notes attached?
  No  -> only a company name: Type A, source mode W
  Yes -> who is on the other side?
         startup, no earlier meeting   -> Type A, source mode T
         startup, earlier meeting      -> Type B (follow-up)
         investor, LP, co-investor     -> Type C
         conference talk or panel      -> Type D
```

Source mode T: a transcript or detailed notes exist. The meeting is the primary source. Web research only checks claims and fills background.
Source mode W: web research only. The note is a research profile.

### Rules for mode T
- Meeting content drives every section. A note that reads like a web profile when a transcript exists has failed.
- State confirmed facts directly. Write "The company has finished the pilot line", not "The founder said they finished it".
- Describe information gaps as gaps: "The test conditions behind that figure were not shared on this call."
- If something was not discussed, say so and fill it from public sources: "Competition did not come up in the meeting. Public sources show..."
- If the meeting and a public source disagree, write both side by side and name the likely cause. Do not quietly pick one.

### Rules for mode W
- Never imply the meeting confirmed anything. Attribute to "company materials" or "public sources".
- Leave thin sections short. Write "Not disclosed" and turn the gap into a follow-up question. Do not pad by restating.
- Separate "nothing public exists" from "I could not find it".

## Step 1: Lock the entity name

Before research, confirm the official name and spelling of the company, person, or fund from an authoritative external source (the company domain or a funding database). Do not trust names in your own earlier notes. If they differ from the external source, use the external one. Check for same-name companies by domain, sector, and investors. Use the locked name everywhere.

## Step 2: Research

Pick 8 to 12 sources by sector. Quality of fit matters more than count.

- Always: company site, a funding database, founder profiles, recent press releases.
- Power and electrical hardware: trade press, market data providers, one or two key patents, two or three competitor sites.
- Software and AI: analyst blogs, developer and industry press, competitor sites, customer partnership announcements.
- Energy and climate: market data providers, government grant databases, reports from international agencies, competitor sites.
- Biotech and medical devices: PubMed, regulatory databases, sector trade press, competitor sites.
- Manufacturing and materials: patents, trade journals, supplier announcements, competitor sites.

Keep a light claims ledger while you research. One line per number or proper noun: claim, value, source, date. In mode T, mark the source as `transcript` or a URL. Anything in the note that is not in the ledger is a defect.

Also run these checks:
- Cross-source names. If the same counterparty appears under different names, decide whether it is a typo, a rebrand, or a separate entity. If you cannot tell, say so in the note and add a follow-up question.
- Stale information. Search for anything newer than the top result on funding stage, leadership, and product status.
- Ownership structure. If the company is an operating subsidiary of a holding company, say so.
- Press-release bias. If all key claims come from the company, look for at least one independent source.
- Units. Recheck kW vs MW, $M vs $B, annual vs quarterly.

## Type A: First startup meeting (eight sections)

The order follows how a newcomer understands a company: problem, technology, money, evidence, competition, judgment.

1. **At a Glance.** Four one-sentence bullets: What, Why now, Stage, Open question. Write them fresh. Do not copy body sentences.
2. **Company Snapshot.** Bullets only: Founded and HQ, Team (headcount, founders, key background), Funding (stage, date, investors, size or "undisclosed"), History (pivots, renames). Add one or two sentences of prose if a pivot needs context.
3. **The Problem.** One or two lead sentences describing the problem without naming the company. Then two to four evidence bullets with numbers and sources. Separate independently documented facts from the company's own claims.
4. **Technology: What It Is and How It Works.** This is the most important section.
   - Lead prose (2 to 3 sentences): what the product physically is and where it is installed.
   - System Components: bullets by layer (hardware, software, AI).
   - Mechanism prose (2 to 4 sentences): the causal chain that explains why the performance claim holds. If you cannot explain the cause, say so.
   - Claimed vs Verified: two bullets per key metric. This is the only place to discuss verification.
   - Manufacturing and Deployment (hardware companies only, only if public).
5. **Business Model and Go-to-Market.** Pricing model, channels, partnerships. If undisclosed, write "Not disclosed", say what is missing, and link it to a follow-up question.
6. **Commercial Traction.** Customers, pilots, letters of intent, revenue signals. If none, write "No customers, pilots, or LOIs have been disclosed (as of [date])". Distinguish "nothing public" from "search was thin".
7. **Competitive Landscape.** One or two sentences defining how many approaches exist. Then bullets grouped by approach: who, what they do, what scale. End with one or two sentences on where the company sits, including any funding gap. Mention the funding gap here only.
8. **Investment View and Key Considerations.** One prose paragraph of four to six sentences: two or three strengths and two or three risks, with evidence. Refer to earlier facts briefly. No recommendation to invest or pass and no next steps.

Sections 5 and 6 are never dropped, even if empty.

## Type B: Startup follow-up

Transcript first. Web search only for flagged claims.

Read the whole transcript and flag: unclear numbers, claims that need checking ("we are the only one"), missing context (a customer named without size or contract), urgent items (M&A, LOIs, deadlines, short runway), and words that may be transcription errors. Search only the flagged items. Mark unverified items "(unconfirmed)".

Structure: title, thin horizontal rule, then topic sections built from the transcript. Typical topics: Product Development, Roadmap, Software or Platform, Customer Pipeline, Commercialization Timeline (by year), Funding (burn, runway, next round). No company overview and no closing paragraph. Start each topic with one sentence on what changed, then plain bullets.

Use red text only for urgent items (acquisition talks, round deadlines, imminent runway problems), at most three bullets per document.

## Type C: Investor or LP meeting

Relationship context matters more than a company pitch.

Research supplements the transcript only: fund size and vintage, public portfolio, the contact's public career, deals in the last 12 months. Flag likely transcription errors in fund names, LP names, family office names, and portfolio company names.

Four sections under a title and a thin rule:
1. **Meeting Context.** Fund, contact and title, size if public, focus sectors, how the meeting came about.
2. **Their Investment Focus.** Current sectors and stages, themes they mentioned. Add a judgment on overlap with your own focus.
3. **Collaboration Signals.** Co-investment interest, specific deals mentioned, willingness to share sourcing or introduce portfolio companies. Judge how warm the relationship is: information exchange or real collaboration.
4. **Follow-up Items.** Agreed next steps, requests made by either side.

Judgments must rest on what was said. No speculation about future collaboration.

## Type D: Conference session

Shortest format, one to two pages. Keep only claims with numbers or cases and Q&A where the speaker gave a concrete answer. Drop generalities and promotion.

Research: confirm speaker identity and affiliation, and find the original source of any quoted report or statistic.

Three sections under a title and a thin rule:
1. **Session Overview.** Conference, session title, speaker name, affiliation, title, date.
2. **Key Points.** Five to seven bullets, each with data or a concrete case. Then one or two sentences on the strongest signal for an investor.
3. **Notable Q&A.** One to three exchanges with real insight. A dodged question is also worth recording.

Speaker names, affiliations, session names, cited reports, and time expressions are the most error-prone items here. Check all of them.

## Writing rules

- Plain, short English. One piece of information per sentence. Mix short (8 to 12 words) and longer (20 to 30 words) sentences.
- Explain jargon once, in a short phrase, at first use.
- Use everyday verbs ("use", "help", "rely on"). Avoid stacked noun phrases.
- Avoid filler words such as "notably", "importantly", "furthermore", "moreover", "cutting-edge", "revolutionary". Avoid runs of -ing clauses. Vary how sentences start.
- Say each key fact once. Reference it later only when adding something new. The At a Glance bullets are the only allowed restatement, and only as fresh compressed wording.
- Each major section opens with one or two prose sentences. Use bullets for lists of facts (specs, numbers, names, milestones) and prose for cause, context, and judgment. No bullet-only sections (except Company Snapshot) and no walls of prose.
- Put analysis in the prose, in the same voice and font as the rest. No labels like "[Insight]" and no separate styling. Do not attach a hedge sentence to every section.
- Delete unsourced or estimated numbers. Delete generalities such as "X is a growing market" unless replaced by a specific figure.
- No investment recommendation and no next steps in the note.
- Keep the author out of the text. No first person and no author name. Where an action by your own side is needed, use "the team" or your firm's neutral name. Named people on the other side keep their names.
- Keep internal signals out: mode names, tool names, review labels, "[UNVERIFIED]", private shorthand from the transcript.

## Follow-up questions (chat only)

Five to eight questions, grouped by type.
- Type A: technology validation, business validation, team and execution, market and competition, funding and exit.
- Type B: milestone verification, customer acquisition, cash position, risks.
- Type C: co-investment potential, information exchange, portfolio collaboration.
- Type D: claim verification, further research, market implications.

Each question must be specific. Avoid "What do you think about...". Include every unverified item from the note.

## DOCX format (fixed values)

- Letter, 1 inch margins. Calibri 11 pt for body, headers, and bullets. Title Calibri bold 13 pt, section headers bold 11 pt, all black. No colored headers.
- Bullets: round bullet character, 0.25 inch indent, 2 pt after. Body line spacing 1.15, 6 pt after. Section header spacing 12 pt before, 4 pt after.
- Type A has no horizontal rule. Types B, C, D have a 0.5 pt rule under the title.
- Bullet styles: bold label then colon for spec facts; bold keyword without colon for technology terms; plain text for everything else.
- Bold the company name once at first mention (Type A).
- File name: `<Company>_Meeting_Notes_<MMDDYYYY>.docx`.

Write the note in markdown first and show it in chat. Then convert the same text to DOCX with a small script (python-docx). Do not write content and layout code in the same step. Give the script a fallback font list and wrap the run in try/except.

## Review before delivery

1. Fact check. Confirm the locked name everywhere. Check titles, fund names, conference names, technical figures, and team names against outside sources. Compare each number to the claims ledger. For transcript-based types, also check for transcription errors: similar-sounding fund names, ordinals that should be numbers ("thirty-second" heard as "32nd"), dropped title prefixes, mangled conference names.
2. Freshness. For any competitor or comparable company, search for financing, valuation, or regulatory news in the six months before the meeting date.
3. Quotes and arithmetic. Direct quotes must match the source word for word. Compute month gaps from dates. Do not mark a paywalled paper as confirmed unless you read it.
4. Consistency. No repeated facts across sections, all required sections present, mode W has no meeting attribution, mode T has no reporting-style attribution ("the founder said...").
5. Render check. Extract text from the saved DOCX and compare it with the approved markdown. Report only what you actually verified.

If a check fails, revise and repeat at most twice. Then stop and report which items failed and why.
