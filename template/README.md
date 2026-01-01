# Legacy Modernization Template

## Structure
- legacy/: original scripts
- src/core/: core business logic
- src/services/: API wrapper (FastAPI)
- tests/: Golden Master tests
- requirements.txt: dependencies

## Usage
1. Copy template folder to new project
2. Replace legacy scripts
3. Update core logic in src/core
4. Update API in src/services
5. Run tests: pytest
6. Run API: uvicorn src.services.api:app --reload
