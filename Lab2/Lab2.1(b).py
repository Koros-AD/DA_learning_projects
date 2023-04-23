#b)	Обработка отсутствующих данных (заполнение отсутствующих значений определенным значением или интерполяция отсутствующих значений)
import pandas as pd
df1=pd.read_csv('D:/Media/email.csv')
df1.fillna(0)
print(df1)
df2=pd.read_csv('D:/Media/username.csv')
df2.fillna(0)
print(df2)
