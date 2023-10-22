# Assignment02



----- 
> [Live Application link](https://algodm-fall2023-team4-assignment02-streamlitmain-l1iq34.streamlit.app/) <br>
> [Codelab Slides](https://codelabs-preview.appspot.com/?file_id=1yFpF8W8DZRi_x_wzwsiOPCgmOqK-mBJh2v4GWBY8gVU#0) <br>
> [Application Demo/Presentation]()

----- 

## Index
  - [Objective](#objective)
  - [Project Structure](#project-structure)
  - [How to run the application](#how-to-run-the-application-locally)
----- 

## Objective
<replace-this>

## Project Structure
```
  ├── Assets                          # ipynb files
  │   ├── ROI
  │   ├── CLV
  │   └── PCS
  │── requirements.txt                  # relevant package requirements file for main
  └── streamlit
      ├── main.py                       # entry point for the streamlit application
      ├── roi.py
      ├── pcs.py
      ├── clv.py
      ├── forecast_anomaly_detection.py                      
      └── roi.py                        
```

## How to run the application
- Clone the repo to get all the source code on your machine

```bash
git clone https://github.com/AlgoDM-Fall2023-Team4/Assignment02.git
```
- All the code related to the streamlit is in the streamlit/ directory of the project

- First, create a virtual environment, activate and install all requirements from the requirements.txt file present
```bash
python -m venv <virtual_environment_name>
```
```bash
source <virtual_environment_name>/bin/activate
```
```bash
pip install -r <path_to_requirements.txt>
```
- Create all the required snowflake resources as per the documentation and also run all the models before proceeding further.

- Add all necessary credentials into a .env file:
```txt
SNOWFLAKE_USERNAME=<snowflake_username>
SNOWFLAKE_PASSWORD=**********
SNOWFLAKE_ACCOUNT_IDENTIFIER=<account_identifier>
SNOWFLAKE_DB=<db_name>
SNOWFLAKE_SCHEMA=<schema_name>
```

- Run the application

```bash
streamlit run streamlit/main.py
```

