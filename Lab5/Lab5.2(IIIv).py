#Работа с видео: Вариант 3
# Уменьшить размер видео, повернуть его на 180 градусов, вывести два окна: перевёрнутое видео и его версию в размытии.
import cv2
video_path = 'D:/Media/757449034368.mp4'
cap = cv2.VideoCapture(video_path)

# Определение кодировщика видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_size = (int(cap.get(3)), int(cap.get(4)))
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, output_size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Уменьшить размера видео
    resized_frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    # Повернуть его на 180 градусов
    rotated_frame = cv2.rotate(resized_frame, cv2.ROTATE_180)
    cv2.imshow('Rotated Video', rotated_frame)
    # Создать размытое видео
    blurred_frame = cv2.GaussianBlur(rotated_frame, (15, 15), 0)
    cv2.imshow('Blurred Video', blurred_frame)

    # Запись кадра в выходное видео
    out.write(blurred_frame)
    # Завершить программу по клавише q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
