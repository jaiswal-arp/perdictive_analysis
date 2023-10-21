
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
    st.header("Customer Lifetime Value")
    
    
    
   # Open the JSON file for reading
    
    with open("./query.json") as f:
        data = json.load(f)  

    
    #Parsing the variables in json file
    variable_list = []
    for var in data['variables']:
        var_value = st.sidebar.selectbox(label=var["name"], options= var["values"])
        variable_list.append(var_value)

    #Slider for Birth Year selection
    values = st.sidebar.slider('Select a range for Birth Year',1900, 2010, (1970, 1980))

    #Using match case to modify columns for the query
    var = a = b = c = d = e = f =0 
    
    if variable_list[0] == "Male":
            a = 'M'
    elif variable_list[0] == "Female":  
            a = 'F'
            
                
    if variable_list[1] == 'Married':
            b = 'M'
    elif variable_list[1] == 'Single': 
            b = 'S'       
    elif variable_list[1] == 'Widowed': 
            b = 'W'            
    elif variable_list[1] == 'Divorced': 
            b = 'D'            

    
    if variable_list[2] == 'Primary': 
            c = 'PRIMARY' 
    elif variable_list[2] == 'SEecondary': 
            c = 'SECONDARY'  
    elif variable_list[2] == 'College': 
            c = 'COLLEGE' 
    elif variable_list[2] == '2 Year Degree': 
            c = '2YRDEGREE'  
    elif variable_list[2] == '4 Year Degree': 
            c = '4YRDEGREE'
    elif variable_list[2] == 'Advanced Degree': 
            c = 'Advanced'

            
    if variable_list[3] == 'Good': 
            d = 'GOOD'   
    elif variable_list[3] == 'High Risk': 
            d = 'HIGHRISK' 
    elif variable_list[3] == 'Low Risk': 
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
           aggregated_data = df_clv.groupby('BIRTH_YEAR').agg({'ACTUAL_SALES': 'sum', 'PREDICTED_SALES': 'sum'}).reset_index()
           st.line_chart(aggregated_data.set_index('BIRTH_YEAR'), color=["#FF0000", "#0000FF"])
           st.write(df_clv)
        except Exception as e:
          st.error(f"Error executing the query: {str(e)}")

    
    
    
 
    
    
