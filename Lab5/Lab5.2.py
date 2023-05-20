#2.Распознавание лиц на фото.
#Написать алгоритм, который будет распознавать лица на фотографии, обводить их прямоугольными рамками и выводить количество найденных лиц
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image_path = 'D:/Media/students.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Распознавание лиц
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Обводка лиц
num_faces = 0
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    num_faces += 1

# Показ результатов
cv2.putText(image, f"Total number of faces: {num_faces}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.imshow("Faces Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

