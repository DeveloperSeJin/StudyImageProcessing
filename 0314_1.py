
# 명암 대비 스트레칭
import cv2
import numpy as np
import matplotlib.pylab as plt


# 그레이 스케일로 원본 이미지 읽기
img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE) # grayscale로 지정

# 명암 대비할 이미지 복사
result = img.copy()

# 원본 이미지의 크기를 확인
height, width = img.shape

# 명암대비 스트레칭의 공식
# P'(x,y) = ((P(x,y) - min) / (max - min)) * 255
high = img.max() # 원본 이미지의 최댓값
low = img.min() # 최솟값

# 이중 반복을 사용하여 명암대비 스트레칭 공식 적용
for h in range(height):
    for l in range(width):
        result[h, l] = ((img[h][l] - low)  / (high - low)) * 255
        
# 명암 대비 스트레칭 공식 적용 결과 이미지
cv2.imshow('original',img)
cv2.imshow('result', result)


# matplotlib.pylab로 그래프로 확인하기
# x축이 넓은 그래프로 확인하기
plt.figure(figsize=(15, 5)) 
plt.subplot(1, 1, 1)
plt.hist(img.ravel(), 256, [0, 256])

plt.figure(figsize=(15, 5))
plt.subplot(1, 1, 1)
plt.hist(result.ravel(), 256, [0, 256])
plt.show()
