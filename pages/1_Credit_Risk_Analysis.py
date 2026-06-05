import streamlit as st
import pandas as pd
import os

# Page Configuration
st.set_page_config(page_title="Credit Risk Analysis Project", page_icon="🏦", layout="centered")

# ==========================================
# CUSTOM CSS: NATIVE SIDEBAR NAVIGATION & TEXT
# ==========================================
st.markdown("""
    <style>
    /* Styling teks agar tidak terpotong */
    .stMarkdown p {
        word-break: normal !important;
        overflow-wrap: normal !important;
    }
    .stMarkdown a {
        white-space: nowrap !important;
    }
    
    /* 1. Sembunyikan teks asli "app" dengan mengecilkan ukurannya */
    span[label="app"] {
        font-size: 0px !important;
    }
    
    /* 2. Munculkan teks baru "About Me" di titik yang sama */
    span[label="app"]::before {
        content: "About Me";
        font-size: 18px !important;
        font-weight: 800 !important;
        visibility: visible !important;
    }
    
    /* 3. Membuat tulisan pemisah "P R O J E C T S" di bawah menu */
    div[data-testid="stSidebarNav"] ul li:nth-child(1)::after {
        content: "P R O J E C T S";
        display: block;
        margin-top: 30px;
        margin-bottom: 10px;
        margin-left: 0px;
        font-size: 13px;
        font-weight: 700;
        color: #888;
        letter-spacing: 1px;
    }

    /* 4. Sembunyikan teks asli "Credit Risk Analysis" dengan mengecilkan ukurannya */
        span[label="Credit Risk Analysis"] {
        font-size: 0px !important;
    }

    /* 5. Munculkan teks baru "Credit Risk Analysis" di titik yang sama */
    span[label="Credit Risk Analysis"]::before {
        content: "Credit Risk Analysis Project";
        font-size: 15px !important;
        visibility: visible !important;
    }

    /* 6. Menghilangkan garis separator bawaan Streamlit */
    div[data-testid="stSidebarNavSeparator"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)
# ==========================================

st.title("Credit Risk Analysis Project")
st.caption("Context: This is an independent portfolio project. The raw data was sourced from Kaggle to practice analyzing a Fintech lending dataset.")
st.divider()

# SIDEBAR NAVIGATION (INTERNAL TABS)
st.sidebar.markdown("---")
st.sidebar.header("Navigation")

if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Project Overview"

tab_names = [
    "Project Overview", 
    "Phase 1: SQL", 
    "Phase 2: Python", 
    "Phase 3: Power BI",
    "Ad-Hoc Request",
    "Project Files"
]

for tab in tab_names:
    button_type = "primary" if st.session_state.active_tab == tab else "secondary"
    
    if st.sidebar.button(tab, type=button_type, use_container_width=True):
        st.session_state.active_tab = tab
        st.rerun()

@st.cache_data
def load_raw_data():
    file_path = "data/credit_risk_analysis/credit_risk_dataset.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

df_raw = load_raw_data()

active_tab = st.session_state.active_tab

# TAB 1: PROJECT OVERVIEW
if active_tab == "Project Overview":
    
    st.info("""
    **Technical Skills & Tools:**
    - **Programming & Database:** Python (Pandas, NumPy), SQL, PostgreSQL, pgAdmin4
    - **Data Analytics & Visualization:** Power BI, Dashboarding, Streamlit
    - **Analytical Methodologies:** Exploratory Data Analysis (EDA), Data Cleaning, Data Profiling, Outlier Detection, Missing Value Imputation, Ad-Hoc Analysis, Relational Database Design (DDL)
    - **Domain Knowledge:** Credit Risk Analysis, Non-Performing Loan (NPL) Monitoring
    """)
    st.divider()

    st.header("Project Context & Summary")
    st.write("The goal of this project is to understand credit default risks by analyzing historical borrower data and finding useful patterns.")
    
    st.write("")
    st.markdown("### - **Key Findings** -")
    st.write("""
    Based on the analysis using Python and Power BI, here are the main findings:
    - **Overall Performance:** The total Non-Performing Loan (NPL) rate is **21.55%**.
    - **Renter Risk:** Borrowers who **RENT** have a higher default rate of **31.08%** compared to homeowners.
    - **Loan Purpose:** Loans taken for **DEBT CONSOLIDATION** have the highest default rate among loan types at **28.38%**.
    - **Specific Group Risk (Ad-Hoc):** Young borrowers (<= 25 years old) with high interest rates (> 15%) have a very high default rate of **60.69%**.
    """)
    
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Overall Portfolio NPL", value="21.55%")
    c2.metric(label="Renter Segment Default Rate", value="31.08%", delta="High Risk")
    c3.metric(label="Ad-Hoc High-Interest Segment NPL", value="60.69%", delta="Critical Risk")
    
    st.write("")
    st.markdown("### - **Recommendations** -")
    st.success("""
    Based on the findings, here are a few suggestions:
    1. **Review Renter Policies:** Consider asking for more collateral or a co-signer for applicants who **RENT** to manage their 31.08% default risk.
    2. **Limit Debt Consolidation Loans:** We might need to set a lower maximum loan amount for **DEBT CONSOLIDATION** to reduce overall risk.
    3. **Re-evaluate Young Borrower Criteria:** Consider pausing loan approvals for borrowers **under 25 years old** with interest rates **> 15%**, because a 60.69% NPL indicates they struggle to pay back the loan.
    """)
    
    st.divider()
    st.markdown("### - **Raw Dataset Preview** -")
    if df_raw is not None:
        st.dataframe(df_raw.head(), use_container_width=True)
    else:
        st.warning("'credit_risk_dataset.csv' is missing from the data folder.")

# TAB 2: SQL
elif active_tab == "Phase 1: SQL":
    st.header("Phase 1: Database Ingestion & SQL Pre-Filtering")
    st.write("To practice working with databases, I imported the raw CSV into a local PostgreSQL database (`prt_credit_risk_db`) and used SQL to extract the data instead of loading it directly into Python.")
    
    st.markdown("### Step 1: Table Creation (DDL)")
    st.markdown("**What I Did:** I created the database table in pgAdmin4. I chose the standard data types (`INT`, `FLOAT`, `VARCHAR`) for each column based on the raw dataset to make sure the data is imported correctly.")
    st.code("""
CREATE TABLE loan_portfolio ( 
    person_age INT, 
    person_income INT, 
    person_home_ownership VARCHAR(20), 
    person_emp_length FLOAT, 
    loan_intent VARCHAR(50), 
    loan_grade VARCHAR(5), 
    loan_amnt INT, 
    loan_int_rate FLOAT, 
    loan_status INT, 
    loan_percent_income FLOAT, 
    cb_person_default_on_file VARCHAR(5), 
    cb_person_cred_hist_length INT 
);
    """, language="sql")

    st.divider()

    st.markdown("### Step 2: Data Extraction & Pre-Filtering")
    st.markdown("**What I Did:** I wrote a SQL `SELECT` query to get the columns I needed. I used a `WHERE` clause to filter the data, excluding applicants under 21 years old and removing rows where the target label (`loan_status`) was missing.")
    st.code("""
SELECT 
    person_age,
    person_income,
    person_home_ownership,
    person_emp_length,
    loan_intent,
    loan_grade,
    loan_amnt,
    loan_int_rate,
    loan_status 
FROM loan_portfolio 
WHERE person_age >= 21
AND loan_status IS NOT NULL;
    """, language="sql")
    
    st.markdown("**pgAdmin4 Data Output Preview:**")
    st.code("""
 person_age | person_income | person_home_ownership | person_emp_length | loan_intent | loan_grade | loan_amnt | loan_int_rate | loan_status 
------------+---------------+-----------------------+-------------------+-------------+------------+-----------+---------------+-------------
         22 |         59000 | RENT                  |             123.0 | PERSONAL    | D          |     35000 |         16.02 |           1
         21 |          9600 | OWN                   |               5.0 | EDUCATION   | B          |      1000 |         11.14 |           0
...
(32566 rows returned)
    """, language="text")
    st.caption("Data Export: I successfully exported this query output as `01_extracted_loan_data.csv` for the next step in Python.")

# TAB 3: PYTHON
elif active_tab == "Phase 2: Python":
    st.header("Phase 2: Python Data Profiling, Cleaning & EDA")
    
    st.markdown("### Step 1: Data Ingestion & Initial Profiling")
    st.markdown("**What I Did:** I loaded the SQL data into a Pandas DataFrame. I used `.info()` to check for empty values and `.describe()` to see the basic statistics. I found some strange values right away, like a maximum age of 144 and an employment length of 123 years.")
    st.code("""
import pandas as pd

df = pd.read_csv('01_extracted_loan_data.csv')
print("--- DATA INFO ---")
df.info()

print("\\n--- STATISTICAL SUMMARY ---")
df.describe()
    """, language="python")
    st.markdown("**Console Output:**")
    st.code("""
--- DATA INFO ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32566 entries, 0 to 32565
Data columns (total 9 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   person_age             32566 non-null  int64  
 1   person_income          32566 non-null  int64  
 2   person_home_ownership  32566 non-null  object 
 3   person_emp_length      31671 non-null  float64 
 4   loan_intent            32566 non-null  object 
 5   loan_grade             32566 non-null  object 
 6   loan_amnt              32566 non-null  int64  
 7   loan_int_rate          29451 non-null  float64 
 8   loan_status            32566 non-null  int64  

--- STATISTICAL SUMMARY ---
         person_age  person_income  person_emp_length      loan_amnt  loan_int_rate   loan_status
count  32566.000000   3.256600e+04       31671.000000   32566.000000   29451.000000  32566.000000
max      144.000000   6.000000e+06         123.000000   35000.000000      23.220000      1.000000
    """, language="text")

    st.divider()

    st.markdown("### Step 2: Data Cleaning (Outliers & Missing Values)")
    st.markdown("**What I Did:** To clean the data, I filtered out the extreme outliers (keeping age < 100 and employment length < 60). Then, I filled the missing values in `person_emp_length` and `loan_int_rate` using the median value, so I didn't have to delete those rows.")
    st.code("""
# Filtering out impossible values (age < 100, employment length < 60)
df_clean = df[(df['person_age'] < 100) & (df['person_emp_length'] < 60)].copy()

# Median Imputation for missing values
df_clean['person_emp_length'] = df_clean['person_emp_length'].fillna(df_clean['person_emp_length'].median())
df_clean['loan_int_rate'] = df_clean['loan_int_rate'].fillna(df_clean['loan_int_rate'].median())

print("Total rows after cleaning:", len(df_clean))
print("\\nMissing Values Check:")
print(df_clean.isnull().sum())
    """, language="python")
    st.markdown("**Console Output:**")
    st.code("""
Total rows after cleaning: 31664

Missing Values Check:
person_age               0
person_income            0
...
dtype: int64
    """, language="text")

    st.divider()

    st.markdown("### Step 3: Exploratory Data Analysis (Hypothesis Testing)")
    st.markdown("**What I Did:** I wanted to see what factors might cause loan defaults. By grouping the data by `loan_status`, I calculated the overall Non-Performing Loan (NPL) rate and checked the risk levels based on Home Ownership and Loan Intent.")
    st.code("""
# Calculate Overall Portfolio NPL
print(f"Total Default Rate (NPL): {df_clean['loan_status'].mean() * 100:.2f}%\\n")

# Risk based on Home Ownership
print("--- DEFAULT RATE BY HOME OWNERSHIP (%) ---")
print(df_clean.groupby('person_home_ownership')['loan_status'].mean() * 100)

# Risk based on Loan Intent
print("\\n--- DEFAULT RATE BY LOAN INTENT (%) ---")
print(df_clean.groupby('loan_intent')['loan_status'].mean() * 100)
    """, language="python")
    st.markdown("**Console Output:**")
    st.code("""
Total Default Rate (NPL): 21.55%

--- DEFAULT RATE BY HOME OWNERSHIP (%) ---
person_home_ownership
RENT        31.080408
OTHER       30.841121
MORTGAGE    12.455081
OWN          6.929461

--- DEFAULT RATE BY LOAN INTENT (%) ---
loan_intent
DEBTCONSOLIDATION    28.387989
MEDICAL              26.543419
HOMEIMPROVEMENT      25.555556
    """, language="text")
    
    st.info("""
    **Phase 2 Insights:**
    * **Home Ownership:** Borrowers who RENT have the highest default rate at 31.08%.
    * **Loan Intent:** Loans taken for DEBT CONSOLIDATION have the highest risk at 28.38%.
    """)
    st.success("""
    **Phase 2 Recommendations:**
    * Consider asking for a larger down payment or collateral for Renters.
    * Review the requirements for approving Debt Consolidation loans.
    """)

    st.divider()

    st.markdown("### Step 4: Exporting Clean Data for Dashboarding")
    st.markdown("**What I Did:** After cleaning the data, I saved the final DataFrame into a new CSV file without the Pandas index, making it easier to load into Power BI.")
    st.code("""
# Exporting the finalized, clean dataset for Power BI ingestion
df_clean.to_csv('03_cleaned_loan_data.csv', index=False)
    """, language="python")

# TAB 4: POWER BI
elif active_tab == "Phase 3: Power BI":
    st.header("Phase 3: Power BI Dashboard")
    st.markdown("**What I Did:** I connected the cleaned dataset (`03_cleaned_loan_data.csv`) to Power BI and built a simple dashboard. I focused on 3 main charts to give a clear view of the loan performance.")
    
    if os.path.exists("assets/dashboard_screenshot.png"):
        st.image("assets/dashboard_screenshot.png", caption="Power BI Risk Monitoring Dashboard Snapshot", use_container_width=True)
    else:
        st.warning("Place your dashboard screenshot as 'dashboard_screenshot.png' inside your assets folder to show it here.")

    st.info("""
    **Phase 3 Insights:**
    * **KPI Card (Total NPL):** *Our overall Non-Performing Loan rate is **21.55%**.*
    * **Bar Chart 1 (Home Ownership):** *Borrowers who **RENT** have the highest default rate, noticeably higher than those with a Mortgage.*
    * **Bar Chart 2 (Loan Intent):** ***DEBT CONSOLIDATION** is the category with the most defaults compared to other loan types.*
    """)
    
    st.success("""
    **Phase 3 Recommendations:**
    1. **Stricter Rules for Renters:** Ask for additional collateral or co-signers for applicants who RENT.
    2. **Lower Debt Consolidation Limits:** Consider lowering the maximum loan amount for Debt Consolidation to reduce risk.
    """)

# TAB 5: AD-HOC
elif active_tab == "Ad-Hoc Request":
    st.header("Ad-Hoc Request: High-Interest Youth Segment")
    st.write("**Scenario:** I wanted to investigate young borrowers (<= 25 years old) who have high interest rates (> 15%).")
    st.markdown("**What I Did:** To answer this request, I wrote a SQL query to filter this specific group, exported the data, and used Python to calculate their NPL rate.")
    
    st.markdown("### 1. SQL Extraction")
    st.code("""
SELECT person_age, loan_intent, loan_int_rate, loan_status 
FROM loan_portfolio 
WHERE person_age <= 25 
  AND loan_int_rate > 15 
  AND loan_status IS NOT NULL;
    """, language="sql")
    
    st.markdown("**Query Output Preview:**")
    st.code("""
 person_age | loan_intent       | loan_int_rate | loan_status 
------------+-------------------+---------------+-------------
         22 | PERSONAL          |         16.02 |           1
         23 | MEDICAL           |         15.23 |           1
...
(1595 rows returned)
    """, language="text")
    
    st.divider()
    
    st.markdown("### 2. Python NPL Calculation")
    st.code("""
import pandas as pd
df_adhoc = pd.read_csv('ad_hoc_young_risk.csv')

total = len(df_adhoc)
npl = df_adhoc['loan_status'].mean() * 100

print(f"Total: {total} borrowers")
print(f"NPL: {npl:.2f}%")
    """, language="python")
    
    st.markdown("**Console Output:**")
    st.code("""
Total: 1595 borrowers
NPL: 60.69%
    """, language="text")
    
    st.error("**Key Finding:** Out of **1,595** young borrowers with high interest rates, the default rate was **60.69%** (which is much higher than the average).")
    
    st.success("""
    **Recommendations:**
    * **Suggestion:** Consider pausing approvals for borrowers under 25 years old with interest rates > 15%. 
    * **Reason:** The data suggests that this group struggles to pay back loans with such high interest rates. Continuing to approve these loans might result in more defaults.
    """)

# TAB 6: FILES
elif active_tab == "Project Files":
    st.header("Project Repository Access")
    def create_download_button(file_path, label, mime_type, description):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(label=label, data=f, file_name=os.path.basename(file_path), mime=mime_type, use_container_width=True)
                st.caption(description)
        else:
            st.warning(f"File {os.path.basename(file_path)} placeholder active.")

    st.markdown("### 1. Code & Automation Scripts")
    create_download_button("data/credit_risk_analysis/02_data_cleaning_and_eda.ipynb", "Download Jupyter Notebook (.ipynb)", "application/vnd.jupyter", "Contains Data Cleaning & EDA logic.")
    
    st.markdown("### 2. Datasets & Exports")
    c1, c2 = st.columns(2)
    with c1:
        create_download_button("data/credit_risk_analysis/credit_risk_dataset.csv", "Download Raw Data (.csv)", "text/csv", "Original dataset.")
        create_download_button("data/credit_risk_analysis/03_cleaned_loan_data.csv", "Download Cleaned Data (.csv)", "text/csv", "Cleaned data used for Power BI Dashboard.")
    with c2:
        create_download_button("data/credit_risk_analysis/01_extracted_loan_data.csv", "Download SQL Extracted Data (.csv)", "text/csv", "Data extracted directly from pgAdmin4.")
        create_download_button("data/credit_risk_analysis/ad_hoc_young_risk.csv", "Download Ad-Hoc Data (.csv)", "text/csv", "Raw filtered data from SQL for Ad-Hoc investigation.")
        
    st.markdown("### 3. Dashboard Presentation")
    create_download_button("data/credit_risk_analysis/04_Credit_Risk_Dashboard.pbix", "Download Power BI Dashboard (.pbix)", "application/octet-stream", "Interactive Dashboard file.")