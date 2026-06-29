# Mutual Fund Analytics - Data Dictionary

## Dataset: nav_history_clean.csv

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | Integer   | Unique AMFI scheme identifier |
| date      | Date      | NAV date                      |
| nav       | Float     | Net Asset Value of fund       |

---

## Dataset: scheme_performance_clean.csv

| Column             | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | Integer   | Unique scheme identifier         |
| scheme_name        | Text      | Mutual fund scheme name          |
| fund_house         | Text      | Asset Management Company         |
| category           | Text      | Fund category                    |
| plan               | Text      | Direct / Regular plan            |
| return_1yr_pct     | Float     | 1-year return percentage         |
| return_3yr_pct     | Float     | 3-year return percentage         |
| return_5yr_pct     | Float     | 5-year return percentage         |
| benchmark_3yr_pct  | Float     | Benchmark return                 |
| alpha              | Float     | Excess return metric             |
| beta               | Float     | Market sensitivity metric        |
| sharpe_ratio       | Float     | Risk-adjusted return metric      |
| sortino_ratio      | Float     | Downside risk-adjusted return    |
| std_dev_ann_pct    | Float     | Annualized volatility            |
| max_drawdown_pct   | Float     | Maximum drawdown percentage      |
| aum_crore          | Integer   | Assets Under Management (Crores) |
| expense_ratio_pct  | Float     | Expense ratio percentage         |
| morningstar_rating | Integer   | Morningstar rating               |
| risk_grade         | Text      | Risk classification              |

---

## Dataset: investor_transactions_clean.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor ID         |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Fund identifier            |
| transaction_type   | Text      | SIP / Lumpsum / Redemption |
| amount_inr         | Integer   | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | T30 / B30 classification   |
| age_group          | Text      | Investor age category      |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income in lakhs     |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

---

## Data Sources

* AMFI Mutual Fund Data
* Simulated Investor Transaction Dataset
* Scheme Performance Dataset
* Fund House AUM Dataset

---

## Database Schema

Dimension Tables:

* dim_fund

Fact Tables:

* fact_nav
* fact_performance
* fact_transactions

Database:

* SQLite
* bluestock_mf.db


# 📊 Mutual Fund Analytics Dashboard

A production-style Mutual Fund Analytics Dashboard built using **Python, SQL, Pandas, Plotly, Seaborn, Matplotlib, SQLite, and Streamlit**. The project analyzes multiple mutual fund datasets to generate business insights, interactive visualizations, and performance metrics.

---

# 🚀 Project Overview

This project performs end-to-end data analysis on Indian Mutual Fund datasets.

The workflow includes:

* Data Cleaning
* SQL Database Design
* Exploratory Data Analysis (EDA)
* Data Visualization
* Benchmark Analysis
* Portfolio Analysis
* Streamlit Dashboard

The objective is to transform raw mutual fund data into meaningful insights through interactive charts and dashboards.

---

# 🎯 Project Objectives

* Analyze NAV trends of multiple mutual funds
* Compare Fund House AUM growth
* Study SIP inflow trends
* Analyze investor demographics
* Compare category-wise inflows
* Evaluate benchmark performance
* Analyze portfolio holdings
* Build an interactive analytics dashboard

---

# 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Data Analysis              |
| Pandas     | Data Processing            |
| NumPy      | Numerical Operations       |
| Matplotlib | Static Charts              |
| Seaborn    | Statistical Visualizations |
| Plotly     | Interactive Charts         |
| SQLite     | Database                   |
| SQL        | Data Queries               |
| Streamlit  | Dashboard                  |
| Git        | Version Control            |
| GitHub     | Repository Management      |

---

# 📂 Project Structure

```text
MutualFundAnalytics/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── EDA_Analysis.ipynb
│
├── reports/
│   ├── aum_growth.png
│   ├── nav_trend_analysis.png
│   ├── sip_inflow_trend.png
│   ├── category_heatmap.png
│   ├── age_group_distribution.png
│   ├── sip_amount_boxplot.png
│   ├── gender_distribution.png
│   ├── state_sip_distribution.png
│   ├── t30_b30_distribution.png
│   ├── folio_growth.png
│   ├── sector_allocation.png
│   ├── sector_allocation_donut.png
│   ├── top_holdings.png
│   ├── benchmark_trend.png
│   ├── nav_return_correlation.png
│   └── data_dictionary.md
│
├── sql/
│
├── requirements.txt
└── README.md
```

---

# 🔄 Project Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
SQL Queries
      │
      ▼
EDA
      │
      ▼
Visualizations
      │
      ▼
Business Insights
      │
      ▼
Streamlit Dashboard
```

---

# 📊 Exploratory Data Analysis

The notebook includes more than **15 visualizations**, including:

* NAV Trend Analysis
* Fund House AUM Growth
* SIP Inflow Trend
* Category-wise Heatmap
* Age Group Distribution
* Gender Distribution
* SIP Amount Boxplot
* State-wise Investment Distribution
* T30 vs B30 Distribution
* Folio Growth Trend
* Sector Allocation
* Sector Allocation Donut Chart
* Top Portfolio Holdings
* Benchmark Performance
* NAV Return Correlation Heatmap

---

# 📈 Key Insights

* SBI Mutual Fund recorded the highest AUM among major fund houses.
* Monthly SIP inflows reached an all-time high of ₹31,002 Crore.
* Equity mutual funds showed a strong upward NAV trend between 2022 and 2025.
* T30 cities contributed significantly more investments than B30 cities.
* Banking and Technology sectors dominated portfolio allocations.
* Mutual fund folios nearly doubled from 13.26 Crore to 26.12 Crore.
* Large Cap and Flexi Cap funds attracted consistently high inflows.
* Strong positive correlations were observed among several equity mutual funds.

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/MutualFundAnalytics.git
```

Move into the project directory:

```bash
cd MutualFundAnalytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 📁 Reports Generated

The project automatically generates visualization reports in PNG format inside the `reports/` directory.

---

# 📚 Deliverables

* Data Cleaning Pipeline
* SQLite Database
* SQL Queries
* Jupyter EDA Notebook
* 15+ Charts
* Business Insights
* Streamlit Dashboard

---

# 🚀 Future Improvements

* Live Mutual Fund API Integration
* Real-Time NAV Updates
* Portfolio Risk Analysis
* AI-Based Mutual Fund Recommendation
* Performance Forecasting using Machine Learning
* Investor Portfolio Optimization

---

# 👨‍💻 Author

**Siddharth**

Mutual Fund Analytics Dashboard Project

Built using Python, SQL, Pandas, Plotly, Streamlit, and SQLite.

