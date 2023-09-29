import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
print(xml_path)

face_cascade = cv2.CascadeClassifier(xml_path)

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    # print(faces)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y + h, x:x + w]  # face_roi is a smaller image containing just the face

        # Analyze the emotion of the detected face using DeepFace
        result = DeepFace.analyze(face_roi, actions=["emotion"], enforce_detection=False)

        # Access the emotions dictionary from the result
        emotions = result[0]['emotion']
        # Access the dominant emotion

        dominant_emotion = max(emotions, key=emotions.get)

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the emotion on the frame
        cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow('Live Emotion Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
