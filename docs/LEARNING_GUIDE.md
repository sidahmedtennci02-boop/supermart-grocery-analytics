# Learning Guide - Supermart Grocery Sales Project

This guide explains the main Python and SQL concepts used in this project in simple terms for beginners.

## Python Concepts

### 1. pandas - Data Manipulation
- **DataFrames**: Like Excel spreadsheets in Python
- **read_csv()**: Loading data from CSV files
- **groupby()**: Grouping data for aggregation
- **to_csv()**: Saving data to files
- **dropna(), drop_duplicates()**: Cleaning data

### 2. Data Cleaning Techniques
- **Type conversion**: Converting dates and numbers to correct types
- **Missing value handling**: Identifying and dealing with nulls
- **Standardization**: Making column names consistent
- **Feature engineering**: Creating new columns (profit_margin, order_month)

### 3. Data Visualization
- **Matplotlib**: Basic plotting library
- **Seaborn**: Statistical visualizations built on matplotlib
- **Plotly**: Interactive charts for dashboards

### 4. File Handling with pathlib
- Using Path objects for cross-platform file paths
- Creating directories with mkdir()

## SQL Concepts

### 1. Basic Queries
- **SELECT**: Retrieving data
- **FROM**: Specifying the table
- **WHERE**: Filtering rows
- **ORDER BY**: Sorting results

### 2. Aggregations
- **SUM()**: Total calculations
- **COUNT()**: Counting records
- **AVG()**: Average values
- **GROUP BY**: Grouping for aggregates

### 3. Calculations
- **Percentage calculations**: Using multiplication and division
- **CASE statements**: Creating categories
- **ROUND()**: Rounding numbers

### 4. Database Operations
- **CREATE TABLE / INSERT**: Building SQLite database
- **sqlite3**: Python's built-in SQLite module

## Tips for Learning

1. **Experiment**: Modify the code and see what happens
2. **Read errors**: Error messages tell you what's wrong
3. **Google is your friend**: Search for concepts you don't understand
4. **Practice SQL**: Try the queries in the .sql file
5. **Explore the dashboard**: Interact with filters to understand the data better
