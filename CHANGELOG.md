\# Changelog



All notable changes to this project are documented in this file.

This project uses Semantic Versioning: vMAJOR.MINOR.PATCH.



\## \[v1.0.0] - 2026-10-04



First tested release baseline for the ISYS3001 A2 individual phase.

All seven backlog items (A2-01 to A2-07) are implemented, reviewed and verified by CI.



\### Added

\- Client records management: add, list and search clients by name or phone (A2-01)

\- Property records linked to clients (A2-03)

\- Animal records linked to clients (A2-02)

\- Local data persistence with SQLite, database path configurable via .env (A2-04)

\- In-clinic consultation booking with room/time conflict validation (A2-05)

\- Farm visit booking with minimum 60-minute duration validation (A2-06)

\- Appointment cancellation that retains history and releases the room (A2-07)

\- Automated test suite: 12 pytest cases covering all backlog items

\- GitHub Actions CI pipeline: ruff lint + pytest on every push and pull request

\- In-repository project documentation: product backlog, decision log, test traceability



\### Notes

\- A2 local backlog identifiers A2-01 to A2-07 map to A3 Jira user stories US-01 to US-07

&#x20; (see docs/product-backlog.md for the mapping table).

\- ruff rule DTZ007 is intentionally suppressed in ruff.toml: this application runs

&#x20; locally in a single time zone, so naive datetimes are acceptable.

