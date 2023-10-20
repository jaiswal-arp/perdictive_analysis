
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

    values = st.sidebar.slider('Select a range for Birth Year',1900, 2010, (1970, 1980))

    #Using match case to modify columns for the query
    var = a = b = c = d = e = f =0 
    
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

    match variable_list[2]:
        case "Primary":
            c = 'PRIMARY'
        case "Secondary":
            c = 'SECONDARY'
        case "College": 
            c = 'COLLEGE'
        case "2 Year Degree": 
            c = '2YRDEGREE'
        case "4 Year Degree": 
            c = '4YRDEGREE'
        case "Advanced": 
            c = 'ADVANCEDDEGREE'

    match variable_list[3]:
        case "Good":
            d = 'GOOD'
        case "High Risk":
            d = 'HIGHRISK'
        case "Low Risk": 
            d = 'LOWRISK'

    
    
    #Assign values to the parameters selected by user 
    e = values[0]
    f = values[1]

    #Update the query with all the parameter values
    updated_query = data['query'].format(a= a,b = b, c =c , d= d, e=e, f=f)


    if st.sidebar.button('Run'):
        try:
           df_clv = session.sql(updated_query).to_pandas()
           st.write("Query executed successfully")
           st.write(df_clv)
           aggregated_data = df_clv.groupby('BIRTH_YEAR').agg({'ACTUAL_SALES': 'sum', 'PREDICTED_SALES': 'sum'}).reset_index()
           st.line_chart(aggregated_data.set_index('BIRTH_YEAR'), color=["#FF0000", "#0000FF"])
        except Exception as e:
          st.error(f"Error executing the query: {str(e)}")

    
    
    
 
    
    