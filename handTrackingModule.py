import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
from handTrackingModule import handDetector  # import your existing class

# ---------------- Streamlit Page Config ----------------
st.set_page_config(page_title="Live Hand Tracking", layout="wide")
st.title("🖐 Live Hand Tracking using MediaPipe")
st.write("Real-time hand tracking using your browser webcam!")

# ---------------- WebRTC Processor ----------------
detector = handDetector()

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = detector.findHands(img)
        return img

# ---------------- WebRTC Streamer ----------------
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

webrtc_streamer(
    key="handtracking",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)
