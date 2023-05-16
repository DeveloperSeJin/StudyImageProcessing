import cv2
import numpy as np


# 이미지 불러오기
image = cv2.imread('images/5.jpg', cv2.IMREAD_GRAYSCALE)

# 가우시안 블러 적용
# 이미지에 가우시안 블러를 적용하여 잡음을 제거
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# 캐니 윤곽선 검출
# 최소 및 최대 임계값을 인자로 받으며, 이 임계값 범위 내의 경계값을 가진 픽셀을 윤곽선으로 간주
edges = cv2.Canny(blurred, 50, 150)

# 검출된 윤곽선 출력
cv2.imshow('Edges', edges)

# 선 검출
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=10, minLineLength=10, maxLineGap=5)

# 검출된 직선 그리기
# 점찍기 
vertices = []
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        vertices.append((x1, y1)) # 점 찍기
        # vertices.append((x2, y2)) # 점 찍기
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('circle', image)


# 좌표를 시각화 하기
print(type(vertices[0])) # check

# 폰트 및 텍스트 속성 설정
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.3
color = (255, 0, 0)  # 파란색
thickness = 1

for vertex in vertices:
    position = vertex
    text = str(vertex) # 화면에 보여줄 좌표값
    cv2.putText(image, text, position, font, font_scale, color, thickness)
    cv2.circle(image, vertex, 2, (0, 255, 0), 0)
    



# 점찍기 위한 리스트 삽입
# vertices = []
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     vertices.append((x1, y1))
#     vertices.append((x2, y2))

# 해당 끝 점에 좌표 찍기
# 꼭짓점 표시
# for vertex in vertices:
#     cv2.circle(image, vertex, 5, (0, 255, 0), -1)

# 결과 이미지 출력
cv2.imshow('Final', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
