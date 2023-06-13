import cv2
import numpy as np

def detect_color_in_roi(image=None):
    def mouse_callback(event, x, y, flags, param):
        nonlocal selected_roi, roi_corners, cnt

        if event == cv2.EVENT_LBUTTONDOWN:
            selected_roi = True
            roi_corners.append((x, y))
            cnt += 1

    # 이미지 로드
    img = 0
    if isinstance(image, str): # 이미지 경로가 주어진 경우   
        img = cv2.imread(image)
    elif image is None: # 이미지가 없는 경우
        print('Could not open or find the image:')
        return
    else: img = image
    
    # 변수 초기화
    selected_roi = False
    roi_corners = []
    cnt = -1
    detecting_result = [] # index, (x, y), RGB 저장됨

    # 윈도우 생성 및 마우스 이벤트 설정
    cv2.namedWindow('Select ROI')
    cv2.setMouseCallback('Select ROI', mouse_callback)

    while True:
        cv2.imshow('Select ROI', img)

        # ROI 선택이 완료되면 색상 검출 수행
        if selected_roi:
            # BGR에서 HSV로 변환
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

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

def detect_color_without_mouse(x, y, image):
    
    # BGR에서 HSV로 변환
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    h, s, v = map(int, hsv_img[y, x])
    
    # 마스크 생성 및 추출된 색상 영역 표시
    lower = (h-20, s-50, v-50)
    upper = (h+20, s+50, v+50)
    # lower = (h-10, 30, 30)
    # upper = (h+10, 230, 230)
    mask = cv2.inRange(hsv_img, lower, upper)
    color_extracted = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)
    
    # HSV to RGB
    color_extracted = cv2.cvtColor(color_extracted, cv2.COLOR_HSV2RGB)

    # 추출된 색상 영역에서 평균 색상 계산
    average_color = cv2.mean(color_extracted, mask=mask)
    
    # 평균 색상 출력
    # print(f"Average RGB values at {list(x, y)}: {average_color}")
    
    return average_color

# 함수 호출 예시
if __name__ == '__main__':
    # image_path = './imgs/wuze.jpg'
    image_path = 'imgs/wuze.jpg'
    # image_path = 'images/test2.jpg'
    result = detect_color_without_mouse(480, 257, cv2.imread(image_path, 1))
    # result = detect_color_in_roi(image_path)
    print(result)