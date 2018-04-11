#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
使用 Matplotlib 载入图片
https://www.kancloud.cn/aollo/aolloopencv/259610
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

'''
报错：RuntimeError: Python is not installed as a framework
https://blog.csdn.net/patrick75/article/details/50885025
'''
