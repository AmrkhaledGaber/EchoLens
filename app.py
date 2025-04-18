import streamlit as st

# Apply modern dark-glass style with custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(to bottom right, #0f0f0f, #1f1f1f);
        color: #fff;
        font-family: 'Outfit', sans-serif;
    }

    h1, h2, h3 {
        color: #FF6B6B;
        text-align: center;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
    }

    .glass-box input, .glass-box textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #fff !important;
        border-radius: 10px !important;
    }

    .glass-box label {
        font-weight: 500;
    }

    .btn-primary {
        background: linear-gradient(to right, #ff4b4b, #ff6b6b);
        border: none;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }

    .btn-primary:hover {
        background: linear-gradient(to right, #ff3c3c, #ff5c5c);
        transform: translateY(-2px);
    }

    a {
        color: #FF6B6B;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📂 Menu")
page = st.sidebar.radio("Navigate to", ["Home", "About", "Contact"])

# Logo and Heading
st.markdown("""
<div style='text-align:center'>
    <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png" style='width:120px; border-radius:50%; margin-top:30px;'>
    <h1>Echolens</h1>
    <p style='color:#bbb'>Turning Videos into Stories with AI</p>
</div>
""", unsafe_allow_html=True)

if page == "Home":
    st.markdown("""
    <div class="glass-box">
        <h2>🎬 Upload your video</h2>
        <p style='text-align:center;'>Supported formats: mp4, avi (max 200MB)</p>
    """, unsafe_allow_html=True)

    uploaded_video = st.file_uploader("Upload your video", type=["mp4", "avi"])

    if uploaded_video:
        st.video(uploaded_video)
        st.success("Video uploaded successfully! Ready to process.")

    st.markdown("</div>", unsafe_allow_html=True)

elif page == "About":
    st.markdown("""
    <div class="glass-box">
        <h2>👩‍💻 About Echolens</h2>
        <p>
            Echolens is a smart AI-powered tool designed to turn videos into readable, meaningful stories.
            It analyzes motion, extracts keyframes, classifies content, and even generates summaries in multiple languages.
        </p>
        <p style='text-align:center;'>Built with ❤️ using Streamlit, YOLO, ViViT, and Gemini API.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("""
    <div class="glass-box">
        <h2>📫 Contact Us</h2>
        <p style='text-align:center;'>We're happy to hear from you! Drop us a message below or reach out directly.</p>

        <form action="mailto:echolens9@gmail.com" method="post" enctype="text/plain">
            <label>Your Name</label><br>
            <input type="text" name="name" style="width:100%; padding:10px;"><br><br>

            <label>Your Email</label><br>
            <input type="email" name="email" style="width:100%; padding:10px;"><br><br>

            <label>Your Message</label><br>
            <textarea name="message" rows="5" style="width:100%; padding:10px;"></textarea><br><br>

            <input type="submit" value="Send Message" class="btn-primary">
        </form>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="margin-top:50px; border-color:#444">
<div style='text-align:center; color:#999'>
    <small>© 2025 Echolens | <a href='mailto:echolens9@gmail.com'>echolens9@gmail.com</a></small>
</div>
""", unsafe_allow_html=True)
