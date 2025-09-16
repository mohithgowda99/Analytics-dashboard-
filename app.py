# app.py

import streamlit as st
import pandas as pd

from config import REQUIRED_COLUMNS
from data_processing import process_file, combine_dataframes
from analytics import (
    total_revenue, monthly_revenue, average_ticket_size,
    speciality_tests, clients_added, revenue_by_salesperson,
    transactions_by_salesperson, referral_analysis,
    discount_trend, gross_vs_net, organisation_revenue,
    marketing_impact
)
from ml_models import anomaly_detection, run_rate_forecasting, generate_alerts
from visualization import (
    plot_monthly_revenue, plot_bar, display_table,
    display_alerts, plot_forecast, plot_speciality_tests,
    plot_clients_added, plot_gross_vs_net
)

def main():
    st.set_page_config(page_title="Analytics Dashboard", layout="wide")
    st.title("📊 Truemedix Analytics Dashboard")

    st.sidebar.header("Upload Data Files")
    historical_file = st.sidebar.file_uploader("Upload historical data (optional)", type=['xlsx', 'csv'])
    daily_file = st.sidebar.file_uploader("Upload today's data", type=['xlsx', 'csv'])

    if daily_file is not None:
        try:
            daily_df = process_file(daily_file)
        except Exception as e:
            st.error(f"Error processing daily file: {str(e)}")
            return

        dfs = [daily_df]
        if historical_file is not None:
            try:
                hist_df = process_file(historical_file)
                dfs.append(hist_df)
            except Exception as e:
                st.error(f"Error processing historical file: {str(e)}")
                return

        data = combine_dataframes(dfs)

        if not all(col in data.columns for col in REQUIRED_COLUMNS):
            st.error("Some required columns are missing after processing.")
            return

        # --- Analytics ---
        total_rev = total_revenue(data)
        avg_ticket = average_ticket_size(data)
        spec_tests = speciality_tests(data)
        monthly_rev = monthly_revenue(data)
        clients_monthly, clients_total = clients_added(data)
        sales_rev = revenue_by_salesperson(data)
        sales_trans = transactions_by_salesperson(data)
        referrals = referral_analysis(data)
        discounts = discount_trend(data)
        gross_net = gross_vs_net(data)
        org_rev = organisation_revenue(data)
        marketing_org, marketing_ref = marketing_impact(data)

        # --- Machine Learning ---
        anomalies = anomaly_detection(data)
        forecast = run_rate_forecasting(data)
        alerts = generate_alerts(anomalies)

        # --- Visualization ---
        st.header("Key Performance Indicators")
        st.metric("Total Revenue", f"₹{total_rev:,.2f}")
        st.metric("Average Ticket Size", f"₹{avg_ticket:,.2f}")
        plot_speciality_tests(spec_tests)
        plot_forecast(forecast)
        plot_clients_added(clients_monthly, clients_total)

        st.header("Revenue Trends")
        plot_monthly_revenue(anomalies)
        plot_gross_vs_net(gross_net)

        st.header("Detailed Analysis")
        plot_bar(sales_rev, 'Salesperson', 'Revenue', "Revenue by Salesperson")
        plot_bar(sales_trans, 'Salesperson', 'Transactions', "Transactions by Salesperson")
        plot_bar(referrals, 'Referral', 'Revenue', "Referral Revenue Impact")
        plot_bar(org_rev, 'Organisation', 'Revenue', "Organisation Revenue")
        plot_bar(discounts, 'Month', 'Discount', "Monthly Discount Trend")
        plot_bar(marketing_org, 'MarketingOrg', 'Revenue', "Marketing Organisation Impact")
        plot_bar(marketing_ref, 'MarketingReferral', 'Revenue', "Marketing Referral Impact")

        display_alerts(alerts)

    else:
        st.info("Please upload today's data file to view the dashboard.")

if __name__ == "__main__":
    main()
