# Tiers, gate points, and log schema

## Tiers

Assign by workflow type. Replace the examples with your own workflows.

| Tier | Typical workflows | Handling |
| --- | --- | --- |
| 0 | Daily news digests, link roundups, source lists | Skip scoring. Run the lint stage only. |
| 1 | Weekly summaries, sector reports, market maps, meeting notes | Score and log. Threshold 0.90. Warn, never block. |
| 2 | Investment memos, due-diligence reports, one-pagers, anything sent externally or filed in a system of record | Full pipeline. Threshold 0.95. Block below threshold. |

New workflows default to Tier 2. A workflow that states its own tier in its instructions overrides the default.

## Gate points

1. **First gate (Tier 1 and 2, required).** The producing workflow includes the scoring step in its own procedure. For Tier 1 this is the only guarantee it runs, so it must be written as required.
2. **Second gate (Tier 2 only).** The send or filing step checks the log for a passing record for that document. If none exists, stop and ask the owner before proceeding. Unattended scheduled sends should only carry Tier 0 or Tier 1 content.

Roll out second gates in order of impact, starting with the step that files records.

## Log schema

`ledger.jsonl`, one JSON record per line, two record types.

Verification record, one per run:

```json
{
  "record_type": "verification",
  "ts": "2026-01-15T18:03:00Z",
  "entity": "Example Robotics",
  "skill": "diligence-report",
  "skill_version": "2.1",
  "tier": 2,
  "score": 0.94,
  "verified": 18, "unsupported": 1, "contradicted": 1, "synthesis": 4,
  "blocked": false,
  "high_materiality_claims": [
    {"text": "Series B of $22M led by Example Capital", "category": "VERIFIED"}
  ]
}
```

Only high-materiality claims are stored. This keeps the file small and keeps the sweep focused on claims that matter.

Pattern record, only when a repeated mistake is caught:

```json
{
  "record_type": "pattern",
  "ts": "2026-01-15T18:10:00Z",
  "skill": "diligence-report",
  "pattern": "Cites profile URLs that do not exist",
  "source_entity": "Example Robotics"
}
```

Patterns attach to the workflow, not the entity, because they describe a habit of the workflow.
