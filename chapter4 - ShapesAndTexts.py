import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#print(img)
#img[:] = 255, 0, 0
#img[200:300, 100:300] = 255, 0, 0 #range is height then width

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) #shape[1] is width and shape[0] is height
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED) #image, starting point, ending pointm color, width/ fill
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)#image, center, radius, color, thickness
cv2.putText(img, "OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1) #image, text, starting point, font, size, color, thickness

cv2.imshow("Image", img)

cv2.waitKey(0)