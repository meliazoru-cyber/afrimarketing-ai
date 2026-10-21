import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI | FAFI Digitals",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Full-Black Background & White Text Styling
st.markdown("""
    <style>
    /* Full Pure Black Background for Main Screen & Sidebar */
    .stApp, [data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    /* All Text Controls & Body Text set to Pure White */
    p, span, label, div, li, h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    /* Main Header & Branding Accents (Metallic Gold) */
    .main-header {
        font-size: 2.6rem;
        color: #D4AF37 !important;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.0rem;
        color: #FFFFFF !important;
        margin-bottom: 25px;
    }
    .brand-badge {
        background-color: #111111;
        color: #D4AF37 !important;
        padding: 5px 14px;
        border-radius: 20px;
        border: 1px solid #D4AF37;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }

    /* Full Black Output Cards with Gold Left Border */
    .black-card {
        background-color: #050505;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #D4AF37;
        border-right: 1px solid #1A1A1A;
        border-top: 1px solid #1A1A1A;
        border-bottom: 1px solid #1A1A1A;
        margin-bottom: 18px;
        color: #FFFFFF !important;
    }
    .black-card * {
        color: #FFFFFF !important;
    }

    .ai-badge {
        background-color: #D4AF37;
        color: #000000 !important;
        font-weight: bold;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
    }

    /* Input Text Area Styling - Dark Background with White Text */
    textarea, input {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Setup
st.sidebar.markdown("<h2 style='color: #D4AF37 !important;'>FAFI DIGITALS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.85rem;'>AfriMarketing AI Core</p>", unsafe_allow_html=True)
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

payment_method = st.sidebar.multiselect(
    "Accepted Payment Methods",
    ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery", "Free Local Delivery"],
    default=["telebirr", "Cash on Delivery"]
)

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
    st.markdown("<h4 style='color: #D4AF37 !important;'>📊 AI Market Analytics</h4>", unsafe_allow_html=True)
    st.info("""
    • Peak Telegram Engagement: 12:30 PM & 7:00 PM EAT.
    • Top Conversion Method: telebirr call-to-actions + Telegram direct admin link.
    • Best Format: Short video clips paired with mixed Amharic/English captions.
    """)

# Campaign Generation Trigger
