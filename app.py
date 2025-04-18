import streamlit as st
import cv2
import numpy as np
import av
import torch
from ultralytics import YOLO
from transformers import VivitForVideoClassification, VivitImageProcessor
from transformers import MarianMTModel, MarianTokenizer  # Imports for translation
import google.generativeai as genai
import os
import io
from PIL import Image
from google.api_core.exceptions import ResourceExhausted
from collections import Counter

# Add custom CSS for styling the UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1E1E1E, #121212);
        color: white;
        font-family: 'Poppins', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }

    h1, h2, h3 {
        color: #FF4B4B;
        text-align: center;
        transition: transform 0.3s ease;
        animation: fadeIn 1s ease-in-out;
    }

    h1 {
        background: linear-gradient(45deg, #FF4B4B, #D32F2F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 75, 75, 0.5);
        position: relative;
        margin-bottom: 40px;
    }

    h1::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(45deg, #FF4B4B, #D32F2F);
        border-radius: 2px;
    }

    h1:hover, h2:hover, h3:hover {
        transform: scale(1.05);
    }

    /* Fade-in Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
        width: 100%;
    }

    .logo-image {
        width: 200px;
        height: auto;
        transition: transform 0.3s ease;
        border-radius: 50%;
    }

    .logo-image:hover {
        transform: translateY(-5px) scale(1.03);
    }

    .clearfix::after {
        content: "";
        display: table;
        clear: both;
    }

    .content-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }

    /* Instructions Icon and Popup */
    .instructions-icon {
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(45deg, #FF4B4B, #D32F2F);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        z-index: 1001;
    }

    .instructions-icon:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(255, 75, 75, 0.6);
    }

    .instructions-popup {
        display: none;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #2A2A2A, #1E1E1E);
        color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        z-index: 1000;
        width: 90%;
        max-width: 450px;
        text-align: left;
        border: 1px solid #FF4B4B;
    }

    .instructions-popup.show {
        display: block;
    }

    .instructions-popup h4 {
        margin-top: 0;
        color: #FF4B4B;
        font-size: 20px;
        border-bottom: 1px solid #FF4B4B;
        padding-bottom: 10px;
    }

    .instructions-popup p {
        line-height: 1.6;
    }

    .close-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        background: #FF4B4B;
        color: white;
        border: none;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        cursor: pointer;
        font-size: 16px;
        line-height: 30px;
        text-align: center;
        transition: background 0.3s ease;
    }

    .close-btn:hover {
        background: #D32F2F;
    }

    /* File Uploader Card */
    .file-uploader-card {
        background: linear-gradient(135deg, #2A2A2A, #1E1E1E);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        margin: 20px 0;
        border: 2px solid transparent;
        border-image: linear-gradient(45deg, #FF4B4B, #D32F2F) 1;
        width: 100%;
        max-width: 600px;
    }

    .stFileUploader {
        background: transparent !important;
    }

    .stFileUploader label {
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    .stFileUploader div[role="button"] {
        background: linear-gradient(45deg, #FF4B4B, #D32F2F) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    .stFileUploader div[role="button"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4) !important;
    }

    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #D32F2F);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #2A2A2A, #1E1E1E);
        margin-top: 40px;
        border-radius: 10px 10px 0 0;
        box-shadow: 0 -3px 10px rgba(0, 0, 0, 0.2);
        border-top: 1px solid #FF4B4B;
        width: 100%;
    }

    a {
        color: #FF4B4B;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# Home Page
if page == "Home":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Instructions Icon and Popup
    st.markdown("""
    <div class="instructions-icon" onclick="document.getElementById('instructions-popup').classList.toggle('show')">
        ?
    </div>
    <div id="instructions-popup" class="instructions-popup">
        <button class="close-btn" onclick="document.getElementById('instructions-popup').classList.remove('show')">×</button>
        <h4>Usage Instructions</h4>
        <p>
            1. Upload a video (up to 200 MB) in MP4 or AVI format.<br>
            2. Wait for the video to be processed.<br>
            3. The results (classification, story, and video details) will appear below in English.<br>
            4. Use the buttons to translate the story into other languages.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Logo and Title (Centered Block)
    st.markdown("""
    <div style="width: 100%; max-width: 600px; margin: 0 auto; padding:50px 10px; text-align: center;">
        <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png"
             alt="Logo"
             width="180"
             style="border-radius: 50%; margin-bottom: 15px;">
        <h2 style="margin: 0; color: #FF4B4B;">Echolens</h2>
        <p style="margin-top: 5px; font-size: 25px; color: #ccc;">Turning Videos into Stories with AI</p>
    </div>
    """, unsafe_allow_html=True)

    # File uploader for video input wrapped in a card
    st.markdown('<div class="file-uploader-card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
    st.markdown('</div>', unsafe_allow_html=True)

    # Main function to handle the app logic
    def main():
        if uploaded_file is not None:
            # Save the uploaded video
            with open("input_video.mp4", "wb") as f:
                f.write(uploaded_file.read())

            # Process the video with a spinner
            with st.spinner("Processing..."):
                yolo_model, processor, vivit_model, gemini_model = load_models()
                
                # Calculate original video duration and frame count
                original_duration, original_frame_count = get_video_info("input_video.mp4")
                
                # Preprocess the video
                preprocessed_video = preprocess_video("input_video.mp4", "preprocessed_video.mp4")
                
                # Extract keyframes and collect event timings and objects
                keyframes_video, event_timestamps, object_counts, saved_frames = extract_keyframes(preprocessed_video, yolo_model)
                
                # Calculate keyframes video duration and frame count
                keyframes_duration, keyframes_frame_count = get_video_info(keyframes_video) if keyframes_video else (0, 0)
                
                # Detect anomaly
                prediction = anomaly_detection(keyframes_video, processor, vivit_model)
                
                # Generate story in English based on the keyframes video
                story = generate_story(keyframes_video, prediction, gemini_model)

            # Display the processed video
            st.video("input_video.mp4")

            # Display video details in an expander
            with st.expander("Video Details"):
                st.subheader("Video Information")
                st.write(f"**Original Video Duration**: {original_duration:.2f} seconds")
                st.write(f"**Original Video Frame Count**: {original_frame_count}")
                st.write(f"**Keyframes Video Duration**: {keyframes_duration:.2f} seconds")
                st.write(f"**Keyframes Video Frame Count**: {keyframes_frame_count}")
                st.write("**Event Timings (seconds)**:")
                if event_timestamps:
                    for i, timestamp in enumerate(event_timestamps, 1):
                        st.write(f"- Event {i}: {timestamp:.2f} seconds")
                else:
                    st.write("- No significant events detected.")
                st.write("**Detected Objects (by YOLO)**:")
                if object_counts:
                    for obj, count in object_counts.items():
                        st.write(f"- {obj}: {count}")
                else:
                    st.write("- No objects detected.")

            # Display results in an expander
            with st.expander("Processing Results"):
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Classification")
                    st.write(prediction)
                with col2:
                    st.subheader("Story (English)")
                    st.write(story)

            # Add translation buttons for the story
            st.subheader("Translate Story")
            target_languages = ["es", "fr", "de", "ar"]
            language_names = {"es": "Spanish", "fr": "French", "de": "German", "ar": "Arabic"}
            st.markdown('<div class="translate-buttons">', unsafe_allow_html=True)
            cols = st.columns(len(target_languages))  # Create columns for buttons
            translations = {}  # Store translations to avoid re-computing

            for idx, lang in enumerate(target_languages):
                with cols[idx]:
                    if st.button(f"To {language_names[lang]}"):
                        if lang not in translations:
                            # Translate the story to the target language
                            with st.spinner(f"Translating to {language_names[lang]}..."):
                                translated_story = translate_text(story, lang)
                                if translated_story:
                                    translations[lang] = translated_story
                        # Display the translated story if available
                        if lang in translations:
                            st.write(f"Story ({language_names[lang]}):")
                            st.write(translations[lang])
            st.markdown('</div>', unsafe_allow_html=True)

            # Add a download button for the story (English version)
            st.download_button(
                label="Download Story (English)",
                data=story,
                file_name="video_description.txt",
                mime="text/plain"
            )

    # Function to load models with caching to avoid reloading
    @st.cache_resource
    def load_models():
        # Load YOLOv8 model
        yolo_model = YOLO("yolov8n.pt")  # Load directly from Ultralytics
        
        # Load ViViT model for anomaly detection
        processor = VivitImageProcessor.from_pretrained("prathameshdalal/vivit-b-16x2-kinetics400-UCF-Crime", token=os.getenv("HF_TOKEN"))
        vivit_model = VivitForVideoClassification.from_pretrained("prathameshdalal/vivit-b-16x2-kinetics400-UCF-Crime", token=os.getenv("HF_TOKEN"))

        # Configure Gemini model with API key
        genai.configure(api_key="AIzaSyCZFf2r-fmE9uRQjKebHfF_MZhDKwiZP7A")
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")

        return yolo_model, processor, vivit_model, gemini_model

    if __name__ == "__main__":
        main()

    st.markdown('</div>', unsafe_allow_html=True)  # Close content-container
