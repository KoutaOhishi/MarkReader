#coding: utf-8
import cv2
import numpy as np

#ボックスが塗りつぶされているかを確認する関数
def is_checked(img, left_x, left_y, right_x, right_y):
    #画素の値を調べる
    #画像サイズは10x10なので、画素は１００個ある
    thre = 60
    black = 0
    white = 0

    for _x in range(left_x, right_x):
        if black >= thre:
            return True

        elif white >= thre:
            return False

        else:
            for _y in range(left_y, right_y):
                #print img[_y][_x]
                if img[_y][_x] == 0:
                    black+=1

                elif img[_y][_x] == 255:
                    white+=1

                else:
                    pass

if __name__ == "__main__":
    
