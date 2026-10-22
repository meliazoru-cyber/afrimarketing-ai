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
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling - Obsidian Black, Metallic Gold & Telegram Mockup
st.markdown("""
    <style>
    /* Global Pure Dark Background */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    /* Reset Typography */
    h1, h2, h3, h4, h5, h6, p, span, label, div, li, small {
        color: #FFFFFF !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Hero Branding Card */
    .hero-container {
        padding: 32px 24px;
        background: linear-gradient(145deg, #080808 0%, #121212 100%) !important;
        border: 1px solid #222222 !important;
        border-radius: 18px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.95);
    }
    .hero-title {
        font-size: 2.9rem;
        font-weight: 900;
        color: #D4AF37 !important;
        letter-spacing: -0.5px;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #DDDDDD !important;
        margin-top: 6px;
    }
    .agency-tag {
        display: inline-block;
        background: rgba(212, 175, 55, 0.12) !important;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    /* Telegram Message Preview Simulation */
    .tg-preview-card {
        background: #17212B !important;
        border: 1px solid #2B5278 !important;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 24px rgba(0,0,0,0.7);
    }
    .tg-header {
        color: #64B5F6 !important;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Creative Result Card */
    .result-card {
        background: #080808 !important;
        border: 1px solid #222222 !important;
        border-left: 4px solid #D4AF37 !important;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }
    .result-card p, .result-card span, .result-card div, .result-card li, .result-card b, .result-card i {
        color: #FFFFFF !important;
    }

    /* Style Pills */
    .style-pill {
        background: #D4AF37 !important;
        color: #000000 !important;
        font-weight: 800;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        text-transform: uppercase;
    }

    /* Analytics Boxes */
    .metric-box {
        background: #080808 !important;
        border: 1px solid #222222 !important;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.15rem;
        font-weight: bold;
    }

    /* Dark Input Controls */
    .stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        color: #FFFFFF !important;
    }
    ul[data-baseweb="menu"] {
        background-color: #111111 !important;
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

# Sidebar Setup
st.sidebar.markdown("<h3 style='color: #D4AF37 !important;'>✨ FAFI DIGITALS</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.8rem;'>AfriMarketing AI Studio v3.5</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
location = st.sidebar.selectbox("📍 Target Market", ["Addis Ababa Urban", "Regional Centers (Hawassa, Adama, etc.)", "Ethiopian Diaspora", "Nationwide"])
brand_tone = st.sidebar.selectbox("🎨 Campaign Vibe / Tone", ["High-End Luxury", "Gen-Z Viral Slang", "Direct Sales Heavy", "Educational & Trust"])
payment_method = st.sidebar.multiselect("💳 Payment Methods", ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery"], default=["telebirr", "Cash on Delivery"])

st.sidebar.markdown("---")
gemini_api_key = st.sidebar.text_input("🔑 Gemini API Key (Optional)", type="password", help="Leave blank for built-in local engine!")

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="agency-tag">FAFI Digitals Creative Engine</div>
        <p class="hero-title">AfriMarketing AI 🇪🇹</p>
        <p class="hero-subtitle">High-converting copywriting intelligence, viral TikTok scripts, and Telegram previews built for the Ethiopian market.</p>
    </div>
""", unsafe_allow_html=True)

# Main Form Layout
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    product_description = st.text_area(
        "✍️ What product or service are you launching today?",
        placeholder="e.g., Premium logo vectors, visual identity design, and social media video editing packages for startups in Addis Ababa...",
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
            <div style="font-size: 0.8rem; color: #CCCCCC;">TikTok Video Hook Peak</div>
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
        except Exception as e:
            return None
    return None

# Campaign Generation Trigger
if st.button("🚀 GENERATE CREATIVE CAMPAIGN SUITE", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please describe your offer or business goal first!")
    else:
        with st.spinner("FAFI Digitals AI is crafting your customized marketing suite..."):
            payments_str = " | ".join(payment_method) if payment_method else "Contact admin"
            
            ai_prompt = f"""
            Act as a top-tier digital marketer for {business_name} in Ethiopia.
            Tone: {brand_tone}
            Offer: {product_description}
            Location: {location}
            Payment: {payments_str}
            Phone: {phone_number}

            Create:
            1. 5 Ethio-English social captions with clear calls-to-action to call {phone_number}.
            2. A 15-second viral TikTok video storyboard with precise visual actions, voiceovers, and on-screen text.
            3. A Telegram post layout optimized for channel broadcats.
            4. Local trending hashtags.
            """
            
            ai_output = generate_ai_content(ai_prompt)
            time.sleep(1.0)

        st.success("Campaign Suite Crafted Successfully!")

        # Tabs Setup
        tab1, tab2, tab3, tab4 = st.tabs([
            "📲 Live Telegram Mockup", 
            "🔥 5 High-Conversion Captions", 
            "🎬 TikTok Storyboard Script", 
            "📅 Weekly Growth Blueprint"
        ])

        # TAB 1: LIVE TELEGRAM MOCKUP
        with tab1:
            st.markdown("<h3 style='color: #D4AF37 !important;'> Telegram Post Channel Preview</h3>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 0.85rem;'>Here is how your broadcast will appear on your audience's phones:</p>", unsafe_allow_html=True)

            tg_sample_text = f"✨ <b>{business_name.upper()}</b> | {location.upper()}<br><br>📌 <b>ለድርጅትዎ የሚሆን ምርጥ አሰራር:</b><br>{product_description}<br><br>💳 <b>የክፍያ መንገዶች / Payment:</b> {payments_str}<br>📍 <b>አድራሻ / Location:</b> {location}<br><br>📞 <b>ለማዘዝ በቀጥታ ይደውሉ:</b> {phone_number}<br>📲 <b>Telegram Admin:</b> @FAFIdigitals"

            st.markdown(f"""
            <div class="tg-preview-card">
                <div class="tg-header">📢 {business_name} Official Broadcast</div>
                <div style="font-size: 0.95rem; line-height: 1.6;">{tg_sample_text}</div>
                <div style="text-align: right; font-size: 0.75rem; color: #64B5F6; margin-top: 10px;">12:30 PM • 1.4K views</div>
            </div>
            """, unsafe_allow_html=True)

        # TAB 2: CAPTIONS
        with tab2:
            st.markdown("<h3 style='color: #D4AF37 !important; margin-bottom: 20px;'>Copywriting Options ({})</h3>".format(brand_tone), unsafe_allow_html=True)
            
            if ai_output:
                st.markdown(f"""
                <div class="result-card">
                    <span class="style-pill">DYNAMIC GEMINI AI OUTPUT</span>
                    <p style="color: #FFFFFF !important; white-space: pre-line; line-height: 1.6; margin-top: 15px;">{ai_output}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                captions = [
                    ("STYLE 1: Direct Sales CTA", f"✨ **{business_name}** - {location}\n\n📌 **ለድርጅትዎ የሚሆን ምርጥ አሰራር:**\n{product_description}\n\n💳 **Payment:** {payments_str}\n📍 **Location:** {location}\n📞 **ለማዘዝ በቀጥታ ይደውሉ / Call/Text Now:** {phone_number}\n👉 Join our official channel for direct daily updates!"),
                    ("STYLE 2: Storytelling & Solution", f"\"አዲስ ነገር ለሚፈልጉ ሁሉ! 🇪🇹🔥\"\n\nStruggling to stand out in {location}? **{business_name}** provides the exact solution you need.\n\n{product_description}\n\n💡 Simple, reliable, and tailored for your brand growth.\n📲 **Direct Contact:** Call or message us directly at {phone_number}\n💳 **Accepted:** {payments_str}"),
                    ("STYLE 3: Urgency & Limited Slots", f"⚡ **SPECIAL LIMITED OFFER THIS WEEK!** ⚡\n\n**{business_name}** brings you exclusive services in {location}.\n\n👉 {product_description}\n\n🔥 Only 5 client slots remaining for this week! Secure yours now.\n📞 **Quick Booking:** Call or Telegram us at {phone_number}\n💳 **Payment via:** {payments_str}"),
                    ("STYLE 4: Educational & Value-First", f"💡 **Did you know?** Professional presentation increases customer trust by over 60% in local markets.\n\nAt **{business_name}**, we handle it effortlessly:\n• {product_description}\n\n📩 Request a consultation today! Call/SMS: {phone_number}"),
                    ("STYLE 5: Gen-Z Viral Hook", f"\"አዲስ አበቤዎች Check this out! 🇪🇹✨\"\n\nIf you want top-tier quality without the usual hassle, **{business_name}** has you covered.\n\n{product_description}\n\n👇 Text us on Telegram or call {phone_number} to order instantly! 💬")
                ]

                for title, text in captions:
                    short_title = title.split(':')[0]
                    card_html = """
                    <div class="result-card">
                        <span class="style-pill">{}</span>
                        <h4 style="color: #D4AF37 !important; margin-top: 10px;">{}</h4>
                        <p style="color: #FFFFFF !important; white-space: pre-line; line-height: 1.6;">{}</p>
                    </div>
                    """.format(short_title, title, text)
                    st.markdown(card_html, unsafe_allow_html=True)

        # TAB 3: TIKTOK SCRIPT
        with tab3:
            st.markdown("<h3 style='color: #D4AF37 !important;'>15-Second Viral Video Storyboard</h3>", unsafe_allow_html=True)
            script_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.8;">
                🎥 <b>0–3s (Visual Hook):</b> High-energy fast cuts showing your work or studio process in {} with trending audio.<br>
                🗣️ <b>
