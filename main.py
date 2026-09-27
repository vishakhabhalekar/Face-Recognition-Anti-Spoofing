import cv2
import os
import face_recognition
import pickle
import numpy as np
import re

# ============================== 
# SAFE NAME INPUT
# ==============================

def clean_name(name):
    # remove invalid Windows characters
    return re.sub(r'[\\/*?:"<>|&]', "", name).strip()

person_name = input("Enter person name: ")
person_name = clean_name(person_name)

if person_name == "":
    print("Invalid name! Please restart and enter proper name.")
    exit()

# ==============================
# DATASET PATH
# ==============================

dataset_path = r"C:\vishakha\wavegrove internship 2026\face_dataset"

# Create dataset folder if not exists
os.makedirs(dataset_path, exist_ok=True)

person_folder = os.path.join(dataset_path, person_name)
os.makedirs(person_folder, exist_ok=True)

# ==============================
# STEP 1 - CAPTURE IMAGES
# ==============================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)
count = 0

print("\nPress SPACE to capture image")
print("Press Q to stop capturing\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        key = cv2.waitKey(1) & 0xFF

        if key == 32:   # SPACE
            file_name = f"{count}.jpg"
            file_path = os.path.join(person_folder, file_name)
            cv2.imwrite(file_path, face)
            print("Saved:", file_path)
            count += 1

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"\nTotal images saved for {person_name}: {count}")

# ==============================
# STEP 2 - TRAIN MODEL
# ==============================

known_encodings = []
known_names = []

print("\nTraining model...")

for person in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person)

    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person)

print("Total faces trained:", len(known_encodings))

data = {"encodings": known_encodings, "names": known_names}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Training Completed!")

# ==============================
# STEP 3 - LIVE RECOGNITION
# ==============================

print("\nStarting Recognition Camera...")

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

cap = cv2.VideoCapture(0)
printed = False   # print only once

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for (top, right, bottom, left), face_encoding in zip(faces, encodings):

        name = "Unknown"
        confidence_score = 0

        matches = face_recognition.compare_faces(
            data["encodings"],
            face_encoding,
            tolerance=0.6
        )

        face_distances = face_recognition.face_distance(
            data["encodings"],
            face_encoding
        )

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = data["names"][best_match_index]
                distance = face_distances[best_match_index]
                confidence_score = round((1 - distance) * 100, 2)

        # PRINT ONLY ONE TIME
        if not printed and name != "Unknown":
            print("\nDetected Name:", name)
            print("Accuracy:", confidence_score, "%")
            print("--------------------------")
            printed = True

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame,
                    f"{name} ({confidence_score}%)",
                    (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nProgram Finished Successfully.")