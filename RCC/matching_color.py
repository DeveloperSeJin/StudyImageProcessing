import pandas as pd
import numpy as np
import cv2

# 엑셀 파일 읽어오기
matching_color_data = pd.read_csv('./matching color.csv')
color_data = pd.read_csv('./color.csv')

# 사용자로부터 Name 입력 받기
name = input("Name을 입력하세요: ")

# 입력된 Name과 일치하는 행을 찾고 해당하는 matching color 값을 가져옴
filtered_matching_color = matching_color_data.loc[matching_color_data['Name'] == name, 'matching color']

# 만약 해당 Name이 없다면 "해당 데이터는 없습니다" 출력
if filtered_matching_color.empty:
    print("해당 데이터는 없습니다")
else:
    # matching color 값을 추출
    matching_color_values = filtered_matching_color.str.split(', ').explode().unique()
    print(matching_color_values)

    bgr_values = []
    # matching color에 해당하는 Name을 찾고 해당하는 BGR 값을 가져옴
    for matching_color_value in matching_color_values:
        filtered_color = color_data.loc[color_data['Name'] == matching_color_value, 'BGR']
        if not filtered_color.empty:
            bgr_value = filtered_color.values[0]
            bgr_values.append(bgr_value)

    if len(bgr_values) == 0:
        print("해당하는 BGR 값이 없습니다")
    else:
        print("BGR 값:")
        for bgr_value in bgr_values:
            print(bgr_value)
            # BGR 값을 기반으로 색상 추출
            bgr_list = bgr_value.split(',')
            b, g, r = int(bgr_list[0]), int(bgr_list[1]), int(bgr_list[2])
            color = [b, g, r]

            # 색상을 표현하는 사각형 이미지 생성
            color_image = np.zeros((500, 500, 3), np.uint8)
            color_image[:, :] = color

            # 색상 이미지 출력
            cv2.imshow('Color', color_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
