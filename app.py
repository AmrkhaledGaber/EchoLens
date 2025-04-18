# app.py (Echolens - Sleek Neon Theme)
import streamlit as st

# Apply custom CSS for an ultra-modern neon theme
st.markdown("""
    <style>
    body {
        background: #0a0a0a;
        font-family: 'Segoe UI', sans-serif;
        color: #fff;
    }
    .stApp {
        padding: 0;
        margin: 0;
        background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
        color: #eee;
    }
    .header {
        text-align: center;
        padding: 60px 0 30px;
    }
    .header img {
        width: 130px;
        border-radius: 50%;
        margin-bottom: 20px;
        box-shadow: 0 0 30px #00eaff;
    }
    .header h1 {
        font-size: 48px;
        color: #00eaff;
        text-shadow: 0 0 10px #00eaff;
    }
    .header p {
        font-size: 18px;
        color: #ccc;
    }
    .section {
        background: #1a1a1a;
        border: 1px solid #00eaff44;
        border-radius: 12px;
        padding: 30px;
        margin: 30px auto;
        max-width: 900px;
        box-shadow: 0 0 15px #00eaff33;
    }
    .section h2 {
        color: #00eaff;
        margin-bottom: 20px;
    }
    .footer {
        margin-top: 50px;
        padding: 20px;
        text-align: center;
        font-size: 14px;
        color: #777;
        border-top: 1px solid #333;
    }
    .team-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
    }
    .team-card {
        text-align: center;
        background: #121212;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #00eaff33;
        box-shadow: 0 0 10px #00eaff22;
    }
    .team-card img {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
        border: 2px solid #00eaff;
    }
    .team-card h4 {
        color: #00eaff;
        margin: 5px 0;
    }
    .team-card p {
        color: #aaa;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Echolens")
page = st.sidebar.radio("Navigate", ["Home", "About Us", "Contact Us"])

# Header
st.markdown("""
<div class="header">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png">
    <h1>Echolens</h1>
    <p>Turning Videos into Stories with AI</p>
</div>
""", unsafe_allow_html=True)

if page == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Video Story Generator")
    uploaded_file = st.file_uploader("Upload your MP4/AVI file", type=["mp4", "avi"])
    if uploaded_file:
        st.video(uploaded_file)
        st.success("Video uploaded successfully! (processing code not included in this demo)")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "About Us":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Our Team")
    st.markdown("""
    <div class="team-container">
        <div class="team-card">
            <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/mohamed_elsmawy.png">
            <h4>Mohamed ElSmawy</h4>
            <p>AI Developer</p>
        </div>
        <div class="team-card">
            <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/george_nashaat.png">
            <h4>George Nashaat</h4>
            <p>Vision Engineer</p>
        </div>
        <div class="team-card">
            <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/aya_tamer.png">
            <h4>Aya Tamer</h4>
            <p>Project Leader</p>
        </div>
        <div class="team-card">
            <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/ahmed_dawood.png">
            <h4>Ahmed Dawood</h4>
            <p>Backend Developer</p>
        </div>
        <div class="team-card">
            <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/amr_khaled.png">
            <h4>Amr Khaled</h4>
            <p>Frontend Developer</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Contact Us":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Contact Us")
    st.markdown("""
    <p>Email: <a href="mailto:echolens9@gmail.com" style="color:#00eaff">echolens9@gmail.com</a></p>
    <p>GitHub: <a href="https://github.com/AmrkhaledGaber/EchoLens" style="color:#00eaff">Echolens Project</a></p>
    <p>LinkedIn: <a href="https://linkedin.com/company/echolens" style="color:#00eaff">Echolens Team</a></p>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thanks {name}, we'll reach out at {email}.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    &copy; 2025 Echolens. Designed with 🚀 and 💙.
</div>
""", unsafe_allow_html=True)
