#4) Создайте класс для университета с атрибутами имени, адреса и студентов.
class University:
    def __init__(self,name,adress,students):
        self.name=name
        self.adress=adress
        self.students=students

uni1=University("Moscow State University","Moscow,Leninsiye Gory,dom 1",38150)
print(uni1.name,uni1.adress,uni1.students)