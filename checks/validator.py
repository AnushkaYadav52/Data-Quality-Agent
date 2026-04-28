# Importing the pandas library. 
import pandas as pd 

# Function: Reads the CSV and loads the data into a DataFrame. 
def load_data(file_path): 
    df = pd.read_csv(file_path)
    return df

# Function: Checks for missing values in the DataFrame. 
def check_missing_values(df):
    # Empty list for any issues. 
    issues = []
    
    # df.isnull() --> Turns the table in true and false. 
    # .sum() --> Counts the number of true (missing values) per column. Becomes a series with column names and count of missing values. 
    missing = df.isnull().sum()

    # Iterate through through the series. 
    # .items turnns the series into a tupple of column name and count of missing values.
    for column, count in missing.items():
        # Should only loop if there is a missing value. 
        if count > 0:
            issues.append(f"{column} has {count} missing value(s).")
    return issues

# Function: Checks for duplicate rows in the DataFrame. 
def check_duplicates(df): 
    
    # Empty list for any issues. 
    issues = []

    # df.duplicated() --> Marks the repeated rows, as true and false. 
    # .sum() --> Counts the number of true (duplicated rows)
    duplicates = df.duplicated().sum()

    #Should only append if there is a duplicate. 
    if duplicates > 0:
        issues.append(f"{duplicates} duplicate row(s) found.")
    return issues

# Function: Checks email formatting in the DataFrame. 
def check_email_format(df): 

    # Empty list for any issues.    
    issues = []
    
    # Iterate through the columns of the DataFrame.
    for column in df.columns:
        #Find the email columns by looking for "email" in the column name.
        if "email" in column.lower():

            # Check if the email contains "@" symbol. If not, it's invalid.
            invalid = df[~df[column].astype(str).str.contains("@", na=False)]

            # Checks the count of invalid emails in each column.
            if len(invalid) > 0:
                issues.append(f"{len(invalid)} invalid email(s) found in the {column} column.")
    return issues

# Function: Checks for any empty strings in the DataFrame. 
def check_empty_strings(df):
    
    # Empty list for any issues.
    issues = []

    # Iterate through the columns of the DataFrame.
    for column in df.columns:
        # Count the number of empty strings in the column.
        empty_count = (df[column].astype(str).str.strip() == "").sum()

        # Checks the count of empty strings in each column.
        if empty_count > 0:
            issues.append(f"{empty_count} empty string(s) found in the {column} column.")

    return issues

# Function: Runs all the checks and returns a list of issues.
def run_all_checks(df): 

    # Empty list for any issues.
    issues = []

    # Run all checks and aggregate the issues.
    issues += check_missing_values(df)
    issues += check_duplicates(df)
    issues += check_email_format(df)
    issues += check_empty_strings(df)

    return issues 