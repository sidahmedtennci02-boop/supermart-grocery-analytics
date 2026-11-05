import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'
RAW_DATA = DATA_DIR / 'supermart_original.csv'
CLEAN_DATA = DATA_DIR / 'supermart_cleaned.csv'

def load_raw_data():
    """Load the original dataset"""
    df = pd.read_csv(RAW_DATA)
    return df

def clean_data(df):
    """Clean and validate the dataset"""
    df_clean = df.copy()
    
    # Standardize column names (lowercase with underscores)
    df_clean.columns = [col.strip().lower().replace(' ', '_') for col in df_clean.columns]
    
    # Convert order_date to datetime (handle mixed formats)
    df_clean['order_date'] = pd.to_datetime(df_clean['order_date'], dayfirst=False, errors='coerce')
    
    # Convert numeric columns
    numeric_cols = ['sales', 'discount', 'profit']
    for col in numeric_cols:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # Check for missing values
    missing_before = df_clean.isnull().sum()
    
    # Drop rows with critical missing values if any
    df_clean = df_clean.dropna(subset=['order_id', 'order_date', 'sales', 'profit'])
    
    # Remove duplicates
    duplicates_before = df_clean.duplicated().sum()
    df_clean = df_clean.drop_duplicates()
    
    # Add derived columns for analysis
    df_clean['order_year'] = df_clean['order_date'].dt.year
    df_clean['order_month'] = df_clean['order_date'].dt.month
    df_clean['order_month_name'] = df_clean['order_date'].dt.month_name()
    df_clean['order_quarter'] = df_clean['order_date'].dt.quarter
    df_clean['profit_margin'] = (df_clean['profit'] / df_clean['sales'] * 100).round(2)
    df_clean['sales_after_discount'] = df_clean['sales']  # sales as given
    
    # Clean categorical columns
    cat_cols = ['customer_name', 'category', 'sub_category', 'city', 'region', 'state']
    for col in cat_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip()
    
    return df_clean, missing_before, duplicates_before

def main():
    """Main cleaning pipeline"""
    print('Loading raw data...')
    df_raw = load_raw_data()
    print(f'Raw data shape: {df_raw.shape}')
    
    print('\nCleaning data...')
    df_clean, missing_before, duplicates_before = clean_data(df_raw)
    print(f'Cleaned data shape: {df_clean.shape}')
    print(f'Missing values before: {missing_before.sum()}')
    print(f'Duplicates removed: {duplicates_before}')
    
    print('\nSaving cleaned data...')
    df_clean.to_csv(CLEAN_DATA, index=False)
    print(f'Saved to: {CLEAN_DATA}')
    
    # Validation
    print('\n=== Validation ===')
    print(f'Date range: {df_clean["order_date"].min()} to {df_clean["order_date"].max()}')
    print(f'Unique orders: {df_clean["order_id"].nunique()}')
    print(f'Categories: {sorted(df_clean["category"].unique())}')
    
    return df_clean

if __name__ == '__main__':
    df_clean = main()
