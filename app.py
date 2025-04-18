# app.py

import streamlit as st
import os

# ----- Page Config -----
st.set_page_config(
    page_title="Echolens - AI Video Story Generator",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ----- CSS Styling -----
st.markdown("""
<style>
body {
    background-color: #0e0e0e;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Hero Section */
.hero {
    text-align: center;
    padding-top: 60px;
}
.hero img {
    width: 150px;
    border-radius: 50%;
    box-shadow: 0 0 20px #00fff7;
}
.hero h1 {
    color: #00fff7;
    margin-top: 20px;
    font-size: 36px;
}
.hero p {
    color: #aaaaaa;
    font-size: 18px;
}

/* Upload Card */
.upload-card {
    background: #1a1a1a;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #00fff7;
    box-shadow: 0 0 15px #00fff740;
    margin-top: 40px;
}

/* Result Box */
.result-box {
    background: #1a1a1a;
    padding: 25px;
    border-radius: 12px;
    border-left: 5px solid #00fff7;
    margin-top: 30px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 30px 0 10px 0;
    color: #777;
    font-size: 14px;
    margin-top: 50px;
    border-top: 1px solid #222;
}
</style>
""", unsafe_allow_html=True)

# ----- Sidebar Navigation -----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# ----- Pages -----
if page == "Home":
    st.markdown("""
    <div class="hero">
        <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_transparent.png" alt="Echolens Logo">
        <h1>Echolens</h1>
        <p>Transforming Videos into Stories with AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="upload-card">
        <h3 style="color: #00fff7;">Upload your video</h3>
        <p style="color: #ccc;">Supported formats: MP4, AVI. Max size: 200 MB.</p>
    </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["mp4", "avi"])

    if uploaded_file:
        with st.spinner("\U0001F9E0 AI is analyzing your video..."):
            # Simulate logic
            st.success("Analysis complete!")
            st.video(uploaded_file)

            st.markdown("""
            <div class="result-box">
                <h4 style="color: #00fff7;">Classification</h4>
                <p style="color: white;">Example: Violence</p>
            </div>
            <div class="result-box">
                <h4 style="color: #00fff7;">Generated Story</h4>
                <p style="color: white;">This video depicts a scene of sudden aggression in a public area, possibly signaling an urgent situation. A person runs while others react in panic.</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "About Us":
    st.markdown("""
    <div class="hero">
        <h1>About Echolens</h1>
        <p>We are a team of AI enthusiasts passionate about turning video content into meaningful narratives through advanced machine learning models.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Contact Us":
    st.markdown("""
    <div class="hero">
        <h1>Contact Us</h1>
        <p>Email: contact@echolens.com<br>GitHub: <a style="color:#00fff7" href="https://github.com/echolens">Echolens Project</a></p>
    </div>
    """, unsafe_allow_html=True)

# ----- Footer -----
st.markdown("""
<div class="footer">
    <p>© 2025 Echolens. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
