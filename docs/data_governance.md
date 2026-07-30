# 🛡️ Data Governance & Quality Assurance Framework

This document details the automated data governance, assertion, and observability framework implemented for the NYC Taxi pipeline using **dbt tests** and **Dagster**.

---

## 🔍 Automated Data Assertions (dbt Tests)

Data quality is enforced declaratively through `schema.yml` configurations across the transformation layers. Every time the pipeline is materialized, automated assertions check for schema and data integrity:

### 1. Uniqueness & Nullability Constraints
* **Primary Key Validation:** Ensures trip identifiers and surrogate keys are strictly `unique` and `not_null` to prevent duplication in downstream financial aggregations.

### 2. Referential Integrity
* **Relationship Tests:** Validates foreign key constraints across models, ensuring that staging layers properly map into intermediate and fact layers without orphaned records.

### 3. Value Range & Validity Assertions
* **Accepted Values / Accepted Ranges:** Custom or built-in tests ensure business rules hold true (e.g., `trip_distance >= 0`, `fare_amount >= 0`, and valid status codes).

---

## 📊 Pipeline Observability & Orchestration (Dagster)

Operational governance and dependency management are handled via Dagster:
* **Asset Lineage Graph:** Visualizes explicit upstream-to-downstream dependencies from raw sources to final dbt marts.
* **Execution Tracking:** Monitors run statuses, logs compute errors, and tracks asset freshness.
* **Fail-Safe Execution:** Halts downstream presentation updates if upstream data assertions or staging transformations fail, protecting end-users from consuming bad data.