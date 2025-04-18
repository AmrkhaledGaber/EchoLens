# -*- coding: utf-8 -*-
"""
Echolens: AI-Powered Video Story Generator
Redesigned Streamlit App UI (Full Version)
"""

import streamlit as st
import os

# === CONFIG ===
st.set_page_config(page_title="Echolens - Video Story Generator", layout="centered")

# === STYLING ===
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
    font-family: 'Segoe UI', sans-serif;
    color: white;
}
h1, h2, h3 {
    color: #FF4B4B;
    text-align: center;
}
a { color: #FF4B4B; text-decoration: none; }
a:hover { text-decoration: underline; }
.logo-container {
    text-align: center;
    margin-top: 2em;
}
.logo-container img {
    width: 140px;
    border-radius: 50%;
    transition: transform 0.3s ease;
    box-shadow: 0 0 20px rgba(255, 75, 75, 0.5);
}
.logo-container img:hover {
    transform: scale(1.05);
}
.section {
    max-width: 900px;
    margin: 2em auto;
    padding: 2em;
    background: #1f1f1f;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1.5em;
    justify-content: center;
    padding: 2em 1em;
}
.team-card {
    background: #2b2b2b;
    border: 1px solid #FF4B4B;
    border-radius: 10px;
    padding: 1em;
    text-align: center;
    color: white;
}
.team-card img {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 0.8em;
    box-shadow: 0 0 10px rgba(255, 75, 75, 0.4);
}
.footer {
    margin-top: 3em;
    text-align: center;
    font-size: 0.9em;
    padding: 2em;
    color: #999;
}
</style>
""", unsafe_allow_html=True)

# === NAV ===
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# === HOME ===
if page == "Home":
    st.markdown('<div class="logo-container"><img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png" alt="Logo"></div>', unsafe_allow_html=True)
    st.markdown("""<h1>Echolens</h1><h3>Turning Videos into Stories with AI</h3>""", unsafe_allow_html=True)
    st.markdown("""
    <div class='section'>
        <h2>Upload Your Video</h2>
        <p style='text-align:center;'>Supported formats: MP4, AVI | Max size: 200MB</p>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        st.video(uploaded_file)
    st.markdown("</div>", unsafe_allow_html=True)

# === ABOUT US ===
# === ABOUT US ===
elif page == "About Us":
    st.markdown("<div class='section' style='padding: 40px 0; background-color: #121212;'>", unsafe_allow_html=True)

    # Title and Description
    st.markdown("""
    <h1 style='text-align:center; font-size: 36px; color: #FF4B4B;'>About Echolens</h1>
    <p style='text-align:center; font-size: 18px; color: #ccc; max-width: 800px; margin: 0 auto;'>
        We are a passionate team of AI developers turning vision into insight through video analysis and storytelling.
    </p>
    """, unsafe_allow_html=True)

    # Team Heading
    st.markdown("<h2 style='text-align:center; font-size: 30px; color: #FF4B4B; margin-top: 50px;'>Our Team</h2>", unsafe_allow_html=True)

    # Team Grid Section
    st.markdown("<div class='team-grid' style='display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 30px; justify-items: center; padding: 30px;'>", unsafe_allow_html=True)

    # List of Team Members
    team_members = [
        {"name": "Aya Tamer", "role": "AIS", "img": "aya_tamer.png"},
        {"name": "Mohamed ElSmawy", "role": "AIS", "img": "mohamed_elsmawy.png"},
        {"name": "George Nashaat", "role": "AIS", "img": "george_nashaat.png"},
        {"name": "Ahmed Dawood", "role": "AIS", "img": "ahmed_dawood.png"},
        {"name": "Amr Khaled", "role": "AIS", "img": "amr_khaled.png"},
    ]
    
    for member in team_members:
        st.markdown(f"""
        <div class='team-card' style='background: linear-gradient(135deg, #2A2A2A, #121212); padding: 20px; text-align: center; border-radius: 15px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);'>
            <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/{member['img']}' alt='{member['name']}' style='border-radius: 50%; width: 150px; height: 150px; object-fit: cover; margin-bottom: 15px;'>
            <h3 style='color: #FF4B4B;'>{member['name']}</h3>
            <p style='color: #ccc;'>{member['role']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)  # Closing the team grid section



# === CONTACT US ===
elif page == "Contact Us":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("""<h1>Contact Us</h1>
    <p style='text-align: center;'>Questions or feedback? Reach out to us anytime.</p>
    <div style='text-align:center; font-size:18px;'>
        📧 <strong>Email:</strong> <a href='mailto:echolens9@gmail.com'>echolens9@gmail.com</a><br>
        🌐 <strong>GitHub:</strong> <a href='https://github.com/AmrkhaledGaber/EchoLens'>Echolens Project</a><br>
        🔗 <strong>LinkedIn:</strong> <a href='https://linkedin.com/company/echolens'>Echolens Team</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center;'>Send Us a Message</h2>", unsafe_allow_html=True)
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"Thanks, {name}! We'll contact you soon at {email}.")
    st.markdown("</div>", unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""<div class='footer'>
© 2025 Echolens | <a href='mailto:echolens9@gmail.com'>Email</a> | <a href='https://github.com/AmrkhaledGaber/EchoLens'>GitHub</a>
</div>""", unsafe_allow_html=True)
