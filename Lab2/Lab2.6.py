#6)  Вычисление статистики для массива numpy
import numpy as np
data=np.loadtxt('D:/Media/cars.csv',delimiter=',',skiprows=1,usecols=range(2,8))
mean = np.mean(data)
std = np.std(data)
max_val = np.max(data)

print(f"Среднее значение: {mean}")
print(f"Стандартное отклонение: {std}")
print(f"Максимальное значение: {max_val}")
