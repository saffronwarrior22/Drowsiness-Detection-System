import cv2
import mediapipe as mp
import numpy as np
import pygame 
import threading
import math

# Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1
)

# Webcam
cap = cv2.VideoCapture(0)

# Eye landmark indexes
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Alarm control
alarm_on = False

pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

# Calculate Eye Aspect Ratio
def eye_aspect_ratio(eye_points, landmarks, w, h):

    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[1]]
    p3 = landmarks[eye_points[2]]
    p4 = landmarks[eye_points[3]]
    p5 = landmarks[eye_points[4]]
    p6 = landmarks[eye_points[5]]

    def distance(a, b):
        return math.hypot(a.x - b.x, a.y - b.y)

    vertical1 = distance(p2, p5)
    vertical2 = distance(p3, p6)
    horizontal = distance(p1, p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear

# Counter
closed_frames = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    h, w, _ = frame.shape

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            landmarks = face_landmarks.landmark

            left_ear = eye_aspect_ratio(LEFT_EYE, landmarks, w, h)
            right_ear = eye_aspect_ratio(RIGHT_EYE, landmarks, w, h)

            ear = (left_ear + right_ear) / 2

            # Draw eye points
            for eye in [LEFT_EYE, RIGHT_EYE]:
                for point in eye:
                    x = int(landmarks[point].x * w)
                    y = int(landmarks[point].y * h)
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Eye closed condition
            if ear < 0.38:
                closed_frames += 1

            else:
                closed_frames = 0
                alarm_on = False

            # If eyes closed for long
            if closed_frames > 15:

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                if not alarm_on:
                    alarm_on = True
                    threading.Thread(target=play_alarm).start()

            # EAR value display
            cv2.putText(
                frame,
                f"EAR: {ear:.2f}",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

    cv2.imshow("Drowsiness Detection", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()