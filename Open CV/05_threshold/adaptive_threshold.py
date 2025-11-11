import os
import cv2

image_path = os.path.join("..", "assets", "handwritten.png")
# image_path = os.path.join("..", "assets", "my_notes.jpg")


img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)

thresh = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30
)

cv2.imshow("img", img)
cv2.imshow("thresh", thresh)

cv2.waitKey(20000)
cv2.destroyAllWindows()
