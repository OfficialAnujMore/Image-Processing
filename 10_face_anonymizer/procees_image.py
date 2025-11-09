import os
import cv2
import mediapipe as mp


def process_image(image, face_detection):

    H, W, _ = image.shape

    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    output = face_detection.process(img_rgb)
    if output.detections is not None:
        for detection in output.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # image = cv2.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0, 3))
            #
            # image[y1:y1+h, x1:x1+w, :] =  y1 to y1+h, x1 to x1+w and all color channel
            image[y1 : y1 + h, x1 : x1 + w, :] = cv2.blur(
                image[y1 : y1 + h, x1 : x1 + w, :], (50, 50)
            )

            # # Set only the red channel in that region to max (255)
            # image[y1:y1+h, x1:x1+w, 2] = 255  # full red
            # image[y1:y1+h, x1:x1+w, 0] = 0    # remove blue
            # image[y1:y1+h, x1:x1+w, 1] = 0    # remove green

        return image
