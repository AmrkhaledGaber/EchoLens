import streamlit as st

# --- Custom CSS (Glassmorphism + Dark Neon Theme) ---
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(145deg, #0f0f0f, #1c1c1c);
    font-family: 'Segoe UI', sans-serif;
    color: #FFFFFF;
}

h1, h2, h3, h4 {
    text-align: center;
    color: #ffffff;
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.glass-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 30px;
    margin: 30px auto;
    max-width: 700px;
}

.stButton > button {
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    color: white;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #ff4b2b;
}

.footer {
    text-align: center;
    margin-top: 50px;
    padding: 20px;
    color: #999;
    font-size: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}
a {
    color: #ff4b2b;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# --- Page Title ---
st.markdown('<h1>Echolens</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#bbb;">AI-powered video insights made simple.</p>', unsafe_allow_html=True)

# --- Upload Card ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.subheader("Upload Your Video")
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])

if uploaded_file:
    st.success("Video uploaded successfully!")
    st.video(uploaded_file)

    st.subheader("Select Language for Story")
    lang = st.selectbox("Choose language", ["English", "Arabic", "French", "German"])

    if st.button("Process Video"):
        st.info(f"Processing video in {lang}...")
        st.success("✅ Story generated successfully!")
        st.write("This is a mock story generated from your video. (Integrate your logic here.)")

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    &copy; 2025 Echolens — Crafted with ❤️ by Team AIS |
    <a href="https://github.com/AmrkhaledGaber/EchoLens" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)
