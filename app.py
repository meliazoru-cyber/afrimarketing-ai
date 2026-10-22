import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI | FAFI Digitals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End SaaS Styling
st.markdown("""
    <style>
    /* Hero Header */
    .hero-container {
        padding: 30px 20px;
        background: linear-gradient(135deg, #050505 0%, #111111 100%);
        border: 1px solid #1A1A1A;
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
        background: #080808 !important;
        border: 1px solid #1A1A1A;
        border-left: 4px solid #D4AF37;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }
    .result-card p, .result-card span, .result-card div, .result-card li, .result-card b, .result-card i {
        color: #FFFFFF !important;
    }
    .result-card h4 {
        color: #D4AF37 !important;
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

    /* Custom Metric Cards */
    .metric-box {
        background: #080808;
        border: 1px solid #1A1A1A;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .metric-val {
        color: #D4AF37 !important;
        font-size: 1.1rem;
        font-weight: bold;
    }

    /* Footer text color */
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

# Sidebar Design & Variables Definition
st.sidebar.markdown("<h3 style='color: #D4AF37 !important;'>✨ FAFI DIGITALS</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #FFFFFF !important; font-size: 0.8rem;'>AI Marketing Suite v2.0</p>", unsafe_allow_html=True)
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
        <p class="hero-subtitle">High-converting copywriting intelligence and localized campaign strategy built for modern African markets.</p>
    </div>
""", unsafe_allow_html=True)

# Main Form Layout
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    product_description = st.text_area(
        "✍️ Describe your product, service, or campaign goal:",
        placeholder="e.g., Luxury brand identity design, custom monograms, and video editing for local startups in Addis Ababa with fast telebirr checkout...",
        height=140
    )

with col2:
    st.markdown("<h4 style='color: #D4AF37 !important;'>⏰ Optimal Posting Times</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #FFFFFF;">Telegram Peak</div>
            <div class="metric-val">12:30 PM & 7:30 PM</div>
        </div>
        <br>
        <div class="metric-box">
            <div style="font-size: 0.8rem; color: #FFFFFF;">TikTok & Reels Peak</div>
            <div class="metric-val">6:00 PM – 9:30 PM</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Action Generator Button
if st.button("🚀 GENERATE CAMPAIGN SUITE", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please provide a description or campaign goal first!")
    else:
        with st.spinner("FAFI Digitals AI is synthesizing consumer behavior patterns..."):
            time.sleep(1.2)

        st.success("Campaign Suite Successfully Generated!")
        payments_str = " | ".join(payment_method) if payment_method else "Contact admin"

        # Tabs Setup
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔥 5 High-Conversion Captions", 
            "🎬 Video Storyboard Script", 
            "🧠 Consumer Persona Breakdown", 
            "📅 Weekly Schedule & Posting Times"
        ])

        # TAB 1: 5 CAPTIONS
        with tab1:
            st.markdown("<h3 style='color: #D4AF37 !important; margin-bottom: 20px;'>Generated Copy Options</h3>", unsafe_allow_html=True)

            captions = [
                ("STYLE 1: Direct Conversion", f"✨ **{business_name}** - {location}\n\n📌 **ለድርጅትዎ የሚሆን ምርጥ አሰራር:**\n{product_description}\n\n💳 **Payment:** {payments_str}\n📍 **Location:** {location}\n📞 **ለማዘዝ በቀጥታ ይደውሉ / Call/Text Now:** {phone_number}\n👉 Join our Telegram channel for exclusive updates!"),
                ("STYLE 2: Storytelling & Problem Solver", f"\"አዲስ ነገር ለሚፈልጉ ሁሉ! 🇪🇹🔥\"\n\nStruggling to stand out in {location}? **{business_name}** delivers the exact solution you need.\n\n{product_description}\n\n💡 Simple, reliable, and tailored for you.\n📲 **Direct Contact:** Call or message us directly at {phone_number}\n💳 **Accepted:** {payments_str}"),
                ("STYLE 3: Urgency & Flash Offer", f"⚡ **SPECIAL LIMITED OFFER THIS WEEK!** ⚡\n\n**{business_name}** brings you exclusive services in {location}.\n\n👉 {product_description}\n\n🔥 Only a few slots remaining for this week! Secure yours right now.\n📞 **Quick Booking:** Call or Telegram us at {phone_number}\n💳 **Payment via:** {payments_str}"),
                ("STYLE 4: Educational & Authority", f"💡 **Did you know?** Professional presentation increases customer trust by over 60% in local markets.\n\nAt **{business_name}**, we handle it effortlessly:\n• {product_description[:120]}...\n\n📩 Request a consultation today! Call/SMS: {phone_number}"),
                ("STYLE 5: Gen-Z / Trendy Hook", f"\"አዲስ አበቤዎች Check this out! 🇪🇹✨\"\n\nIf you want top-tier quality without the hassle, **{business_name}** has you covered.\n\n{product_description}\n\n👇 Message us on Telegram or call {phone_number} to order instantly! 💬")
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
                🎬 <b>0–3s (Visual Hook):</b> High-paced aesthetic montage of your work or workspace with trending Ethiopian background beat.<br><br>
                🗣️ <b>3–10s (Value Pitch):</b> Voiceover / On-screen text: <i>"Looking to upgrade your brand in {}? {} makes it seamless."</i><br><br>
                🎯 <b>10–15s (Call to Action):</b> Clean screen displaying your direct phone number <b>{}</b> and telebirr badge: <i>"Call or Telegram us right now at {} to book your slot!"</i>
                </p>
            </div>
            """.format(location, business_name, phone_number, phone_number)
            st.markdown(script_html, unsafe_allow_html=True)

        # TAB 3: INTELLIGENCE
        with tab3:
            st.markdown("<h3 style='color: #D4AF37 !important;'>🧠 AI Audience Insights</h3>", unsafe_allow_html=True)
            insight_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.7;">
                • <b>Target Audience:</b> Urban entrepreneurs, growing startups, and digital consumers (Ages 20–40) in {}.<br><br>
                • <b>Funnel Strategy:</b> TikTok / Instagram Awareness ➔ Telegram Channel / Direct Call ({}) ➔ telebirr Checkout.<br><br>
                • <b>Direct Conversion Tip:</b> Having phone number <b>{}</b> visible at the bottom of every post increases trust and phone orders by over 40%.
                </p>
            </div>
            """.format(location, phone_number, phone_number)
            st.markdown(insight_html, unsafe_allow_html=True)

        # TAB 4: CALENDAR & TIMINGS
        with tab4:
            st.markdown("<h3 style='color: #D4AF37 !important;'>📅 Weekly Schedule & Best Posting Hours</h3>", unsafe_allow_html=True)
            calendar_html = """
            <div class="result-card">
                <p style="color: #FFFFFF !important; line-height: 1.7;">
                🕒 <b>Best Hours to Post in Ethiopia (EAT):</b><br>
                • <b>Lunch Hours:</b> 12:30 PM – 2:00 PM (Highest Telegram & Facebook reading rate)<br>
                • <b>Evening Hours:</b> 6:30 PM – 9:30 PM (Peak TikTok & Instagram video consumption)<br><br>
                📅 <b>Weekly Posting Blueprint:</b><br>
                • <b>Monday (12:30 PM):</b> Post Educational (Style 4) to build market authority.<br>
                • <b>Wednesday (7:00 PM):</b> Share behind-the-scenes video or client proof with Storytelling (Style 2).<br>
                • <b>Friday (1:00 PM):</b> Push Limited Offer (Style 3) on Telegram with telebirr instructions & phone call CTA ({}).
                </p>
            </div>
            """.format(phone_number)
            st.markdown(calendar_html, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p class='main-footer'>AfriMarketing AI • Designed & Developed by <b>FAFI Digitals</b></p>", unsafe_allow_html=True)
