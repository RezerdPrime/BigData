import numpy as np
import cv2 as cv

img = cv.imread("a60.png") #, cv.IMREAD_GRAYSCALE
#img = cv.resize(img, (600, 600))

cv.imshow("1", cv.GaussianBlur(img, (5,5), 100))

cv.imshow("2", cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT))

cv.imshow("3", cv.rotate(img, cv.ROTATE_90_CLOCKWISE))

cv.imshow("4", cv.bilateralFilter(img, 10, 50, 50))

img2 = cv.imread("a59.png")
cv.imshow("5", cv.addWeighted(img, 0.5, img2, 0.5, 0))

cv.waitKey(0)

print(img.shape)