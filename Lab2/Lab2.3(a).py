#a)Необходимо создать простой линейный график из файла csv (два любых столбца, в которых есть зависимость)
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('D:\Media/climate.csv')
df.plot(x='cri_rank',y='cri_score')
plt.show()

