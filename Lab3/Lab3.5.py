#5) Создайте класс для прямоугольника с атрибутами длины и ширины и методами вычисления площади и периметра.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

Rec1 = Rectangle(12, 8)
print(Rec1.length,Rec1.width)
print(Rec1.area())
print(Rec1.perimeter())
