# Supermart Grocery Sales — Retail Business Intelligence

A complete, portfolio-ready data analytics project demonstrating data cleaning, exploratory data analysis, SQL querying, visualization, and an interactive dashboard using the Supermart Grocery Sales dataset.

## 📊 Project Overview

This project analyzes grocery sales data from a supermarket chain to uncover business insights, identify profitable product categories, understand customer purchasing patterns, and provide actionable recommendations for business growth.

## 🎯 Objectives

- Clean and preprocess raw sales data for analysis
- Perform comprehensive exploratory data analysis (EDA)
- Write SQL queries to extract business insights
- Create professional visualizations
- Build an interactive Streamlit dashboard
- Generate actionable business recommendations

## 🛠️ Tech Stack

- **Python** - Data manipulation and analysis
- **pandas & NumPy** - Data processing
- **Matplotlib & Seaborn** - Static visualizations
- **Plotly** - Interactive visualizations
- **SQLite** - SQL database and querying
- **Streamlit** - Interactive web dashboard
- **Jupyter Notebook** - Exploratory analysis

## 📁 Project Structure

`
Supermart-Analytics/
├── data/                    # Raw and cleaned datasets
├── notebooks/              # Jupyter notebooks for exploration
├── src/                    # Python scripts for cleaning and analysis
├── outputs/figures/        # Generated visualizations
├── sql/                    # SQLite database and SQL queries
├── dashboard/              # Streamlit dashboard application
├── reports/                # Business reports and summaries
├── docs/                   # Learning guides and documentation
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
`

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
`ash
git clone <your-repo-url>
cd Supermart-Analytics
`

2. Create a virtual environment (recommended):
`ash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
`

3. Install dependencies:
`ash
pip install -r requirements.txt
`

### Usage

#### 1. Data Cleaning
`ash
python src/data_cleaning.py
`

#### 2. Exploratory Data Analysis
`ash
python src/eda_analysis.py
`

#### 3. SQL Database Creation
`ash
python src/create_database.py
`

#### 4. Run the Interactive Dashboard
`ash
streamlit run dashboard/app.py
`

The dashboard will open in your browser at http://localhost:8501

## 📈 Key Findings

Based on analysis of 4,042 orders:

- **Total Sales:** ,053,500
- **Total Profit:** ,503,059
- **Overall Profit Margin:** 24.83%
- **Top Performing Category:** Eggs, Meat & Fish (highest sales)
- **Best Profit Margin:** Snacks (25.52%)
- **Time Period:** 2015-2018

## 💡 Business Recommendations

1. **Focus on High-Margin Categories** - Prioritize Snacks and Fruits & Veggies for promotions
2. **Optimize Discount Strategy** - Analyze discount impact to maintain profitability
3. **Regional Focus** - Leverage top-performing regions for expansion
4. **Inventory Management** - Stock more of best-selling sub-categories
5. **Seasonal Planning** - Plan promotions around identified sales trends

## 📝 License

This project is for educational and portfolio purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For questions or feedback, please open an issue in the repository.
