import cv2
import numpy as np

alpha = 0.7 # 합성에 사용할 값 또는 가중치

img1 = cv2.imread('images/Lenna.png') 
img2 = cv2.imread('images/flowers-413.jpg')

addWeighted = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
#img1의 가중치 = alpha
#img2의 가중치 = (1-alpha) 

#addWeighted(A, a, B, b, C)
#A,B 그림, a,b 해당 영상 가중치 [A의 가중치 a, B의 가중치b]
#C 결과 이미지에 추가적으로 더할 값

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('cv2.addWeighted', addWeighted)
#제목:addWeighhted

cv2.waitKey(0)
cv2.destroyAllWindows
