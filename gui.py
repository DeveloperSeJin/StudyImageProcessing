import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import cv2

def open_image():
    
    # 이미지 삽입을 위해 내 파일 탐색기를 열고 파일 경로를 가져옴
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    print(file_path)
    ############ 파일 탐색기 열기
    if file_path:
        # 색 조합 추천 상단에 위치
        canvas = tk.Canvas(window, width=750, height=55, background="white") # 그림을 넣을 부분 넣기
        canvas.pack(side="top", pady=20)
        # insert 버튼 삭제하기
        button.destroy()
        
        # 사각형의 길이와 높이, 패딩 정의
        rect_width = 40
        rect_height = 40
        rect_padding = 150
         
        # 텍스트의 폰트 정의
        text_color = ("Arial", 15, "bold")
        text_rgb = ("Arial", 10)
        
        # 추천하는 색상이 4개여야 하기 때문에 색상과 
        for i in range(4):
            print('for insert')
            x1 = i * (rect_width + rect_padding) + 10
            y1 = 10
            x2 = x1 + rect_width
            y2 = y1 + rect_height
            
            # 사각형 그리기
            canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
            
            # 색상 이름 텍스트의 좌표 계산 = 사각형 옆에 글자 넣기
            textName_x = x2 + 40
            textName_y = y2/2 - 5

            # 글자 삽입
            canvas.create_text(textName_x, textName_y, text=f"Rect {i+1}", font=text_color)
            
            # 색상 16진수 값 보여주기?
            textColor_x = x2 + 30
            textColor_y = y2/2 + 14
            
            # 글자 삽입
            canvas.create_text(textColor_x, textColor_y, text=f"Rect {i+1}", font=text_rgb)
        
        
        
        
        ############ 설명 라벨 생성
        explain = tk.Label(window, text="궁금한 색상의 위치를 클릭하세요.")
        explain.pack(anchor="center", side="top")
        explain.config(font=("Arial", 15, "bold"), fg="black")
        
        global image # 전역변수로 지정
        
        # 이미지에서 파일을 업로드하여 opencv로 이미지를 열기
        image = cv2.imread(file_path)  
        #cv2.imshow("Processed Image", image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # 이미지의 색상을 RGB로 변환
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 이미지를 PIL로 변환
        pil_image = Image.fromarray(image)
        # image = func.resizeImage(image) # 이미지 크기 비율 맞춰서 조정 ... 아직 미완성
        # print(image.shape)
        pil_image = pil_image.resize((300, 300))  # 이미지 크기 조정
        photo = ImageTk.PhotoImage(pil_image)
        
        
        # 이미지를 라벨에 삽입
        buttonImage = tk.Button(window, image=photo)
        buttonImage.config(image=photo, relief=tk.SOLID, borderwidth=1, background="pink")
        buttonImage.bind("<Button-1>", callback_mouse)
        buttonImage.pack()
        
        buttonImage.image = photo
        
        
        
        ########## 선택한 부분의 rgb 값 가져오기
        clickcanvas = tk.Canvas(window, width=200, height=55, background="white") # 그림을 넣을 부분 넣기
        clickcanvas.pack(side="top")
        
        x1 = 10
        y1 = 10
        x2 = x1 + rect_width
        y2 = y1 + rect_height

        # 사각형 그리기
        clickcanvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')

        # 색상 이름 텍스트의 좌표 계산 = 사각형 옆에 글자 넣기
        textName_x = x2 + 40
        textName_y = y2/2 - 5

        # 글자 삽입
        clickcanvas.create_text(textName_x, textName_y, text=f"fdfdfdf", font=text_color)

        # 색상 16진수 값 보여주기?
        textColor_x = x2 + 30
        textColor_y = y2/2 + 14

        # 글자 삽입
        clickcanvas.create_text(textColor_x, textColor_y, text=f"Rect {i+1}", font=text_rgb)



        
        ########### 버튼 다시 생성하기
        button2 = tk.Button(window, text="Insert Image", command=open_image)
        button2.config(width=20, height=2, bg="white", fg="black")
        button2.pack(anchor="center", side="top", pady=20)
        
        
        



############ 마우스 좌표 찍기 rgb 값 가져오기
def callback_mouse(event):
    print('-' * 50)
    print(event.x, event.y) # 마우스 좌표 찍기
    
    
    
    


############ 창 생성
window = tk.Tk()
window.title("의류 색상 조합 추천 프로그램") # 창 제목 지정
# 창의 크기 지정
window.geometry("800x600")
window.configure(background="white") # 창의 배경색 지정


# 라벨을 생성하여 window에 배치
title = tk.Label(window, text='의류 색상 조합 추천 프로그램' )
title.pack(anchor="center")
title.config(font=("Arial", 20, "bold"), fg="black")


# window에 insert Image라는 텍슽가 들어간 버튼 생성 
# 클릭하면 open_image 함수 실행
button = tk.Button(window, text="Insert Image", command=open_image)

# button을 window에 배치
button.config(width=20, height=2, bg="white", fg="black")
button.pack(anchor="center", side="top", pady=20)

window.mainloop()