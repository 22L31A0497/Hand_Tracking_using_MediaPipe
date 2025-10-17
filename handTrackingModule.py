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

# ---------------- WebRTC Processor ----------------
# Replace your old VideoProcessor class with this one
class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.detector = handDetector(maxHands=1, detectionCon=0.5, trackCon=0.5)
        self.frame_counter = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame_counter += 1

        if self.frame_counter % 2 == 0:
            img = cv2.resize(img, (640, 480))
            img = self.detector.findHands(img)

        return img

# ---------------- Streamlit WebRTC ----------------
webrtc_streamer(
    key="handtracking",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)


webrtc_streamer(
    key="handtracking",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)

