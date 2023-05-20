#Рисование.
# С помощью opencv python написать функции, которые по действиям мыши будут рисовать фигуры или переключаться в режим свободного рисования.
# ЛКМ - рисовать прямоугольники, ПКМ - рисовать круги в режиме свободного рисования
import cv2
import numpy as np

class Painter:
    def __init__(self):
        self.drawing_rectangle = False
        self.drawing_circle = False
        self.start_x, self.start_y = -1, -1
        self.radius = 5
        self.image = np.zeros((500, 500, 3), np.uint8)
#Функции рисования и назначение действий
    def draw_shape(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if flags == cv2.EVENT_FLAG_LBUTTON:
                self.drawing_rectangle = True
                self.start_x, self.start_y = x, y
# ЛКМ назначение действий
        elif event == cv2.EVENT_LBUTTONUP:
            if self.drawing_rectangle:
                cv2.rectangle(self.image, (self.start_x, self.start_y), (x, y), (255, 255, 255), 2)
                self.drawing_rectangle = False
# ПКМ назначение действий
        elif event == cv2.EVENT_RBUTTONDOWN:
            if flags == cv2.EVENT_FLAG_RBUTTON:
                self.drawing_circle = True

        elif event == cv2.EVENT_RBUTTONUP:
            if self.drawing_circle:
                self.drawing_circle = False

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing_circle:
                cv2.circle(self.image, (x, y), self.radius, (255, 255, 255), -1)

    def run(self):
        cv2.namedWindow("Canvas")
        cv2.setMouseCallback("Canvas", self.draw_shape)

        while True:
            cv2.imshow("Canvas", self.image)
            key = cv2.waitKey(1) & 0xFF
#При нажатии q, программа закрывается
            if key == ord("q"):
                break

        cv2.destroyAllWindows()
Painter().run()
