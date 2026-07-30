import streamlit as st
import duckdb
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="NYC Taxi Analytics Dashboard",
    page_icon="🚖",
    layout="wide"
)

st.title("🚖 NYC Taxi Executive Analytics Dashboard")
st.markdown("Real-time operational and financial insights powered by DuckDB, dbt, and Streamlit.")

# Connect to DuckDB Warehouse (Read-Only Mode)
@st.cache_resource
def get_db_connection():
    # Points to your local DuckDB database file
    return duckdb.connect("warehouse/warehouse.duckdb", read_only=True)

try:
    conn = get_db_connection()

    # Fetch high-level KPIs from your dbt Marts
    st.subheader("📊 High-Level Performance Metrics")
    
    # Example query pulling from your pre-aggregated marts or fact tables
    # (Adjust table name based on your exact dbt model name, e.g., mart_daily_revenue)
    query_kpis = "SELECT count(*) as total_trips, sum(fare_amount) as total_revenue FROM fct_taxi_trips"
    df_kpis = conn.execute(query_kpis).df()

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Trips Recorded", value=f"{df_kpis['total_trips'].iloc[0]:,}")
    with col2:
        st.metric(label="Total Revenue", value=f"${df_kpis['total_revenue'].iloc[0]:,.2f}")

    st.divider()

    # Detailed data view
    st.subheader("📋 Recent Trip Records")
    query_recent = "SELECT * FROM fct_taxi_trips LIMIT 50"
    df_recent = conn.execute(query_recent).df()
    st.dataframe(df_recent, use_container_width=True)

except Exception as e:
    st.warning("⚠️ Database warehouse file not found or not yet generated. Run your dbt models to build the warehouse first!")
    st.info(f"Details: {e}")