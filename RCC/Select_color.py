import pandas as pd
import numpy as np
import cv2

def get_color() :
    color_data = pd.read_csv('./color.csv')
    color_data.dropna(inplace=True)
    color = color_data['Name'].to_numpy()
    bgr = color_data['BGR'].to_numpy()

    b = []
    g = []
    r = []

    for c in bgr :
        b.append(int(c.split(',')[0]))
        g.append(int(c.split(',')[1]))
        r.append(int(c.split(',')[2]))

    b = np.array(b)
    g = np.array(g)
    r = np.array(r)

    return color, b, g, r


def get_similar_color(rgb) :
    
    color, b, g, r = get_color()

    select_r, select_g, select_b = rgb

    index = np.argmin((b - select_b) ** 2 + (g - select_g) ** 2 + (r - select_r) ** 2)

    return (r[index], g[index], b[index]), color[index]
    # image = cv2.imread(img_path)


    # def mouse_callback(event, x, y, flags, param) :
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         image_color = image[y, x]

    #         print(color[np.argmin((b - image_color[0]) ** 2 + (g - image_color[1]) ** 2 + (r - image_color[2]) ** 2)])

    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image', mouse_callback)


    # while(True) :
    #     image = cv2.imread('./imgs/wuze.jpg')
        
    #     cv2.imshow('image', image)

    #     if cv2.waitKey(1) & 0xFF == 27:
    #         break
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    get_similar_color('./imgs/wuze.jpg')