#coding: utf-8
import cv2
import numpy as np

#ボックスが塗りつぶされているかを確認する関数
def is_checked(img, left_x, left_y, right_x, right_y):
    #画素の値を調べる
    #boxのサイズは10x10なので合計100個の画素
    threshold = 50 #黒色の画素がthresholdより多ければその時点で塗りつぶされているとする
    black_count = 0
    white_count = 0

    for _x in range(left_x, right_x):
        if black_count >= threshold:
            return True

        elif white_count >= threshold:
            return False

        else:
            for _y in range(left_y, right_y):
                #print img[_y][_x]
                if img[_y][_x] <= 200: #200以下は塗られていると仮定
                    black_count += 1

                elif img[_y][_x] >= 200:
                    white_count += 1

                else:
                    pass

def main():
    img = cv2.imread("./boxes.png")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # boxの位置はきちんと揃えて置く事
    for i in range(10):
        for k in range(5):
            print is_checked(img, 100+20*k, 50+20*i, 110+20*k, 60+20*i)

    #別パターン
    for i in range(10):
        result = []
        for k in range(5):
            if is_checked(img, 100+20*k, 50+20*i, 110+20*k, 60+20*i) == True:
                result.append(1)
            else:
                result.append(0)
        print result

if __name__ == "__main__":
    main()
