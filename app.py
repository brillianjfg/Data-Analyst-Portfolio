import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Data Analyst Portfolio | Brillian", page_icon="📊", layout="centered")

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

# Header Section
st.title("Hi, I'm Brillian Gultom 👋")
st.subheader("Entry-Level Data Analyst")

st.divider()

# Profile Section Layout
col1, col2 = st.columns([1, 2.5])

with col1:
    if os.path.exists("assets/profile.png"):
        st.image("assets/profile.png", width=230)
    elif os.path.exists("assets/profile.jpg"):
        st.image("assets/profile.jpg", width=230)
    else:
        st.info("file profile.png/jpg di folder assets")
        
    st.write("📍 Jakarta Selatan, Indonesia") 
    st.write("**Phone:** 082146464766") 
    st.write("**Email:** brilliangultom@gmail.com") 
    st.write("**Linkedin:** [linkedin.com/in/brilliangultom](https://linkedin.com/in/brilliangultom)")

    st.write("")

    if os.path.exists("assets/cv.pdf"):
        with open("assets/cv.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download My CV",
                data=pdf_file,
                file_name="CV_Brillian Gultom_Data Analyst.pdf",
                mime="application/pdf"
            )

with col2:
    st.header("About Me")
    st.write("""
    Engineering graduate with a strong foundation in data processing, data structuring, and quantitative analysis. 
    Experienced in handling multivariate and time-series datasets, including data cleaning, transformation, and trend analysis. 
    Able to translate raw data into actionable insights and build data visualizations using Power BI to support decision-making.
    """) 

st.divider()

# Skills Section
st.header("Skills")
st.write("""
- **Data Analysis:** Data Cleaning, Transformation, Exploratory Data Analysis (EDA), Time-Series Analysis
- **Tools:** Microsoft Excel (Advanced), Google Sheets, Power BI
- **Programming:** Python (Pandas, NumPy), SQL
- **Analytical:** Problem Solving, Critical Thinking, Pattern Recognition
- **Soft Skills:** Attention to Detail, Time Management, Teamwork
""") 

st.divider()

# Experience & Education Section
tab1, tab2 = st.tabs(["💼 Experience", "🎓 Education"])

with tab1:
    st.subheader("Construction Management Intern - PT. Biro Arsitek dan Insinjur Sangkuriang")
    st.caption("Aug 2023 - Oct 2023 | Bogor, Indonesia")
    st.write("""
    - Analyzed project data to support progress tracking and performance monitoring.
    - Monitored daily metrics to identify delays, inefficiencies, and anomalies.
    - Structured and maintained project data for reporting and analysis purposes.
    """) 

with tab2:
    st.subheader("Bachelor of Engineering (Civil Engineering) - Pancasila University")
    st.caption("Graduated: 2026 | Jakarta, Indonesia")
    st.write("**Final Project:** Data-Driven Traffic Analysis (Multivariate Time-Series Dataset)")
    st.write("""
    - Structured multivariate dataset across 2 road directions, 2 observation days, 3 time segments, and 15-minute intervals.
    - Processed data with multiple variables including 3 vehicle categories and 5 side friction factors.
    - Conducted time-series aggregation and trend analysis to identify peak patterns and anomalies.
    """) 

st.divider()

# Certifications & Training Section
st.header("Certifications & Training")

@st.dialog("Certificate Details")
def show_cert_excel():
    st.image("assets/cert_excel.png", use_container_width=True)
    st.write("**Microsoft Excel**")
    st.write("Issued by: Coursera | Year: 2026") 
    st.markdown("[🔗 Verify this certificate here](https://coursera.org/verify/professional-cert/1I3DVROAKC15)")

@st.dialog("Certificate Details")
def show_cert_construction():
    st.image("assets/cert_construction.png", use_container_width=True)
    st.write("**Construction Management**")
    st.write("Issued by: Coursera | Year: 2026") 
    st.markdown("[🔗 Verify this certificate here](https://coursera.org/verify/specialization/6DJ8UIDANSUO)")

@st.dialog("Certificate Details")
def show_cert_heccons():
    st.image("assets/cert_heccons.png", use_container_width=True)
    st.write("**Internal Audit Integrated Management System ISO 9001, ISO 14001, ISO 45001**")
    st.write("Issued by: Heccons | Year: 2026") 
    st.caption("Credential No: 075/CERT-IAIMS-9001,14001,45001/HEC/II/2026")

if st.button("🏅 Microsoft Excel — Coursera (2026)", key="btn_excel"):
    show_cert_excel()

if st.button("🏅 Construction Management — Coursera (2026)", key="btn_construction"):
    show_cert_construction()

if st.button("🏅 Internal Audit Integrated Management System ISO 9001, ISO 14001, ISO 45001 — Heccons (2026)", key="btn_heccons"):
    show_cert_heccons()