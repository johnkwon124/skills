# Skills for venture investing workflows

A set of reusable skills for research, deal evaluation, meetings, monitoring and writing. Each folder holds a `SKILL.md` with the instructions, plus optional `references/` and `scripts/`. They are written to be tool-agnostic. Adapt the inputs, sources and output formats to your own setup.

All examples use fictional companies. Figures in the templates are placeholders, not data.

## Research and reports

- [`sector-deep-dive-report`](./sector-deep-dive-report): Covers an entire investment sector or technology, from pain point through competitive landscape, market conditions, regulation, key players, risks, and conclusion.
- [`sector-market-map`](./sector-market-map): Scores startups across an investment sector on investors, founders, and partnerships, then outputs a workbook and a sector overview report.
- [`theme-memo-writer`](./theme-memo-writer): A short, issue-driven memo on one theme, technical inflection, or open debate, built around competing hypotheses and ending in a watch list.
- [`research-topic-scanner`](./research-topic-scanner): Reviews recent reading and signal sources on a daily or weekly schedule, scores topic candidates, and returns a ranked shortlist of about ten deep-research topics with rationale and supporting company facts.
- [`weak-signal-scanner`](./weak-signal-scanner): Watches non-mainstream sources, such as preprints, open-source trending lists, technical forums, niche newsletters, new-fund first bets, accelerator batches, and technical conference papers, for early signals that mainstream news does not cover, and returns a scored digest.

## Deal evaluation

- [`deeptech-pitch-memo`](./deeptech-pitch-memo): An early-stage investment memo on a single company or a single technology bet, built through a research pass, a writer pass, and a question-and-answer loop between the two.
- [`pre-diligence-report`](./pre-diligence-report): Written just before formal diligence, this report covers a single company in depth, with footnoted sources, a SWOT, funding and deal dynamics, structural debates framed as competing hypotheses, and a diligence checklist.
- [`deal-one-pager`](./deal-one-pager): Turns web research and an optional meeting transcript into a one-page company introduction for a pipeline or investment-committee meeting, with every fact tied to a source in a claims ledger.
- [`startup-screening-scorecard`](./startup-screening-scorecard): Rates one startup or a batch of startups on a 100-point rubric (investor quality, founding team, notable backers, strategic fit, traction), assigns an A-to-D grade, and recommends a next action.
- [`pitch-day-sourcing`](./pitch-day-sourcing): Extracts the startup list from a shared pitch-day or demo-day deck link, enriches each company with web research, filters by target region, and ranks them into priority tiers against your investment focus before writing a formatted Excel sourcing list.

## Meetings

- [`investor-meeting-notes`](./investor-meeting-notes): Converts a meeting transcript, raw notes, or just a company name into an analytical meeting note, covering four meeting types, a first startup meeting, a startup follow-up, an investor or LP meeting, and a conference session.
- [`conference-report`](./conference-report): For a conference you just attended, assembles a DOCX report covering sector theme diagnosis, session deep dives with analysis, briefs for sessions missed, meeting cards for startups and investors met, and a conclusion with investment implications.
- [`web-transcript-extractor-otter`](./web-transcript-extractor-otter): Pulls the full raw transcript of an otter.ai recording using browser automation and saves it as a .txt file in a local scratch folder.
- [`web-transcript-extractor-soniox`](./web-transcript-extractor-soniox): Pulls the full raw transcript of a Soniox recording, from either the Smart Scribe (standard) or Translator (bilingual, live-translated) list, via the Soniox web or desktop app, and saves it as a .txt file in the local Downloads folder.

## News and monitoring

- [`weekly-vc-news-curation`](./weekly-vc-news-curation): Scans five tiers of public sources across three configurable focus areas, selects the top items per sector, and produces a table document plus short insight notes for the items you pick.
- [`vc-news-digest`](./vc-news-digest): Sorts items from Google Alerts and similar feeds by sector, flags relevance as HIGH or MEDIUM, and delivers one daily or twice-daily digest email, optionally in a second language.
- [`daily-tech-news-digest`](./daily-tech-news-digest): Assembles a daily, sector-first tech news digest as a styled HTML email, with curated sources, per-item investment insight, a funding table, and a pre-send QA gate.
- [`youtube-channel-monitor`](./youtube-channel-monitor): Follows chosen YouTube channels through their RSS feeds and tracks people or keywords through search, then writes a report for each new video with a summary, glossary, fact-check, and investment angle.

## Writing and email

- [`newsletter-writing-workflow`](./newsletter-writing-workflow): Handles topic selection, first drafts, reviewer feedback, and a pre-publish check for a personal analytic newsletter.
- [`newsletter-draft-writer`](./newsletter-draft-writer): Moves a finished markdown post into a newsletter platform's web editor and saves it as a draft, never published.
- [`professional-email-drafting`](./professional-email-drafting): Drafts strategic emails and short messages for a senior investor, such as founder outreach, investor updates, replies, and introductions.
- [`email-attachment-send-checklist`](./email-attachment-send-checklist): Runs a pre-send checklist for an email with attachments, confirming recipient, subject, body and files before it goes out.
- [`sourcing-summary-email`](./sourcing-summary-email): Compiles meeting notes on recently sourced startups into a five-bullet-per-company summary email draft for a team.

## Quality and tooling

- [`document-fact-gate`](./document-fact-gate): Puts a document (docx, md, or txt) through a four-stage fact-check pipeline, covering mechanical lint, fresh-context claim verification, fail-closed merge, and a writing-standard gate.
- [`deliverable-trust-scoring`](./deliverable-trust-scoring): Layers tiered verification gates, a document-level confidence score, a persistent verification audit log, and a periodic consistency sweep on top of a fact-check pipeline.
- [`skill-token-audit`](./skill-token-audit): Flags token cost and quality problems in a library of skill files (SKILL.md), such as unclear triggers, dead references, duplicated guidance, and over-built agent chains.
- [`skill-packager`](./skill-packager): Checks a skill folder and packages it as a versioned zip, with a single top-level folder, an updated changelog, and its references.
