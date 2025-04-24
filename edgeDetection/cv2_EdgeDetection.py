# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:32:37 2025

@author: TadLocal
"""

import cv2
import numpy as np

image = cv2.imread('image2.jpg')

edges = cv2.Canny(image, 75, 155)

cv2.imwrite("cv2CannyOutput.jpg", edges)