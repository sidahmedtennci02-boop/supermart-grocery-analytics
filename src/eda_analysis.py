import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'
FIG_DIR = Path(__file__).parent.parent / 'outputs' / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)

def load_clean_data():
    df = pd.read_csv(DATA_DIR / 'supermart_cleaned.csv')
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

def main():
    df = load_clean_data()
    
    print('=== OVERALL METRICS ===')
    total_sales = df['sales'].sum()
    total_profit = df['profit'].sum()
    overall_margin = (total_profit / total_sales * 100)
    print(f'Total Sales: {total_sales:,.2f}')
    print(f'Total Profit: {total_profit:,.2f}')
    print(f'Overall Profit Margin: {overall_margin:.2f}%')
    print(f'Order Count: {df.shape[0]:,}')
    
    # Sales by category
    cat_perf = df.groupby('category').agg({
        'sales': 'sum',
        'profit': 'sum',
        'order_id': 'count'
    }).rename(columns={'order_id': 'order_count'}).round(2)
    cat_perf['profit_margin'] = (cat_perf['profit'] / cat_perf['sales'] * 100).round(2)
    cat_perf = cat_perf.sort_values('sales', ascending=False)
    print('\n=== SALES & PROFIT BY CATEGORY ===')
    print(cat_perf)
    
    # Save summary
    cat_perf.to_csv(Path(__file__).parent.parent / 'outputs' / 'category_performance.csv')
    
    # Visualizations
    plt.style.use('seaborn-v0_8')
    
    # 1. Sales by category
    fig, ax = plt.subplots(figsize=(10, 6))
    cat_perf['sales'].plot(kind='bar', ax=ax, color='steelblue')
    ax.set_title('Total Sales by Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(FIG_DIR / '01_sales_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Profit by category
    fig, ax = plt.subplots(figsize=(10, 6))
    cat_perf['profit'].plot(kind='bar', ax=ax, color='green')
    ax.set_title('Total Profit by Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('Category')
    ax.set_ylabel('Profit')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(FIG_DIR / '02_profit_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Monthly trend
    monthly = df.groupby(['order_year', 'order_month'])['sales'].sum().reset_index()
    monthly['date'] = pd.to_datetime(monthly['order_year'].astype(str) + '-' + monthly['order_month'].astype(str) + '-01')
    monthly = monthly.sort_values('date')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly['date'], monthly['sales'], marker='o', linewidth=2, markersize=6)
    ax.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(FIG_DIR / '03_monthly_sales_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Sales vs Profit scatter
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['sales'], df['profit'], alpha=0.5, c=df['discount'], cmap='coolwarm')
    ax.set_title('Sales vs Profit (colored by discount)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Sales')
    ax.set_ylabel('Profit')
    plt.colorbar(ax.collections[0], label='Discount')
    plt.tight_layout()
    plt.savefig(FIG_DIR / '04_sales_vs_profit.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f'\nVisualizations saved to {FIG_DIR}')
    
if __name__ == '__main__':
    main()
