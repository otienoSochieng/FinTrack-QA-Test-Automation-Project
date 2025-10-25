# FinTrack Test Plan

## Project overview
FinTrack is a personal finance management web app. This Test Plan outlines scope, strategy, environment,
risks, entry/exit criteria, and deliverables for QA.

## Scope
In scope:
- User authentication & session management
- Transactions: CRUD operations for incomes & expenses
- Budget creation and alerts
- Analytics and reports
- Export CSV
- Role-based access (User, Admin)
- APIs for all above functions

Out of scope:
- Third-party payment gateway (sandbox only)
- Mobile native app

## Testing types
- Functional testing
- API testing (contract & data validation)
- Integration testing
- Regression testing
- Performance (smoke) testing guidance
- Security checks (auth, permissions)
- Database integrity testing

## Environments
- Local (dev)
- Staging (https://staging.fintrack.example)
- Production (read-only checks)

## Tools
- Selenium, PyTest
- Postman + Newman
- Requests (Python)
- MySQL / PostgreSQL
- Docker, GitHub Actions
- Allure for advanced reporting

## Test data & privacy
- Use synthetic test data. No PII in repo.

## Entry criteria
- Smoke tests pass on staging
- Test environment stable

## Exit criteria
- All critical/blocker defects resolved
- Test coverage >= agreed threshold for critical flows

## Risks
- Unstable test environment
- Flaky UI selectors - use data-testids where possible

