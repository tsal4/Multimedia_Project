# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:08:07 2025

@author: TadLocal
"""

import cv2

#set up the model
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'hed_pretrained_bsds.caffemodel')

#import image
image = cv2.imread('image2.jpg')
(H, W) = image.shape[:2]

#use the model to transform the image
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(W, H),
                             mean=(104.00698793, 116.66876762, 122.67891434),
                             swapRB=False, crop=False)

net.setInput(blob)
hed = net.forward()
hed = hed[0, 0]
hed = cv2.resize(hed, (W, H))
hed = (255 * hed).astype("uint8") #output

#apply threshold (optional)
#threshold_value = 30  #between 0-255
#_, edge_thresh = cv2.threshold(hed, threshold_value, 255, cv2.THRESH_BINARY)

#save output
cv2.imwrite("hed_model_output.jpg", hed)
