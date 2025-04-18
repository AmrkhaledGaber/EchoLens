# -*- coding: utf-8 -*-
"""
app.py

Main application for Echolens - Video Story Generator.
This app allows users to upload a video, detects anomalies and objects,
generates a descriptive story using Gemini AI, and allows translation to other languages.
"""

import streamlit as st
import cv2
import numpy as np
import av
import torch
from ultralytics import YOLO
from transformers import VivitForVideoClassification, VivitImageProcessor
from transformers import MarianMTModel, MarianTokenizer
import google.generativeai as genai
import os
import io
from PIL import Image
from google.api_core.exceptions import ResourceExhausted
from collections import Counter

# -----------------------------
# UI Custom CSS
# -----------------------------
# Injects dark mode themed CSS styles for modern visual design
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
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "Contact Us"])

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Upload Instructions Icon
    st.markdown("""... (instructions markup omitted for brevity) ...""", unsafe_allow_html=True)

    # App Branding Block (Logo + Title)
    st.markdown("""
    <div style="width: 100%; max-width: 600px; text-align: center; padding: 50px 10px;">
        <img src="https://raw.githubusercontent.com/AmrkhaledGaber/EchoLens/main/logo_Ech.png" width="180" style="border-radius: 50%;">
        <h2 style="color: #FF4B4B;">Echolens</h2>
        <p style="color: #ccc; font-size: 25px;">Turning Videos into Stories with AI</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Video Story Generator")

    # File Upload UI
    st.markdown('<div class="file-uploader-card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # Main Logic
    # -----------------------------
    def main():
        if uploaded_file is not None:
            # Save video locally
            with open("input_video.mp4", "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner("Processing..."):
                yolo_model, processor, vivit_model, gemini_model = load_models()

                original_duration, original_frame_count = get_video_info("input_video.mp4")
                preprocessed_video = preprocess_video("input_video.mp4", "preprocessed_video.mp4")

                keyframes_video, timestamps, object_counts, saved = extract_keyframes(preprocessed_video, yolo_model)
                keyframes_duration, keyframes_frame_count = get_video_info(keyframes_video) if keyframes_video else (0, 0)

                prediction = anomaly_detection(keyframes_video, processor, vivit_model)
                story = generate_story(keyframes_video, prediction, gemini_model)

            st.video("input_video.mp4")

            # Display Video Metadata
            with st.expander("Video Details"):
                st.write(f"Original Duration: {original_duration:.2f} sec")
                st.write(f"Original Frames: {original_frame_count}")
                st.write(f"Keyframe Duration: {keyframes_duration:.2f} sec")
                st.write(f"Keyframe Frames: {keyframes_frame_count}")
                st.write("Detected Objects:")
                st.write(object_counts)

            # Display Results
            with st.expander("Processing Results"):
                st.write("Prediction:", prediction)
                st.write("Generated Story:")
                st.write(story)

    # -----------------------------
    # Model Loader (with cache)
    # -----------------------------
    @st.cache_resource
    def load_models():
        yolo_model = YOLO("yolov8n.pt")
        processor = VivitImageProcessor.from_pretrained("prathameshdalal/vivit-b-16x2-kinetics400-UCF-Crime", token=os.getenv("HF_TOKEN"))
        vivit_model = VivitForVideoClassification.from_pretrained("prathameshdalal/vivit-b-16x2-kinetics400-UCF-Crime", token=os.getenv("HF_TOKEN"))
        genai.configure(api_key="AIzaSyCZFf2r-fmE9uRQjKebHfF_MZhDKwiZP7A")
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        return yolo_model, processor, vivit_model, gemini_model

    # -----------------------------
    # Video Utility Functions
    # -----------------------------
    def get_video_info(path):
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()
        return (frames / fps, frames) if fps else (0, frames)

    def preprocess_video(src, dst, size=(224, 224)):
        cap = cv2.VideoCapture(src)
        out = cv2.VideoWriter(dst, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(5)), size)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            resized = cv2.resize(frame, size)
            out.write(resized)
        cap.release()
        out.release()
        return dst

    def extract_keyframes(path, model, output_path="keyframes.mp4"):
        cap = cv2.VideoCapture(path)
        ret, prev = cap.read()
        if not ret:
            return None, [], {}, 0
        fps = cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(cap.get(3)), int(cap.get(4))))
        gray_prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        timestamps, objects, count = [], [], 0
        while cap.isOpened():
            ret, curr = cap.read()
            if not ret:
                break
            gray_curr = cv2.cvtColor(curr, cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(gray_prev, gray_curr)
            if cv2.countNonZero(diff) > 50000:
                out.write(curr)
                count += 1
                timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC)/1000)
                results = model(curr)
                for r in results:
                    for box in r.boxes:
                        objects.append(r.names[int(box.cls)])
            gray_prev = gray_curr
        cap.release()
        out.release()
        return output_path, timestamps, dict(Counter(objects)), count

    def anomaly_detection(path, processor, model):
        container = av.open(path)
        frames = [f.to_image() for f in container.decode(video=0)][:32]
        inputs = processor(frames, return_tensors="pt")
        with torch.no_grad():
            out = model(**inputs)
        return model.config.id2label[out.logits.argmax(-1).item()]

    def generate_story(path, label, gemini_model):
        cap = cv2.VideoCapture(path)
        step = max(1, int(cap.get(7) // 3))
        frames, idx = [], 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if idx % step == 0 and len(frames) < 3:
                fname = f"frame_{idx}.jpg"
                cv2.imwrite(fname, frame)
                frames.append(fname)
            idx += 1
        cap.release()

        descs = []
        for fp in frames:
            with open(fp, "rb") as f:
                image = Image.open(io.BytesIO(f.read()))
            prompt = f"This frame is from a video classified as '{label}'. Describe the event."
            try:
                desc = gemini_model.generate_content([prompt, image])
                descs.append(desc.text)
            except Exception as e:
                descs.append("Description failed.")

        try:
            summary = gemini_model.generate_content("\n".join(descs) + "\nSummarize the story.")
            return summary.text
        except:
            return "Story generation failed."

    main()
    st.markdown('</div>', unsafe_allow_html=True)
