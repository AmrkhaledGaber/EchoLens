# -*- coding: utf-8 -*-
"""
app.py

This is the main application file for the Video Story Generator.
"""

import streamlit as st

# Apply full UI redesign
st.set_page_config(page_title="Echolens", page_icon="🎥", layout="wide")

st.markdown("""
<style>
body {
    background: #0e0e0e;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    color: #FF4B4B;
    font-weight: 700;
    text-align: center;
}

.stApp {
    padding-top: 20px;
    background: linear-gradient(145deg, #1f1f1f, #121212);
    color: white;
    font-family: 'Segoe UI', sans-serif;
    animation: fadeIn 1s ease-in-out;
}

/* Card Style */
.card {
    background-color: #1f1f1f;
    border: 1px solid #FF4B4B;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 15px rgba(255, 75, 75, 0.3);
    margin-bottom: 30px;
    width: 100%;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

/* Button */
.stButton>button {
    background: linear-gradient(45deg, #FF4B4B, #C62828);
    color: white;
    font-weight: bold;
    padding: 10px 25px;
    border: none;
    border-radius: 8px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: #FF1744;
    box-shadow: 0 0 15px rgba(255, 75, 75, 0.6);
}

/* Input fields */
input, textarea {
    background-color: #2A2A2A;
    color: white;
    border: 1px solid #444;
    border-radius: 6px;
    padding: 10px;
    width: 100%;
    font-size: 16px;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    color: #aaa;
    font-size: 14px;
    margin-top: 40px;
    border-top: 1px solid #333;
}

@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# Home Page
if page == "Home":
    st.markdown("""
    <div class="card">
        <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png" style="width: 120px; border-radius: 50%; margin: 0 auto; display: block;">
        <h1>Echolens</h1>
        <p style="text-align:center; font-size:18px; color:#ccc;">Turn videos into stories with AI ✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("🎬 Video Story Generator")
    uploaded_file = st.file_uploader("Upload your video (MP4, AVI)", type=["mp4", "avi"])
    if uploaded_file:
        st.video(uploaded_file)
        st.success("Uploaded Successfully! (Processing not implemented in this mock UI)")

# About Us Page
elif page == "About Us":
    st.markdown("""
    <div class="card">
        <h1>About Us</h1>
        <p style='text-align:center; font-size:18px;'>We are a student team from AIU building AI-powered video analyzers for smarter storytelling.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👨‍💻 Our Team")
    cols = st.columns(5)
    team = [
        ("Mohamed ElSmawy", "AIS", "mohamed_elsmawy.png"),
        ("George Nashaat", "AIS", "george_nashaat.png"),
        ("Aya Tamer", "Team Leader", "aya_tamer.png"),
        ("Ahmed Dawood", "AIS", "ahmed_dawood.png"),
        ("Amr Khaled", "AIS", "amr_khaled.png")
    ]
    for i, (name, role, img) in enumerate(team):
        with cols[i]:
            st.markdown(f"""
            <div style='text-align:center;'>
                <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/{img}' style='width:90px;height:90px;border-radius:50%;margin-bottom:10px;'>
                <p><b>{name}</b><br><span style='color:#aaa;font-size:13px;'>{role}</span></p>
            </div>
            """, unsafe_allow_html=True)

# Contact Us Page
elif page == "Contact Us":
    st.markdown("""
    <div class="card">
        <h1>Contact Us</h1>
        <p style='text-align:center;'>We'd love to hear from you!</p>
        <p style='text-align:center; font-size:16px;'>📧 <a href='mailto:echolens9@gmail.com'>echolens9@gmail.com</a><br>
        🌐 <a href='https://github.com/AmrkhaledGaber/EchoLens'>GitHub Repo</a><br>
        🔗 <a href='https://linkedin.com/company/echolens'>LinkedIn</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✉️ Send Us a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"Thank you {name}! We’ll get back to you at {email} soon.")

# Footer
st.markdown("""
<div class="footer">
    &copy; 2025 Echolens | Built with ❤️ by the AIU Team
</div>
""", unsafe_allow_html=True)
