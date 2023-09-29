import os
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

image_folder = r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images'
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

emotions = ["happy", "angry", "fear", "neutral", "surprise"]
emotions_count = {emotion: 0 for emotion in emotions}

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    img = cv2.imread(image_path)
    plt.imshow(img[:, :, ::-1])
    plt.show()

    result = DeepFace.analyze(img, actions=["emotion"])
    emotion_result = result[0]['emotion']

    print(f"Analysis for {image_file}:")
    print(emotion_result)

    dominant_emotion = max(emotion_result, key=emotion_result.get)

    if dominant_emotion in emotions_count:
        emotions_count[dominant_emotion] += 1

print("Emotion counts:")
for emotion, count in emotions_count.items():
    print(f"{emotion.capitalize()} faces: {count}")

emotions = list(emotions_count.keys())
# print(emotions)
counts = list(emotions_count.values())
# print(counts)



plt.stem(emotions, counts)
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Emotion Counts in Images')
plt.show()
