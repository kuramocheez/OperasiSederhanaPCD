import cv2

img1 = cv2.imread("img/smile.png")
img2 = cv2.imread("img/smile2.png")
AND = cv2.bitwise_and(img2, img1)

cv2.imshow("AND", AND)

cv2.waitKey(0)
cv2.destroyAllWindows()