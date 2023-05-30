import pandas as pd

def get_color_list(color_name) :
    # 엑셀 파일 읽어오기
    matching_color_data = pd.read_csv('./matching color.csv')
    color_data = pd.read_csv('./color.csv')

    # 입력된 Name과 일치하는 행을 찾고 해당하는 matching color 값을 가져옴
    filtered_matching_color = matching_color_data.loc[matching_color_data['Name'] == color_name, 'matching color']

    # matching color 값을 추출
    matching_color_values = filtered_matching_color.str.split(', ').explode().unique()

    # bgr_values = []
    # # matching color에 해당하는 Name을 찾고 해당하는 BGR 값을 가져옴
    # for matching_color_value in matching_color_values:
    #     filtered_color = color_data.loc[color_data['Name'] == matching_color_value, 'BGR']
    #     if not filtered_color.empty:
    #         bgr_value = filtered_color.values[0]
    #         bgr_values.append(bgr_value)

    bgr_values = [color_data.loc[color_data['Name'] == matching_color_value, 'BGR'].values[0] for matching_color_value in matching_color_values if not color_data.loc[color_data['Name'] == matching_color_value, 'BGR'].empty]
    
    color_list = []
    for bgr_value in bgr_values:
        # BGR 값을 기반으로 색상 추출
        bgr_list = bgr_value.split(',')
        b, g, r = int(bgr_list[0]), int(bgr_list[1]), int(bgr_list[2])
        color_list.append((r, g, b))

    return color_list, matching_color_values