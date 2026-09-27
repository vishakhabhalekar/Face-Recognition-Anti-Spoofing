# Face-Recognition-Anti-Spoofing
AI-based Face Recognition and Anti-Spoofing system using Python and Computer Vision.


# 🔐 Face Recognition & Anti-Spoofing

## 📌 About the Project

This project is a **Face Recognition and Anti-Spoofing system** developed using Python and Computer Vision.

The system uses a webcam to detect faces and recognize registered users. If the face matches a registered person, their name is displayed. If the face is not registered, it is shown as **Unknown**.

The project also includes an anti-spoofing feature to check whether the detected face is from a real person or a possible fake/spoof attempt.

---

## 🎯 Project Objective

The main goal of this project is to build a simple real-time face recognition system with an additional liveness/anti-spoofing check.

The project focuses on:

* Detecting faces through a webcam
* Recognizing registered faces
* Identifying unknown faces
* Checking basic liveness using facial features
* Reducing the possibility of face spoofing

---

## 🛠️ Technologies Used

* Python
* OpenCV
* face_recognition
* dlib
* NumPy
* Tkinter / CustomTkinter

---

## ⚙️ How It Works

The system works in the following steps:

```text
Webcam
   ↓
Face Detection
   ↓
Face Recognition
   ↓
Liveness / Anti-Spoofing Check
   ↓
Result
```

### 👤 Face Recognition

First, the system captures the face through the webcam and compares it with the registered face data.

If the face matches:

**Person's Name → Displayed**

If there is no match:

**Unknown → Displayed**

### 🛡️ Anti-Spoofing

The system uses facial features and liveness-related checks to help identify whether the face is from a live person or a possible spoofing attempt.

Blink detection is used as one of the liveness checks.

---

## ✨ Main Features

### 1. Face Registration

Users can enter their name and capture face images using the webcam.

### 2. Real-Time Face Recognition

The system detects and recognizes registered users in real time.

### 3. Unknown Face Detection

If the detected face is not available in the registered dataset, the system displays **Unknown**.

### 4. Anti-Spoofing

The system performs a liveness check using facial features such as eye blinking to help detect possible spoofing attempts.

### 5. Simple GUI

A simple interface is provided for registering users and starting the face recognition system.

---

## 📂 Project Structure

```text
Face-Recognition-Anti-Spoofing/
│
├── README.md
├── main.py
├── requirements.txt
├── encodings.pkl
│
├── screenshots/
│   ├── registration.png
│   ├── face_recognition.png
│   └── anti_spoofing.png
│
└── dataset/
```

> The actual file and folder names may be different depending on the project setup.

---

## 📸 Project Screenshots

### Face Registration

<img width="800" alt="Face Registration" src="YOUR_IMAGE_LINK" />

### Face Recognition

<img width="800" alt="Face Recognition" src="YOUR_IMAGE_LINK" />

### Anti-Spoofing

<img width="800" alt="Anti-Spoofing" src="YOUR_IMAGE_LINK" />

---

## 🚀 How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the project folder

```bash
cd Face-Recognition-Anti-Spoofing
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python main.py
```

Make sure your webcam is connected and working.

---

## 📦 Requirements

The main Python libraries used in this project are:

```text
opencv-python
face-recognition
dlib
numpy
customtkinter
```

---

## 💡 What I Learned

While working on this project, I learned about:

* Computer Vision
* Face Detection
* Face Recognition
* Facial Landmarks
* Face Encodings
* Liveness Detection
* Anti-Spoofing
* OpenCV
* Python GUI development
* Working with webcam-based applications

---

## 🔮 Future Improvements

In the future, this project can be improved by:

* Using advanced deep-learning based anti-spoofing models
* Improving recognition accuracy
* Adding more types of spoofing detection
* Improving performance in different lighting conditions
* Adding secure authentication
* Deploying the application as a web or desktop application

---



## 📌 Project Type

**Computer Vision / AI-ML Project**

This project was developed as part of my learning and internship experience in **Data Science, Artificial Intelligence and Computer Vision**.
