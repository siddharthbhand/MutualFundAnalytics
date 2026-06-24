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
