from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/telemetry"
)

tables = ["raw_events", "stg_events", "mart_daily_counts"]

with engine.connect() as conn:
    for t in tables:
        try:
            count = conn.execute(text(f"SELECT COUNT(*) FROM {t}")).scalar()
            print(f"{t}: {count}")
        except Exception as e:
            print(f"{t}: ERROR -> {e}")
