import os
import cv2

image_path = os.path.join('..', 'assets', 'bird.jpeg')

img = cv2.imread(image_path)


cropped_img = img[10:300, 10:300]
print(img.shape)
print(cropped_img.shape)

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()