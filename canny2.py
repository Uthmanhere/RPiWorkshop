import cv2

img = cv2.imread('the_girl.jpg')

edges = cv2.Canny(img, 70, 70)

#cv2.imshow('Edge', edges)
#cv2.waitKey(0)

cv2.imwrite('edge.jpg', edges)
