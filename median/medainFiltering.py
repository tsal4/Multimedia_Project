import cv2
import os
print("Current working directory:", os.getcwd())

image = cv2.imread('median/input.jpg')


filtered_image = cv2.medianBlur(image, 5)

cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output_median.jpg', filtered_image)
print("Filtered image saved as output_median.jpg")