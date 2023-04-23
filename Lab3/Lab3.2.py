#2) Создайте класс для автомобиля с методами запуска, остановки и подачи сигнала.
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.is_on = False

    def start(self):
        if self.is_on:
            print('The car is already started')
        else:
            self.is_on = True
            print('The car has been started')

    def stop(self):
        if not self.is_on:
            print('The car is already stopped')
        else:
            self.is_on = False
            print('The car has been stopped')

    def signal(self):
        if not self.is_on:
            print("The car is off")
        else:
            print("Honk! Honk!")



car1= Car("Kia","Rio")
car1.start()
car1.stop()
car1.signal()




