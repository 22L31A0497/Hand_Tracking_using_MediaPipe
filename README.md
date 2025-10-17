## 🖐 Project 1: Hand Tracking using MediaPipe

### 🔍 Overview

The **Hand Tracking Project** detects and tracks human hands in real time using **Google’s MediaPipe** framework.
It identifies **21 key hand landmarks** (fingertips, joints, and wrist) per hand, making it suitable for applications like **gesture recognition**, **sign language detection**, and **AR control**.

---

### ⚙️ How It Works

**Stage 1 – Palm Detection:**
A deep-learning-based palm detector locates and crops the palm region from an image or video frame.

**Stage 2 – Hand Landmark Model:**
A lightweight model predicts **21 3D landmarks** (x, y, z coordinates) for each detected hand.
It’s optimized for real-time tracking with **high accuracy** and **low latency**.

---

### 🧠 Model Features

* Detects **multiple hands** in one frame
* Provides **3D coordinates** for each landmark
* Estimates **handedness** (Left / Right)
* Robust under different lighting conditions

---

### 🧪 Requirements

```bash
pip install mediapipe opencv-python
```

---

### ▶️ How to Run

1. Clone or download the repository.
2. Place your input images or open your webcam.
3. Run the script:

   ```bash
   python HandTracking.py
   ```
4. To test with an image, modify:

   ```python
   img = cv2.imread("path_to_your_image.jpg")
   ```
5. The output window displays **21 hand landmarks** and real-time tracking.

---

### 📥 Input

* Webcam feed or image file (`.jpg`, `.png`, `.jpeg`)

### 📤 Output

* Display window showing detected hands and their landmarks
* Console shows handedness (Left/Right)

---

### 📚 Libraries Used

* **MediaPipe** – Hand detection and landmark estimation
* **OpenCV** – Image capture, processing, and visualization

---

### 🚀 Example Applications

* Gesture recognition systems
* Virtual sign language translator
* AR/VR gesture control
* Human-computer interaction

---

### 📸 Demo Example

```python
img = cv2.imread("J:\\my mobile photos\\IMG20230802204829.jpg")
```

Displays the hand with 21 connected landmark points.

---

