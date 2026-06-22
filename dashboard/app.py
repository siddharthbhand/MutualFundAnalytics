import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Mutual Fund Analytics",
    page_icon="📊",
    layout="wide"
)

# ==================================
# TITLE
# ==================================

st.title("📊 Mutual Fund Analytics Dashboard")

# ==================================
# LOAD DATA
# ==================================

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# ==================================
# KPI SECTION
# ==================================

total_schemes = len(fund_master)
total_fund_houses = fund_master["fund_house"].nunique()
total_aum = aum["aum_crore"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Schemes", total_schemes)

with col2:
    st.metric("Fund Houses", total_fund_houses)

with col3:
    st.metric("Total AUM (Cr)", f"{total_aum:,.0f}")

# ==================================
# TOP 5 FUND HOUSES
# ==================================

st.markdown("---")

st.subheader("🏆 Top 5 Fund Houses by AUM")

latest_date = aum["date"].max()

latest_data = aum[aum["date"] == latest_date]

top5 = latest_data.sort_values(
    "aum_crore",
    ascending=False
).head(5)

fig, ax = plt.subplots(figsize=(10, 5))

ax.barh(
    top5["fund_house"],
    top5["aum_crore"]
)

ax.set_title("Top 5 Fund Houses by AUM")
ax.set_xlabel("AUM (Crores)")
ax.set_ylabel("Fund House")

st.pyplot(fig)

# ==================================
# TOP PERFORMING FUNDS
# ==================================

st.markdown("---")

st.header("🚀 Top 10 Performing Funds")

top_funds = pd.read_csv(
    "data/processed/top_performing_funds.csv"
)

# Best Performer Card

best_fund = top_funds.iloc[0]

st.success(
    f"🏆 Best Performer: {best_fund['scheme_name']} | Return: {best_fund['return_pct']:.2f}%"
)

# Table

st.dataframe(
    top_funds[
        [
            "scheme_name",
            "start_nav",
            "end_nav",
            "return_pct"
        ]
    ].head(10),
    use_container_width=True
)

# Download Button

st.download_button(
    label="📥 Download Top Funds CSV",
    data=top_funds.to_csv(index=False),
    file_name="top_performing_funds.csv",
    mime="text/csv"
)

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.caption(
    "Developed by Siddharth | Mutual Fund Analytics Dashboard"
)