# visualization.py

import streamlit as st
import matplotlib.pyplot as plt

def plot_monthly_revenue(monthly_df):
    st.subheader("Monthly Revenue")
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_df['Month'], monthly_df['Revenue'], marker='o')
    plt.plot(monthly_df['Month'], monthly_df['RollingMean'], linestyle='--', label='Rolling Mean')
    plt.fill_between(monthly_df['Month'], 
                     monthly_df['RollingMean'] - 2 * monthly_df['RollingStd'], 
                     monthly_df['RollingMean'] + 2 * monthly_df['RollingStd'], 
                     color='red', alpha=0.1, label='Anomaly Threshold')
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.title("Monthly Revenue with Anomaly Detection")
    plt.legend()
    st.pyplot(plt)

def plot_bar(data, x_col, y_col, title):
    st.subheader(title)
    plt.figure(figsize=(10, 5))
    plt.bar(data[x_col], data[y_col])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    st.pyplot(plt)

def display_table(data, title):
    st.subheader(title)
    st.dataframe(data)

def display_alerts(alerts):
    if alerts:
        st.subheader("Alerts")
        for alert in alerts:
            st.warning(alert)
    else:
        st.info("No anomalies detected.")

def plot_forecast(forecast_value):
    st.subheader("Run-rate Forecast")
    st.metric("Projected Month-End Revenue", f"₹{forecast_value:,.2f}")

def plot_speciality_tests(stats):
    st.subheader("Speciality Tests Summary")
    st.write(f"Total Tests ≥ ₹{999}: {stats['count']}")
    st.write(f"Total Revenue from Speciality Tests: ₹{stats['total_revenue']:,.2f}")
    st.write(f"Contribution to Total Revenue: {stats['percent_of_total']:.2f}%")

def plot_clients_added(monthly_clients, cumulative_clients):
    st.subheader("Clients Added")
    st.write(f"Total Unique Clients: {cumulative_clients}")
    plt.figure(figsize=(10, 5))
    plt.bar(monthly_clients['Month'], monthly_clients['PatientName'])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Month")
    plt.ylabel("Number of Clients Added")
    plt.title("Monthly Clients Added")
    st.pyplot(plt)

def plot_gross_vs_net(df):
    st.subheader("Gross vs Net Revenue")
    plt.figure(figsize=(10, 5))
    plt.plot(df['Month'], df['Gross'], marker='o', label='Gross')
    plt.plot(df['Month'], df['Revenue'], marker='o', label='Net')
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Gross vs Net Revenue Over Time")
    plt.legend()
    st.pyplot(plt)
