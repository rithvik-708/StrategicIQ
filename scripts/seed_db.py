import os
from sqlalchemy import create_engine, text

DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/strategic_iq")

def seed():
    engine = create_engine(DB_URL)
    with engine.begin() as conn:
        # We will insert a proxy company (e.g., Blinkit/Zepto)
        # Note: In a real scenario, this would be robust.
        # This script assumes the schema has already been created.
        conn.execute(text("INSERT INTO companies (name, industry, ticker) VALUES ('Zepto', 'Quick-Commerce', 'ZPTO') ON CONFLICT DO NOTHING;"))
        print("Database seeded with sample Quick-Commerce data.")

if __name__ == "__main__":
    seed()
