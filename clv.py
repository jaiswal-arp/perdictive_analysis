
import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import *
import json
import numpy as np



def main():
    
    # Create a session to Snowflake with credentials
    with open("creds.json") as f:
       connection_parameters = json.load(f)
    session = Session.builder.configs(connection_parameters).create()
    session.use_warehouse("SNOWPARK_OPT_WH")
    session.use_database("TPCDS_XGBOOST")
    session.use_schema("DEMO")
    st.session_state['snowpark_session'] = session

    
    
    # Header
    head1, head2 = st.columns([8, 1])

    with head1:
      st.header("Customer Lifetime Value")
    
    
    
   # Open the JSON file for reading
    
    with open("./query.json") as f:
        data = json.load(f)  

    variable_list = []
    for var in data['variables']:
        var_value = st.sidebar.selectbox(label=var["name"], options= var["values"])
        variable_list.append(var_value)

    print(variable_list)
    var = a = b = 0 
    match variable_list[0]:
        case "Male":
            a = 'M'
        case "Female": 
            a = 'F'
                
    match variable_list[1]:
        case "Married":
            b = 'M'
        case "Single":
            b = 'S'
        case "Widowed": 
            b = 'W'
        case "Divorced": 
            b = 'D'
        case "Unknown": 
            b = 'U'
           
    updated_query = data['query'].format(a= a,b = b)
    print(updated_query)    
    if st.sidebar.button('Run'):
        try:
           df_clv = session.sql(updated_query).to_pandas()
           st.write("Query executed successfully")
           st.write(df_clv)
        except Exception as e:
          st.error(f"Error executing the query: {str(e)}")
    
    
 
    
    