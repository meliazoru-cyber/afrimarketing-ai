import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI - Ethiopian Marketing Engine",
    page_icon="🇪🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header { font-size: 2.3rem; color: #1E293B; font-weight: 700; margin-bottom: 0px; }
    .sub-header { font-size: 1.0rem; color: #64748B; margin-bottom: 25px; }
    .ethiopian-card {
        background-color: #FFFDF9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #009E49; /* Ethiopian Flag Green */
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.title("🇪🇹 AfriMarketing AI")
st.sidebar.markdown("### Local Campaign Settings")

business_name = st.sidebar.text_input("Business / Brand Name", value="FAFI Digitals")

# Target Audience Location
location = st.sidebar.selectbox(
    "Primary Location Focus",
    ["Addis Ababa (Urban)", "Regional Cities (Hawassa, Adama, Bahir Dar, etc.)", "Diaspora Audience", "Nationwide"]
)

# Local Platform Selection
target_platform = st.sidebar.selectbox(
    "Target Channel",
    [
        "Telegram Channel & Bot", 
        "TikTok (Short Video Script)", 
        "Facebook Business Page", 
        "Instagram Carousel", 
        "LinkedIn Professional"
    ]
)

# Language Preference
language_style = st.sidebar.selectbox(
    "Language & Tone Style",
    [
        "Amharic + English Mix (Ethio-English Style)",
        "Pure Amharic (አማርኛ)",
        "Professional English (Export / Corporate)",
        "Trendy & Youthful (Gen-Z TikTok Style)"
    ]
)

# Payment & Delivery Options
payment_method = st.sidebar.multiselect(
    "Supported Payment & Delivery",
    ["telebirr", "CBE Birr", "Bank Transfer", "Cash on Delivery", "Free Local Delivery"],
    default=["telebirr", "Cash on Delivery"]
)

# Main Dashboard Header
st.markdown('<p class="main-header">AfriMarketing AI 🇪🇹</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Localized campaign generation designed for Ethiopian consumer habits and channels.</p>', unsafe_allow_html=True)

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    product_description = st.text_area(
        "Describe product, service, or promo offer:",
        placeholder="e.g., Offering luxury social media branding, logo vectors, and video editing for local startups in Addis Ababa with flexible telebirr payment options...",
        height=130
    )

with col2:
    st.markdown("### 💡 Local Conversion Rules")
    st.info("""
    * **Telegram:** Include clear price and contact handles.
    * **Trust:** Mention telebirr or Cash on Delivery options.
    * **Language:** Mixed Amharic/English performs best in urban centers.
    """)

# Campaign Generation Trigger
if st.button("✨ Generate Ethiopian Campaign", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please enter a description for your campaign or business!")
    else:
        with st.spinner("Analyzing Ethiopian market trends and drafting copy..."):
            time.sleep(1.5)

        st.success("Ethiopian Marketing Campaign Generated!")
        
        tab1, tab2, tab3 = st.tabs(["💬 Channel Ad Copy", "📹 Video / Storyboard Script", "📈 Local Conversion Strategy"])
        
        # TAB 1: Channel-Specific Copy
        with tab1:
            st.markdown("### Optimized Channel Post")
            
            payments_text = " | ".join(payment_method) if payment_method else "Contact for Payment"
            
            if "Telegram" in target_platform:
                st.markdown(f"""
                <div class="ethiopian-card">
                <b>[TELEGRAM POST TEMPLATE]</b><br><br>
                ✨ <b>{business_name}</b> - {location}<br><br>
                📌 <b>ስለ ድርጅታችን / About Us:</b><br>
                {product_description}<br><br>
                💡 <b>ለማዘዝ / How to Order:</b><br>
                • 💳 <b>Payment:</b> {payments_text}<br>
                • 🚚 <b>Delivery:</b> Fast delivery across {location}<br><br>
                📞 <b>Contact Admin:</b> @YourTelegramHandle or Call 09XXXXXXXX<br>
                👇 Join our channel for daily updates!
                </div>
                """, unsafe_allow_html=True)
                
            elif "TikTok" in target_platform:
                st.markdown(f"""
                <div class="ethiopian-card">
                <b>[TIKTOK CAPTION & HOOK]</b><br><br>
                <b>Hook Line (First 3 Sec):</b> "አዲስ አበቤዎች! Did you know this quick trick for your business?" 🇪🇹🔥<br><br>
                <b>Caption:</b> Transform your brand today with <b>{business_name}</b>. {product_description}<br><br>
                <b>Call to Action:</b> Comment 'INFO' or check the link in bio to text us on Telegram! 📩<br>
                <b>Payment Options:</b> {payments_text}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="ethiopian-card">
                <b>[SOCIAL MEDIA POST]</b><br><br>
                <b>{business_name}:</b> {product_description}<br><br>
                📍 Serving: {location}<br>
                💳 Payment Accepted: {payments_text}<br><br>
                📩 Send us a direct message or contact us on Telegram today!
                </div>
                """, unsafe_allow_html=True)

        # TAB 2: Short-Form Video Script
        with tab2:
            st.markdown("### 15-Second Short Video Concept (TikTok / Reels)")
            st.markdown(f"""
            * **0–3 Seconds (Visual Hook):** Show a fast behind-the-scenes shot of designing on a laptop or editing video in Addis Ababa with trendy Ethiopian background music.
            * **3–10 Seconds (Problem & Solution):** Voiceover explaining how **{business_name}** solves key client challenges: *"{product_description[:80]}..."*
            * **10–15 Seconds (Call to Action):** Screen shows your Telegram username and telebirr icon: *"Message us today to get started!"*
            """)

        # TAB 3: Strategic Local Recommendations
        with tab3:
            st.markdown("### Local Market Growth Tips")
            st.markdown(f"""
            1. **Channel Synergy:** Drive traffic from TikTok / Instagram directly into your **Telegram Channel** to build a retargetable subscriber list.
            2. **Trust & Social Proof:** Share client reviews, finished logo graphics, or video clips as screenshot posts on Telegram.
            3. **Payment Callouts:** Explicitly mention support for **{payments_text}** on graphics to remove friction for buyers.
            """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94A3B8;'>FAFI Digitals • Ethiopian Digital Marketing Framework</p>", unsafe_allow_html=True)
