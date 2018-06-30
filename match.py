#coding: utf-8
import cv2
import numpy as np

def one(img, temp):
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)

    # テンプレート画像の高さ・幅
    h, w = temp.shape

    # テンプレートマッチング（OpenCVで実装）
    match = cv2.matchTemplate(gray, temp, cv2.TM_SQDIFF_NORMED)
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    pt = min_pt

    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0,0,200), 1)
    cv2.imwrite("output.png", img)

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




def mul(img, temp):
    template_width = temp.shape[0]
    template_height = temp.shape[1]


    box_pt = []

    matches = cv2.matchTemplate(img, temp, cv2.TM_CCORR_NORMED)

    threshold = 0.90

    #tempの探索
    for y in xrange(matches.shape[0]):
        for x in xrange(matches.shape[1]):
            if matches[y][x] > threshold:
                cv2.rectangle(img, (x, y),
                              (x + template_width, y + template_height),
                              (0, 0, 255), 1)
                box_pt.append((x+5,y+5))

    cv2.imwrite("out.png", img)

    #print box_pt

    #tempは４つしかない
    if len(box_pt) != 4:
        print "Can't find marker correctly"

    else:
        cv2.rectangle(img, box_pt[0], box_pt[3], (255,0,0), 1)

        trim = img[box_pt[0][1]:box_pt[3][1], box_pt[0][0]:box_pt[3][0]]

        new = cv2.cvtColor(trim, cv2.COLOR_RGB2GRAY)

        color = (0,0,0) #black

        for i in range(10):
            for k in range(5):
                cv2.rectangle(new, (200+20*k, 50+20*i), (210+20*k, 60+20*i), color, 1)

        cv2.rectangle(new, (200, 50), (210, 60), color, -1)

        print is_checked(new, 200, 50, 210, 60)
        print is_checked(new, 220, 50, 230, 60)

        #print new.shape
        cv2.imwrite("output.png", new)

def main():
    img = cv2.imread("./format.png")
    temp = cv2.imread("./tmp.png")

    #one(img, temp)
    mul(img,temp)


if __name__ == "__main__":
    main()
