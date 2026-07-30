# Documentation: Local Data Lake Landing Zone

## 📌 Overview
This document outlines the architecture and setup of the local Data Lake Landing Zone. In a traditional cloud-native ELT stack, this layer is built using cloud object storage like AWS S3 or Google Cloud Storage (GCS). For our local-first architecture, we replicate this exact cloud object storage pattern using a structured local directory layout.

---

## 🏗️ Architecture & Core Concepts

### 1. What is a Data Lake Landing Zone?
The **Landing Zone** (often called the raw or bronze layer) is the absolute first entry point for external data entering an organization's data platform. 
* **Rule of Thumb:** Data is ingested "as-is" from external sources (APIs, CSVs, partner exports, web scraping) with **zero modifications, cleaning, or transformations**.
* **Purpose:** It acts as a permanent, immutable historical archive. If downstream pipeline logic changes or corrupts data later, engineers can always reprocess raw files directly from the landing zone.

### 2. Why Local Directory Structure Over Cloud Storage?
By organizing our local file system to mirror cloud storage buckets, we achieve the exact same architectural separation of concerns without incurring cloud costs or requiring active internet connectivity:
* Separation of raw landing files from processed and staging environments.
* Clear directory hierarchy for pipeline tracking and automated ingestion scripts.

---

## 📂 Project Directory Structure

Our local data lake is structured as follows:

```text
nyc-taxi-elt-pipeline/
│
├── data/
│   ├── landing/              <-- Raw, untouched files land here (e.g., Parquet/CSV)
│   ├── processed/            <-- Cleaned or intermediate working files (if applicable)
│   ├── archive/              <-- Historical snapshots of older data batches
│   └── logs/                 <-- Pipeline execution logs
│
├── warehouse/
│   └── warehouse.duckdb      <-- Local analytical data warehouse
│
├── scripts/
│   └── create_warehouse.py   <-- Ingestion automation script
│
├── sql/
│   └── verification_queries.sql <-- Data validation queries
│
└── docs/
    ├── data_lake_landing_zone_notes.md   <-- You are here
    └── data_warehouse_ingestion_notes.md <-- Ingestion phase documentation