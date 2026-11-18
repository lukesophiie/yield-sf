# Submission

## Team card

**Team name:** _(fill in)_

**Statement number:** _(fill in)_

**First names:** Luke, _(add teammates)_

**Statement:** How might we help **San Francisco residents who share narrow sidewalks with delivery robots, especially wheelchair users, people with strollers and older neighbors,** do **a quick check of a robot against the city's own rules** so that **a bad encounter becomes a report with the exact clause attached, sent to the agency that enforces it**? Build idea: **D**. We'll know it worked if **every checkable rule in Public Works Code §794 is a machine-readable test linked to its clause, and a failed test produces a report ready to file with SF311.**

## Six short answers

**1. The concern:** A neighbor on a narrow sidewalk meets a delivery robot moving faster than they walk, with no operator in sight, and has to step off the curb. They don't know whether that is legal or who to tell. San Francisco allows these robots only as permitted tests (3 mph, a human within 30 ft, 3 per permit, 9 citywide, industrial-zoned sidewalks only), but almost nobody knows the rules exist.

**2. What we built,** and the one command that runs it: Yield SF. A Waze-style map of San Francisco: tap where you saw a sidewalk robot, pick what it did, and it is checked against §794, turned into 32 machine-readable rules (`rules.json`), each a testable condition linked to its clause. The map shows the only zones where robots can legally test and the high-injury streets where they never can, and every sighting gets a clause-by-clause verdict and a ready-to-file 311 report. An operator checklist (`checklist.html`) and a command-line checker run on the same rule file.
Run: `python3 check.py examples/resident_fail.json` (or open `index.html`; `python3 check.py --rules` lists every rule).

**How people are rewarded (and why it is hard to game):** a community feedback loop. Posting earns nothing; a sighting earns the reporter +10 points only when 2 or more other people confirm it with enough combined trust (1.5), and correct reviewers earn +2. A confirmed "looks allowed" pays the same as a confirmed violation, so there is no bounty for accusing. Nobody reviews their own sighting, new accounts' reviews count half, a disputed report costs 10 points and 1 trust, only 5 sightings a day can earn, and points are reputation only. Scores are recomputed in the page from the public record. It cannot stop one person running several accounts or a group confirming each other.

**The Sidewalk Fund (proposal, not live):** every permitted operator pays the same flat fee per robot per month into a fund with a public ledger. It pays for running the map, accessibility audits and open incident data, never for individual reports, and paying gives an operator no say over sightings or scores. No money moves through the page and the fee shown is an example; it would need the City to adopt it.

**3. Data we used:** `sf-sidewalk-robot-rules`: San Francisco Public Works Code Sec. 794, subsections (a) to (k), retrieved 2026-11-17. One legal text, 32 rules, 4 penalty provisions. The three files in `examples/` are illustrative observations we wrote, labeled as such, because no incident dataset exists.

**4. What it found:** 32 distinct checkable rules, each linked to its clause (n = 1 code section, 11 subsections). 15 can be checked by a resident from the sidewalk; 19 by an operator (2 overlap). The code requires operators to report incidents and complaints to the City monthly (§794(h)(2)(C)), yet no public incident dataset exists, so the rules are checkable but compliance is not visible to the public.

**5. One honest limitation:** The map is hand-drawn, so zone and high-injury-street checks are approximate and must be confirmed on the City's maps; pins marked demo are examples we wrote. A resident estimates 3 mph and 30 ft by eye, and zoning, high-injury-corridor and permit status need a map or permit-list lookup, so a failed check is grounds to report, not proof. The rules are our paraphrase of the code text; conditions the Director adds to an individual permit (§794(c), (h)(1)) are not in it. It has not been tested on a real robot sighting.

**6. If this were deployed and it failed,** who is accountable, and how would they find out? We are accountable for the rule extraction: if a rule is misread, a resident could file a wrong report or an operator could be wrongly reassured. Each rule cites its clause and shows its test, so anyone can check it against the code and tell us. Enforcement itself sits with the Public Works Director, and compliance with the permittee. Today the public could not find out about a failure of the rules themselves, because the monthly incident reports are not published. Our report's data format is a proposed schema for publishing them.
