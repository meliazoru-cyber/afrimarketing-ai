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
st.markdown("""
    <div class="hero-container">
        <div class="agency-tag">Powered by FAFI Digitals</div>
        <p class="hero-title">AfriMarketing AI 🇪🇹</p>
        <p class="hero-subtitle">High-converting copywriting intelligence and localized campaign strategy engineered for Ethiopia.</p>
    </div>
""", unsafe_allow_html=True)

# Main Form Layout
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    product_description = st.text_area(
        "✍️ Describe your product, service, or campaign goal:",
        placeholder="e.g., Premium logo vectors, visual branding, and video editing packages for startups in Addis Ababa with telebirr checkout...",
        height=140
    )

with col2:
    st.markdown("<h4 style='color: #D4AF37 !important;'>⚡ Local Market Signals</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #CCCCCC;">Telegram Channel Peak</div>
            <div class="metric-val">12:30 PM & 7:30 PM EAT</div>
        </div>
        <br>
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #CCCCCC;">TikTok Hook Peak</div>
            <div class="metric-val">6:00 PM – 9:30 PM EAT</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Helper function for Live Gemini API
def generate_ai_content(prompt):
    if GEMINI_AVAILABLE and gemini_api_key:
        try:
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            return None
    return None

# Action Generator Button
if st.button("🚀 GENERATE CREATIVE CAMPAIGN SUITE", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please describe your offer or business goal first!")
    else:
        with st.spinner("FAFI Digitals AI is crafting your marketing suite..."):
            payments_str = " | ".join(payment_method) if payment_method else "Contact admin"
            
            ai_prompt = f"Act as a top digital marketer for {business_name} in Ethiopia.\nTone: {brand_tone}\nOffer: {product_description}\nLocation: {location}\nPayment: {payments_str}\nPhone: {phone_number}\n\nCreate 5 Ethio-English social captions, a 15-second TikTok video script, and local marketing tips."
            
            ai_output = generate_ai_content(ai_prompt)
            time.sleep(1.0)

        st.success("Campaign Suite Successfully Generated!")

        # Tabs Setup
        tab1, tab2, tab3, tab4 = st.tabs([
            "📲 Live Telegram Mockup", 
            "🔥 5 High-Conversion Captions", 
            "🎬 TikTok Storyboard Script", 
            "📅 Weekly Growth Blueprint"
        ])

        # TAB 1: LIVE TELEGRAM MOCKUP
        with tab1:
            st.markdown("<h3 style='color: #D4
