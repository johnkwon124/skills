# Sectors and Relevance Criteria

Example sector set for the digest. Replace or trim to fit your own focus. Each sector lists what counts as HIGH, what counts as MEDIUM, and what to skip.

## Suggested alert queries

- Funding: `"Series A" OR "Series B" OR "Series C" startup funding`
- AI: `AI startup funding OR AI infrastructure`
- Energy: `energy startup OR cleantech OR hydrogen OR energy storage`
- Data center: `data center cooling OR GPU cluster OR AI infrastructure`
- Semiconductors: `semiconductor funding OR chip design OR custom silicon`

## 1. VC and Startup Funding

- HIGH: priced rounds from Series A onward, new fund closes, LP trends that affect fundraising, exits and acquisitions of venture-backed companies, a new institutional investor entering a sector, secondary market or down-round signals.
- MEDIUM: angel and seed announcements, corporate venture arms making a first move, market trend pieces with data, individual investor moves.
- Skip: founder profiles with no funding news, firm rebrands, office openings, thought leadership without data.

## 2. AI and ML

- HIGH: foundation model releases, inference optimization, AI chip announcements, funding for AI infrastructure (compute, data, training platforms), regulation that changes market access, enterprise applications with a defensible moat, acquisitions of AI teams.
- MEDIUM: AI-enabled SaaS tools, robotics or autonomy with new funding, ML tooling, regulatory discussion, academic results with no product yet.
- Skip: "AI comes to industry X" op-eds, consumer app updates, usage statistics, ethics debates with no business or regulatory effect.

## 3. Energy and Cleantech

- HIGH: long-duration storage, hydrogen production and infrastructure, grid modernization and distributed energy controls, nuclear (small modular reactors, fusion progress), sustainable fuels, carbon capture with a plausible commercial path, AI for energy efficiency and forecasting.
- MEDIUM: solar and wind efficiency, EV charging, building efficiency, general energy startup funding, climate policy announcements, corporate renewable commitments.
- Skip: EV consumer news without a charging or grid angle, climate op-eds without a business angle, plain deployment statistics.

## 4. Data Center and Infrastructure

- HIGH: GPU and accelerator supply news, data center cooling (liquid, immersion), specialized AI compute, AI networking, data center power supply and power purchase agreements, AI hosting capacity.
- MEDIUM: general expansion announcements, server refresh cycles, data center energy efficiency, process node improvements, non-AI networking.
- Skip: generic cloud capacity news, real estate deals, telecom infrastructure, IT procurement trends.

## 5. Semiconductors

- HIGH: AI-specific chips, process node and yield advances, fab expansions, custom silicon success stories, supply signals that affect AI infrastructure, RISC-V momentum, advanced packaging and chiplets.
- MEDIUM: memory developments, industry M&A, fab R&D announcements, geopolitical chip news.
- Skip: broad market analysis, non-technology chip applications, retrospectives.

## Sector decision tree

1. Is it about a startup, a fund, or an investment? Funding sector.
2. Is it about AI or ML models and applications? AI sector.
3. Is it about clean energy, storage, grid, or hydrogen? Energy sector.
4. Is it about data centers, compute, cooling, or GPUs? Data center sector.
5. Is it about chips or chip design? Semiconductor sector.
6. Otherwise, skip.

An item that fits both Funding and a topical sector goes in the topical sector, with the round noted in the summary. Use the Funding section for deal news that is not tied to a sector above.

## Worked examples (fictional)

- "Acme Grid raises Series B for long-duration storage." Energy sector, HIGH (long-duration storage, priced round).
- "Example Charge expands its network to more stations." Energy sector, MEDIUM (adjacent, not deep technology).
- "Sample Silicon announces a Series D for an AI accelerator." Semiconductor sector, HIGH; cross-reference to AI.
- "A large cloud provider opens data centers in new regions." Data center sector, MEDIUM (capacity news, not AI-specific).
- "New AI spreadsheet app launches." Skip (generic software, no funding or infrastructure angle).
