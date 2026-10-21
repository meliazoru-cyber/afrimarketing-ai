import streamlit as st
import time

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
        color: #D4AF37;
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
    st.markdown("<h4 style='color: #D4AF37;'>📊 AI Market Analytics</h4>", unsafe_allow_html=True)
    st.info("""
    • Peak Telegram Engagement: 12:30 PM & 7:00 PM EAT.
    • Top Conversion Method: telebirr call-to-actions + Telegram direct admin link.
    • Best Format: Short video clips paired with mixed Amharic/English captions.
    """)

# Campaign Generation Trigger
if st.button("✨ Generate Full AI Campaign Suite", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please enter your business description first!")
    else:
        with st.spinner("FAFI Digitals AI is analyzing consumer behavior and generating copy..."):
            time.sleep(1.2)

        st.success("Campaign Suite Successfully Generated!")
        payments_text = " | ".join(payment_method) if payment_method else "Contact admin"

        # Tab Views
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔥 5 Caption Styles", 
            "📹 Video Script", 
            "🧠 AI Consumer Intelligence", 
            "📅 Weekly Calendar"
        ])

        # TAB 1: 5 CAPTION VARIATIONS
        with tab1:
            st.markdown("<h3 style='color: #D4AF37;'>Choose from 5 High-Converting Styles:</h3>", unsafe_allow_html=True)

            # Style 1
            st.markdown(f"""
            <div class="gold-card">
            <span class="ai-badge">STYLE 1</span> <b style="color: #D4AF37;">Direct Sales & Features</b><br><br>
            ✨ <b>{business_name}</b> - {location}<br><br>
            📌 <b>ለድርጅትዎ የሚሆን ምርጥ አሰራር / Looking for top quality?</b><br>
            {product_description}<br><br>
            💳 <b>Payment Options:</b> {payments_text}<br>
            📍 <b>Location:</b> {location}<br><br>
            📞 <b>ለማዘዝ / To Order:</b> DM us on Telegram or Call directly!<br>
            👉 Join our Telegram channel for exclusive updates.
            </div>
            """, unsafe_allow_html=True)

            # Style 2
            st.markdown(f"""
            <div class="gold-card">
            <span class="ai-badge">STYLE 2</span> <b style="color: #D4AF37;">Storytelling & Problem Solver</b><br><br>
            "አዲስ ነገር ለሚፈልጉ ሁሉ! 🇪🇹🔥"<br><br>
            Struggling to build a standout presence in {location}? <b>{business_name}</b> provides the exact solution you need.<br><br>
            {product_description}<br><br>
            💡 Simple process, guaranteed quality, and direct local support.<br>
            📲 <b>Contact us today:</b> Send a direct message or click the bio link.<br>
            💳 Accepted: {payments_text}
            </div>
            """, unsafe_allow_html=True)

            # Style 3
            st.markdown(f"""
            <div class="gold-card">
            <span class="ai-badge">STYLE 3</span> <b style="color: #D4AF37;">Limited-Time Promo & Urgency</b><br><br>
            ⚡ <b> SPECIAL OFFER FOR THIS WEEK ONLY! ⚡</b><br><br>
            <b>{business_name}</b> is offering premium services right here in {location}.<br><br>
            👉 {product_description}<br><br>
            🔥 Only 5 slots remaining for this week's bookings! Message right now to claim yours.<br>
            💳 Easy payment via <b>{payments_text}</b>.
            </div>
            """, unsafe_allow_html=True)

            # Style 4
            st.markdown(f"""
            <div class="gold-card">
            <span class="ai-badge">STYLE 4</span> <b style="color: #D4AF37;">Educational & Value-First</b><br><br>
            💡 <b>Did you know?</b> A strong digital visual identity can increase client trust by over 60% in local markets.<br><br>
            At <b>{business_name}</b>, we help you achieve this effortlessly:<br>
            • {product_description[:100]}...<br><br>
            📩 Send us a quick message today to request a free consultation!
            </div>
            """, unsafe_allow_html=True)

            # Style 5
            st.markdown(f"""
            <div class="gold-card">
            <span class="ai-badge">STYLE 5</span> <b style="color: #D4AF37;">Trendy Hook (TikTok / Stories)</b><br><br>
            "አዲስ አበቤዎች Check this out! 🇪🇹✨"<br><br>
            If you've been looking for quality service without the hassle, <b>{business_name}</b> has you covered.<br><br>
            {product_description}<br><br>
            👇 Tap the link in bio to text us on Telegram directly! 💬
            </div>
            """, unsafe_allow_html=True)

        # TAB 2
        with tab2:
            st.markdown("<h3 style='color: #D4AF37;'>15-Second Short Video Concept (TikTok / Reels)</h3>", unsafe_allow_html=True)
            st.markdown(f"""
            * **0–3s (Visual Hook):** Quick visual clip of vector graphics or design process with trending audio.
            * **3–10s (Value Pitch):** Voiceover: *"Looking to upgrade your brand identity in {location}? {business_name} makes it effortless."*
            * **10–15s (Call to Action):** Screen shows your Telegram handle and telebirr badge: *"Message us on Telegram to get started!"*
            """)

        # TAB 3
        with tab3:
            st.markdown("<h3 style='color: #D4AF37;'>🧠 AI Market Insights & Target Persona</h3>", unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("""
                <div class="gold-card">
                <b style="color: #D4AF37;">Target Customer Persona:</b><br><br>
                • <b>Demographic:</b> Urban entrepreneurs, startup owners, and content creators (Ages 20–40).<br>
                • <b>Primary Hubs:</b> Telegram channels, TikTok, and Instagram.<br>
                • <b>Key Buying Trigger:</b> Fast response rate on Telegram and price transparency.
                </div>
                """, unsafe_allow_html=True)

            with col_b:
                st.markdown("""
                <div class="gold-card">
                <b style="color: #D4AF37;">Conversion Rate Optimization:</b><br><br>
                • <b>Channel Funnel:</b> TikTok video -> Telegram Channel -> Direct Admin Call.<br>
                • <b>Trust Signals:</b> Display telebirr logo and past design samples.<br>
                • <b>Best Language:</b> Amharic/English mixed dialect.
                </div>
                """, unsafe_allow_html=True)

        # TAB 4
        with tab4:
            st.markdown("<h3 style='color: #D4AF37;'>📅 Recommended Weekly Content Calendar</h3>", unsafe_allow_html=True)
            st.markdown("""
            * **Monday (Awareness):** Post **Style 4 (Educational)** to introduce key service benefits.
            * **Wednesday (Social Proof):** Share a completed project screenshot with **Style 2**.
            * **Friday (Conversion / Deal):** Post **Style 3 (Limited Offer)** on Telegram with telebirr payment instructions.
            """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888888;'>AfriMarketing AI • Created by <b>FAFI Digitals</b></p>", unsafe_allow_html=True)
