import cv2

img = cv2.imread('img/khairul.jpg')
neg = 255 - img
cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", neg)

cv2.waitKey(0)
cv2.destroyAllWindows()