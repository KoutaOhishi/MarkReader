#coding: utf-8
import cv2
import numpy as np

def creat_boxes():
    img = cv2.imread("./blank.png")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    box_color = (0,0,0) #black

    for i in range(10):
        for k in range(5):
            cv2.rectangle(gray, (100+20*k, 50+20*i), (110+20*k, 60+20*i), box_color, 1)

    cv2.imwrite("boxes.png", gray)

def main():
    creat_boxes()

if __name__ == "__main__":
    main()
