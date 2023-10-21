import streamlit as st
import roi, forecast_anomaly_detection,pcs,clv

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Forecast & Anomaly Detection", "Customer Lifetime Value", "Predict Customer Spend", "Return On Investment"])

if page == "Customer Lifetime Value":
    clv_model()
elif page == "Forecast & Anomaly Detection":
    homepage()
    clv.main()
    pass
elif page == "Predict Customer Spend":
    pcs.main()
    pass
elif page == "Return On Investment":
    roi.main()


