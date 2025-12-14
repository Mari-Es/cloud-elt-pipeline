import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

def assert_positive_rowcount(engine, table):
    with engine.connect() as conn:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table};")).scalar()

    print(f"{table}: {count} rows")

    if count <= 0:
        raise ValueError(f"Validation failed: {table} is empty")

def main():
    print("Running data quality checks...")

    engine = create_engine(
        f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    )

    for table in ["raw_events", "stg_events", "mart_daily_counts"]:
        assert_positive_rowcount(engine, table)

    print("All data quality checks passed.")

if __name__ == "__main__":
    main()
