Markdown
# 🚖 NYC Taxi ELT & Analytics Pipeline

A production-grade, local Modern Data Stack implementation built using **DuckDB**, **dbt (data build tool)**, **Dagster**, and **Streamlit**. This project ingests, transforms, governs, and visualizes large-scale taxi trip data following clean architecture principles.

---

## 🏗️ Architecture & Tech Stack

The project follows a **Medallion-inspired ELT architecture** combined with strict separation of concerns across infrastructure layers:

* **Storage & Ingestion:** `DuckDB` (embedded, high-performance analytical database).
* **Transformation & Testing:** `dbt` (modular SQL models, automated data assertions).
* **Orchestration:** `Dagster` (asset-based pipeline management, dependency tracking, scheduling).
* **Presentation Layer:** `Streamlit` (decoupled, read-only executive dashboard UI).

```text
[Raw Sources] ➔ [DuckDB Storage] ➔ [dbt Transformations & Tests] ➔ [Dagster Orchestration] ➔ [Streamlit UI]

📂 Project Directory Structure
Plaintext
nyc-taxi-elt-pipeline/
│
├── .dagster/                 # Dagster local storage/state (Ignored by Git)
├── .venv/                    # Python virtual environment (Ignored by Git)
├── dashboard.py              # Streamlit presentation layer (UI)
├── docs/                     # Engineering documentation
│   ├── dimensional_modeling.md
│   └── data_governance.md
├── dagster_pipeline/         # Dagster orchestration definitions & assets
│   └── defs.py
├── nyc_taxi_dbt/             # dbt project directory
│   ├── models/               # Staging, intermediate, and mart models
│   ├── tests/                # Custom data assertions
│   ├── dbt_project.yml
│   └── schema.yml
├── warehouse/                # Local DuckDB database file storage
├── .gitignore                # Git exclusion rules
└── README.md                 # Project front door

📐 Data Modeling & Governance
Dimensional Modeling Strategy: Breaks down the pipeline's progression from raw staging tables (stg_) to intermediate business logic (int_), granular fact tables (fct_), and pre-aggregated financial data marts (mart_).

Data Governance & Assertions: Details how automated dbt tests enforce unique constraints, non-null requirements, and logical range boundaries, backed by Dagster asset graph observability.

🚀 Quickstart Guide
Follow these steps to set up, execute, and view the entire pipeline locally.

1. Clone the Repository & Setup Environment
Bash
git clone [https://github.com/aditi0103singh/nyc-taxi-elt-pipeline.git](https://github.com/aditi0103singh/nyc-taxi-elt-pipeline.git)

cd nyc-taxi-elt-pipeline

# Create and activate virtual environment
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1

# On macOS/Linux:
# source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

2. Execute Transformations via dbt
Navigate into your dbt project folder, run transformations, and verify data quality assertions:

cd nyc_taxi_dbt
dbt run
dbt test
cd ..

3. Launch Dagster Orchestrator (Optional Control Plane)
To inspect the asset lineage and monitor execution visually:

dagster dev -f dagster_pipeline/defs.py
Open your browser and navigate to http://localhost:3000.

4. Launch the Streamlit Dashboard
Open a new terminal window, activate your virtual environment, and run the UI:

streamlit run dashboard.py
Open your browser and navigate to http://localhost:8501 to view live executive KPIs and trends.

📄 License
This project is open-source and available under the MIT License.