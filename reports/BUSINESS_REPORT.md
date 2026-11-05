# Business Report - Supermart Grocery Sales Analysis

## Business Problem
Supermart needs to understand its sales performance across different product categories, regions, and time periods to make data-driven decisions for improving profitability and growth.

## Objectives
1. Analyze overall sales and profitability
2. Identify top-performing and underperforming products
3. Understand discount impact on profit
4. Evaluate regional and category performance
5. Provide actionable recommendations

## Dataset Description
- **Source**: Supermart Grocery Sales Dataset
- **Records**: 4,042 cleaned orders (from original 9,994)
- **Time Period**: 2015-2018
- **Location**: Tamil Nadu, India (based on cities/states in data)
- **Features**: Order details, customer info, product categories, location, sales, discount, profit

## Methodology

### Data Cleaning
- Standardized column names
- Converted dates to datetime format
- Handled mixed date formats
- Removed/validated missing values
- Created derived features (profit margin, time dimensions)
- No duplicates found in cleaned data

### Analysis Techniques
- Descriptive statistics
- Group by aggregations
- Time series analysis
- Correlation analysis (Sales vs Profit)
- SQL-based querying

## Key Findings

### Overall Performance
- **Total Sales**: ,053,500.00
- **Total Profit**: ,503,059.03
- **Overall Profit Margin**: 24.83%
- **Total Orders**: 4,042
- **Unique Customers**: Multiple customers across locations

### Category Performance
All categories show healthy profit margins (24-25.5%). Snacks have the highest profit margin (25.52%) despite moderate sales volume.

### Regional Insights
Analysis shows performance varies by region, with opportunities for optimization.

### Discount Impact
Discounts affect profitability - need careful discount strategy to maintain margins.

## Actionable Business Recommendations

1. **Product Mix Optimization**
   - Focus on high-margin categories like Snacks and Fruits & Veggies
   - Evaluate low-margin items for pricing/cost optimization

2. **Discount Strategy**
   - Implement data-driven discount policies
   - Monitor discount impact by category
   - Avoid deep discounts on already low-margin items

3. **Geographic Expansion**
   - Invest more in top-performing cities
   - Analyze underperforming locations for improvement opportunities

4. **Inventory Management**
   - Stock best-selling sub-categories appropriately
   - Reduce inventory for consistently unprofitable items

5. **Seasonal Planning**
   - Leverage monthly trends for promotional planning
   - Prepare inventory for peak periods

## Limitations
- Dataset only covers Tamil Nadu region
- Missing cost data - profit calculated differently than full P&L
- Limited customer demographic information
- No product-level SKU details beyond category/sub-category

## Future Improvements
- Add customer segmentation analysis
- Include forecasting models for sales prediction
- Implement RFM analysis
- Add more detailed profitability metrics
- Integrate with real-time data sources
