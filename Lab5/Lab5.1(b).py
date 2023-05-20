#b)	Добавление надписей, кадрирование, изменение размера
import cv2
img=cv2.imread('D:/Media/leaf.jpg')

def add_caption(image, caption, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    font_thickness = 2
    text_size, _ = cv2.getTextSize(caption, font, font_scale, font_thickness)
    text_position = (position[0], position[1] + text_size[1])
    cv2.putText(image, caption, text_position, font, font_scale, font_color, font_thickness)

def crop_image(image, x, y, width, height):
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

def resize_image(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image
img = 'D:\Media/leaf.jpg'
image = cv2.imread(img)
# добавление надписей
caption = "Hello, World!"
caption_position = (50, 50)
add_caption(image, caption, caption_position)
# кадрирование
x = 100
y = 100
crop_width = 300
crop_height = 200
cropped_image = crop_image(image, x, y, crop_width, crop_height)
# Изменение размера
resize_width = 600
resize_height = 400
resized_image = resize_image(image, resize_width, resize_height)
# Показ результатов
cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped_image)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
