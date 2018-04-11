#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
图像的基本操作
https://www.kancloud.cn/aollo/aolloopencv/262768
'''

import cv2

img = cv2.imread('image.jpg')
# 获取并修改像素值
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)
img[101, 101] = [255, 255, 255]
print(img[101, 101])

# 等同于 img[10, 10, 2]
print(img.item(10, 10, 2))

# 行数，列数，通道数  (240, 320, 3)
print(img.shape)
# 像素数目 230400
print(img.size)
# 图片数据类型 uint8
print(img.dtype)
