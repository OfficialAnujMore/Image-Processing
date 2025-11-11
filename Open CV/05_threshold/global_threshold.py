"""
Threshold is a segmentation technique which will convert a grayscale image into a binary image (Black and white) based on the threshold value

"""

import os
import cv2

image_path = os.path.join("..", "assets", "bear.jpeg")

img = cv2.imread(image_path)


"""
All the pixel values that are below 80 will be taken to 0 and other will be taken to 255

Every pixel brighter than that number becomes white (255),
and every pixel darker than that number becomes black (0).
"""
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
thresh = cv2.blur(thresh, (10, 10))

ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)


cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("thresh", thresh)

cv2.waitKey(5000)
cv2.destroyAllWindows()
