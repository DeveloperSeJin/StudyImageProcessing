import pandas as pd

#엑셀파일 읽어오기
matching_color_data = pd.read_csv('./matching color.csv')

# 사용자로부터 Name 입력 받기
name = input("Name을 입력하세요: ")

# 입력된 Name과 일치하는 행을 찾고 해당하는 matching color 값을 가져옴
filterd_df = matching_color_data.loc[matching_color_data['Name']== name, 'matching color']

#만약 해당 Name이 없다면 "해당 데이터는 없습니다" 출력
if filterd_df.empty:
    print("해당 데이터는 없습니다")
else: #해당 matching color 출력
    color_values = filterd_df.values
    print(color_values)