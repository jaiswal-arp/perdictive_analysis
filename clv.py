
import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import *
import json
import time
import numpy as np

def main():
    
    # Create a session to Snowflake with credentials
    with open("creds.json") as f:
       connection_parameters = json.load(f)
    session = Session.builder.configs(connection_parameters).create()


    # Header
    head1, head2 = st.columns([8, 1])

    with head1:
      st.header("Customer Lifetime Value")
