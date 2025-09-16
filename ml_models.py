# ml_models.py

import pandas as pd
import numpy as np
from config import ROLLING_WINDOW_SIZE, FORECAST_ALPHA

def anomaly_detection(df):
    """
    Detect anomalies in monthly revenue based on rolling mean and standard deviation.
    Returns a DataFrame with anomalies flagged.
    """
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly = df.groupby('Month')['Revenue'].sum().reset_index()
    monthly['Month'] = monthly['Month'].dt.to_timestamp()
    monthly['RollingMean'] = monthly['Revenue'].rolling(window=ROLLING_WINDOW_SIZE, min_periods=1).mean()
    monthly['RollingStd'] = monthly['Revenue'].rolling(window=ROLLING_WINDOW_SIZE, min_periods=1).std().fillna(0)
    monthly['Anomaly'] = abs(monthly['Revenue'] - monthly['RollingMean']) > 2 * monthly['RollingStd']
    return monthly

def run_rate_forecasting(df):
    """
    Forecasts month-end revenue based on current month-to-date performance.
    Uses a simple exponential smoothing approach.
    """
    today = pd.Timestamp.today()
    current_month = df[df['InvoiceDate'].dt.to_period('M') == today.to_period('M')]
    mtd_revenue = current_month['Revenue'].sum()
    days_in_month = today.days_in_month
    current_day = today.day
    forecast = (mtd_revenue / current_day) * days_in_month if current_day > 0 else 0
    return forecast

def client_segmentation(df, n_clusters=3):
    """
    Placeholder for client segmentation using clustering algorithms.
    This can be extended with scikit-learn's KMeans or other models.
    """
    from sklearn.cluster import KMeans
    # Example: Use total revenue and number of transactions per client
    client_data = df.groupby('PatientName').agg({
        'Revenue': 'sum',
        'InvoiceID': 'count'
    }).rename(columns={'InvoiceID': 'Transactions'}).reset_index()

    # Avoid clustering if not enough data
    if client_data.shape[0] < n_clusters:
        return pd.DataFrame()

    model = KMeans(n_clusters=n_clusters, random_state=42)
    features = client_data[['Revenue', 'Transactions']]
    client_data['Cluster'] = model.fit_predict(features)
    return client_data

def generate_alerts(anomaly_df):
    """
    Create alerts based on detected anomalies.
    """
    anomalies = anomaly_df[anomaly_df['Anomaly']]
    alerts = []
    for _, row in anomalies.iterrows():
        alert_msg = f"Anomaly detected for {row['Month'].strftime('%B %Y')}: Revenue {row['Revenue']} deviates from rolling average {row['RollingMean']:.2f}"
        alerts.append(alert_msg)
    return alerts
