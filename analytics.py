# analytics.py

import pandas as pd
from config import SPECIALITY_TEST_THRESHOLD

def total_revenue(df):
    """
    Calculate the total revenue from all records.
    """
    return df['Revenue'].sum()

def monthly_revenue(df):
    """
    Calculate total revenue grouped by month.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('Month')['Revenue'].sum().reset_index()
    monthly['Month'] = monthly['Month'].dt.to_timestamp()
    return monthly

def average_ticket_size(df):
    """
    Calculate the average revenue per transaction.
    """
    return df['Revenue'].mean()

def speciality_tests(df):
    """
    Identify and count tests where the bill amount is >= ₹999.
    """
    spec_df = df[df['Revenue'] >= SPECIALITY_TEST_THRESHOLD]
    total = spec_df['Revenue'].sum()
    count = spec_df.shape[0]
    percent = (total / df['Revenue'].sum()) * 100 if df['Revenue'].sum() > 0 else 0
    return {
        'count': count,
        'total_revenue': total,
        'percent_of_total': percent
    }

def clients_added(df):
    """
    Count unique clients by month and cumulative.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_clients = df.groupby('Month')['PatientName'].nunique().reset_index()
    monthly_clients['Month'] = monthly_clients['Month'].dt.to_timestamp()
    cumulative = df['PatientName'].nunique()
    return monthly_clients, cumulative

def revenue_by_salesperson(df):
    """
    Aggregate total revenue per salesperson.
    """
    result = df.groupby('Salesperson')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def transactions_by_salesperson(df):
    """
    Count total transactions per salesperson.
    """
    result = df.groupby('Salesperson')['InvoiceID'].count().sort_values(ascending=False).reset_index()
    result = result.rename(columns={'InvoiceID': 'Transactions'})
    return result

def referral_analysis(df):
    """
    Analyze the impact of referral sources.
    """
    result = df.groupby('Referral')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def discount_trend(df):
    """
    Analyze discount trends over time.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    trend = df.groupby('Month')['Discount'].sum().reset_index()
    trend['Month'] = trend['Month'].dt.to_timestamp()
    return trend

def gross_vs_net(df):
    """
    Compare gross and net revenue over time.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    result = df.groupby('Month')[['Gross', 'Revenue']].sum().reset_index()
    result['Month'] = result['Month'].dt.to_timestamp()
    return result

def organisation_revenue(df):
    """
    Revenue grouped by organisation.
    """
    result = df.groupby('Organisation')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def marketing_impact(df):
    """
    Analyze revenue contribution from marketing sources.
    """
    org_result = df.groupby('MarketingOrg')['Revenue'].sum().sort_values(ascending=False).reset_index()
    ref_result = df.groupby('MarketingReferral')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return org_result, ref_result# analytics.py

import pandas as pd
from config import SPECIALITY_TEST_THRESHOLD

def total_revenue(df):
    """
    Calculate the total revenue from all records.
    """
    return df['Revenue'].sum()

def monthly_revenue(df):
    """
    Calculate total revenue grouped by month.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('Month')['Revenue'].sum().reset_index()
    monthly['Month'] = monthly['Month'].dt.to_timestamp()
    return monthly

def average_ticket_size(df):
    """
    Calculate the average revenue per transaction.
    """
    return df['Revenue'].mean()

def speciality_tests(df):
    """
    Identify and count tests where the bill amount is >= ₹999.
    """
    spec_df = df[df['Revenue'] >= SPECIALITY_TEST_THRESHOLD]
    total = spec_df['Revenue'].sum()
    count = spec_df.shape[0]
    percent = (total / df['Revenue'].sum()) * 100 if df['Revenue'].sum() > 0 else 0
    return {
        'count': count,
        'total_revenue': total,
        'percent_of_total': percent
    }

def clients_added(df):
    """
    Count unique clients by month and cumulative.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_clients = df.groupby('Month')['PatientName'].nunique().reset_index()
    monthly_clients['Month'] = monthly_clients['Month'].dt.to_timestamp()
    cumulative = df['PatientName'].nunique()
    return monthly_clients, cumulative

def revenue_by_salesperson(df):
    """
    Aggregate total revenue per salesperson.
    """
    result = df.groupby('Salesperson')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def transactions_by_salesperson(df):
    """
    Count total transactions per salesperson.
    """
    result = df.groupby('Salesperson')['InvoiceID'].count().sort_values(ascending=False).reset_index()
    result = result.rename(columns={'InvoiceID': 'Transactions'})
    return result

def referral_analysis(df):
    """
    Analyze the impact of referral sources.
    """
    result = df.groupby('Referral')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def discount_trend(df):
    """
    Analyze discount trends over time.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    trend = df.groupby('Month')['Discount'].sum().reset_index()
    trend['Month'] = trend['Month'].dt.to_timestamp()
    return trend

def gross_vs_net(df):
    """
    Compare gross and net revenue over time.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    result = df.groupby('Month')[['Gross', 'Revenue']].sum().reset_index()
    result['Month'] = result['Month'].dt.to_timestamp()
    return result

def organisation_revenue(df):
    """
    Revenue grouped by organisation.
    """
    result = df.groupby('Organisation')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return result

def marketing_impact(df):
    """
    Analyze revenue contribution from marketing sources.
    """
    org_result = df.groupby('MarketingOrg')['Revenue'].sum().sort_values(ascending=False).reset_index()
    ref_result = df.groupby('MarketingReferral')['Revenue'].sum().sort_values(ascending=False).reset_index()
    return org_result, ref_result
