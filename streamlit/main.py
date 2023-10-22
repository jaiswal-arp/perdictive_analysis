import streamlit as st
import roi, pcs,clv, forecast_anomaly_detection

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Forecast & Anomaly Detection", "Customer Lifetime Value", "Predict Customer Spend", "Return On Investment"])

if page == "Customer Lifetime Value":
    clv.main()
elif page == "Forecast & Anomaly Detection":
    forecast_anomaly_detection.main()
elif page == "Predict Customer Spend":
    pcs.main()
elif page == "Return On Investment":
    roi.main()


