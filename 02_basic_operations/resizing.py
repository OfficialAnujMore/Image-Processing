import os
import cv2

# Read image

image_path = os.path.join("..", "assets", "bird.jpeg")
img = cv2.imread(image_path)


resized_img  = cv2.resize(img, (155, 81))
print(img.shape)
print(resized_img.shape)


cv2.imshow("img", img)

cv2.imshow("resized_img", resized_img)
cv2.waitKey(5000)
