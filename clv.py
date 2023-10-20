
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

    
        var = a = b = 0
        match variable_list[0]:
            case "Male":
                 b = 1
            case "Female": 
                 a = 1
                
        
           
    updated_query = data['query'].format(a= a,b = b)
    print(updated_query)    
    if st.sidebar.button('Run'):
        try:
           result = session.sql(updated_query)
           st.write("Query executed successfully")
           st.write(result)
        except Exception as e:
          st.error(f"Error executing the query: {str(e)}")
       
        
    
    st.write(variable_list)     
    
    
 
    
    
