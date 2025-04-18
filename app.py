# Echolens Web App (Streamlit Version)

import streamlit as st

# Page Configuration
st.set_page_config(page_title="Echolens | AI Video Story Generator", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body, .stApp {
            background: linear-gradient(135deg, #101010, #1a1a1a);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            text-align: center;
            color: #FF4B4B;
        }
        .hero {
            text-align: center;
            padding: 3em;
        }
        .hero img {
            width: 150px;
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255, 75, 75, 0.5);
        }
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            padding: 2em 1em;
        }
        .member-card {
            background: #2c2c2c;
            border: 1px solid #FF4B4B;
            border-radius: 10px;
            padding: 1em;
            width: 200px;
            text-align: center;
        }
        .member-card img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 1em;
        }
        .footer {
            text-align: center;
            color: #888;
            font-size: 0.9em;
            padding: 2em;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# Home Page
if page == "Home":
    st.markdown("""
        <div class='hero'>
            <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png' alt='Echolens Logo'>
            <h1>Echolens</h1>
            <h3>Turning Videos into Stories with AI</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.header("Upload Your Video")
    st.write("Supported formats: MP4, AVI | Max size: 200MB")
    uploaded_video = st.file_uploader("Upload Video", type=["mp4", "avi"])
    if uploaded_video:
        st.success("File uploaded successfully!")
        st.video(uploaded_video)

# About Us Page
elif page == "About Us":
    st.markdown("""
        <h1>About Echolens</h1>
        <p style='text-align:center; max-width: 800px; margin: 0 auto;'>
            We are a passionate team of AI developers turning vision into insight through video analysis and storytelling.
        </p>
        <h2 style='margin-top: 40px;'>Our Team</h2>
    """, unsafe_allow_html=True)

    team = [
        {"name": "Aya Tamer", "role": "AIS", "img": "aya_tamer.png"},
        {"name": "Mohamed ElSmawy", "role": "AIS", "img": "mohamed_elsmawy.png"},
        {"name": "George Nashaat", "role": "AIS", "img": "george_nashaat.png"},
        {"name": "Ahmed Dawood", "role": "AIS", "img": "ahmed_dawood.png"},
        {"name": "Amr Khaled", "role": "AIS", "img": "amr_khaled.png"},
    ]

    st.markdown("<div class='team-container'>", unsafe_allow_html=True)
    for member in team:
        st.markdown(f"""
            <div class='member-card'>
                <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/{member['img']}' alt='{member['name']}'>
                <h4>{member['name']}</h4>
                <p style='color:#ccc'>{member['role']}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Us Page
elif page == "Contact Us":
    st.markdown("""
        <h1>Contact Us</h1>
        <p style='text-align: center;'>We'd love to hear from you! Contact us using the info below:</p>
        <div style='text-align:center;'>
            📧 Email: <a href='mailto:echolens9@gmail.com'>echolens9@gmail.com</a><br>
            🌐 GitHub: <a href='https://github.com/AmrkhaledGaber/EchoLens'>Echolens Project</a><br>
            🔗 LinkedIn: <a href='https://linkedin.com/company/echolens'>Echolens Team</a>
        </div>
        <br><br>
    """, unsafe_allow_html=True)

    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        send = st.form_submit_button("Send")
        if send:
            st.success(f"Thank you, {name}. We'll get back to you at {email}.")

# Footer
st.markdown("""
<div class='footer'>
    &copy; 2025 Echolens | Designed with ❤️ by the AI Team
</div>
""", unsafe_allow_html=True)
