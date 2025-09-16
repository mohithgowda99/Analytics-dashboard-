# config.py

# Column mapping to standardize data across different files
COLUMN_MAPPING = {
    'InvoiceDate': 'InvoiceDate',
    'TransactionDate': 'InvoiceDate',
    'Date': 'InvoiceDate',
    'Salesperson': 'Salesperson',
    'Agent': 'Salesperson',
    'Amount': 'Revenue',
    'Total': 'Revenue',
    'Bill ID': 'InvoiceID',
    'Patient Name': 'PatientName',
    'Organisation Revenue Amount': 'OrgRevenue',
    'Referral Revenue Amount': 'ReferralRevenue',
    'Discount': 'Discount',
    'Gross': 'Gross',
    'Organisation': 'Organisation',
    'Referral': 'Referral',
    'Marketing Person(Referral)': 'MarketingReferral',
    'Marketing Person(Organisation)': 'MarketingOrg'
}

# KPI thresholds
SPECIALITY_TEST_THRESHOLD = 999  # Bills above this are considered speciality tests

# Rolling window size for anomaly detection
ROLLING_WINDOW_SIZE = 3

# Forecasting model parameters
FORECAST_ALPHA = 0.3  # Smoothing factor for simple exponential smoothing

# Columns required for processing
REQUIRED_COLUMNS = [
    'InvoiceDate',
    'InvoiceID',
    'Salesperson',
    'Revenue',
    'OrgRevenue',
    'ReferralRevenue',
    'PatientName',
    'Discount',
    'Gross',
    'Organisation',
    'Referral'
]

# Default values for missing data
DEFAULT_VALUES = {
    'Revenue': 0.0,
    'OrgRevenue': 0.0,
    'ReferralRevenue': 0.0,
    'Discount': 0.0,
    'Gross': 0.0
}
