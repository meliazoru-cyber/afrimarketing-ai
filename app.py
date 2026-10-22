import streamlit as st
import time

# Optional Live AI Integration
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

# Custom High-End SaaS Styling (Locked Obsidian Black, Gold & Crisp White)
st.markdown("""
    <style>
    /* Force Full Black Background Everywhere */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    /* Force All Text and Headers to Pure White */
    h1, h2, h3, h4, h5, h6, p, span, label, div, li, small {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }

    /* Hero Header Container */
    .hero-container {
        padding: 30px 20px;
        background: #0A0A0A !important;
        border: 1px solid #222222 !important;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.9);
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
        margin-top: 5px;
    }
    .agency-tag {
        display: inline-block;
        background: rgba(212, 175, 55, 0.1) !important;
        color: #D4AF37 !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    /* Result Cards Styling */
    .result-card {
        background: #080808 !important;
        border: 1px solid #222222 !important;
        border-left: 4px solid #D4AF37 !important;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }
    .result-card p, .result-card span, .result-card div, .result-card li, .result-card b {
        color: #FFFFFF !important;
    }
    .result-card h4 {
        color: #D4AF37 !important;
    }

    /* Style Badges */
    .style-pill {
        background: #D4AF37 !important;
        color: #000000 !important;
        font-weight: 800;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        text-transform: uppercase;
    }

    /* Metric Boxes */
    .metric-box {
        background: #080808 !important;
        border: 1px solid #222222 !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.1rem;
        font-weight: bold;
    }

    /* Input Fields & Dropdowns Black Background */
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
    .main-footer b {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Design & Controls
st.sidebar.markdown("<h3 style='color: #D4AF37 !important;'>✨ FAFI DIGITALS</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.8rem;'>AI Marketing Suite v3.0</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

gemini_api_key = st.sidebar.text_input("🔑 Gemini API Key (Optional)", type="password")
st.sidebar.markdown("---")

business_name = st.sidebar.text_input("🏢 Business / Brand Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("📞 Direct Contact Number", value="0901183481")
location = st.sidebar.selectbox("📍 Target Market", ["Addis Ababa Urban", "Regional Centers", "Ethiopian Diaspora", "Nationwide"])
target_platform = st.sidebar.selectbox("🎯 Primary Channel", ["Telegram Channel & Bot", "TikTok / Reels", "Instagram Carousel", "Facebook Page"])
payment_method = st.sidebar.multiselect("💳 Payment Options", ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery"], default=["telebirr", "Cash on Delivery"])

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="agency-tag">Powered by FAFI Digitals</div>
        <p class="hero-title">AfriMarketing AI 🇪🇹</p>
        <p class="hero-subtitle">Advanced AI copywriting intelligence and deep localized marketing strategy engineered for Ethiopia.</p>
    </div>
""", unsafe_allow_html=True)

# Main Form Layout
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    product_description = st.text_area(
        "✍️ Describe your product, service, or campaign goal in detail:",
        placeholder="e.g., Premium branding, logo design, and automated marketing tools for startups in Addis Ababa with fast telebirr checkout...",
        height=140
    )

with col2:
    st.markdown("<h4 style='color: #D4AF37 !important;'>⏰ Optimal Posting Times</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #FFFFFF;">Telegram Peak</div>
            <div class="metric-val">12:30 PM & 7:30 PM EAT</div>
        </div>
        <br>
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #FFFFFF;">TikTok & Reels Peak</div>
            <div class="metric-val">6:00 PM – 9:30 PM EAT</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

def generate_ai_content(prompt):
    if GEMINI_AVAILABLE and gemini_api_key:
        try:
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"API Error: {str(e)}"
    return None

# Action Generator Button
if st.button("🚀 GENERATE ADVANCED AI CAMPAIGN", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please provide a detailed product description first!")
    else:
        with st.spinner("FAFI Digitals AI is analyzing Ethiopian consumer data and generating deep campaign assets..."):
            payments_str = " | ".join(payment_method) if payment_method else "Contact admin"
            
            ai_prompt = f"""
            You are an expert Ethiopian digital marketing strategist working for {business_name}. 
            Product/Service: {product_description}
            Target Market: {location}
            Primary Platform: {target_platform}
            Payment Methods: {payments_str}
            Direct Phone Number: {phone_number}

            Provide a comprehensive, highly detailed marketing output including:
            1. 5 distinct high-converting social media captions mixing Amharic and English (Ethio-English style), ensuring phone number {phone_number} and payment methods are included.
            2. A 15-second viral TikTok/Reels video script with hook, body, and call-to-action.
            3. Deep consumer persona breakdown and conversion strategy for Addis Ababa.
            4. Tailored local hashtags for Ethiopian social media.
            """
            
            ai_output = generate_ai_content(ai_prompt)
            time.sleep(1.0)

        st.success("Advanced Campaign Suite Successfully Generated!")

        # Tabs Setup
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔥 AI Copy & Captions", 
            "🎬 Video Script & Hook", 
            "🧠 Deep Market Persona", 
            "🏷️ Hashtags & Growth Plan"
        ])

        # TAB 1: CAPTIONS
        with tab1:
            st.markdown("<h3 style='color: #D4AF37 !important; margin-bottom: 20px;'>Generated Copy Options</h3>", unsafe_allow_html=True)
            
            if ai_output and "API Error" not in ai_output:
                st.markdown(f"""
                <div class="result-card">
                    <span class="style-pill">LIVE GEMINI AI GENERATION</span>
                    <p style="color: #FFFFFF !important; white-space: pre-line; line-height: 1.6;">{ai_output}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                captions = [
                    ("STYLE 1: Direct Conversion & Value", f"✨ **{business_name}** - {location}\n\n📌 **ለድርጅትዎ የሚሆን ምርጥ አሰራር:**\n{product_description}\n\n💳 **Payment Methods:** {payments_str}\n📍 **Location:** {location}\n📞 **ለማዘዝ በቀጥታ ይደውሉ / Call/Text Now:** {phone_number}\n👉 Join our official Telegram channel for daily updates & offers!"),
                    ("STYLE 2: Problem-Solver & Storytelling", f"\"አዲስ ነገር ለሚፈልጉ ሁሉ! 🇪🇹🔥\"\n\nAre you struggling to get results in {location}? **{business_name}** is here to solve your exact challenges.\n\n{product_description}\n\n💡 Professional quality, fast delivery, and trusted local support.\n📲 **Direct Contact:** Call or message us directly at {phone_number}\n💳 **Accepted:** {payments_str}"),
                    ("STYLE 3: Urgency & Flash Offer", f"⚡ **SPECIAL LIMITED-TIME OFFER!** ⚡\n\n**{business_name}** brings you high-end solutions right here in {location}.\n\n👉 {product_description}\n\n🔥 Only a few client slots left this week! Don't miss out.\n📞 **Quick Booking:** Call or Telegram us at {phone_number}\n💳 **Payment via:** {payments_str}"),
                    ("STYLE 4: Educational & Trust Building", f"💡 **Did you know?** Investing in professional digital presentation increases customer trust by over 65% in the Ethiopian market.\n\nAt **{business_name}**, we make it effortless:\n• {product_description}\n\n📩 Request your consultation today! Call/SMS: {phone_number}"),
                    ("STYLE 5: Gen-Z / Trendy TikTok Hook", f"\"አዲስ አበቤዎች Check this out! 🇪🇹✨\"\n\nIf you want premium results without the usual hassle, **{business_name}** has got you covered.\n\n{product_description}\n\n👇 Message us on Telegram or call {phone_number} to order instantly! 💬")
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

        # TAB 2: SCRIPT
        with tab2:
            st.markdown("<h3 style='color: #D4AF37 !important;'>15-Second Short Video Concept (TikTok / Reels)</h3>", unsafe_allow_html=True)
            script_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.7;">
                🎬 <b>0–3s (Visual Hook):</b> High-paced aesthetic footage of your work or workspace in Addis Ababa with trending Ethiopian background beat.<br><br>
                🗣️ <b>3–10s (Value Pitch):</b> Voiceover / On-screen text: <i>"Looking for top-tier quality in {}? {} delivers exactly what you need."</i><br><br>
                🎯 <b>10–15s (Call to Action):</b> Clean screen displaying your direct phone number <b>{}</b> and telebirr badge: <i>"Call or Telegram us right now at {} to book your slot!"</i>
                </p>
            </div>
            """.format(location, business_name, phone_number, phone_number)
            st.markdown(script_html, unsafe_allow_html=True)

        # TAB 3: INTELLIGENCE
        with tab3:
            st.markdown("<h3 style='color: #D4AF37 !important;'>🧠 Deep Addis Ababa Market Persona</h3>", unsafe_allow_html=True)
            insight_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.7;">
                • <b>Target Demographic:</b> Urban entrepreneurs, young professionals, and digital business owners (Ages 20–40) in {}.<br><br>
                • <b>Consumer Psychology:</b> Ethiopian buyers heavily value transparency, quick responses, and local payment trust (telebirr). Displaying phone number <b>{}</b> builds immediate human credibility.<br><br>
                • <b>Conversion Funnel:</b> TikTok / Instagram Short Video ➔ Telegram Channel Subscriber ➔ Direct Call / Telebirr Checkout.
                </p>
            </div>
            """.format(location, phone_number)
            st.markdown(insight_html, unsafe_allow_html=True)

        # TAB 4: HASHTAGS & GROWTH
        with tab4:
            st.markdown("<h3 style='color: #D4AF37 !important;'>🏷️ Local Hashtags & Growth Blueprint</h3>", unsafe_allow_html=True)
            growth_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.7;">
                📌 <b>Recommended Ethiopian Hashtags:</b><br>
                #AddisAbaba #Ethiopia #AddisBusiness #HabeshaDigital #Telebirr #FAFI_Digitals #EthiopianStartups #MadeInEthiopia #AddisTraders<br><br>
                🕒 <b>Best Posting Hours (EAT):</b><br>
                • <b>Lunch (12:30 PM – 2:00 PM):</b> Best for Telegram channel updates.<br>
                • <b>Evening (6:30 PM – 9:30 PM):</b> Best for TikTok videos and Instagram reels with phone call CTA ({}).
                </p>
            </div>
            """.format(phone_number)
            st.markdown(growth_html, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p class='main-footer'>AfriMarketing AI • Designed & Developed by <b>FAFI Digitals</b></p>", unsafe_allow_html=True)
