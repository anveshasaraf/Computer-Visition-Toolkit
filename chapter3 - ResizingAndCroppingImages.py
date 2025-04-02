import cv2

img = cv2.imread("Resources/LARRY’S GUIDE.png")
print(img.shape)  #2304, 1728, 3

imgResize = cv2.resize(img,(300, 200)) #can stretch or shrink
print(imgResize.shape)

imgCropped = img[0:200, 200:500] #height then width - opposite of openCV

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)