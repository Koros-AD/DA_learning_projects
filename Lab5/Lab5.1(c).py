#c)	Поворот изображения, размытие и сглаживание.
import cv2
img = 'D:/Media/leaf.jpg'
image = cv2.imread(img)

# Поворот изображения
angle = 45
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

#Размытие
blur_radius = (7, 7)
blurred_image = cv2.blur(image, blur_radius)

# Сглаживание
scale_percent = 70
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
aliased_image = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)

# Показ результатов
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Aliased Image", aliased_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


