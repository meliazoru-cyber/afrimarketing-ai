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

# High-Contrast Luxury SaaS CSS (Obsidian Black, Metallic Gold & Bright White Text)
st.markdown("""
    <style>
    /* Force Dark Theme Background Everywhere */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    /* Force Pure White Typography */
    h1, h2, h3, h4, h5, h6, p, span, label, div, li, small {
        color: #FFFFFF !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Hero Branding Header */
    .hero-container {
        padding: 28px 22px;
        background: #0A0A0A !important;
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
        margin-bottom: 10px;
    }

    /* Telegram Message Preview Box */
    .tg-preview-card {
        background: #17212B !important;
        border: 1px solid #2B5278 !important;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.8);
    }
    .tg-header {
        color: #64B5F6 !important;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 12px;
    }

    /* Clear High-Contrast Output Cards */
    .result-card {
        background: #0D0D0D !important;
        border: 1px solid #282828 !important;
        border-left: 4px solid #D4AF37 !important;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }
    .result-card p, .result-card span, .result-card div, .result-card li, .result-card b, .result-card i {
        color: #FFFFFF !important;
    }

    /* Gold Style Badges */
    .style-pill {
        background: #D4AF37 !important;
        color: #000000 !important;
        font-weight: 800;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.75rem;
        text-transform: uppercase;
    }

    /* Metric Display Cards */
    .metric-box {
        background: #0D0D0D !important;
        border: 1px solid #282828 !important;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.15rem;
        font-weight: bold;
    }

    /* Dark Input Controls Fix */
    .stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
        background-color: #121212 !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        color: #FFFFFF !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #121212 !important;
    }
    ul[data-baseweb="menu"] li {
        color: #FFFFFF !important;
    }

    /* Footer */
    .main-footer {
        text-align: center; 
        color: #AAAAAA !important; 
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Options
st.sidebar.markdown("<h3 style='color: #D4AF37 !important;'>✨ FAFI DIGITALS</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.8rem;'>AI Marketing Suite v3.5</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
