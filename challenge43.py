# challenge 43

import cv2

img1 = cv2.imread('first.jpg')
img2 = cv2.imread('second.jpg')

#sum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
sum = cv2.add(img2,img1)

cv2.imshow('Sum', sum)
cv2.waitKey(0)
cv2.destroyAllWindows()
