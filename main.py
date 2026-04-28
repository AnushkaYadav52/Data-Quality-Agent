# Testing pandas version. 
'''import pandas as pd
print(pd.__version__)'''

# Testing requests.
'''import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)'''

# Testing dotenv.
'''from dotenv import load_dotenv
print("dotenv works")'''

# Import pandas.
import pandas as pd

# Import all functions. 
from checks.validator import run_all_checks
from ai.explainer import explain_issues
from api.fetch_data import fetch_api_data
from utils.report_writer import save_report_json

# Fetch the data from the API and store it in a DataFrame.
df = fetch_api_data()

#print(df)

# Run all data quality checks and get the list of issues.
issues = run_all_checks(df)

# Print the results.
print("\n🐼 DATA QUALITY REPORT\n")
if len(issues) == 0:
    print("No issues found. Data looks clean!")
else:
    for issue in issues:
        print("-", issue)


print("\n🤖 AI EXPLANATION\n")

# Get AI explanation for the issues and print it.
ai_output = explain_issues(issues, df)
print(ai_output)

# Clean the AI output and save the report as a JSON file.
ai_explanation_clean = ai_output.split("\n")
save_report_json(issues, ai_explanation_clean)

