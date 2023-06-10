import cv2
import numpy as np

def change(image, color):

    def mouse_callback(event, x, y, flags, param):
        nonlocal selected_roi, roi_corners, cnt

        if event == cv2.EVENT_LBUTTONDOWN:
            selected_roi = True
            roi_corners.append((x, y))
            cnt += 1

    # cv2.destroyAllWindows()

    cv2.namedWindow('color_change_mode')
    cv2.setMouseCallback('color_change_mode', mouse_callback)

    selected_roi = False
    roi_corners = []
    cnt = -1
    detecting_result = [] # index, (x, y), RGB 저장됨

    while True :
        cv2.imshow('color_change_mode', image)
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        if selected_roi:
            mask = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
            roi_corners = np.array([roi_corners], dtype=np.int32)
            cv2.fillPoly(mask, roi_corners, 255)
            color_extracted = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

            # HSV to RGB
            color_extracted = cv2.cvtColor(color_extracted, cv2.COLOR_HSV2RGB)
            
            cv2.imshow('asfd', color_extracted)

            # ROI 선택 초기화 
            selected_roi = False
            roi_corners = []
        # ESC 키를 누르면 종료
        if cv2.waitKey(1) == 27:
            break

if __name__ == '__main__' :
    image = cv2.imread('./imgs/wuze.jpg')
    color = (200, 0, 0)

    change(image, color)