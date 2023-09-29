import os
from fer import FER
import matplotlib.pyplot as plt
import cv2

image_folder = r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images'
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    paths = os.path.join(image_folder, image_file)

    img = cv2.imread(paths)
    plt.imshow(img[:, :, :: -1])

    plt.show()
    emotion_detector = FER(mtcnn=True)

    dominant_emotion = emotion_detector.top_emotion(img)
    # dominant_emotion= emotion_detector.detect_emotions(img)
    print(dominant_emotion)
