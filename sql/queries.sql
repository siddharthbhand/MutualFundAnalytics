-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Highest Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 3. Lowest Expense Ratio Funds

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 5;


-- 4. Average NAV by Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- 5. Transaction Count by Type

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 6. Total Investment Amount by Transaction Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 7. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 8. KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status;


-- 9. Average Annual Income by City Tier

SELECT
    city_tier,
    AVG(annual_income_lakh) AS avg_income
FROM fact_transactions
GROUP BY city_tier;


-- 10. High Risk High Return Funds

SELECT
    scheme_name,
    return_5yr_pct,
    risk_grade
FROM fact_performance
WHERE risk_grade IN ('High','Very High')
ORDER BY return_5yr_pct DESC;