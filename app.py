import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="AfriMarketing AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Theme
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #FF6B35;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4A5568;
        margin-bottom: 30px;
    }
    .card {
        background-color: #F7FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B35;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=70)
st.sidebar.title("AfriMarketing AI")
st.sidebar.markdown("### Campaign Settings")

business_name = st.sidebar.text_input("Business Name", value="My Startup")
industry = st.sidebar.selectbox(
    "Industry / Niche",
    ["E-commerce & Retail", "AgriTech & Farming", "Fintech & Services", "Arts, Crafts & Fashion", "Tech & Software", "Hospitality & Tourism"]
)

target_platform = st.sidebar.selectbox(
    "Primary Platform",
    ["Telegram Channel", "TikTok / Reels", "Facebook Business", "Instagram Feed", "LinkedIn Professional"]
)

tone = st.sidebar.select_slider(
    "Brand Tone",
    options=["Professional", "Informative", "Energetic & Bold", "Warm & Cultural", "Persuasive"],
    value="Energetic & Bold"
)

# Main Content Area
st.markdown('<p class="main-header">AfriMarketing AI 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Empowering African businesses with AI-driven marketing strategies and high-converting copy.</p>', unsafe_allow_html=True)

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    product_description = st.text_area(
        "Describe your product, service, or campaign goal:",
        placeholder="e.g., Launching a new eco-friendly coffee packaging service in Addis Ababa with free delivery via Telegram...",
        height=120
    )

with col2:
    st.markdown("### Quick Tips")
    st.info("• Be specific about your target audience.\n• Mention key benefits (e.g., price, speed, local delivery).\n• Choose your tone carefully.")

# Generate Button
if st.button("✨ Generate AI Marketing Campaign", type="primary", use_container_width=True):
    if not product_description:
        st.warning("Please enter a product or campaign description first!")
    else:
        with st.spinner("AI is analyzing market trends and crafting your campaign..."):
            time.sleep(2) # Simulating AI processing time
            
        st.success("Campaign generated successfully!")
        
        # Results Tabs
        tab1, tab2, tab3 = st.tabs(["📢 Ad & Social Copy", "📅 Content Strategy", "🏷️ Hashtags & Keywords"])
        
        with tab1:
            st.markdown("### Generated Copy")
            st.markdown(f"""
            <div class="card">
            <b>Platform Optimized For:</b> {target_platform} <br>
            <b>Tone:</b> {tone}<br><br>
            <b>[Hook]:</b> Tired of the same old options? Discover how <b>{business_name}</b> is transforming the way you experience quality! 🇪🇹🔥<br><br>
            <b>[Value Proposition]:</b> {product_description}<br><br>
            <b>[Call to Action]:</b> Don't miss out! Tap the link below or message us directly on Telegram to place your order today. Limited stock available! 📦✨
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("📋 Copy to Clipboard (Simulated)"):
                st.toast("Copy action simulated successfully!")

        with tab2:
            st.markdown("### Recommended Weekly Content Calendar")
            st.markdown(f"""
            * **Monday (Awareness):** Introduce the core problem your product solves for customers in {industry}.
            * **Wednesday (Social Proof):** Share a customer success story or behind-the-scenes look at your operations.
            * **Friday (Conversion / Offer):** Highlight a weekend special discount or exclusive bundle deal tailored for {target_platform}.
            """)

        with tab3:
            st.markdown("### Recommended Hashtags & Keywords")
            st.code(f"#{business_name.replace(' ', '')} #MarketingAfrica #ECommerce #Innovation #AddisBusiness #{industry.replace(' ', '')} #GrowYourBusiness", language="text")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #A0AEC0;'>AfriMarketing AI • Built for the Innovation Café Showcase</p>", unsafe_allow_html=True)
