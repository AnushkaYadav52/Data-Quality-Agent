# Import json
import json

# Import datetime for timestamping the report.
from datetime import datetime

# Function: Saves the data quality issues and AI explanations into a JSON file with a timestamped filename.
def save_report_json(issues, ai_output):

    # Create a timestamp for the filename.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a filename using the timestamp.
    filename = f"report_{timestamp}.json"

    # Create a dictionary to store the data quality issues and AI explanations.
    data = {
        "timestamp": timestamp,
        "issues": issues,
        "ai_explanation": ai_output
    }

    # Write the data to the JSON file with proper formatting.
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    # Print a message to confirm that the report has been saved.
    print(f"\n📄 JSON report saved as: {filename}")