# Documentation: Analytics Engineering & dbt Architecture

## 📌 Overview
This document outlines the principles of **Analytics Engineering**, the role of **dbt (data build tool)** in a modern ELT pipeline, and the structural separation between data storage (DuckDB) and data transformation.

---

## 🏗️ Core Architectural Concepts

### 1. What is Analytics Engineering?
Analytics Engineering bridges the gap between raw data engineering and business analytics. It is the practice of safely transforming messy raw warehouse data into clean, tested, documented, and reliable business datasets using software engineering best practices (Version Control, CI/CD, Automated Testing).

### 2. Where dbt Fits in the ELT Stack
A common misconception is that dbt replaces a database or warehouse. **It does not.** 
* **DuckDB** acts as the analytical execution engine and storage layer.
* **dbt** acts as the compiler and orchestrator that sends SQL transformations (`CREATE VIEW` / `CREATE TABLE AS`) down into DuckDB.

The data flow structure:
```text
Raw Parquet File
    │
    ▼ (Ingestion Script)
DuckDB (raw_staging.raw_trips)
    │
    ▼ (dbt Transformations)
Staging Models (Light cleaning, typecasting)
    │
    ▼
Fact & Dimension Tables (Business logic, star schema)