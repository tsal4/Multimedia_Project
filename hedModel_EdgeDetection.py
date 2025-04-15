# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:08:07 2025

@author: TadLocal
"""

import cv2

# Load the network
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'hed_pretrained_bsds.caffemodel')

# Read the image
image = cv2.imread('image2.jpg')
(H, W) = image.shape[:2]

# Prepare the image as input to the network
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(W, H),
                             mean=(104.00698793, 116.66876762, 122.67891434),
                             swapRB=False, crop=False)

# Set the blob as input to the network and perform a forward pass
net.setInput(blob)
hed = net.forward()
hed = hed[0, 0]
hed = cv2.resize(hed, (W, H))
hed = (255 * hed).astype("uint8")

# Apply binary threshold to get cleaner, high-contrast edges
threshold_value = 30  # You can tweak this (try 30–100)
_, edge_thresh = cv2.threshold(hed, threshold_value, 255, cv2.THRESH_BINARY)

# Save or display the result
cv2.imwrite("hedModelOutput.jpg", edge_thresh)