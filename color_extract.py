import cv2
import numpy as np

def detect_color_in_roi(image_path):
    def mouse_callback(event, x, y, flags, param):
        nonlocal selected_roi, roi_corners, cnt

        if event == cv2.EVENT_LBUTTONDOWN:
            selected_roi = True
            roi_corners.append((x, y))
            cnt += 1

    # 이미지 로드
    img = cv2.imread(image_path)

    # 변수 초기화
    selected_roi = False
    roi_corners = []
    cnt = -1
    detecting_result = []

    # 윈도우 생성 및 마우스 이벤트 설정
    cv2.namedWindow('Select ROI')
    cv2.setMouseCallback('Select ROI', mouse_callback)

    while True:
        cv2.imshow('Select ROI', img)

        # ROI 선택이 완료되면 색상 검출 수행
        if selected_roi:
            # BGR에서 HSV로 변환
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # 마스크 생성 및 추출된 색상 영역 표시
            mask = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
            roi_corners = np.array([roi_corners], dtype=np.int32)
            cv2.fillPoly(mask, roi_corners, 255)
            color_extracted = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
            
            # HSV to RGB
            color_extracted = cv2.cvtColor(color_extracted, cv2.COLOR_HSV2RGB)

            # 추출된 색상 영역에서 평균 색상 계산
            average_color = cv2.mean(color_extracted, mask=mask)
            
            # 평균 색상 출력
            print(f"{cnt} Average RGB values at {list(roi_corners[0][0])}: {average_color}")
            
            detecting_result.append((cnt, list(roi_corners[0][0]), average_color))
            
            # 선택된 ROI 영역 표시
            cv2.polylines(img, roi_corners, True, (0, 255, 0), 2)

            # ROI 선택 초기화 
            selected_roi = False
            roi_corners = []

        # ESC 키를 누르면 종료
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    return detecting_result

# 함수 호출 예시
image_path = 'images/test.jpg'
result = detect_color_in_roi(image_path)
print(result)