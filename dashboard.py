import streamlit as st
import duckdb

# 1. Page Configuration
st.set_page_config(
    page_title="NYC Taxi Executive Dashboard",
    page_icon="🚖",
    layout="wide"
)

# 2. Sidebar Guide
with st.sidebar:
    st.header("🚖 NYC Taxi Analytics")
    st.markdown("Viewing production-ready data transformed via **dbt** and stored in **DuckDB**.")
    st.markdown("---")
    st.markdown("**Pipeline Workflow:**\n1. Run pipeline in terminal (`dbt run`)\n2. View live metrics here.")

# 3. Read-Only Database Connection
@st.cache_resource
def get_db_connection():
    return duckdb.connect("warehouse/warehouse.duckdb", read_only=True)

con = get_db_connection()

# 4. Main Title
data_load_state = st.text("Loading data from DuckDB...")
try:
    df_revenue = con.sql("SELECT * FROM main.mart_daily_revenue ORDER BY trip_date DESC").df()
    df_trips_sample = con.sql("SELECT * FROM main.fct_taxi_trips LIMIT 100").df()
    data_load_state.empty() # Clear loading text
except Exception as e:
    st.error("⚠️ Database tables not found! Please run `dbt run` in your `nyc_taxi_dbt/` folder first.")
    st.stop()

st.title("🚖 NYC Taxi Executive Analytics Dashboard")

# 5. KPIs
total_trips = df_revenue["total_trips"].sum()
total_revenue = df_revenue["total_overall_revenue"].sum()
avg_tip_pct = df_revenue["average_tip_percentage"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Trips", f"{total_trips:,}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Avg Tip %", f"{avg_tip_pct:.2f}%")

st.divider()

# 6. Chart
st.subheader("📈 Daily Revenue Trend")
st.line_chart(df_revenue.set_index("trip_date")[["total_overall_revenue"]])

# 7. Tables
tab1, tab2 = st.tabs(["📋 Daily Revenue Mart", "🔍 Fact Table Sample"])
with tab1:
    st.dataframe(df_revenue, use_container_width=True)
with tab2:
    st.dataframe(df_trips_sample, use_container_width=True)