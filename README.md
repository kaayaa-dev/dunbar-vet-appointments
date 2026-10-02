# Dunbar Veterinary Clinic Appointment Management System

A local-first appointment and records management system for the Dunbar
Veterinary Clinic, built with Flask and SQLite. Developed as part of
ISYS3001 Managing Software Development (Assessment 2).

## Features

- Client records management: add, list and search clients
- Property records management: add properties and list them per client

## Tech Stack

- Python 3, Flask, SQLite, Jinja2 templates
- pytest (testing), ruff (linting)
- GitHub Actions (CI)
- python-dotenv (environment configuration)

## Setup and Run

```bash
git clone https://github.com/kaayaa-dev/dunbar-vet-appointments.git
cd dunbar-vet-appointments
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
flask --app app run
```

Then open http://127.0.0.1:5000 in your browser.

## Running Tests

```bash
pytest
```

## Lint

```bash
ruff check .
```

## Branching Strategy

This project follows GitHub Flow:

- `main` is protected; all changes arrive via pull request
- `feature/A2-XX-*` branches for new functionality
- `fix/*` branches for bug fixes
- `release/*` branches for release baselines (e.g. v1.0.0)

## Project Management

- Product backlog: `docs/product-backlog.md`
- Decision log: `docs/decision-log.md`
- Test traceability: `docs/test-traceability.md`

## License

MIT