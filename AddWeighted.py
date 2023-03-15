import cv2
import numpy as np

img1 = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE) #해당 이미지는 교수님께서 
img2 = cv2.imread('images/flowers-413.jpg', cv2.IMREAD_GRAYSCALE)#올려주신 파일에 있는 사진으로 했습니다

TEST01 = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('TEST01',TEST01)
cv2.waitKey(0)
cv2.destroyAllWindows
