import streamlit as st
from clv import main as clv_model
from home import main as homepage

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["HOME", "CLV", "PCS", "ROI"])

if page == "CLV":
    clv_model()
elif page == "HOME":
    homepage()

