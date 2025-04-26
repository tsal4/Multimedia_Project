# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:32:37 2025

@author: TadLocal
"""

import cv2
import numpy as np

#import image
image = cv2.imread('image2.jpg')

#transform image
edges = cv2.Canny(image, 75, 155) #thresholds between 0-255

#save image
cv2.imwrite("cv2_output.jpg", edges)
