-- Supermart Grocery Sales SQL Analysis
-- Query 1: Overall Business Performance
SELECT 
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct,
    COUNT(DISTINCT customer_name) AS unique_customers
FROM sales;

-- Query 2: Sales and Profit by Category
SELECT 
    category,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Query 3: Top 10 Sub-Categories by Sales
SELECT 
    sub_category,
    category,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY sub_category, category
ORDER BY total_sales DESC
LIMIT 10;

-- Query 4: Performance by Region
SELECT 
    region,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- Query 5: Monthly Sales Trend
SELECT 
    order_year,
    order_month,
    order_month_name,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY order_year, order_month, order_month_name
ORDER BY order_year, order_month;

-- Query 6: Impact of Discounts on Profitability
SELECT 
    CASE 
        WHEN discount = 0 THEN 'No Discount'
        WHEN discount <= 0.1 THEN 'Low (0-10%)'
        WHEN discount <= 0.2 THEN 'Medium-Low (11-20%)'
        WHEN discount <= 0.3 THEN 'Medium-High (21-30%)'
        ELSE 'High (>30%)'
    END AS discount_range,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_pct,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY discount_range
ORDER BY avg_discount_pct;

-- Query 7: Top 10 Most Profitable Products (by Sub-Category)
SELECT 
    sub_category,
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY sub_category, category
ORDER BY total_profit DESC
LIMIT 10;

-- Query 8: Cities with Highest Sales
SELECT 
    city,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY city
ORDER BY total_sales DESC
LIMIT 15;
