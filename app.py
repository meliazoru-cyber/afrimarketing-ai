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
    .stApp {
        background-color: #0F0F0F;
        color: #FFFFFF;
    }
    .stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 8px !important;
    }
    label, .stMarkdown label {
        color: #D4AF37 !important;
        font-weight: bold !important;
        font-size: 1.05rem !important;
    }
    .result-card {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-left: 5px solid #D4AF37;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #FFFFFF;
    }
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
st.sidebar.subheader("AI Marketing & Pricing Suite")
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
st.caption("Powered by FAFI Digitals • High-Converting Campaign & Pricing Suite")
st.markdown("---")

# Main Navigation Tabs
main_tab1, main_tab2 = st.tabs(["🚀 AI Campaign & Copy Suite", "💰 Ethio Pricing Calculator"])

with main_tab1:
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

            sub_tab1, sub_tab2, sub_tab3 = st.tabs(["📲 Telegram Broadcast", "🔥 Captions", "🎬 TikTok Script"])

            with sub_tab1:
                st.subheader("Telegram Preview")
                b_upper = business_name.upper()
                loc_upper = location.upper()
                
                tg_text = f"✨ **{b_upper}** | {loc_upper}\n\n📌 **ለድርጅትዎ የሚሆን ምርጥ አሰራር:**\n{product_description}\n\n💳 **Payment:** {payments_str}\n📍 **Location:** {location}\n📞 **ለማዘዝ በቀጥታ ይደውሉ:** {phone_number}\n📲 **Telegram Direct:** @FAFIdigitals"
                st.code(tg_text, language="markdown")

            with sub_tab2:
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

            with sub_tab3:
                st.subheader("15-Second Viral Storyboard")
                st.markdown(f"""
                <div class="result-card">
                    <b>🎥 0–3s (Visual Hook):</b> Fast-cut visual of your work in {location} with trending audio.<br>
                    <b>🗣️ Voiceover:</b> <i>"አዲስ አበቤዎች! If you want your business to stand out, watch this."</i><br><br>
                    <b>🎬 3–10s (Value Pitch):</b> Show portfolio results for {business_name}.<br><br>
                    <b>🎯 10–15s (Call to Action):</b> Display telebirr badge and direct contact: <b>{phone_number}</b>.
                </div>
                """, unsafe_allow_html=True)

with main_tab2:
    st.subheader("💰 Ethiopian Service & Product Pricing Calculator")
    st.write("Instantly generate tiered pricing packages in ETB for your clients.")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        base_service_cost = st.number_input("Estimated Base Value / Cost (ETB)", min_value=100, value=1500, step=500)
    with col_p2:
        markup_percentage = st.slider("Target Profit Margin (%)", min_value=20, max_value=200, value=50)

    if st.button("📊 CALCULATE CLIENT PACKAGES", type="primary"):
        startup_price = int(base_service_cost * (1 + markup_percentage / 100))
        pro_price = int(startup_price * 2.2)
        enterprise_price = int(startup_price * 4.5)

        st.markdown(f"""
        <div class="result-card">
            <h3>🏷️ Recommended Client Tiers for {business_name}</h3>
            <hr style="border-color: #D4AF37;">
            <p><b>1. Startup Tier:</b> <span style="color: #D4AF37; font-size: 1.2rem;"><b>{startup_price:,} ETB</b></span><br>
            <i>Includes basic service delivery + 1 revision + telebirr support.</i></p>
            
            <p><b>2. Professional Tier (Best Seller):</b> <span style="color: #D4AF37; font-size: 1.2rem;"><b>{pro_price:,} ETB</b></span><br>
            <i>Includes priority delivery + full social media captions + Telegram broadcast post.</i></p>
            
            <p><b>3. Enterprise / Agency Tier:</b> <span style="color: #D4AF37; font-size: 1.2rem;"><b>{enterprise_price:,} ETB</b></span><br>
            <i>Includes full custom branding suite, TikTok video script, and dedicated support.</i></p>
            
            <p><b>📞 Book Client Now:</b> Call <b>{phone_number}</b> or pay via <b>{ ' | '.join(payment_method) }</b></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("AfriMarketing AI • Developed by FAFI Digitals")
