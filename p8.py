import cv2
import numpy as np
img=cv2.imread("E:/pictures/p2.jpg")
img=cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
