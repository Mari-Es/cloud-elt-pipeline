# Cloud ELT Pipeline (AWS S3 → PostgreSQL)

This repository contains an end-to-end **cloud-based ELT (Extract–Load–Transform) pipeline** designed to ingest raw data from AWS S3, load it into a relational database, transform it using SQL, and validate data quality through automated checks.

The project follows **industry-standard data engineering practices** and is fully reproducible via a single execution command.

---

## Project Architecture

AWS S3 (raw files)  
→ Python ingestion  
→ PostgreSQL (raw layer)  
→ SQL transformations (staging layer)  
→ Analytics mart  
→ Data quality validation  

This architecture mirrors common production ELT patterns used in analytics and data engineering teams.

---

## Tech Stack

- **Cloud Storage**: AWS S3  
- **Programming Language**: Python  
- **Database**: PostgreSQL (Dockerized)  
- **Transformations**: SQL (ELT pattern)  
- **Libraries**: pandas, boto3, SQLAlchemy  
- **Infrastructure**: Docker  
- **Version Control**: Git & GitHub  

---

## Pipeline Overview

### 1. Extract
- Downloads raw data files (CSV / Excel) from AWS S3
- Designed to handle real-world data formats robustly

### 2. Load
- Loads raw data into PostgreSQL (`raw_events`)
- Ensures persistent, queryable storage for downstream processing

### 3. Transform
- Executes SQL transformations inside the database
- Creates:
  - `stg_events` (cleaned and standardized staging table)
  - `mart_daily_counts` (analytics-ready aggregation)

### 4. Validate
- Runs automated data quality checks
- Verifies that all pipeline layers contain valid records

---

## How to Run the Pipeline

Run the entire pipeline end-to-end with a single command:

```bash
python src/run_pipeline.py
This command performs:

S3 data extraction

PostgreSQL data loading

SQL-based transformations

Data quality validation

Example Results
Raw records ingested: ~1,000,000

Staging records: ~1,000,000

Analytics mart created and ready for reporting

Repository Structure
pgsql
Copy code
cloud-elt-pipeline/
├── src/
│   ├── extract_from_s3.py
│   ├── load_to_postgres.py
│   ├── transform_sql.py
│   ├── validate.py
│   └── run_pipeline.py
├── sql/
│   ├── 01_staging.sql
│   └── 02_marts.sql
├── requirements.txt
├── README.md
└── .gitignore
Design Principles & Key Learnings
Separation of concerns between ingestion, transformation, and validation

SQL-based transformations executed inside the database for scalability

Robust handling of real-world data formats

Reproducible, automation-friendly pipeline design

Secure handling of credentials and raw data (excluded from version control)

Notes
Raw data files are intentionally not included in this repository.
The pipeline is designed to retrieve data directly from cloud storage (AWS S3), ensuring reproducibility without committing large or sensitive datasets.
