# Echolens - Stylish AI Video Story Generator

import streamlit as st

# === Page Configuration ===
st.set_page_config(page_title="Echolens | AI Video Generator", layout="wide")

# === Custom CSS Styling ===
st.markdown("""
<style>
body, .stApp {
    background: linear-gradient(135deg, #101010, #1a1a1a);
    color: #f2f2f2;
    font-family: 'Segoe UI', sans-serif;
    font-size: 16px;
}

h1, h2, h3 {
    color: #FF4B4B;
    text-align: center;
    margin-bottom: 20px;
}

a { color: #FF4B4B; text-decoration: none; }
a:hover { text-decoration: underline; }

.nav-title {
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
    color: #fff;
}

.logo {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}
.logo img {
    width: 150px;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(255, 75, 75, 0.6);
    transition: transform 0.3s ease;
}
.logo img:hover {
    transform: scale(1.1);
}

.section {
    max-width: 1200px;
    margin: auto;
    padding: 3rem 2rem;
}

.team-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    padding-top: 2rem;
}
.team-card {
    background: #1f1f1f;
    border: 2px solid #FF4B4B;
    border-radius: 12px;
    width: 200px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 5px 15px rgba(255, 75, 75, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.team-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(255,75,75,0.3);
}
.team-card img {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border-radius: 50%;
    margin-bottom: 0.8rem;
    box-shadow: 0 0 12px rgba(255, 75, 75, 0.4);
}

.footer {
    text-align: center;
    padding: 2rem;
    color: #aaa;
    border-top: 1px solid #333;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# === Sidebar Navigation ===
st.sidebar.markdown("""<p class='nav-title'>Navigation</p>""", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# === Home Page ===
if page == "Home":
    st.markdown('<div class="logo"><img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png"></div>', unsafe_allow_html=True)
    st.markdown("""
    <h1>Echolens</h1>
    <h3>Turning Videos into Stories with AI</h3>
    <div class='section'>
        <h2>Upload Your Video</h2>
        <p style='text-align:center;'>Supported formats: MP4, AVI | Max size: 200MB</p>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
    if uploaded_file:
        st.success("File uploaded successfully!")
        st.video(uploaded_file)
    st.markdown("</div>", unsafe_allow_html=True)

# === About Us Page ===
elif page == "About Us":
    st.markdown("""
        <div class='section'>
            <h1>About Echolens</h1>
            <p style='text-align:center; max-width:700px; margin:auto;'>
                We are a passionate team of AI developers turning vision into insight through video analysis and storytelling.
            </p>
            <h2>Our Team</h2>
            <div class='team-container'>
                <div class='team-card'>
                    <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/aya_tamer.png' />
                    <h4>Aya Tamer</h4>
                    <p>AIS</p>
                </div>
                <div class='team-card'>
                    <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/mohamed_elsmawy.png' />
                    <h4>Mohamed ElSmawy</h4>
                    <p>AIS</p>
                </div>
                <div class='team-card'>
                    <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/george_nashaat.png' />
                    <h4>George Nashaat</h4>
                    <p>AIS</p>
                </div>
                <div class='team-card'>
                    <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/ahmed_dawood.png' />
                    <h4>Ahmed Dawood</h4>
                    <p>AIS</p>
                </div>
                <div class='team-card'>
                    <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/amr_khaled.png' />
                    <h4>Amr Khaled</h4>
                    <p>AIS</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# === Contact Page ===
elif page == "Contact Us":
    st.markdown("""
    <div class='section'>
        <h1>Contact Us</h1>
        <p style='text-align:center;'>We’d love to hear from you. Contact us anytime:</p>
        <div style='text-align:center; line-height:2em;'>
            📧 <strong>Email:</strong> <a href='mailto:echolens9@gmail.com'>echolens9@gmail.com</a><br>
            🌐 <strong>GitHub:</strong> <a href='https://github.com/AmrkhaledGaber/EchoLens'>Echolens Project</a><br>
            🔗 <strong>LinkedIn:</strong> <a href='https://linkedin.com/company/echolens'>Echolens Team</a>
        </div>
        <br><br>
        <h2 style='text-align:center;'>Send a Message</h2>
    """, unsafe_allow_html=True)

    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"Thanks, {name}! We'll contact you at {email} soon.")
    st.markdown("</div>", unsafe_allow_html=True)

# === Footer ===
st.markdown("""<div class='footer'>© 2025 Echolens | <a href='mailto:echolens9@gmail.com'>Email</a> | <a href='https://github.com/AmrkhaledGaber/EchoLens'>GitHub</a></div>""", unsafe_allow_html=True)
