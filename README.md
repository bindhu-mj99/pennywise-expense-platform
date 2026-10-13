# Pennywise — Expense Tracker API

## Current implementation
Runnable FastAPI starter with API documentation, validation, and a simple test. Some advanced product features remain to be implemented.

## Run on Windows
```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs for interactive API documentation.

## Next improvements
- Add a frontend and persistent/authenticated production data model where relevant.
- Add tests for invalid input, failure paths, and the main user journey.
- Add deployment, architecture diagram, screenshots, and design decisions.
- Review security and limitations before using real data or deploying publicly.

Do not commit secrets, real personal data, or employer code. This is a learning starter, not a production-certified application.
