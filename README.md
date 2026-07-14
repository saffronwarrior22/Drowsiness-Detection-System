# 🚗 Driver Drowsiness Detection System

An AI-powered Driver Drowsiness Detection System developed using **Python, OpenCV, MediaPipe, and Pygame**. The application monitors a driver's eyes in real time through a webcam, calculates the **Eye Aspect Ratio (EAR)** using facial landmarks, and triggers an alarm when signs of drowsiness are detected.

---

## 📌 Overview

Driver fatigue is one of the leading causes of road accidents. This project aims to improve road safety by detecting drowsiness in real time. Using a webcam, the system continuously tracks facial landmarks, measures eye openness, and alerts the driver with an audio alarm if the eyes remain closed for a predefined duration.

---

## ✨ Features

* 👁️ Real-time face and eye detection
* 🧠 Eye Aspect Ratio (EAR) based drowsiness detection
* 📷 Live webcam monitoring
* 🔊 Audio alarm for drowsiness alerts
* ⚡ Fast and lightweight implementation using MediaPipe Face Mesh
* 💻 Cross-platform Python application

---

## 🛠️ Technologies Used

* Python 3.11
* OpenCV
* MediaPipe
* NumPy
* Pygame
* Threading
* Math

---

## 📂 Project Structure

```text
Drowsiness-Detection-System/
│
├── main.py
├── alarm.mp3
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Drowsiness-Detection-System.git
cd Drowsiness-Detection-System
```

### Create a virtual environment

**macOS/Linux**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Allow camera access when prompted.

---

## 📈 Working

1. Captures live video using the webcam.
2. Detects facial landmarks using MediaPipe Face Mesh.
3. Calculates the Eye Aspect Ratio (EAR).
4. Monitors whether the driver's eyes remain closed.
5. Plays an alarm if drowsiness is detected.
6. Displays the EAR value and alert message on the screen.

---

## 📦 Dependencies

* OpenCV
* MediaPipe
* NumPy
* Pygame

Generate the latest dependencies using:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Future Enhancements

* Blink detection and blink rate analysis
* Yawn detection using mouth landmarks
* Head pose estimation
* Driver distraction detection
* Mobile application support
* Raspberry Pi deployment
* Email/SMS emergency alerts
* Driver activity logging and analytics

---

## 👨‍💻 Author

**Ramprasad Udhe**

Bachelor of Engineering (Artificial Intelligence & Data Science)

PES Modern College of Engineering, Pune

---

## 📄 License

This project is developed for educational and research purposes.

