import cv2 as cv
import numpy as np


hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0


def mouse_callback(event, x, y, flags, param):
    global hsv, lower_blue1, upper_blue1, lower_blue2, upper_blue2, lower_blue3, upper_blue3

    # 마우스 왼쪽 버튼 누를시 위치에 있는 픽셀값을 읽어와서 HSV로 변환 (x, y 값으로 저장)
    if event == cv.EVENT_LBUTTONDOWN:
        print(img_color[y, x])
        color = img_color[y, x]

        one_pixel = np.uint8([[color]])
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)
        hsv = hsv[0][0]

        # HSV 색공간에서 마우스 클릭으로 얻은 픽셀값과 유사한 픽셀값의 범위를 정함
        if hsv[0] < 10:
            print("case1")
            lower_blue1 = np.array([hsv[0]-10+180, hsv[1] - 10, hsv[2] - 10]) # 색상만 조절
            upper_blue1 = np.array([180, hsv[1] + 10, hsv[2] + 10])
            lower_blue2 = np.array([0, hsv[1] - 10, hsv[2] - 10])
            upper_blue2 = np.array([hsv[0], hsv[1] + 10, hsv[2] + 10])
            lower_blue3 = np.array([hsv[0], hsv[1] - 10, hsv[2] - 10])
            upper_blue3 = np.array([hsv[0]+10, hsv[1] + 10, hsv[2] + 10])
            #     print(i-10+180, 180, 0, i)
            #     print(i, i+10)

        elif hsv[0] > 170:
            print("case2")
            lower_blue1 = np.array([hsv[0], hsv[1] - 10, hsv[2] - 10])
            upper_blue1 = np.array([180, hsv[1] + 10, hsv[2] + 10])
            lower_blue2 = np.array([0, hsv[1] - 10, hsv[2] - 10])
            upper_blue2 = np.array([hsv[0]+10-180, hsv[1] + 10, hsv[2] + 10])
            lower_blue3 = np.array([hsv[0]-10, hsv[1] - 10, hsv[2] - 10])
            upper_blue3 = np.array([hsv[0], hsv[1] + 10, hsv[2] + 10])
            #     print(i, 180, 0, i+10-180)
            #     print(i-10, i)
        else:
            print("case3")
            lower_blue1 = np.array([hsv[0], hsv[1] - 10, hsv[2] - 10])
            upper_blue1 = np.array([hsv[0]+10, hsv[1] + 10, hsv[2] + 10])
            lower_blue2 = np.array([hsv[0]-10, hsv[1] - 10, hsv[2] - 10])
            upper_blue2 = np.array([hsv[0], hsv[1] + 10, hsv[2] + 10])
            lower_blue3 = np.array([hsv[0]-10, hsv[1] - 10, hsv[2] - 10])
            upper_blue3 = np.array([hsv[0], hsv[1] + 10, hsv[2] + 10])
            #     print(i, i+10)
            #     print(i-10, i)

        print(hsv[0])
        print("@1", lower_blue1, "~", upper_blue1)
        print("@2", lower_blue2, "~", upper_blue2)
        print("@3", lower_blue3, "~", upper_blue3)


cv.namedWindow('img_color')
cv.setMouseCallback('img_color', mouse_callback)



while(True):
    img_color = cv.imread('./imgs/wuze.jpg')
    height, width = img_color.shape[:2]
    img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

    img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
    img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
    img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
    img_mask = img_mask1 | img_mask2 | img_mask3

    img_result = cv.bitwise_and(img_color, img_color, mask=img_mask)


    cv.imshow('img_color', img_color)
    cv.imshow('img_result', img_result)


    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()