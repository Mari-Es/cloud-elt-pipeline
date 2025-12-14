import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")

FILE_PATH = os.path.join("data", "downloaded.csv")  # content may be Excel
RAW_TABLE = "raw_events"

def main():
    print("Connecting to Postgres...")

    engine = create_engine(
        f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
    )

    print("Reading data file...")

    try:
        # Try CSV first
        df = pd.read_csv(FILE_PATH)
        print("Detected CSV format.")
    except UnicodeDecodeError:
        # Fallback to Excel
        df = pd.read_excel(FILE_PATH)
        print("Detected Excel format.")

    print(f"Rows read from file: {len(df)}")

    df.to_sql(RAW_TABLE, engine, if_exists="replace", index=False)

    print(f"Loaded {len(df)} rows into table: {RAW_TABLE}")

if __name__ == "__main__":
    main()
