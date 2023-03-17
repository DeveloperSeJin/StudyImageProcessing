# 두 영상의 합성
import cv2
import numpy as np
import matplotlib.pylab as plt

dog_cat = cv2.imread('images/dog_cat.jpg', cv2.IMREAD_COLOR) 
doc = cv2.imread('images/document.jpg', cv2.IMREAD_COLOR) 
print(dog_cat.shape)
print(doc.shape)

# 영상을 합성하기 전 두 영상의 크기가 동일해야 함
dog_catsize = dog_cat.shape
docsize=doc.shape

# cv2.resize를 사용하여 이미지의 크기 조절
dc = cv2.resize(dog_cat, (350,200))
doc = cv2.resize(doc,(350,200))
print(dc.shape)
print(doc.shape)


# d = A의 가중치 * A + b의 가중치 * B
# A의 가중치 + B의 가중치 = 1
# cv2.addWeighted(dog_cat, 0.7, doc, 0.3, 0) => dog_Cat이미지에 0.7만큼의 가중치, doc 이미지에 0.3만큼의 가중치 부여
result = cv2.addWeighted(dc, 0.7, doc, 0.3, 0)
cv2.imshow(result)
