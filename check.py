#!/usr/bin/env python3
"""Sidewalk robot check: SF Public Works Code Sec. 794 as code.

  python3 check.py examples/resident_fail.json            # check one observation
  python3 check.py examples/operator_fail.json operator   # operator pre-flight
  python3 check.py --rules                                # list every rule

An observation is a JSON object of the fields in rules.json. Missing or null = unknown.
"""
import json, sys, pathlib
D = json.loads((pathlib.Path(__file__).parent / "rules.json").read_text())

def ev(c, o):
    """Three-valued: True (complies), False (violation), None (can't tell)."""
    if "any" in c:
        r = [ev(x, o) for x in c["any"]]
        return True if True in r else None if None in r else False
    if "all" in c:
        r = [ev(x, o) for x in c["all"]]
        return False if False in r else None if None in r else True
    v = o.get(c["field"])
    if v is None: return None
    t = c["value"]
    if "plus" in c:
        p = o.get(c["plus"]["field"])
        if p is None: return None
        t += p * c["plus"]["times"]
    return v <= t if c["op"] == "<=" else v >= t if c["op"] == ">=" else v == t

def check(o, mode="resident"):
    rules = [r for r in D["rules"] if r["who"] in (mode, "both")]
    res = [(r, ev(r["check"], o)) for r in rules]
    return ([r for r, x in res if x is False], [r for r, x in res if x is None], len(rules))

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    if sys.argv[1] == "--rules":
        for r in D["rules"]: print(f"{r['id']}  §{r['clause']:<14} {r['who']:<9} {r['title']}")
        sys.exit(print(f"\n{len(D['rules'])} checkable rules from {D['source']}"))
    mode = sys.argv[2] if len(sys.argv) > 2 else "resident"
    fails, unk, n = check(json.loads(pathlib.Path(sys.argv[1]).read_text()), mode)
    print(f"{n} {mode} checks: {n-len(fails)-len(unk)} pass, {len(fails)} fail, {len(unk)} unknown\n")
    for r in fails: print(f"  VIOLATION §{r['clause']} {r['title']}: {r['text']}")
    if unk: print("\n  Could not check: " + ", ".join(f"§{r['clause']}" for r in unk))
    print(("\nNOT ALLOWED. " + ("Report to SF311 (call 311 or sf311.org); call 911 if anyone is hurt." if mode == "resident" else "Fix before testing: citations run up to $1,000 per day per violation.")) if fails else "\nNo violations found.")
    sys.exit(1 if fails else 0)
