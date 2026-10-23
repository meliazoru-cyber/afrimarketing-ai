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

# Custom High-Contrast Styling (Safe & Tested)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0F0F0F;
        color: #FFFFFF;
    }
    
    /* Input Boxes: White Background with Bold Black Text */
    .stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 8px !important;
    }

    /* Labels: Metallic Gold */
    label, .stMarkdown label {
        color: #D4AF37 !important;
        font-weight: bold !important;
        font-size: 1.05rem !important;
    }

    /* Output Cards */
    .result-card {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-left: 5px solid #D4AF37;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #FFFFFF;
    }

    /* Gold Pill Badges */
    .gold-badge {
        background-color: #D4AF37;
        color: #000000;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.8rem;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("✨ FAFI DIGITALS")
st.sidebar.subheader("AI Marketing Suite")
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
location = st.sidebar.selectbox("📍 Target Market", ["Addis Ababa Urban", "Regional Centers", "Ethiopian Diaspora", "Nationwide"])
brand_tone = st.sidebar.selectbox("🎨 Brand Tone", ["High-End Luxury", "Gen-Z Viral Slang", "Direct Sales Heavy", "Educational & Trust"])
payment_method = st.sidebar.multiselect("💳 Payment Methods", ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery"], default=["telebirr", "Cash on Delivery"])

st.sidebar.markdown("---")
gemini_api_key = st.sidebar.text_input("🔑 Gemini API Key (Optional)", type="password", help="Leave blank for built-in templates!")

# Header Section
st.title("AfriMarketing AI 🇪🇹")
st.caption("Powered by FAFI Digitals • High-Converting Campaign Suite")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    product_description = st.text_area(
        "✍️ Describe your product, service, or promo goal:",
        placeholder="e.g., Premium logo vectors, visual branding, and video editing packages in Addis Ababa with telebirr checkout...",
        height=140
    )

with col2:
    st.subheader("⚡ Market Signals")
    st.info("**Telegram Peak:** 12:30 PM & 7:30 PM EAT\n\n**TikTok Peak:** 6:00 PM – 9:30 PM EAT")

st.markdown("<br>", unsafe_allow_html=True)

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

if st.button("🚀 GENERATE CREATIVE CAMPAIGN SUITE", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please describe your offer first!")
    else:
        with st.spinner("FAFI Digitals AI is generating..."):
            payments_str = " | ".join(payment_method) if payment_method else "Contact admin"
            
            prompt = f"Act as a top digital marketer for {business_name} in Ethiopia.\nTone: {brand_tone}\nOffer: {product_description}\nLocation: {location}\nPayment: {payments_str}\nPhone: {phone_number}\n\nCreate 5 Ethio-English social captions and a 15-second TikTok video script."
            
            ai_output = generate_ai_content(prompt)
            time.sleep(1.0)

        st.success("Campaign Suite Generated!")

        tab1, tab2, tab3 = st.tabs(["📲 Telegram Broadcast", "🔥 Captions", "🎬 TikTok Script"])

        with tab1:
            st.subheader("Telegram Preview")
            b_upper = business_name.upper()
            loc_upper = location.upper()
            
            tg_text = f"✨ **{b_upper}** | {loc_upper}\n\n📌 **ለድርጅትዎ የሚሆን ምርጥ አሰራር:**\n{product_description}\n\n💳 **Payment:** {payments_str}\n📍 **Location:** {location}\n📞 **ለማዘዝ በቀጥታ ይደውሉ:** {phone_number}\n📲 **Telegram Direct:** @FAFIdigitals"
            
            st.code(tg_text, language="markdown")

        with tab2:
            st.subheader(f"Social Captions ({brand_tone})")
            if ai_output:
                st.write(ai_output)
            else:
                st.markdown(f"""
                <div class="result-card">
                    <span class="gold-badge">Option 1</span><br><br>
                    ✨ <b>{business_name}</b> - {location}<br><br>
                    📌 <b>ለድርጅትዎ የሚሆን ምርጥ አሰራር:</b><br>{product_description}<br><br>
                    💳 <b>Payment:</b> {payments_str}<br>
                    📞 <b>Call/Text Now:</b> {phone_number}
                </div>
                """, unsafe_allow_html=True)

        with tab3:
            st.subheader("15-Second Viral Storyboard")
            st.markdown(f"""
            <div class="result-card">
                <b>🎥 0–3s (Visual Hook):</b> Fast-cut visual of your work in {location} with trending audio.<br>
                <b>🗣️ Voiceover:</b> <i>"አዲስ አበቤዎች! If you want your business to stand out, watch this."</i><br><br>
                <b>🎬 3–10s (Value Pitch):</b> Show portfolio results for {business_name}.<br><br>
                <b>🎯 10–15s (Call to Action):</b> Display telebirr badge and direct contact: <b>{phone_number}</b>.
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("AfriMarketing AI • Developed by FAFI Digitals")
