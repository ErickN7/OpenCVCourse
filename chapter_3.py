#Resizing and cropping

import cv2

img = cv2.imread("Resources/lambo.PNG")
print(img.shape)#(height, width, channels(bgr))
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Rezise", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)