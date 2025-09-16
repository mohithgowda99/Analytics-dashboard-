# data_processing.py

import pandas as pd
from config import COLUMN_MAPPING, DEFAULT_VALUES, REQUIRED_COLUMNS

def load_file(file):
    """
    Load an Excel or CSV file into a DataFrame.
    """
    try:
        if file.name.endswith('.xlsx') or file.name.endswith('.xls'):
            df = pd.read_excel(file)
        else:
            df = pd.read_csv(file)
        return df
    except Exception as e:
        raise ValueError(f"Error loading file {file.name}: {str(e)}")

def standardize_columns(df):
    """
    Rename columns based on COLUMN_MAPPING and ensure all required columns are present.
    """
    df = df.rename(columns=lambda x: COLUMN_MAPPING.get(x.strip(), x.strip()))
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    return df

def clean_data(df):
    """
    Clean the DataFrame:
    - Convert date columns to datetime
    - Convert numeric columns to appropriate types
    - Fill missing values
    - Drop rows without required identifiers
    """
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df = df.dropna(subset=['InvoiceDate'])

    # Convert numeric columns and fill missing values
    for col, default in DEFAULT_VALUES.items():
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(default)
    
    # Drop rows without InvoiceID
    df = df.dropna(subset=['InvoiceID'])

    # Ensure InvoiceID is string
    df['InvoiceID'] = df['InvoiceID'].astype(str)

    return df

def deduplicate(df):
    """
    Remove duplicate records based on InvoiceID.
    """
    return df.drop_duplicates(subset=['InvoiceID'])

def process_file(file):
    """
    Complete pipeline to process an uploaded file.
    """
    df = load_file(file)
    df = standardize_columns(df)
    df = clean_data(df)
    df = deduplicate(df)
    return df

def combine_dataframes(dfs):
    """
    Combine multiple DataFrames into one, removing duplicates.
    """
    combined = pd.concat(dfs, ignore_index=True)
    combined = deduplicate(combined)
    return combined
