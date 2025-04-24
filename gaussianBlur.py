# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:38:50 2025

@author: TadLocal
"""

import cv2
import numpy as np

image = cv2.imread('image4.jpg')

blurred = cv2.GaussianBlur(image, (15,15), 0)

cv2.imwrite("blurred.jpg", blurred)