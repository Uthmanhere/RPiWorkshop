import cv2

img = cv2.imread('league.jpg')


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade_face = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

faces_rects = haar_cascade_face.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=2)
print('Faces found: ', len(faces_rects))

for (x,y,w,h) in faces_rects :
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

#cv2.imshow('face', img)
#cv2.waitKey(0)

cv2.imwrite('faceDetect.jpg', img)
