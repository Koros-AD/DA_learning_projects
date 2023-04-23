#3) Создайте класс для человека с атрибутами для имени, возраста и адреса.
class Human:
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress

Human1=Human("Anna",34,"Bolshoy prospekt,11")
print(Human1.name,Human1.age,Human1.adress)

