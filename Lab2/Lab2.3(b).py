#b) Создание визуализации распределения набора данных.
# Создать произвольный датасет через np.random.normal или использовать датасет из csv-файлов, потом построить гистограмму.
import matplotlib.pyplot as plt
import numpy as np
df=np.random.normal(0,1,1000)
plt.hist(df,bins=30,alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Quantity')
plt.title('Histogram1')
plt.show()