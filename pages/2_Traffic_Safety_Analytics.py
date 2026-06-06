import streamlit as st
import pandas as pd
import os

### Page Configuration
st.set_page_config(page_title="Traffic Safety Analytics", layout="centered")

### ==========================================
### CUSTOM CSS: NATIVE SIDEBAR NAVIGATION & TEXT
### ==========================================
st.markdown("""
    <style>
    .stMarkdown p {
        word-break: normal !important;
        overflow-wrap: normal !important;
    }
    .stMarkdown a {
        white-space: nowrap !important;
    }
    /* Mengubah nama menu default 'app' menjadi 'About Me' */
    span[label="app"] {
        font-size: 0px !important;
    }
    span[label="app"]::before {
        content: "About Me";
        font-size: 18px !important;
        font-weight: 800 !important;
        visibility: visible !important;
    }
    /* Menambahkan separator P R O J E C T S */
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
    /* Mengubah nama file ini di sidebar menjadi lebih rapi */
    span[label="Traffic Safety Analytics"] {
        font-size: 0px !important;
    }
    span[label="Traffic Safety Analytics"]::before {
        content: "Traffic Safety Analytics Project";
        font-size: 15px !important;
        visibility: visible !important;
    }
    div[data-testid="stSidebarNavSeparator"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

### ==========================================
st.title("Traffic Performance & Safety Analytics")
st.caption("Context: An independent case study applying SE Dirjen Bina Marga 2023 & PKJI 2023 standards using advanced Excel capabilities (Case Study: Cakung Station - I Gusti Ngurah Rai Road).")
st.divider()

### SIDEBAR NAVIGATION (INTERNAL TABS)
st.sidebar.markdown("---")
st.sidebar.header("Navigation")

# Gunakan key session_state yang unik untuk halaman ini
if 'active_tab_traffic' not in st.session_state:
    st.session_state.active_tab_traffic = "Project Overview"

tab_names = [
    "Project Overview",
    "Phase 1: Power Query (ETL)",
    "Phase 2: PKJI Calculator",
    "Phase 3: Interactive Dashboard",
    "Phase 4: What-If Analysis",
    "Project Files"
]

for tab in tab_names:
    button_type = "primary" if st.session_state.active_tab_traffic == tab else "secondary"
    
    if st.sidebar.button(tab, type=button_type, use_container_width=True, key=f"btn_{tab}"):
        st.session_state.active_tab_traffic = tab
        st.rerun()

active_tab = st.session_state.active_tab_traffic

### ---------- TAB 1: PROJECT OVERVIEW ----------
if active_tab == "Project Overview":
    st.info("""
    **Technical Skills & Tools:**
    - **Core Tool:** Microsoft Excel (Advanced)
    - **Data Engineering:** Power Query (M-Code), Data Merging, Automated ETL Pipeline
    - **Data Analytics:** Pivot Tables, Advanced Formulas (VLOOKUP TRUE/FALSE, Nested IF, GETPIVOTDATA)
    - **Data Visualization:** Interactive Dashboard, Combo Charts (Secondary Axis), Slicers
    - **Domain Knowledge:** Traffic Engineering, PKJI 2023, SE Bina Marga 2023
    """)
    st.divider()

    st.header("Project Context & Summary")
    st.write("The goal of this project is to evaluate the necessity of pedestrian crossing facilities and analyze road performance using primary multivariate field survey data.")
    
    st.write("")
    st.markdown("### - **Key Findings** -")
    st.write("""
    Based on the analysis utilizing automated Excel pipelines, here are the main findings:
    - **Peak Hour Detection:** The absolute peak hour occurred on **Monday, 17:00 - 18:00 WIB** with a total vehicle volume of 7,897 and 332 crossing pedestrians.
    - **Crossing Urgency (PV²):** The PV² conflict value reached **20.7 Billion**, far exceeding the absolute threshold ($2 \\times 10^8$) for a Pedestrian Overpass (JPO).
    - **Traffic Performance:** During peak hours, the Westbound (Jakarta) Degree of Saturation (V/C ratio) was **0.43**, while the Eastbound (Bekasi) was **0.60**.
    """)
    
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Peak Vehicle Vol (V)", value="7,897", delta="Vehicles/Hr")
    c2.metric(label="Crossing Pedestrians (P)", value="332", delta="People/Hr")
    c3.metric(label="PV² Conflict Value", value="20.7B", delta="Critical Hazard", delta_color="inverse")
    
    st.write("")
    st.markdown("### - **Recommendations** -")
    st.success("""
    Based on the findings, here are the actionable recommendations:
    1. **Construct a Pedestrian Overpass (JPO):** The PV² value explicitly mandates a grade-separated crossing (JPO) to prevent fatal accidents.
    2. **Avoid At-Grade Crossings:** Building a Pelican Cross or Zebra Cross would cause extreme traffic delays and severe congestion due to the high volume of vehicles and pedestrians competing for gaps.
    """)

### ---------- TAB 2: POWER QUERY (ETL) ----------
elif active_tab == "Phase 1: Power Query (ETL)":
    st.header("Phase 1: Automated Data Pipeline (Power Query)")
    st.write("To simulate a professional environment, I avoided manual copy-pasting. I built an automated ETL (Extract, Transform, Load) pipeline using Power Query to handle the raw survey datasets.")
    
    st.markdown("### Step 1: Merging Directional Datasets & Handling Duplicates")
    st.markdown("**What I Did:** I imported two separate raw CSV files (Eastbound and Westbound surveys). I added a custom 'Direction' identifier and appended them into a single `Final_Merged_Dataset`. I also resolved double-counting issues for crossing pedestrians.")
    st.code('=[Pejalan Kaki di Bahu Jalan] + [#"Pejalan Kaki di Bahu Jalan.1"]', language='text')
    
    st.divider()
    
    st.markdown("### Step 2: Custom Columns (M-Code)")
    st.markdown("**What I Did:** I created calculated columns directly in Power Query to dynamically compute the total vehicles (V) and the PV² conflict parameter.")
    st.code('=[Crossing Pedestrians] * ([#"Total Vehicles (V)"] * [#"Total Vehicles (V)"])', language='text')

### ---------- TAB 3: PKJI CALCULATOR ----------
elif active_tab == "Phase 2: PKJI Calculator":
    st.header("Phase 2: Dynamic PKJI 2023 Calculator")
    st.markdown("**What I Did:** I built a fully automated Traffic Engineering Calculator using Advanced Excel formulas to compute Capacity (C) and Degree of Saturation (V/C Ratio) per direction.")
    
    st.markdown("### 1. VLOOKUP TRUE/FALSE for Dynamic Parameters")
    st.write("Instead of hardcoding standard values, I created internal lookup tables for City Size Factor, Lane Width Factor, and Side Friction.")
    st.code('=VLOOKUP(X3, Table_FC_CS, 2, TRUE)  // TRUE for approximate range match (Population)', language='excel')
    
    if os.path.exists("assets/rumus_vlookup.png"):
        st.image("assets/rumus_vlookup.png", caption="Screenshot: Automated VLOOKUP TRUE/FALSE logic in Excel", use_container_width=True)
    else:
        st.warning("Place your VLOOKUP screenshot as 'rumus_vlookup.png' inside your assets folder to show it here.")
    
    st.divider()
    
    st.markdown("### 2. Automated PCU Conversion")
    st.write("I dynamically calculated the total Traffic Flow in Passenger Car Units (PCU) to get the accurate V/C Ratio per direction using a `GETPIVOTDATA` architecture.")
    st.code('= ([Total MP] * 1) + ([Total KS] * 1.2) + ([Total SM] * 0.25)', language='excel')
    
    if os.path.exists("assets/rumus_pcu.png"):
        st.image("assets/rumus_pcu.png", caption="Screenshot: Dynamic PCU Conversion & Aggregation", use_container_width=True)
    else:
        st.warning("Place your PCU calculation screenshot as 'rumus_pcu.png' inside your assets folder to show it here.")

### ---------- TAB 4: INTERACTIVE DASHBOARD ----------
elif active_tab == "Phase 3: Interactive Dashboard":
    st.header("Phase 3: Interactive Dashboard")
    st.write("I wrapped the entire calculation engine into an interactive dashboard controlled by Slicers.")
    
    if os.path.exists("assets/excel_dashboard.png"):
        st.image("assets/excel_dashboard.png", caption="Final Interactive Excel Dashboard", use_container_width=True)
    else:
        st.warning("Place your Excel Dashboard screenshot as 'excel_dashboard.png' inside your assets folder to show it here.")
        
    st.markdown("### Interactive Combo Chart (Secondary Axis)")
    st.markdown("**What I Did:** I constructed a PivotChart (Combo Chart) with a Secondary Axis to visualize both Vehicle Volume (thousands) and PV² values (billions) simultaneously. I used a Calculated Field in the PivotTable to ensure mathematical accuracy.")
    st.code("='Crossing Pedestrians' * ('Total Vehicles (V)' ^ 2)", language='text')

### ---------- TAB 5: WHAT-IF ANALYSIS ----------
elif active_tab == "Phase 4: What-If Analysis":
    st.header("Phase 4: What-If Analysis")
    st.markdown("### Scenario Risk Matrix")
    st.markdown("**What I Did:** I built a What-If risk matrix to demonstrate the business impact of choosing sub-optimal crossing facilities due to budget constraints.")
    st.table(pd.DataFrame({
        "Facility Options": ["Scenario 1: JPO / Overpass (Recommended)", "Scenario 2: Pelican Crossing", "Scenario 3: Zebra Crossing Only"],
        "Pedestrian Safety Impact": ["100% Safe (Grade-separated)", "Moderate risk (Depends on driver compliance)", "Extremely high risk of FATAL accidents"],
        "Traffic Flow Impact": ["Traffic is completely undisrupted", "Extreme traffic delay; vehicle queues will elongate", "Severe congestion and traffic chaos"]
    }))
    
    st.info("""
    **Insight & Justification:**
    Based on field survey data during the peak hour on Monday, 17:00 - 18:00 with a PV^2 value of **20,704,386,188**, the recommended facility is definitively a JPO (Overpass).
    
    This is reinforced by the actual traffic performance during that hour. The high traffic density and saturation levels mean there are virtually no safe gaps for pedestrians to cross at-grade.
    """)
    
    st.error("""
    **Risk Warning:**
    If we choose to build sub-optimal facilities like a Pelican Crossing or Zebra Crossing, the resulting risks are fatal accidents for pedestrians (competing for gaps) and total traffic gridlock (extreme delays due to stopping vehicles).
    """)

### ---------- TAB 6: PROJECT FILES ----------
elif active_tab == "Project Files":
    st.header("Project Repository Access")
    
    def create_download_button(file_path, label, mime_type, description):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(label=label, data=f, file_name=os.path.basename(file_path), mime=mime_type, use_container_width=True)
            st.caption(description)
        else:
            st.warning(f"File {os.path.basename(file_path)} placeholder active.")
            
    st.markdown("### 1. Main Dashboard & Calculator")
    create_download_button("data/Traffic_Safety/Traffic_Safety_Analysis.xlsx", "Download Excel Dashboard (.xlsx)", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Fully functional automated PKJI 2023 calculator and interactive dashboard.")
    
    st.markdown("### 2. Raw Datasets")
    c1, c2 = st.columns(2)
    with c1:
        create_download_button("data/Traffic_Safety/dataset_survey_arah_bekasi.csv", "Download Bekasi Data (.csv)", "text/csv", "Raw survey data (Eastbound).")
    with c2:
        create_download_button("data/Traffic_Safety/dataset_survey_arah_jakarta.csv", "Download Jakarta Data (.csv)", "text/csv", "Raw survey data (Westbound).")
