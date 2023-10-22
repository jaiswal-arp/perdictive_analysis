import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

from dotenv import load_dotenv
from snowflake.snowpark.session import Session

load_dotenv()

connection_parameters = {
    "account": os.environ.get("SNOWFLAKE_ACCOUNT_IDENTIFIER"),
    "user": os.environ.get("SNOWFLAKE_USERNAME"),
    "password": os.environ.get("SNOWFLAKE_PASSWORD"),
    "database": "AD_FORECAST_DEMO",
    "schema": "DEMO"
}
session = Session.builder.configs(connection_parameters).create()

def call_foreacst_model(forecast_period: int):
    forecast_data = session.sql(f"CALL impressions_forecast!FORECAST(FORECASTING_PERIODS => {forecast_period})").collect()
    forecast_data_df = pd.DataFrame(forecast_data)
    actual_data_df = session.sql(
        "SELECT day AS ts, impression_count AS actual, NULL AS forecast, NULL AS lower_bound, NULL AS upper_bound FROM daily_impressions").to_pandas()
    complete_data = pd.concat([actual_data_df, forecast_data_df], ignore_index=True)

    return complete_data

def call_anomaly_detection(impressions:int, input_date):
    data = session.sql(f"CALL impression_anomaly_detector!DETECT_ANOMALIES( INPUT_DATA => SYSTEM$QUERY_REFERENCE('select \\'{input_date}\\'::timestamp as day, {impressions} as impressions'), TIMESTAMP_COLNAME => 'day', TARGET_COLNAME => 'impressions');").collect()
    data_df = pd.DataFrame(data)
    return data_df


def chart(complete_data):
    st.header("Line Chart")
    fig, ax = plt.subplots()

    ax.plot(complete_data['TS'], complete_data['ACTUAL'], label='Actual', color='purple')
    ax.plot(complete_data['TS'], complete_data['FORECAST'], label='Forecasted', color='yellow')
    ax.scatter(complete_data['TS'], complete_data['FORECAST'], color='red', s=10)

    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Values')
    ax.legend()

    st.pyplot(fig)

def main():
    tab1, tab2 = st.tabs(["Forecast", "Anomaly Detection"])
    with tab1:
        st.title("Forecast")
        value = st.slider("Forecast Period", 1, 30, 14)
        data = call_foreacst_model(value)
        st.write(data)
        chart(data)
    with tab2:
        st.title("Anomaly Detection")
        input_date = st.date_input(label="timestamp", value=date(2022, 12, 6))
        formatted_date = input_date.strftime('%Y-%m-%d')
        impressions = int(st.text_input("Enter no. of impressions", value="0"))
        if st.button("Submit"):
            data_df = call_anomaly_detection(impressions, formatted_date)
            st.write(data_df)


