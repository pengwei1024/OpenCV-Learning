#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
绘制基础图形
https://www.kancloud.cn/aollo/aolloopencv/260982

涉及的函数：cv2.line() , cv2.cicle() , cv2.rectangle() , cv2.ellipse() , cv2.putText()等
需要设置的参数：
img 你想要绘制的图形的那副图像
color 形状的颜色，以RGB为例，需要传入的元组，例（255,0,0）代表蓝色，对于灰度图只需传入灰度值
thickness 线条的粗细，如果给一个闭合图形设置为-1，那么这个图形就会被填充，默认值为1
linetype 线条的类型，8连接，抗锯齿等。默认是8连接。cv2.LINE_AA为抗锯齿
'''

import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (260, 260), (255, 0, 0), 5, cv2.LINE_AA)

# 绘制矩形
cv2.rectangle(img, (350, 0), (500, 128), (0, 255, 0), 3)

cv2.circle(img, (425, 63), 63, (0, 0, 255), -1)  # 圆，-1为向内填充

# 填充文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
k = cv2.waitKey(0)
