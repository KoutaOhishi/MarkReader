#coding: utf-8
import cv2
import numpy as np

def create_blank_sheet():
    width = 210
    height = 297

    blank_sheet = np.zeros((height, width), dtype=np.uint8)
    blank_sheet.fill(255)

    cv2.imwrite("blank.png", blank_sheet)

def main():
    create_blank_sheet()

if __name__ == "__main__":
    main()
