import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Supermart Grocery Sales Dashboard", page_icon="🛒", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(Path(__file__).parent.parent / "data" / "supermart_cleaned.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df

df = load_data()

st.sidebar.header("Filters")
st.sidebar.caption("All filters default to full dataset")

date_range = st.sidebar.date_input(
    "Date Range",
    value=(df["order_date"].min().date(), df["order_date"].max().date()),
    min_value=df["order_date"].min().date(),
    max_value=df["order_date"].max().date(),
)

categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)

regions = ["All"] + sorted(df["region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Region", regions)

cities = ["All"] + sorted(df["city"].dropna().unique().tolist())
selected_city = st.sidebar.selectbox("City", cities)

filtered_df = df.copy()
if len(date_range) == 2:
    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1])
    filtered_df = filtered_df[(filtered_df["order_date"] >= start_date) & (filtered_df["order_date"] <= end_date)]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]
if selected_city != "All":
    filtered_df = filtered_df[filtered_df["city"] == selected_city]

st.markdown("<h1 style='font-size: 2rem; margin-bottom: 0.5rem;'>Supermart Grocery Sales - Retail Business Intelligence</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    total_sales = filtered_df["sales"].sum()
    st.metric("Total Sales", f"")
with col2:
    total_profit = filtered_df["profit"].sum()
    st.metric("Total Profit", f"")
with col3:
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    st.metric("Profit Margin", f"{profit_margin:.2f}%")
with col4:
    order_count = int(filtered_df["order_id"].nunique())
    st.metric("Total Orders", f"{order_count:,}")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sales & Profit by Category")
    cat_data = filtered_df.groupby("category").agg({"sales": "sum", "profit": "sum"}).reset_index()
    fig = px.bar(cat_data, x="category", y=["sales", "profit"], barmode="group",
                 labels={"value": "Amount ($)", "variable": "Metric"},
                 color_discrete_sequence=["#1f77b4", "#2ca02c"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Amount ($)", legend_title="Metric",
                      margin=dict(l=20, r=20, t=40, b=20), xaxis={"tickangle": -45})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Sales by Region")
    region_data = filtered_df.groupby("region")["sales"].sum().reset_index().sort_values("sales", ascending=False)
    fig = px.pie(region_data, values="sales", names="region", hole=0.4)
    fig.update_traces(textposition="inside", textinfo="percent+label",
                      hovertemplate="<b>%{label}</b><br>Sales: $%{value:,.0f}<br>Percent: %{percent}<extra></extra>")
    fig.update_layout(legend_title="Region", margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
st.subheader("Monthly Sales & Profit Trend")
if not filtered_df.empty and "order_year" in filtered_df.columns:
    monthly_data = filtered_df.groupby(["order_year", "order_month"]).agg({"sales": "sum", "profit": "sum"}).reset_index()
    monthly_data["period"] = monthly_data["order_year"].astype(str) + "-" + monthly_data["order_month"].astype(str).str.zfill(2)
    monthly_data = monthly_data.sort_values(["order_year", "order_month"])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly_data["period"], y=monthly_data["sales"], name="Sales", mode="lines+markers"))
    fig.add_trace(go.Scatter(x=monthly_data["period"], y=monthly_data["profit"], name="Profit", mode="lines+markers"))
    fig.update_layout(xaxis_title="Period (YYYY-MM)", yaxis_title="Amount ($)", legend_title="Metric", hovermode="x unified",
                      margin=dict(l=20, r=20, t=40, b=20), xaxis={"tickangle": -45})
    fig.update_yaxes(tickformat=",.0f")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 10 Sub-Categories by Sales")
    subcat_sales = filtered_df.groupby("sub_category")["sales"].sum().nlargest(10).reset_index().sort_values("sales", ascending=True)
    fig = px.bar(subcat_sales, x="sales", y="sub_category", orientation="h",
                 labels={"sales": "Sales ($)", "sub_category": "Sub-Category"},
                 color="sales", color_continuous_scale="Blues")
    fig.update_layout(xaxis_title="Sales ($)", yaxis_title="Sub-Category", margin=dict(l=20, r=20, t=40, b=20), showlegend=False)
    fig.update_xaxes(tickformat=",.0f")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top 10 Cities by Sales")
    city_sales = filtered_df.groupby("city")["sales"].sum().nlargest(10).reset_index().sort_values("sales", ascending=True)
    fig = px.bar(city_sales, x="sales", y="city", orientation="h",
                 labels={"sales": "Sales ($)", "city": "City"},
                 color="sales", color_continuous_scale="Greens")
    fig.update_layout(xaxis_title="Sales ($)", yaxis_title="City", margin=dict(l=20, r=20, t=40, b=20), showlegend=False)
    fig.update_xaxes(tickformat=",.0f")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Data Source: Supermart Grocery Sales Dataset | Built with Streamlit")
