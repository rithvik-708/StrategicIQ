# StrategicIQ

StrategicIQ is a deterministic analytical core and structured data engine. Phase 1 establishes the mathematical foundation and database structure required for hybrid search and deterministic financial metrics, guaranteeing accuracy and zero LLM hallucination for core logic.

## Architecture & Tech Stack
- **Language**: Python (Pandas & NumPy for deterministic calculations)
- **Database**: PostgreSQL with the `pgvector` extension (configured for `text-embedding-3-small` with 1536 dimensions)
- **Testing**: Pytest

## Directory Structure
```text
strategic_iq/
├── analytics/         # Deterministic python modules (Sizing, Economics, Pricing)
├── db/                # PostgreSQL schema (Vector store + structured relational data)
├── scripts/           # Utilities for database seeding
├── tests/             # Mathematical validations & Plotly JSON export tests
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Setup & Installation

1. **Install Dependencies**
   It's recommended to use a virtual environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Database Setup**
   Ensure you have a PostgreSQL database running with the `pgvector` extension enabled.
   Run the schema setup script:
   ```bash
   psql -U postgres -d your_db_name < db/schema.sql
   ```

3. **Seed Mock Data**
   Inject sample data into the database for testing:
   ```bash
   # Set your connection string
   export DATABASE_URL="postgresql://user:password@localhost:5432/strategic_iq"
   python scripts/seed_db.py
   ```

## Running Tests
Run the deterministic unit test suite to verify all market sizing logic and Plotly integrations.
```bash
pytest tests/test_analytics.py
```
