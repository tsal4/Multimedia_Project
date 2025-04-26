# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:38:50 2025

@author: TadLocal
"""

import cv2
import numpy as np

#import image
image = cv2.imread('image4.jpg')

#transform image
blurred = cv2.GaussianBlur(image, (20,20), 0)

#save image
cv2.imwrite("blurred.jpg", blurred)
