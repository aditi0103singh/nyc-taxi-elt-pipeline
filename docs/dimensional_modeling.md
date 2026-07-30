# 📐 Dimensional Modeling Strategy: NYC Taxi Analytics

This document outlines the dimensional modeling approach used to transform raw, denormalized transactional data into structured, high-performance analytical models within the dbt transformation layer.

---

## 🎯 Design Objectives
* **Performance:** Optimize query execution times for analytical dashboards and aggregations.
* **Clarity:** Separate business events (Facts) from contextual business entities (Dimensions) where applicable, or leverage wide, optimized fact tables for streamlined ELT.
* **Maintainability:** Ensure clear data lineage through modular dbt SQL models.

---

## 🏛️ Schema Architecture

### 1. Staging Models (`stg_`)
* **Role:** Acts as the clean, typed mirror of the raw source data. 
* **Modifications:** Column renaming to consistent `snake_case`, basic casting (e.g., timestamps, floats), and macro-level filtering of erroneous records (e.g., negative passenger counts or zero-mile distances).

### 2. Intermediate Models (`int_`)
* **Role:** Bridges raw ingestion and final presentation by applying complex business logic.
* **Calculations:** 
  * `trip_duration_minutes` derived from dropoff and pickup timestamps.
  * `tip_percentage` calculated against fare amounts.
  * Speed and distance metrics computed for downstream analytical utility.

### 3. Fact Tables (`fct_`)
* **Model Name:** `fct_taxi_trips`
* **Characteristics:** Captures granular, individual trip events. It stores additive and non-additive numerical measures (fare amounts, tip amounts, trip distances, passenger counts) alongside foreign keys pointing to temporal and operational dimensions.

### 4. Data Marts (`mart_`)
* **Model Name:** `mart_daily_revenue`
* **Characteristics:** Pre-aggregated summary tables designed specifically to feed the executive UI layer (Streamlit). It groups metrics by `trip_date` and `vendor_id` to deliver instant analytical performance without heavy runtime compute.