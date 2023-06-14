import cv2
import numpy as np

def change(image, color):
    # 색상 범위 변경 가능
    def on_trackbar(pos) :
        global threshold
        threshold = cv2.getTrackbarPos('threshold', 'Select ROI')

    def mouse_callback(event, x, y, flags, param):
        global threshold

        if event == cv2.EVENT_LBUTTONDOWN:
            mask_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2YUV)

            y_coord, u, v = map(int, mask_img[y, x])
            
            # 마스크 생성 및 추출된 색상 영역 표시
            lower = (y_coord-50, u-3, v-3)
            upper = (y_coord+50, u+3, v+3)
            # lower = (h-10, 30, 30)
            # upper = (h+10, 230, 230)
            mask = cv2.inRange(mask_img, lower, upper)

            for i in range(len(mask)) :
                for j in range(len(mask[i])) :
                    if mask[i][j] == 255 and  x - threshold <= j <= x + threshold and y - threshold <= i <= y + threshold:
                        #  원본 이미지의 명암을 반영하기 위해 원본 이미지의 값 구성 요소(V)를 HSV 형식으로 추출
                        v = cv2.cvtColor(np.uint8([[original_image[i][j]]]), cv2.COLOR_BGR2HSV)[0][0][2]

                        rgb_img = np.zeros((1, 1, 3), dtype=np.uint8)
                        rgb_img[0, 0, :] = color

                        hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)
                        hsv_value = tuple(map(int, hsv_img[0, 0, :]))

                        # 원본 이미지와 어울리는 색상 이미지의 명암 중간 값 설정
                        target_v = v + (hsv_value[2] - v) // 2
                        hsv_value = hsv_value[:2] + (target_v,)
                        hsv_img = np.zeros((1, 1, 3), dtype=np.uint8)
                        hsv_img[0, 0, :] = hsv_value

                        rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
                        rgb_value = tuple(map(int, rgb_img[0, 0, :]))
                        
                        # 범위를 어울리는 색으로 변경
                        result_image[i][j] = rgb_value

    original_image = image.copy()
    result_image = image.copy()
    # 윈도우 생성 및 마우스 이벤트 설정
    cv2.namedWindow('Select ROI')
    cv2.setMouseCallback('Select ROI', mouse_callback)
    cv2.createTrackbar('threshold', 'Select ROI', 0, 100, on_trackbar)
    cv2.setTrackbarPos('threshold', 'Select ROI', 50)

    while True:
        # BGR에서 HSV로 변환
        cv2.imshow('Select ROI', result_image)
        key = cv2.waitKey(1)

        # ESC 키를 누르면 종료
        if key == 27:
            break
        
        # Enter 키를 누르면 초기화
        if key == 13:
            result_image = original_image.copy()

    cv2.destroyAllWindows()

if __name__ == '__main__' :
    image = cv2.imread('./imgs/wuze.jpg')
    color = (255, 255, 255)

    change(image, color)