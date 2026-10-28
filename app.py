import streamlit as st
import time

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

st.set_page_config(page_title="AfriMarketing AI", page_icon="⚡", layout="centered")

# Minimal Obsidian & Gold Styling
st.markdown("""
    <style>
    .stApp { background-color: #0F0F0F; color: #FFFFFF; }
    .stTextInput input, .stTextArea textarea { background-color: #FFFFFF !important; color: #000000 !important; font-weight: bold; border: 2px solid #D4AF37; }
    label { color: #D4AF37 !important; font-weight: bold; }
    .card { background: #1A1A1A; border-left: 4px solid #D4AF37; padding: 16px; border-radius: 8px; margin-bottom: 12px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("✨ FAFI DIGITALS")
business_name = st.sidebar.text_input("Business Name", value="FAFI Digitals")
phone_number = st.sidebar.text_input("Phone Number", value="0901183481")
location = st.sidebar.selectbox("Location", ["Addis Ababa Urban", "Nationwide"])
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Main UI
st.title("AfriMarketing AI 🇪🇹")
st.caption("FAFI Digitals Quick Campaign Generator")

product_desc = st.text_area("Describe your product or service:", placeholder="e.g., Premium branding & logo packages...")

if st.button("🚀 GENERATE CAMPAIGN", type="primary", use_container_width=True):
    if not product_desc:
        st.warning("Please enter a description.")
    else:
        with st.spinner("Generating..."):
            time.sleep(0.5)
            
            # AI or Built-in Output
            caption = f"✨ **{business_name}** ({location})\n\n📌 {product_desc}\n\n📞 Call/Telegram: {phone_number}\n💳 telebirr Accepted!"
            script = f"🎥 **TikTok Hook (15s):**\n1. Show work in {location}\n2. Say: 'አዲስ አበቤዎች! Check this out.'\n3. Call {phone_number}"

        st.success("Generated Successfully!")

        tab1, tab2 = st.tabs(["🔥 Caption", "🎬 TikTok Script"])
        
        with tab1:
            st.markdown(f'<div class="card">{caption}</div>', unsafe_allow_html=True)
            st.code(caption, language="markdown")
            
        with tab2:
            st.markdown(f'<div class="card">{script}</div>', unsafe_allow_html=True)
