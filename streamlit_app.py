'''import streamlit as st
import pandas as pd
import json
from datetime import datetime

from checks.validator import run_all_checks
from ai.explainer import explain_issues
from api.fetch_data import fetch_api_data
from utils.report_writer import save_report_json

# Set the Browser Tab name and page layout to wide. 
st.set_page_config(page_title="Data Quality Agent", layout="wide")

st.markdown("""
<style>

/* Reduce top spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 2000px;
}

/* Main app background */
[data-testid="stAppViewContainer"] {
    background-color: #0F172A;
}

/* FIX 1: Make the top header bar dark instead of white */
[data-testid="stHeader"] {
    background-color: #0F172A;
    border-bottom: 1px solid #1F2937;
}

/* Also target the toolbar area */
[data-testid="stToolbar"] {
    background-color: #0F172A;
}

/* Main content area */
.main {
    background-color: #0F172A;
}

/* Text color */
h1, h2, h3, h4, h5, h6, p, span, div {
    color: #E5E7EB;
}

/* Subtle section separation */
.section {
    padding: 1.2rem 0;
    border-bottom: 1px solid #1F2937;
}

/* Dataframe styling */
[data-testid="stDataFrame"] {
    background-color: #1E293B;
    border-radius: 8px;
    padding: 10px;
}

/* Buttons (primary) */
.stButton>button {
    background-color: #6366F1;
    color: white;
    border-radius: 6px;
    border: none;
    padding: 0.5rem 1rem;
}

/* Download button */
.stDownloadButton>button {
    background-color: #6366F1;
    color: white;
    border-radius: 6px;
    border: none;
    padding: 0.5rem 1rem;
}

/* Success message */
.stAlert-success {
    background-color: #064E3B;
    color: #D1FAE5;
}

/* Spinner text */
.stSpinner > div {
    color: #9CA3AF;
}

/* FIX 2: Style inline code and code blocks from st.markdown */
code {
    color: #7DD3FC !important;
    background-color: #1E293B !important;
}

pre {
    background-color: #1E293B !important;
    border-radius: 6px;
    padding: 1rem;
    border: 1px solid #334155;
}

pre code {
    color: #7DD3FC !important;
    background-color: transparent !important;
    white-space: pre-wrap;
}

</style>
""", unsafe_allow_html=True)

# Sets the title of the page. 
# Note: Tile is for large headings. 
st.title("🧹 AI Data Quality ELT Dashboard")

# Sets the description of the page.
# Write is for regular text/small descriptions.. 
st.markdown("""
**Pipeline Overview**

- 📥 **Data ingestion from API**  
  Data is fetched programmatically from an external API and loaded into a Pandas DataFrame for processing.

- 🐼 **Data quality checks using Python & Pandas**  
  The dataset is analyzed for missing values, duplicates, invalid emails, and empty strings using automated validation functions.

- 🤖 **GROQ AI generates explanations + SQL fixes**  
  Detected issues are passed to a GROQ-powered AI agent, which explains each problem and suggests SQL-based fixes.

- 🧾 **JSON report exported for backend use**  
  A structured report containing timestamps, issues, and AI-generated insights is saved as a JSON file for downstream systems or auditing.
""")

df = fetch_api_data()

st.subheader("📊 Raw Dataset Preview")
st.dataframe(df)

issues = run_all_checks(df)

st.subheader("🚩 Data Quality Issues Detected"
             )
if issues:
    for issue in issues:
        st.write("•", issue)
else:
    st.success("No issues found 🎉")


st.subheader("🤖 AI Explanation of Issues")

if st.button("Generate AI Report"):
    with st.spinner("AI is analyzing data..."):
        ai_output = explain_issues(issues, df)

    st.markdown(ai_output)

    #ai_explanation_clean = ai_output.split("\n")
    #save_report_json(issues, ai_explanation_clean)
    

    ai_explanation_clean = ai_output.split("\n")

    # Create report dictionary
    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
        "issues": issues,
        "ai_explanation": ai_explanation_clean
    }

    # Convert to JSON string (THIS is what download needs)
    json_data = json.dumps(report, indent=4)

    # Optional: still save in backend
    save_report_json(issues, ai_explanation_clean)

    # Download button
    st.download_button(
        label="📥 Download JSON Report",
        data=json_data,
        file_name="data_quality_report.json",
        mime="application/json"
    )'''

# Importing necessary libraries. 
import streamlit as st
import pandas as pd
import json
from datetime import datetime

# Importing all functions from different modules.
from checks.validator import run_all_checks
from ai.explainer import explain_issues
from api.fetch_data import fetch_api_data
from utils.report_writer import save_report_json

st.set_page_config(page_title="Data Quality Agent", layout="wide")

st.markdown("""
<style>

/* ── Layout ── */
.block-container {
    padding-top: 5rem;
    padding-bottom: 2rem;
    max-width: 1700px;
}

/* ── Backgrounds ── */
[data-testid="stAppViewContainer"] { background-color: #080F1E; }
.main                               { background-color: #080F1E; }

/* ── Hide default Streamlit header & replace with custom one ── */
[data-testid="stHeader"]  { display: none; }
[data-testid="stToolbar"] { display: none; }

/* ── Custom fixed header ── */
.custom-header {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 9999;
    background-color: #0D1526;
    border-bottom: 1px solid #1E3A5F;
    padding: 0.75rem 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.custom-header .logo {
    font-size: 1.15rem;
    font-weight: 700;
    color: #E2E8F0;
    letter-spacing: 0.3px;
}
.custom-header .badge {
    font-size: 0.72rem;
    background-color: #1E3A5F;
    color: #7DD3FC;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    border: 1px solid #2563EB44;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* ── Typography ── */
h1, h2, h3, h4, h5, h6 { color: #F1F5F9 !important; }
p, span, li             { color: #FFFFFF; }

/* ── Section subheaders ── */
.stSubheader, [data-testid="stSubheader"] { color: #7DD3FC !important; }

/* ── Pipeline overview cards ── */
.pipeline-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 1.5rem 0 2rem 0;
}
.pipeline-card {
    background-color: #0D1B2E;
    border: 1px solid #1E3A5F;
    border-radius: 10px;
    padding: 1rem 1.2rem;
}
.pipeline-card .icon { font-size: 1.4rem; margin-bottom: 0.4rem; }
.pipeline-card .label {
    font-size: 0.8rem;
    font-weight: 600;
    color: #7DD3FC;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
}
.pipeline-card .desc { font-size: 0.82rem; color: #FFFFFF; line-height: 1.4; }

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    background-color: #0D1B2E;
    border: 1px solid #1E3A5F;
    border-radius: 10px;
    padding: 8px;
}

/* ── Issue bullets ── */
.issue-item {
    background-color: #130F23;
    border-left: 3px solid #A78BFA;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    margin-bottom: 0.5rem;
    font-size: 0.88rem;
    color: #FFFFFF;
    box-shadow: inset 0 0 0 1px #2D1F5E, 0 0 8px #7C3AED33;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.55rem 1.4rem;
    font-weight: 600;
    letter-spacing: 0.3px;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }

.stDownloadButton > button {
    background: linear-gradient(135deg, #0369A1, #0EA5E9);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.55rem 1.4rem;
    font-weight: 600;
}

/* ── Code blocks ── */
code {
    color: #7DD3FC !important;
    background-color: #0D1B2E !important;
    border-radius: 4px;
    padding: 0.15rem 0.4rem;
}
pre {
    background-color: #0D1B2E !important;
    border: 1px solid #1E3A5F;
    border-radius: 8px;
    padding: 1rem;
}
pre code {
    color: #7DD3FC !important;
    background-color: transparent !important;
}

/* ── Success / alerts ── */
.stAlert { border-radius: 8px; }

/* ── Spinner ── */
.stSpinner > div { color: #7DD3FC; }

</style>

<!-- Fixed header -->
<div class="custom-header">
    <span class="logo">🧹 AI Data Quality ELT Dashboard</span>
    <span class="badge">⚡ GROQ Powered</span>
</div>
""", unsafe_allow_html=True)


# ── Pipeline Overview Cards ──
st.markdown("""
<div class="pipeline-grid">
    <div class="pipeline-card">
        <div class="icon">📥</div>
        <div class="label">Data Ingestion</div>
        <div class="desc">Fetched from external API into a Pandas DataFrame.</div>
    </div>
    <div class="pipeline-card">
        <div class="icon">🐼</div>
        <div class="label">Quality Checks</div>
        <div class="desc">Scans for nulls, duplicates, invalid emails & empty strings.</div>
    </div>
    <div class="pipeline-card">
        <div class="icon">💡</div>
        <div class="label">AI Analysis</div>
        <div class="desc">GROQ AI agent explains issues and suggests SQL fixes.</div>
    </div>
    <div class="pipeline-card">
        <div class="icon">🧾</div>
        <div class="label">JSON Export</div>
        <div class="desc">Structured report saved for downstream auditing.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Fetch the data from the API and store it in a DataFrame.
df = fetch_api_data()

# Display the raw dataset in a table format.
st.subheader("📊 Raw Dataset Preview")
st.dataframe(df, use_container_width=True)

# Run all data quality checks and get the list of issues.
issues = run_all_checks(df)

# Display the data quality issues in a styled format.
st.subheader("🚩 Data Quality Issues Detected")
if issues:
    for issue in issues:
        st.markdown(f'<div class="issue-item">⚠ {issue}</div>', unsafe_allow_html=True)
else:
    st.success("No issues found 🎉")

# Display the AI explanation section with a button to generate the report.
st.subheader("🤖 AI Explanation of Issues")

# When the button is clicked, generate the AI report, display it, and provide a download option for the JSON report.
if st.button("Generate AI Report"):
    with st.spinner("AI is analyzing data..."):

        # Get AI explanation for the issues. 
        ai_output = explain_issues(issues, df)

    # Display the AI output in a markdown format to preserve styling.
    st.markdown(ai_output)
    
    # Clean the AI output and prepare the report for JSON export.
    ai_explanation_clean = ai_output.split("\n")

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
        "issues": issues,
        "ai_explanation": ai_explanation_clean
    }
    json_data = json.dumps(report, indent=4)

    # Optionally save the report in the backend as well.
    save_report_json(issues, ai_explanation_clean)

    # Provide a download button for the JSON report.
    st.download_button(
        label="📥 Download JSON Report",
        data=json_data,
        file_name="data_quality_report.json",
        mime="application/json"
    )