import numpy as np
import cv2

img = cv2.imread('neko.jpg',0)
print(type(img))

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()