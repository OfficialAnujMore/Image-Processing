
'''
Edge detection identifies boundaries of objects in an image
where the color or intensity changes sharply.


'''
import os
import cv2
import numpy as np

image_path = os.path.join('..', 'assets', 'bird.jpeg')

img  = cv2.imread(image_path)
img_edge = cv2.Canny(img,200,200)

img_edge_d = cv2.dilate(img_edge, np.ones((3,3), dtype=np.int8))

img_edge_e = cv2.erode(img_edge_d, np.ones((3,3), dtype=np.int8))
 
cv2.imshow('image', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)


cv2.waitKey(20000) 
cv2.destroyAllWindows()