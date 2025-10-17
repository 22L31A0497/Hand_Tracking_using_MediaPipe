"""
Live Hand Tracking - Streamlit
By: Jaganmohan Rao Kuna
"""

import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from handTrackingModule import handDetector

# Streamlit Page
st.set_page_config(page_title="Live Hand Tracking", layout="wide")
st.title("🖐 Live Hand Tracking using MediaPipe")

# Initialize Detector
detector = handDetector(maxHands=2, detectionCon=0.5, trackCon=0.5)

# Display window for frames
FRAME_WINDOW = st.image([])

# Start Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        st.warning("Cannot access webcam.")
        break

    img = cv2.flip(img, 1)  # Mirror view
    img = detector.findHands(img, draw=True)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    FRAME_WINDOW.image(img)

cap.release()
