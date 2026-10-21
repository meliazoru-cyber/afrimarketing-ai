import streamlit as st
import time
import os

# Optional: Try importing Gemini API for real AI generation
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI | FAFI Digitals",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling - Black & Gold Theme by FAFI Digitals
st.markdown("""
    <style>
    .stApp {
        background-color: #0A0A0A;
        color: #F0F0F0;
    }
    .main-header {
        font-size: 2.6rem;
        color: #D4AF37; /* Metallic Gold */
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.0rem;
        color: #A0A0A0;
        margin-bottom: 25px;
    }
    .brand-badge {
        background-color: #1A1A1A;
        color: #D4AF37;
        padding: 5px 14px;
        border-radius: 20px;
        border: 1px solid #D4AF37;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }
    .gold-card {
        background-color: #141414;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #D4AF37;
        border-right: 1px solid #222222;
        border-top: 1px solid #222222;
        border-bottom: 1px solid #222222;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        margin-bottom: 18px;
    }
    .ai-badge {
        background-color: #D4AF37;
        color: #000000;
        font-weight: bold;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Setup
st.sidebar.markdown("<h2 style='color: #D4AF37;'>FAFI DIGITALS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #888888; font-size: 0.85rem;'>AfriMarketing AI Core</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("Business / Brand Name", value="FAFI Digitals")

location = st.sidebar.selectbox(
    "Location Target",
    ["Addis Ababa (Urban)", "Regional Cities (Hawassa, Adama, etc.)", "Ethiopian Diaspora", "Nationwide"]
)

target_platform = st.sidebar.selectbox(
    "Primary Channel",
    ["Telegram Channel", "TikTok / Reels", "Facebook Page", "Instagram Carousel", "LinkedIn"]
)

language_style = st.sidebar.selectbox(
    "Tone & Dialect",
    ["Amharic + English Mix (Ethio-English)", "Pure Amharic (አማርኛ)", "Trendy Gen-Z Style", "Corporate Professional"]
)

payment_method = st.sidebar.multiselect(
    "Accepted Payment Methods",
    ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery", "Free Local Delivery"],
    default=["telebirr", "Cash on Delivery"]
)

# Optional API Key Input for Live Generative AI
st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color: #D4AF37;'>🤖 Real AI Engine Setup</h4>", unsafe_allow_html=True)
api_key = st.sidebar.text_input("Gemini API Key (Optional)", type="password", help="Paste API key here to activate live AI generation.")

# Dashboard Header
st.markdown('<div class="brand-badge">✨ BY FAFI DIGITALS</div>', unsafe_allow_html=True)
st.markdown('<p class="main-header">AfriMarketing AI 🇪🇹</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-powered marketing copy engine & local audience strategy builder for Ethiopian brands.</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    product_description = st.text_area(
        "Describe your product, service, or campaign offer:",
        placeholder="e.g., Luxury digital branding, logo vectors, and video editing packages for startups in Addis Ababa with fast telebirr payment...",
        height=130
    )

with col2:
    st.markdown("<h4 style='color: #D4AF37;'>📊 AI Market Analytics</h4>", unsafe_allow_html=True)
    st.info("""
    • **Peak Telegram Engagement:** 12:30 PM & 7:00 PM EAT.
    • **Top Conversion Method:** telebirr call-to-actions + Telegram direct admin link.
    • **
