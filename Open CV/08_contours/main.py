import os
import cv2
import numpy as np

image_path = os.path.join("..", "assets", "birds.jpg")

img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv2.contourArea(cnt))
    if cv2.contourArea(cnt) > 20:
        cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("image", img)
# cv2.imshow("img_gray", img_gray)
# cv2.imshow("thres", thres)

cv2.waitKey(20000)
cv2.destroyAllWindows()
