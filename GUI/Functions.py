import cv2
import numpy as np


# image 사이즈 조정
def resizeImage(pics):
    size = (400,400)
    print(pics)
    # 리사이즈 처리
    for pic in pics:
        base_pic=np.zeros((size[1],size[0],3),np.uint8)
        pic1=cv2.imread(pic,cv2.IMREAD_COLOR)
        h,w=pic1.shape[:2]
        ash=size[1]/h
        asw=size[0]/w
        if asw<ash:
            sizeas=(int(w*asw),int(h*asw))
        else:
            sizeas=(int(w*ash),int(h*ash))
        pic1 = cv2.resize(pic1,dsize=sizeas)
        base_pic[int(size[1]/2-sizeas[1]/2):int(size[1]/2+sizeas[1]/2),
        int(size[0]/2-sizeas[0]/2):int(size[0]/2+sizeas[0]/2),:]=pic1
        cv2.imshow('title', base_pic)
        

    
    
    