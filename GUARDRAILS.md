# How Yield decides things

Every rule on this page is a fixed threshold. There is no scoring model and no moderator: the same sightings and reviews always produce the same outcome, and anyone can recompute it from the public record. The logic lives in `index.html` (`score()`, `fleet()`, `geoOK()`).

## 1. Geofence: you have to be there

| Rule | Value |
|---|---|
| Where the app works | Inside the San Francisco city boundary only. Taps outside it are refused. |
| Reporting a robot | You must be within 250 m of the spot you report. |
| Reviewing a sighting | Same: within 250 m of the sighting. |
| Outside the fence | The report button is disabled and reviews are refused, with the distance shown. |

How it is checked: the standalone page asks the browser for your device location. The hosted preview cannot read GPS, so it runs a clearly labelled simulated location with a toggle ("Demo: on-site" / "Demo: across town") to show both outcomes. Each sighting records whether its location was `gps` or `sim`.

## 2. Community feedback loop: who earns trust

| Event | Effect |
|---|---|
| Posting a sighting | 0 points |
| Sighting confirmed by 2 or more other people with combined review weight of at least 1.5 | Sighting becomes "community verified"; reporter +10 points, +0.5 trust |
| Sighting disputed by 2 or more people with combined weight of at least 1.5 | Sighting becomes "disputed" and stops counting; reporter -10 points, -1 trust |
| Your review matches the final outcome | +2 points, +0.1 trust |
| Review weight | New neighbor (trust under 2): 0.5. Trusted neighbor (2 to 4): 1. Block Guardian (4 and over): 1.5 |

Fair-play rules:

- You cannot review your own sighting, and you get one review per sighting.
- A confirmed "looks allowed" pays the same as a confirmed violation, so there is no bounty for accusing.
- Only your first 5 sightings a day can earn points.
- Points are reputation only. Nothing can be cashed out.

## 3. Recall ladder: when a robot goes back to its dock

Counted per robot ID (the identifier §794(i)(9) requires on every device), over a rolling 30 days. Only community-verified sightings with at least one broken rule count. Unverified and disputed sightings never count.

| Verified strikes in 30 days | Status | What happens |
|---|---|---|
| 1 | Watch | The robot ID appears on the public watchlist. |
| 2 | Warning | The operator is warned. |
| 3, from 3 different reporters | Recall | The robot must return to its dock and stay off the sidewalk until inspected. |

Recall is a proposed rule. Yield cannot command a robot. It would take effect only if operators agree to honor it or Public Works makes it a permit condition; §794(h)(1) lets the Director add conditions and suspend or revoke permits for safety.

## 4. The Sidewalk Fund (proposal, not live)

- Every permitted operator pays the same flat fee per robot per month (example: $250, so at most $2,250 a month under the 9-robot cap).
- The fee is the same whether or not an operator is reported, and buys no say over sightings, reviews or scores.
- It pays for running the map, accessibility audits and open incident data. It is never paid out per report.
- Every dollar in and out goes on a public ledger.

No money moves through the app.

## What these guardrails cannot do

- **Stop location spoofing.** Device GPS can be faked, and the hosted preview does not read it at all.
- **Tell whether two accounts are one person**, or stop a group agreeing to confirm each other. Half-weight reviews, the two-confirmer rule, the three-reporter rule for recall and the daily cap raise the cost without removing it.
- **Verify a robot ID.** IDs are typed in by the reporter. A robot with no visible ID cannot be put on the ladder (that is itself a violation of §794(i)(9)).
- **Prove a violation.** "Verified" means neighbors agree, not that the City has confirmed it.
- **Bind identity to a report.** In the shared store the reporter field is not cryptographically tied to an account.

The pins, reviews and robot IDs marked "demo" are examples we wrote to show the mechanics. They are not real sightings.
