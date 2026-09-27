---
name: weak-signal-scanner
description: Watches non-mainstream sources, such as preprints, open-source trending lists, technical forums, niche newsletters, new-fund first bets, accelerator batches, and technical conference papers, for early signals that mainstream news does not cover, and returns a scored digest. Use it when asked for weak signals, an off-mainstream scan, or emerging technology and venture signals.
---

# Weak Signal Scanner

## Purpose

Find out what you do not already know. The measure of success is breadth of coverage and share of non-mainstream sources. A signal that a mainstream news or portfolio-monitoring workflow already covers counts as noise.

Output: a digest in the reply (or saved to a file if the user asks). Run it on whatever cadence suits the user, for example weekly.

## Sources

Use these only. Skip mainstream financial and technology press and the main pages of venture firm blogs.

| Source | Type | How to access | Minimum searches |
|--------|------|---------------|------------------|
| arXiv (AI, distributed computing, hardware architecture, systems and control categories) | Papers | Papers from the last 7 days with a burst of citations or bookmarks | 2 |
| GitHub Trending | Open source | Weekly trending repos filtered to your focus topics | 2 |
| Hacker News | Community | Threads with 500+ points where founders or researchers comment | 2 |
| New-fund first bets | Investment pattern | New portfolio companies of funds launched in the last one to two years | 2 |
| Niche newsletters | Sector-specific | Newsletters in your focus fields | 2 |
| Accelerator batches | Startups | Latest cohort announcements and patterns | 1 |
| Technical conference papers | Academic | Recently accepted or spotlighted papers at major ML, systems, networking, circuits, and open-hardware conferences | 1 |

Run at least 12 web searches in total. You may shift counts between sources as long as each minimum holds.

## Workflow

### Phase 1: Baseline for repeat detection

If the user provides the previous one or two digests, extract their keywords, company names, and technology names. This list is the baseline for Phase 4. If no earlier digests are available, skip repeat tagging.

### Phase 2: Scan

Search each source. Example queries:

- `arXiv trending papers this week citations distributed computing`
- `arXiv new papers power inference hardware <year>`
- `GitHub trending repositories machine learning infrastructure this week`
- `GitHub trending <your topic> repositories week`
- `Hacker News top posts <your topic> 500 points`
- `Hacker News Show HN <your topic> <year>`
- `<newly launched fund> new portfolio company <year>`
- `<niche newsletter> highlights this week`
- `accelerator batch <year> <your sector> startups`
- `<conference> <year> accepted papers spotlight`

Keep a signal only if it passes these tests:
- Mainstream outlets have not already covered it.
- It names a company, paper, or repository that is not widely known.
- A well-regarded investor placed a first public bet on it.
- Interest in the topic is rising suddenly in technical communities.

### Phase 3: Curate and score

Group the signals into 5 to 10 items across these categories:
Use categories that match your own focus areas. Example set:
- Software and AI
- Hardware and semiconductors
- Energy and infrastructure
- Venture signal (new-fund bets, partner reactions)
- Research front (papers, repositories)

Score each signal:

| Intensity | Criteria |
|-----------|----------|
| HIGH | Appears in several non-mainstream sources at once, or a top-tier investor's first public bet |
| MED | One source, but the technical impact is clear |
| LOW | Reference only, still early |

### Phase 4: Repeat tagging

Compare each item to the baseline keywords from Phase 1. Tag anything that also appeared before as REPEAT. Repeats are candidates for a deeper thematic write-up.

### Phase 5: Digest

Format:

```
WEAK SIGNAL DIGEST | <date>

[Software / AI]
- HIGH: <one-line description> [#SoftwareAI] | <source or link>
- MED: <one-line description> [#DevTools] | <source or link>

[Energy / Infrastructure]
- MED: <one-line description> [#EnergyInfra] | <source or link>

[Research Front]
- LOW: <one-line description> [#Research] | <source or link>

REPEATS (candidates for a deeper theme write-up):
- <keyword or topic that appeared again>
```

Deliver it in the reply. If the user wants it sent somewhere, use their own email or messaging tool after they approve.

## Boundaries

This scanner covers unknown companies, papers, and technologies. It does not replace mainstream news curation, monitoring of companies you already know, deep theme analysis, or single-company research. Repeated signals from this scanner can feed a theme analysis.

## Checklist

1. If prior digests are provided, extract their keywords.
2. Run at least 12 searches across the sources.
3. Select 5 to 10 signals and score each.
4. Tag repeats against the baseline.
5. Write the digest in the format above.

## Error handling

- Prior digests unavailable: skip repeat tagging and continue.
- Fewer than 5 signals: add two or three queries and retry. If still short, deliver what you have and say so.

## Notes

- Spend effort on search and curation, not on collecting raw text.
- With a short cadence, favor speed and breadth over completeness.
