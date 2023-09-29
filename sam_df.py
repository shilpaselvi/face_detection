# import os
# import cv2
# import matplotlib.pyplot as plt
# from deepface import DeepFace
#
# # path = [r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images\face6.jpg',
# #         r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images\face1.jpg',
# #         r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images\face2.jpg'
# #         ]
# image_folder = r'C:\Users\admin\PycharmProjects\pythonProject1\face_detection\images'
#
# image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
#
# happy_count = 0
# angry_count = 0
# fearful_count = 0
# neutral_count = 0
# surprise_count = 0
#
# for image_file in image_files:
#
#     paths = os.path.join(image_folder, image_file)
#
#     # read image
#     img = cv2.imread(paths)
#
#     # call imshow() using plt  object
#     plt.imshow(img[:, :, :: -1])
#
#     plt.show()
#
#     # storing the result
#     result = DeepFace.analyze(img, actions=["emotion"])
#     emotion_result = result[0]['emotion']
#
#     print(f"Analysis for {image_file}:")
#
#     print(emotion_result)
#
#     dominant_emotion = max(emotion_result, key=emotion_result.get)
#
#     if dominant_emotion == "happy":
#         happy_count += 1
#     if dominant_emotion == "angry":
#         angry_count += 1
#     if dominant_emotion == "fear":
#         fearful_count += 1
#     if dominant_emotion == "neutral":
#         neutral_count += 1
#     if dominant_emotion == "surprise":
#         surprise_count += 1
#
# print(f"Happy faces: {happy_count}")
# print(f"Angry faces: {angry_count}")
# print(f"Fearful faces: {fearful_count}")
# print(f"Neutral faces: {neutral_count}")
# print(f"Surprise faces: {surprise_count}")
#
# emotions = ['Happy', 'Angry', 'Fear', 'Neutral', 'Surprise']
# counts = [happy_count, angry_count, fearful_count, neutral_count, surprise_count]
#
# plt.stem(emotions, counts)
# plt.xlabel('Emotion')
# plt.ylabel('Count')
# plt.title('Emotion Counts in Images')
# plt.show()