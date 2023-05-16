import cv2

# 이미지 불러오기
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 가우시안 블러 적용
# 이미지에 가우시안 블러를 적용하여 잡음을 제거
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# 캐니 윤곽선 검출
# 최소 및 최대 임계값을 인자로 받으며, 이 임계값 범위 내의 경계값을 가진 픽셀을 윤곽선으로 간주
edges = cv2.Canny(blurred, 50, 150)

# 검출된 윤곽선 출력
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
