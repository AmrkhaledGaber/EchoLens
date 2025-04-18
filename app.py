import streamlit as st

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
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2em;
    margin-top: 40px;
}
.team-card {
    background: #2b2b2b;
    border: 1px solid #FF4B4B;
    border-radius: 10px;
    padding: 1em;
    text-align: center;
    color: white;
    width: 180px;
    transition: transform 0.3s ease;
    box-shadow: 0 0 10px rgba(255, 75, 75, 0.4);
}
.team-card img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 0.8em;
}
.team-card:hover {
    transform: scale(1.05);
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

# === ABOUT US ===
if page == "About Us":
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    # Title and Description
    st.markdown("""
    <h1 style='text-align:center; font-size: 36px; color: #FF4B4B;'>About Echolens</h1>
    <p style='text-align:center; font-size: 18px; color: #ccc; max-width: 800px; margin: 0 auto;'>
        We are a passionate team of AI developers turning vision into insight through video analysis and storytelling.
    </p>
    """, unsafe_allow_html=True)

    # Team Heading
    st.markdown("<h2 style='text-align:center; font-size: 30px; color: #FF4B4B; margin-top: 50px;'>Our Team</h2>", unsafe_allow_html=True)

    # Team Grid Section (Horizontal layout)
    team_members = [
        {"name": "Aya Tamer", "role": "AIS", "img": "aya_tamer.png"},
        {"name": "Mohamed ElSmawy", "role": "AIS", "img": "mohamed_elsmawy.png"},
        {"name": "George Nashaat", "role": "AIS", "img": "george_nashaat.png"},
        {"name": "Ahmed Dawood", "role": "AIS", "img": "ahmed_dawood.png"},
        {"name": "Amr Khaled", "role": "AIS", "img": "amr_khaled.png"},
    ]
    
    for member in team_members:
        st.markdown(f"""
        <div class='team-card'>
            <img src='https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/team/{member['img']}' alt='{member['name']}'>
            <h3 style='color: #FF4B4B;'>{member['name']}</h3>
            <p style='color: #ccc;'>{member['role']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Closing the section div

# === FOOTER ===
st.markdown("""<div class='footer'>
© 2025 Echolens | <a href='mailto:echolens9@gmail.com'>Email</a> | <a href='https://github.com/AmrkhaledGaber/EchoLens'>GitHub</a>
</div>""", unsafe_allow_html=True)
