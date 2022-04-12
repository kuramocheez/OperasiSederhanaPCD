import cv2

img = cv2.imread('img/khairul.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Khairul Original", img)
cv2.imshow("Gambar Khairul Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()