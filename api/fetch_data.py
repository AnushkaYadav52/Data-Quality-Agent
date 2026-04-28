import requests
import pandas as pd

# Functions: Introduces data quality issues into the DataFrame for testing purposes.
# Creates missing values, duplicate rows, invalid email formats, and empty strings in the data.
def introduce_data_issues(df):

    # Introduce missing values. 
    df.loc[0, "name"] = None
    df.loc[1, "email"] = None
    df.loc[2, "username"] = None

    # Introduce duplicate rows.
    df = pd.concat([df, df.iloc[[7]]], ignore_index=True)

    # Introduce invalid email format.
    df.loc[3, "email"] = "invalidemail.com"
    
    # Introduce empty strings.
    df.loc[5, "name"] = ""
    df.loc[8, "website"] = " "

    # Return the modified DataFrame.
    return df

# Function: Fetches data from the API and returns it as a DataFrame.
def fetch_api_data():

    # Define the API endpoint URL.
    url = "https://jsonplaceholder.typicode.com/users"

    # This calls the API endpoint and gets a response.
    response = requests.get(url)

    # Convert JSON response into Python list.
    data = response.json()

    # Converts the Python list into a DataFrame. 
    df = pd.DataFrame(data)

    # Keep only useful columns
    df = df[["id", "name", "username", "email", "phone", "website"]]

    #Introduce data quality issues for testing, as the API data is clean.
    df = introduce_data_issues(df)

    # Return the DataFrame.
    return df
    