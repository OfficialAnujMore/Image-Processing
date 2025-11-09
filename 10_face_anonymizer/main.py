import os
import cv2
import mediapipe as mp
from procees_image import process_image
import argparse


# image_path = os.path.join("..", "assets", "bird.jpeg")
# image_path = os.path.join("..", "assets", "human.jpg")
# image_path = os.path.join("..", "assets", "human2.jpeg")
# image_path = os.path.join("..", "assets", "human_group.jpeg")
# image_path = os.path.join("..", "assets", "human_group1.jpeg")


args = argparse.ArgumentParser()
# args.add_argument("--mode", default="image")
# args.add_argument("--filePath", default="../assets/human_group.jpeg")

# args.add_argument("--mode", default="video")
# args.add_argument("--filePath", default="../assets/speaking_video.mp4")

args.add_argument("--mode", default="webcam")
args.add_argument("--filePath", default="None")

args = args.parse_args()

# Detect face
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=1.0
) as face_detection:

    if args.mode in ["image"]:
        image = cv2.imread(args.filePath)
        # image = cv2.imread(image_path)
        image = process_image(image=image, face_detection=face_detection)

        cv2.imshow("image", image)
        cv2.imwrite(os.path.join("..", "assets", "human_out.jpg"), image)

    elif args.mode in ["video"]:
        video = cv2.VideoCapture(args.filePath)
        ret, frame = video.read()

        output_video = cv2.VideoWriter(
            os.path.join("..", "assets", "output.mp4"),
            cv2.VideoWriter_fourcc(*"MP4V"),
            25,
            (frame.shape[1], frame.shape[0]),
        )
        while ret:
            frame = process_image(image=frame, face_detection=face_detection)
            output_video.write(frame)
            ret, frame = video.read()
        video.release()
        output_video.release()

    elif args.mode in ["webcam"]:
        webcam = cv2.VideoCapture(1)

        if not webcam.isOpened():
            print("Error: Could not open webcam.")
            exit(1)

        while True:
            ret, frame = webcam.read()
            if not ret or frame is None:
                print("Failed to grab frame")
                break

            frame = process_image(image=frame, face_detection=face_detection)

            # Critical: guard against bad returns
            if frame is None:
                print("process_image returned None — skipping frame")
                continue
            if not hasattr(frame, "shape") or frame.size == 0:
                print("process_image returned invalid frame")
                continue

            cv2.imshow("frame", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        webcam.release()


cv2.waitKey(10000)
cv2.destroyAllWindows()
