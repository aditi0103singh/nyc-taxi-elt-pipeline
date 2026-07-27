# Documentation: Local Analytical Data Warehouse Ingestion

## 📌 Overview
This document outlines the architecture, tool selection, and implementation steps for ingesting raw transactional data into a local analytical data warehouse using DuckDB.

---

## 🏗️ Architecture & Core Concepts

### 1. What is an Analytical Data Warehouse?
A data warehouse is a centralized repository optimized for **Online Analytical Processing (OLAP)**. Unlike application databases designed for fast row-by-row updates (OLTP), a data warehouse is designed to efficiently scan, aggregate, and join millions of historical records for business reporting and modeling.

### 2. Why DuckDB?
* **Zero-Infrastructure:** Runs entirely in-process as a lightweight library without requiring a separate server daemon, Docker container, or cloud configuration.
* **Columnar Storage Engine:** Stores data by columns rather than rows, drastically reducing disk I/O for analytical queries.
* **Native Parquet Integration:** Instantly reads compressed columnar files (like Apache Parquet) with high performance.

### 3. Namespace Organization (Schemas)
A **schema** is a logical container used to structure database objects. In this pipeline, we use a medallion architecture pattern:
* `raw_staging`: The initial landing zone where source data is ingested with zero transformations, preserving data fidelity for auditing.

---

## 🛠️ Implementation Summary
* **Source Dataset:** `data/landing/yellow_tripdata_2023-01.parquet` (approx. 3.06 million rows)
* **Storage Destination:** `warehouse/warehouse.duckdb`
* **Script Automation:** Managed via `scripts/create_warehouse.py`, which programmatically initializes the database, builds the schema, and bulk-loads the Parquet dataset.

---

## 🔍 Verification & Testing
To verify ingestion success, structural integrity, and row counts, we use SQL queries stored in `sql/verification_queries.sql`:
* Validated total row count (`3,066,766 rows`).
* Inspected table schemas and data types using `DESCRIBE`.