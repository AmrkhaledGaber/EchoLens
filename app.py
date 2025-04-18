# app.py (Echolens - Redesigned UI)
import streamlit as st

# Inject custom CSS for stylish UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f0f0f, #1c1c1c);
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }
    .main-header {
        text-align: center;
        padding: 50px 0;
    }
    .main-header h1 {
        font-size: 48px;
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .main-header p {
        font-size: 20px;
        color: #ccc;
        margin-top: 10px;
    }
    .nav-sidebar .css-1d391kg { background-color: #1c1c1c !important; }
    .section {
        padding: 30px 20px;
        margin: 20px 0;
        background-color: #2a2a2a;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.2);
    }
    .section h2 {
        color: #ff4b4b;
    }
    .footer {
        margin-top: 60px;
        padding: 20px;
        text-align: center;
        border-top: 1px solid #333;
        color: #777;
    }
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }
    .team-card {
        background-color: #1c1c1c;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #ff4b4b44;
    }
    .team-card img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .team-card h4 { color: #ff4b4b; margin: 5px 0; }
    .team-card p { color: #aaa; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Echolens")
page = st.sidebar.radio("Navigate", ["Home", "About Us", "Contact Us"])

# Header Section
st.markdown("""
<div class="main-header">
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png" width="120" style="border-radius: 50%;">
    <h1>Echolens</h1>
    <p>Turning Videos into Stories with AI</p>
</div>
""", unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Video Story Generator")
    uploaded_file = st.file_uploader("Upload your MP4/AVI file", type=["mp4", "avi"])
    if uploaded_file:
        st.video(uploaded_file)
        st.success("Video uploaded successfully! (processing code not included in this demo)")
    st.markdown('</div>', unsafe_allow_html=True)

# About Us Page
elif page == "About Us":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Meet Our Team")
    st.markdown("""
    <div class="team-grid">
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

# Contact Us Page
elif page == "Contact Us":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Contact Us")
    st.markdown("""
    <p>Email: <a href="mailto:echolens9@gmail.com" style="color:#FF4B4B">echolens9@gmail.com</a></p>
    <p>GitHub: <a href="https://github.com/AmrkhaledGaber/EchoLens" style="color:#FF4B4B">Echolens Project</a></p>
    <p>LinkedIn: <a href="https://linkedin.com/company/echolens" style="color:#FF4B4B">Echolens Team</a></p>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thanks {name}, we will contact you at {email}!")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2025 Echolens. Built with ❤️ by the Team.
</div>
""", unsafe_allow_html=True)
