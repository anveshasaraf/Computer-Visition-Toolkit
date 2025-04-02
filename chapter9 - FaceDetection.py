import cv2

#method by Viola & Jones
#Positive: Faces,  Negative: NonFaces
#Will use OpenCV Cascades

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml") #prexisting cascade - can create custom cascades too
img = cv2.imread('Resources/face.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)