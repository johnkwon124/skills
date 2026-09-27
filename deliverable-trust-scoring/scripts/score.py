#!/usr/bin/env python3
"""Materiality-weighted confidence score. Deterministic, no model.

Score = weight(VERIFIED) / weight(VERIFIED + UNSUPPORTED + CONTRADICTED).
SYNTHESIS claims are excluded. Compute on the ORIGINAL classification,
before any fail-closed merge, so deleting risky claims cannot raise the score.

Usage:
    python3 score.py --claims claims.json [--tier 0|1|2]

claims.json:
    [{"id": "c1", "category": "VERIFIED|UNSUPPORTED|CONTRADICTED|SYNTHESIS",
      "materiality": "high|normal", "text": "..."}]

Always exits 0. The caller acts on the "verdict" field:
not_gated (tier 0 or no scored claims), pass, warn (tier 1 miss), block (tier 2 miss).
"""
import sys, json, argparse

WEIGHTS = {"high": 2, "normal": 1}
THRESHOLDS = {0: None, 1: 0.90, 2: 0.95}
MISS_ACTION = {0: "not_gated", 1: "warn", 2: "block"}


def compute(claims):
    counts = {"VERIFIED": 0, "UNSUPPORTED": 0, "CONTRADICTED": 0, "SYNTHESIS": 0}
    num = den = 0.0
    scored = 0
    high = []
    for c in claims:
        cat = c.get("category", "").upper()
        if cat not in counts:
            continue
        counts[cat] += 1
        if cat == "SYNTHESIS":
            continue
        w = WEIGHTS.get(c.get("materiality", "normal"), 1)
        den += w
        scored += 1
        if cat == "VERIFIED":
            num += w
        if c.get("materiality") == "high":
            high.append({"text": c.get("text", ""), "category": cat})
    score = num / den if den > 0 else None
    return {
        "score": round(score, 4) if score is not None else None,
        "verified": counts["VERIFIED"],
        "unsupported": counts["UNSUPPORTED"],
        "contradicted": counts["CONTRADICTED"],
        "synthesis": counts["SYNTHESIS"],
        "total_scored_claims": scored,
        "high_materiality_claims": high,
        "had_contradiction": counts["CONTRADICTED"] > 0,
    }


def verdict(result, tier):
    threshold = THRESHOLDS.get(tier)
    if threshold is None or result["score"] is None:
        return "not_gated"
    return "pass" if result["score"] >= threshold else MISS_ACTION.get(tier, "block")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", required=True)
    ap.add_argument("--tier", type=int, default=2, choices=[0, 1, 2])
    args = ap.parse_args()
    with open(args.claims, encoding="utf-8") as f:
        claims = json.load(f)
    result = compute(claims)
    result["tier"] = args.tier
    result["threshold"] = THRESHOLDS.get(args.tier)
    result["verdict"] = verdict(result, args.tier)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
