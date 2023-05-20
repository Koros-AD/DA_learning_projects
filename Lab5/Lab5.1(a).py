#a)	Перевод в градации серого и в чёрно-белое изображение по порогу
import cv2
img=cv2.imread('D:\Media/leaf.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
