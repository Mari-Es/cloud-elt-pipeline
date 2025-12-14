import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

def run_sql_file(engine, path):
    print(f"Running SQL file: {path}")
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.execute(text(sql))

    print(f"Finished: {path}")

def main():
    print("Connecting to Postgres for SQL transformations...")

    engine = create_engine(
        f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    )

    run_sql_file(engine, "sql/01_staging.sql")
    run_sql_file(engine, "sql/02_marts.sql")

    print("All SQL transformations completed successfully.")

if __name__ == "__main__":
    main()
