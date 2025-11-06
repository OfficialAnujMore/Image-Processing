import os
import cv2
import numpy as np

image_path = os.path.join('..', 'assets', 'bird.jpeg')

img  = cv2.imread(image_path)
cv2.imshow('image', img)

cv2.waitKey(20000) 
cv2.destroyAllWindows()