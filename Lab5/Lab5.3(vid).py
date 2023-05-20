#3. Обнаружение движущихся объектов на видео. Задачи:
#a)	Окрыть видео в opencv
#b)	Использовать алгоритм вычитания фона (fgMask = bgSubtractor.apply) и морфологические операции для удаления шума
#c)	Настроить границы (контуры) прямоугольников или иных фигур вокруг движущихся объектов
#d)	Отобразить результат.

import cv2
video_path = 'D:/Media/elvideo.mp4'
cap = cv2.VideoCapture(video_path)
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

# Вычитание фона
    fg_mask = bg_subtractor.apply(frame)
# Удаление шума
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

# Обводка движущихся объектов
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Motion Detector', frame)

    # Окончание программы по клавише q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
