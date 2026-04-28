# Python's tool that let's you read enviorment variables and interact with the Gemini API.
import os 

# Tell Python to read the .env file and load the variables into the environment.
from dotenv import load_dotenv

# Load the environment variables from the .env file.
load_dotenv()

# Import Groq client. 
# Client --> Connection to the Groq API. 
from groq import Groq

# api_key=os.getenv("GROQ_API_KEY") --> Getting the API key from the enviorment variable. 
# Initialize the Groq client with the API key.
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function: Communicates with the AI agent, sharing the prompt and returns a response in text.
def explain_issues(issues, df):

    # Instructions for the AI Agent.
    # Includes data quality issues, data, missing values and instructions on how to format the response.
    prompt = f"""
You are a senior data engineer. Use the following data quality issues and the sample data to provide a clear and concise explanation of each issue, why it matters, and how to fix it using SQL.
DATA QUALITY ISSUES:
{issues}
DATA:
{df.to_string()}
MISSING VALUES:
{df.isnull().sum().to_string()}

If no issues are found, respond with "No issues found. Data looks clean!"

Return the response in STRICT format:

For each issue, use this format:
1. ISSUE NAME
- Summary: ((2-3 lines max)
- Why it matters: (2-3 lines max)

SQL Fix:
(provide clean SQL only)

2. ISSUE NAME
- Summary: ((2-3 lines max)
- Why it matters: (2-3 lines max)

SQL Fix:
(provide clean SQL only)
...
---
Rules:
- Keep it structured
- No long paragraphs
- Use bullet points only
- Be concise
- Use headings exactly as shown
"""
    
    # Send the prompt to the AI model and get the response.
    # Include the model name and the prompt in the request to the Groq API.
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the content from the response and return it.
    result = response.choices[0].message.content
    return result.strip()
