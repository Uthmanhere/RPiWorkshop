import cv2

im = cv2.imread('the_girl.jpg')

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.jpg', im_gray)
