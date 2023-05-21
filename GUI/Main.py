import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def open_image():
    # 이미지 삽입을 위해 내 파일 탐색기를 열고 파일 경로를 가져옴
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # 파일 탐색기 열기
    if file_path:
        # 설명 라벨 생성
        explain = tk.Label(window, text="궁금한 색상의 위치를 클릭하세요.")
        explain.pack(anchor="center")
        explain.config(font=("Arial", 15, "bold"), fg="blue")
        
        image = Image.open(file_path)
        image = image.resize((300, 350))  # 이미지 크기 조정
        photo = ImageTk.PhotoImage(image)
        
        # 입력한 이미지로 화면이 바뀜
        label.config(image=photo, relief=tk.SOLID, borderwidth=2, background="pink")
        label.image = photo
        
        







# 창 생성
window = tk.Tk()
window.title("의류 색상 조합 추천 프로그램") # 창 제목 지정
# 창의 크기 지정
window.geometry("500x500")
window.configure(background="white") # 창의 배경색 지정


# 라벨을 생성하여 window에 배치
label = tk.Label(window, text='의류 색상 조합 추천 프로그램' )
label.pack(anchor="center")
label.config(font=("Arial", 20, "bold"), fg="blue")

# window에 insert Image라는 텍슽가 들어간 버튼 생성 
# 클릭하면 open_image 함수 실행
button = tk.Button(window, text="Insert Image", command=open_image)


# button을 window에 배치
button.config(width=20, height=2, bg="white", fg="blue")
button.pack(anchor="center", side="bottom")

window.mainloop()
