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

    /* Force Sidebar Specific Visibility Rules */
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #D4AF37 !important;
        font-weight: bold !important;
    }

    /* All Header and Body Text Forced Bright White */
    h1, h2, h3, h4, h5, h6, p, span, label, div, li, small {
        color: #FFFFFF !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Main Form Input Labels Bright Gold */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label, .stMultiSelect > label {
        color: #D4AF37 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }

    /* Input Fields Background & Contrast */
    .stTextInput input, .stTextArea textarea {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }

    /* Selectbox Container & Dropdown Styling */
    div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        color: #FFFFFF !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
    }
    ul[data-baseweb="menu"] li {
        color: #FFFFFF !important;
        background-color: #1A1A1A !important;
    }
    ul[data-baseweb="menu"] li:hover {
        background-color: #D4AF37 !important;
        color: #000000 !important;
    }

    /* MultiSelect Tags */
    span[data-baseweb="tag"] {
        background-color: #D4AF37 !important;
        color: #000000 !important;
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

    /* High-Contrast Output Cards */
    .result-card {
        background: #121212 !important;
        border: 1px solid #2E2E2E !important;
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
        background: #121212 !important;
        border: 1px solid #2E2E2E !important;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.15rem;
        font-weight: bold;
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
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.85rem;'>AI Marketing Suite v3.5</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
location = st.sidebar.selectbox("📍 Target Market", ["Addis Ababa Urban", "Regional Centers", "Ethiopian Diaspora", "Nationwide"])
brand_tone = st.sidebar.selectbox("🎨 Brand Tone", ["High-End Luxury", "Gen-Z Viral Slang", "Direct Sales Heavy", "Educational & Trust"])
payment_method = st.sidebar.multiselect("💳 Payment Methods", ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery"], default=["telebirr", "Cash on Delivery"])

st.sidebar.markdown("---")
gemini_api_key = st.sidebar.text_input("🔑 Gemini API Key (Optional)", type="password", help="Leave blank for built-in local engine!")

# Hero Section
st.markdown
