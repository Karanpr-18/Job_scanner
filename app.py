import streamlit as st
from PyPDF2 import PdfReader
import warnings
from job_scanner import calculate_match_score,__init__

warnings.filterwarnings("ignore")

# ────────────────────────── PAGE CONFIG ──────────────────────────
st.set_page_config(
    page_title="CV Job Matcher AI", 
    page_icon="📄", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ──────────────────────────── CSS STYLING ─────────────────────────────────
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
            
    /* Responsive button width styling */
    .stButton > button {
        width: 500px !important;           
        height: 50px !important;           
        font-size: 16px !important;        
        margin: 0 auto !important;         
        display: block !important;
        max-width: 90% !important;         /* Prevent overflow on small screens */
    }
    
    /* Mobile responsive adjustments */
    @media (max-width: 768px) {
        .stButton > button {
            width: 90% !important;         /* Use 90% width on mobile */
            min-width: 250px !important;   /* Minimum width */
            max-width: 400px !important;   /* Maximum width on mobile */
        }
    }
    
    @media (max-width: 480px) {
        .stButton > button {
            width: 95% !important;         /* Use 95% width on very small screens */
            min-width: 200px !important;   /* Smaller minimum width */
            font-size: 14px !important;    /* Smaller font on mobile */
        }
    }
    
    .social-icons {
        display: flex;
        justify-content: left;
        gap: 50px;
        margin: 15px 0;
    }
    
    .social-icon-link {
        display: inline-block;
        width: 100px;
        height: 100px;
        border-radius: 25%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .github-icon {
        background-color: #24292e;
        color: white;
    }
    
    .github-icon:hover {
        background-color: #444d56;
        transform: scale(1.1);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    .linkedin-icon {
        background-color: #0077b5;
        color: white;
    }
    
    .linkedin-icon:hover {
        background-color: #005885;
        transform: scale(1.1);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    .icon-svg {
        width: 24px;
        height: 24px;
        fill: white;
    }
</style>
""", unsafe_allow_html=True)


# ───────────────────────────── SESSION STATE ─────────────────────────────────
if "show_menu" not in st.session_state:
    st.session_state.show_menu = True

# ───────────────────────────── HEADER ─────────────────────────────────
st.markdown("""
<div style="text-align: center; 
           padding: 30px; 
           max-width: 700px;                     /* Add this to control width */
           margin: 0 auto 10px auto;             /* Add this to center and maintain bottom margin */
           background: linear-gradient(90deg, #ff6b6b 0%, #4ecdc4 100%); 
           color: white; 
           border-radius: 15px; 
           box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">📄 CV Job Matcher AI</h1>
    <p style="margin: 10px 0 0 0; font-size: 1.2rem; opacity: 0.9;">Instant CV and job description compatibility check</p>
</div>
""", unsafe_allow_html=True)


# ───────────────────────────── LAYOUT ─────────────────────────────────
menu_col, content_col = st.columns([1, 2])

# ───────────────────────────── LEFT MENU COLUMN ─────────────────────────────────
with menu_col:
    def toggle_menu():
        st.session_state.show_menu = not st.session_state.show_menu

    if st.button("ℹ️ Instructions", on_click=toggle_menu):
        pass

    if st.session_state.show_menu:
        st.info("📋 **How to use:**\n\n**Step 1:** Enter the job description in the text area\n\n**Step 2:** Upload your CV as a PDF file\n\n**Step 3:** Click 'Analyze Match' to get compatibility score")
        
        # Social Icons
        st.markdown("**Connect with me:**")
        
        st.markdown("""
        <div class="social-icons">
            <a href="https://github.com/Karanpr-18" target="_blank" class="social-icon-link github-icon" title="GitHub">
                <svg class="icon-svg" viewBox="0 0 24 24">
                    <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
                </svg>
            </a>
            <a href="https://www.linkedin.com/in/karan-bhoriya-b5a3382b7" target="_blank" class="social-icon-link linkedin-icon" title="LinkedIn">
                <svg class="icon-svg" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("*Made by Karan*", unsafe_allow_html=True)

# ───────────────────────────── RIGHT CONTENT COLUMN ─────────────────────────────────
with content_col:
    # Job Description Input
    st.markdown("### 📝 Job Description")
    job_description = st.text_area(
        "Paste the job description here:",
        height=200,
        placeholder="Enter the complete job description including requirements, responsibilities, and qualifications...",
        key="job_desc"
    )
    
    # CV Upload
    st.markdown("### 📄 Upload CV")
    uploaded_file = st.file_uploader(
        "Choose your CV file (PDF only)",
        type=["pdf"],
        help="Upload your CV in PDF format for analysis",
        key="cv_upload"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")

# ───────────────────────────── TEXT EXTRACTION ─────────────────────────────────
cv_text = ""
if uploaded_file is not None:
    try:
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                cv_text += page_text
    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")

# ───────────────────────────── ANALYSIS SECTION ─────────────────────────────────
st.markdown("---")

if st.button("🔍 Analyze Match", type="primary", use_container_width=True):
    if job_description.strip() == "":
        st.error("⚠️ Please enter a job description")
    elif cv_text.strip() == "":
        st.error("⚠️ Please upload a valid CV PDF")
    else:
        with st.spinner("🔄 Analyzing compatibility..."):
            try:
                match_score = calculate_match_score(job_description, cv_text)
                
                # Results Display
                st.markdown("---")
                st.markdown("## 📊 Analysis Results")
                
                # Center the results
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col2:
                    # Match score with color coding
                    if match_score >= 80:
                        st.success(f"### 🎯 Excellent Match: {match_score}%")
                        st.balloons()
                    elif match_score >= 60:
                        st.warning(f"### ⚡ Good Match: {match_score}%")
                    elif match_score >= 40:
                        st.info(f"### 📈 Fair Match: {match_score}%")
                    else:
                        st.error(f"### 📉 Low Match: {match_score}%")
                
                # Progress bar
                st.progress(match_score / 100)
                
                # Match interpretation
                if match_score >= 80:
                    st.success("🌟 **Your CV is highly compatible with this job description!**")
                elif match_score >= 60:
                    st.warning("✨ **Your CV shows good alignment with the job requirements.**")
                elif match_score >= 40:
                    st.info("💡 **Your CV has some relevant skills but may need improvements.**")
                else:
                    st.error("🔧 **Consider updating your CV to better match the job requirements.**")
                    
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")

# ───────────────────────────── FOOTER ─────────────────────────────────
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>Built By Karan | CV Job Matcher AI © 2025</p>
    </div>
    """,
    unsafe_allow_html=True
)
