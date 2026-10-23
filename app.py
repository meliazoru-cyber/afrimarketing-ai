import streamlit as st
import time

# Optional Live AI Import
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI | FAFI Digitals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-Contrast High-Visibility Styling
st.markdown("""
    <style>
    /* Global App Background */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: #050505 !important;
        color: #FFFFFF !important;
    }

    /* Sidebar Labels Bright Gold */
    [data-testid="stSidebar"] label {
        color: #D4AF37 !important;
        font-weight: 800 !important;
        font-size: 1.0rem !important;
    }
    [data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }

    /* All Header and Body Text Forced Bright White */
    h1, h2, h3, h4, h5, h6, p, span, label, div, li, small {
        color: #FFFFFF !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Main Form Input Labels Bright Gold */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label, .stMultiSelect > label {
        color: #D4AF37 !important;
        font-weight: 800 !important;
        font-size: 1.0rem !important;
    }

    /* Input Fields Background White & Text SOLID BLACK */
    .stTextInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }

    /* Fix Selectbox & Dropdown Containers - Bright White Field with BLACK Text */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="select"] div {
        color: #000000 !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CCCCCC !important;
    }
    ul[data-baseweb="menu"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    ul[data-baseweb="menu"] li:hover {
        background-color: #D4AF37 !important;
        color: #000000 !important;
    }

    /* MultiSelect Tags */
    span[data-baseweb="tag"] {
        background-color: #D4AF37 !important;
        color: #000000 !important;
        font-weight: 800 !important;
    }

    /* Hero Branding Header */
    .hero-container {
        padding: 28px 22px;
        background: #0F0F0F !important;
        border: 1px solid #2B2B2B !important;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.9);
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        color: #D4AF37 !important;
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #FFFFFF !important;
        margin-top: 6px;
    }
    .agency-tag {
        display: inline-block;
        background: rgba(212, 175, 55, 0.15) !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10
