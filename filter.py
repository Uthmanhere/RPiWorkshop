import cv2
import numpy as np

img = cv2.imread('the_girl.jpg')

#kernel = np.ones((5,5), np.float32)/25
kernel = np.array([	[-1.0, -1.0, -1.0],
			[-1.0, 9.0, -1.0],
			[-1.0, -1.0, -1.0]	])
img_filt = cv2.filter2D(img, -1, kernel)

cv2.imwrite('im_filt.jpg', img_filt)
