import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI | FAFI Digitals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End SaaS Styling (Obsidian Black & Metallic Gold)
st.markdown("""
    <style>
    /* Global App Background */
    .stApp {
        background-color: #030303 !important;
        color: #FFFFFF !important;
    }
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 1px solid #1A1A1A;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }

    /* Hero Header */
    .hero-container {
        padding: 30px 20px;
        background: linear-gradient(135deg, #0A0A0A 0%, #141414 100%);
        border: 1px solid #222222;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
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
        color: #A0A0A0 !important;
        margin-top: 5px;
    }
    .agency-tag {
        display: inline-block;
        background: rgba(212, 175, 55, 0.1);
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    /* Creative Result Cards */
    .result-card {
        background: #0A0A0A;
        border: 1px solid #222222;
        border-left: 4px solid #D4AF37;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .result-card:hover {
        border-color: #D4AF37;
        transition: all 0.3s ease;
    }

    /* Badges & Pills */
    .style-pill {
        background: #D4AF37;
        color: #000000 !important;
        font-weight: 800;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        text-transform: uppercase;
    }

    /* Input Fields & Textareas Styling */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #0D0D0D !important;
        color: #FFFFFF !important;
        border: 1px solid #2A2A2A !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #D4AF37 !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.2) !important;
    }

    /* Custom Metric Cards */
    .metric-box {
        background: #0A0A0A;
        border: 1px solid #1F1F1F;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.1rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Design
st.sidebar.markdown("<h3 style='color: #D4AF37 !important;'>✨ FAFI DIGITALS</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #888888 !important; font-size: 0.8rem;'>AI Marketing Suite v2.0</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
location = st.sidebar.selectbox("📍 Target Market", ["Addis Ababa Urban", "Regional Centers", "Ethiopian Diaspora", "Nationwide"])
target_platform = st.sidebar.selectbox("🎯 Primary Channel", ["Telegram Channel & Bot", "TikTok / Reels", "Instagram Carousel", "Facebook Page"])
payment_method
