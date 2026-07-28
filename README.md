# 🚖 Modern Local-First ELT Pipeline (NYC Taxi)

An enterprise-grade, cost-effective Extract, Load, Transform (ELT) data pipeline built locally using **Python**, **DuckDB**, **dbt (data build tool)**, and **Parquet**, replicating modern cloud analytical architectures (such as cloud object storage $\rightarrow$ cloud data warehousing) with zero infrastructure overhead.

---

## 🏗️ Architecture & Pipeline Phases

This project is built iteratively following industry-grade data engineering patterns. Detailed architectural documentation for each completed phase is available below:

* **[Phase 1: Data Lake Landing Zone (`docs/data_lake_landing_zone_notes.md`)](docs/data_lake_landing_zone_notes.md)**
  * Implements a local directory structure mirroring enterprise cloud object storage (AWS S3 / GCS buckets).
  * Establishes an immutable raw landing zone (`data/landing/`) to securely ingest untouched source datasets.

* **[Phase 2: Analytical Data Warehouse Ingestion (`docs/data_warehouse_ingestion_notes.md`)](docs/data_warehouse_ingestion_notes.md)**
  * Replaces heavy cloud data warehouses with **DuckDB**, a high-performance, in-process columnar analytical engine (OLAP).
  * Programmatically automates ingestion via Python scripts, creating logical namespaces (`raw_staging`) and bulk-loading over 3 million rows of compressed Parquet data.

* **[Phase 3: Transformations & Dimensional Modeling (`dbt`)](dbt_project.yml)**
  * Integrates **dbt (data build tool)** to manage the transformation layer inside DuckDB.
  * Implements modular staging models (`stg_yellow_tripdata`) with data type casting, renaming conventions, and automated source testing (`schema.yml`).

---

## 📂 Project Directory Structure

```text
nyc-taxi-elt-pipeline/
│
├── data/
│   └── landing/              # Raw source data files (Parquet/CSV)
│
├── warehouse/
│   └── warehouse.duckdb      # Local analytical database file (Generated)
│
├── models/                   # dbt transformation models
│   └── staging/              
│       ├── schema.yml        # dbt sources and data quality tests
│       └── stg_yellow_tripdata.sql # Cleaned and casted staging view
│
├── scripts/
│   └── create_warehouse.py   # Automated warehouse setup & ingestion script
│
├── sql/
│   └── verification_queries.sql # Data validation & schema checks
│
├── docs/
│   ├── data_lake_landing_zone_notes.md   # Landing zone architecture notes
│   └── data_warehouse_ingestion_notes.md # Data warehouse ingestion notes
│
├── dbt_project.yml           # dbt project configuration
├── README.md                 # Project homepage & documentation index
├── requirements.txt          # Python dependencies
└── .gitignore                # Excludes virtual 
environments & binaries

Quick Start / How to Run
1. Clone the Repository

git clone [https://github.com/aditi0103singh/nyc-taxi-elt-pipeline.git](https://github.com/aditi0103singh/nyc-taxi-elt-pipeline.git)

cd nyc-taxi-elt-pipeline

2. Set Up the Environment
Create and activate your virtual environment, then install dependencies:

python -m venv .venv

# On Windows PowerShell:
.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

3. Run Ingestion
Execute the pipeline script to automatically initialize the local DuckDB warehouse and ingest the raw Parquet dataset into the staging layer:

python scripts/create_warehouse.py

4. Configure & Run dbt Transformations
Configure your local dbt profile pointing to your warehouse.duckdb file inside your user profile directory (~/.dbt/profiles.yml).

Test your dbt connection:

dbt debug

Execute your dbt transformation models:

dbt run

5. Verify Data Integrity
Run the verification queries stored in sql/verification_queries.sql via your Python terminal or DuckDB extension to validate row counts, schemas, and performance metrics.