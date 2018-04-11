#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2

'''
opencv载入图片和展示图片
https://www.kancloud.cn/aollo/aolloopencv/259610
'''

# 灰度读入 cv2.IMREAD_GRAYSCALE  彩色图像 cv2.IMREAD_COLOR
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# 写入文件
img = cv2.imread('image.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()  # wait for ESC key to exit
elif k == ord('s'):
    cv2.imwrite('image1.jpg', img)  # wait for 's' key to save and exit
    cv2.destoryAllWindows()
