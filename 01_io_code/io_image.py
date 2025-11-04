import os
import cv2


image_path = os.path.join('..', 'assets', 'bird.jpeg')

# Read image
img  = cv2.imread(image_path)
# Write image
cv2.imwrite(os.path.join('..', 'assets', 'bird_out.jpg'), img)

# Visualize image
cv2.imshow('image', img)
# Close image viewer after x millisecond
cv2.waitKey(5000) 