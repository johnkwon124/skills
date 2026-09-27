#!/usr/bin/env python3
"""Verification audit log (JSON Lines): append, lookup, patterns, sweep.

The log is a plain local file. Keeping it somewhere that persists between
sessions, and fetching the latest copy before appending, is the caller's job.

Subcommands (all take --ledger PATH):
  append           add one verification record
  lookup           past high-materiality claims for an entity
  flag-pattern     log a repeated, workflow-level mistake
  lookup-patterns  list logged patterns for a workflow
  sweep            group claims by entity, show score trend per workflow,
                   list open patterns. Does not auto-judge anything.
"""
import json, argparse, datetime
from collections import defaultdict


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_records(path, record_type):
    try:
        with open(path, encoding="utf-8") as f:
            rows = [json.loads(line) for line in f if line.strip()]
    except FileNotFoundError:
        return []
    return [r for r in rows if r.get("record_type", "verification") == record_type]


def write(path, record):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(json.dumps({"appended": True, "record": record}, ensure_ascii=False, indent=2))


def cmd_append(a):
    high = []
    if a.claims:
        with open(a.claims, encoding="utf-8") as f:
            high = [{"text": c.get("text", ""), "category": c.get("category", "")}
                    for c in json.load(f) if c.get("materiality") == "high"]
    write(a.ledger, {
        "record_type": "verification", "ts": now(), "entity": a.entity,
        "skill": a.skill, "skill_version": a.skill_version, "tier": a.tier,
        "score": a.score, "verified": a.verified, "unsupported": a.unsupported,
        "contradicted": a.contradicted, "synthesis": a.synthesis,
        "blocked": a.blocked.lower() == "true", "high_materiality_claims": high})


def cmd_lookup(a):
    rows = [r for r in read_records(a.ledger, "verification")
            if r.get("entity", "").strip().lower() == a.entity.strip().lower()]
    rows.sort(key=lambda r: r.get("ts", ""))
    print(json.dumps({"entity": a.entity, "prior_records": rows}, ensure_ascii=False, indent=2))


def cmd_flag_pattern(a):
    write(a.ledger, {"record_type": "pattern", "ts": now(), "skill": a.skill,
                     "pattern": a.pattern, "source_entity": a.entity})


def cmd_lookup_patterns(a):
    rows = [r for r in read_records(a.ledger, "pattern")
            if r.get("skill", "").strip().lower() == a.skill.strip().lower()]
    rows.sort(key=lambda r: r.get("ts", ""))
    print(json.dumps({"skill": a.skill, "prior_patterns": rows}, ensure_ascii=False, indent=2))


def cmd_sweep(a):
    ver = read_records(a.ledger, "verification")
    pats = read_records(a.ledger, "pattern")

    # 1. entities that appear in more than one run, for human contradiction review
    by_entity = defaultdict(list)
    runs = defaultdict(int)
    for r in ver:
        e = r.get("entity", "(unknown)")
        runs[e] += 1
        for c in r.get("high_materiality_claims", []):
            by_entity[e].append({"ts": r.get("ts"), "skill": r.get("skill"),
                                 "text": c.get("text"), "category": c.get("category")})
    flagged = {e: items for e, items in by_entity.items() if runs[e] > 1}

    # 2. score trend per workflow, in time order
    by_skill = defaultdict(list)
    for r in ver:
        if r.get("score") is not None:
            by_skill[r.get("skill", "(unknown)")].append(
                {"ts": r.get("ts"), "skill_version": r.get("skill_version"), "score": r.get("score")})
    trend = {}
    for skill, pts in by_skill.items():
        pts.sort(key=lambda p: p["ts"])
        s = [p["score"] for p in pts]
        direction = "flat_or_single_run"
        if len(s) > 1 and s[-1] > s[0]:
            direction = "improving"
        elif len(s) > 1 and s[-1] < s[0]:
            direction = "declining"
        trend[skill] = {"runs": len(s), "latest_score": s[-1],
                        "avg_score": round(sum(s) / len(s), 4),
                        "trend": direction, "history": pts}

    # 3. patterns logged and not yet closed by a person
    open_patterns = defaultdict(list)
    for r in pats:
        open_patterns[r.get("skill", "(unknown)")].append(
            {"ts": r.get("ts"), "pattern": r.get("pattern"), "source_entity": r.get("source_entity")})

    print(json.dumps({"entities_reviewed": len(by_entity),
                      "flagged_for_human_review": flagged,
                      "score_trend_by_skill": trend,
                      "open_patterns_by_skill": dict(open_patterns)},
                     ensure_ascii=False, indent=2))


def main():
    # --ledger is defined on a shared parent so it can follow the subcommand
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--ledger", required=True)
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("append", parents=[common])
    p.add_argument("--entity", required=True)
    p.add_argument("--skill", required=True)
    p.add_argument("--skill-version", default="unknown")
    p.add_argument("--tier", type=int, required=True)
    p.add_argument("--score", type=float, required=True)
    for k in ("verified", "unsupported", "contradicted", "synthesis"):
        p.add_argument(f"--{k}", type=int, default=0)
    p.add_argument("--blocked", default="false")
    p.add_argument("--claims", default=None)
    p.set_defaults(func=cmd_append)

    p = sub.add_parser("lookup", parents=[common])
    p.add_argument("--entity", required=True)
    p.set_defaults(func=cmd_lookup)

    p = sub.add_parser("flag-pattern", parents=[common])
    p.add_argument("--skill", required=True)
    p.add_argument("--pattern", required=True)
    p.add_argument("--entity", default=None)
    p.set_defaults(func=cmd_flag_pattern)

    p = sub.add_parser("lookup-patterns", parents=[common])
    p.add_argument("--skill", required=True)
    p.set_defaults(func=cmd_lookup_patterns)

    p = sub.add_parser("sweep", parents=[common])
    p.set_defaults(func=cmd_sweep)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
