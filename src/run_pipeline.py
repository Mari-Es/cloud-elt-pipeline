import subprocess
import sys

def run_step(description, command):
    print(f"\n=== {description} ===")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"FAILED at step: {description}")
        sys.exit(result.returncode)
    print(f"SUCCESS: {description}")

def main():
    print("Starting full ELT pipeline...")

    run_step(
        "Extract data from AWS S3",
        "python src/extract_from_s3.py"
    )

    run_step(
        "Load raw data into PostgreSQL",
        "python src/load_to_postgres.py"
    )

    run_step(
        "Run SQL transformations (staging + mart)",
        "python src/transform_sql.py"
    )

    run_step(
        "Run data quality validation",
        "python src/validate.py"
    )

    print("\nELT pipeline completed successfully!")

if __name__ == "__main__":
    main()
