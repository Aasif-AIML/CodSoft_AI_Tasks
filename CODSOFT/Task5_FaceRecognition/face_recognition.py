import cv2
import os
import datetime

# Path jahan save karna hai
save_path = "Task5_FaceRecognition/screenshots"

# Agar folder exist nahi karta toh bana do
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Start webcam
cap = cv2.VideoCapture(0)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

screenshot_count = 0  # unique names ke liye

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Internship Face Detection Demo", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save screenshot
    if key == ord('s'):
        screenshot_count += 1
        filename = os.path.join(save_path, f"screenshot_{screenshot_count}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)
        print(f"[INFO] Screenshot saved: {filename}")

    # Press 'q' to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
