\# Decision Log



\## Summary Table



| Date | Decision | Rationale |

|---|---|---|

| 2026-10-02 | Use SQLite instead of PostgreSQL | Local-first requirement, zero setup |

| 2026-10-02 | No cloud services at runtime | Offline operation requirement |

| 2026-10-02 | GitHub Flow branching model | Individual A2 phase, short delivery window |

| 2026-10-02 | Docker optional, not core | Time constraint; local venv deployment is sufficient |



\## Detailed Decision Records



\### 2026-10-03 — Combined PR for A2-05 and A2-06 (recorded 2026-10-04)



Decision: A2-05 (in-clinic consultation) and A2-06 (farm visit) were implemented together in a single pull request (PR #4), as an exception to the one-PR-per-story rule.



Reason: both items share the same appointment model and the same conflict-validation module (\_has\_room\_conflict); splitting them would have produced two PRs touching identical code.



\### 2026-10-03 — README merge conflict resolution (recorded 2026-10-04)



Event: two documentation branches (PR #6 and PR #7) edited the same README line. After PR #6 merged, PR #7 could not merge automatically.



Resolution: the conflict was resolved locally (git pull origin main, manual edit, resolution commit 41b1b1a), pushed, and PR #7 was then merged normally.



\### 2026-10-03 — Independent peer reviewer arrangement (recorded 2026-10-04)



Decision: an independent peer reviewer (GitHub: samm4567) was onboarded on 2026-10-03 to review pull requests. PRs #1–#3 predate the reviewer onboarding and were merged by the repository administrator via the ruleset bypass; formal peer review applies from PR #4 onwards.



Reason: A2 is an individual assessment; an external reviewer was added to satisfy the review requirement honestly rather than simulating self-review.



\### 2026-10-04 — Rollback strategy



Decision: small defects are rolled back with git revert via a pull request (CI + review required). A major release issue is handled by restoring the known-good release tag (v1.0.0). Destructive git reset on main is forbidden.



\### 2026-10-04 — Buffer time between appointments (future improvement)



Noted from PR #4 review: a buffer time between consecutive appointments in the same room is a candidate refinement. Deferred: recorded on the product backlog for the A3 team phase rather than added to the A2 baseline.



