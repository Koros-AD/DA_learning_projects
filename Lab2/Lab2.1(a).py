#1) Есть два файла с данными турагенства: email.csv и username.csv.  C ними нужно проделать все манипуляции, указанные в лекции 2, а именно:
#a)	Группировка и агрегирование ( сгруппировать набор данных по значениям в столбце, а затем вычислить среднее значение для каждой группы)
import pandas as pd
df1=pd.read_csv("D:/Media/email.csv")
grouped_data1=df1.groupby('Trip count').mean()
print(grouped_data1)
grounped_data2=df1.groupby('State ID copy').mean()
print(grounped_data2)

df2=read_csv("D:/Media/username.csv")
grounped_data3=df2.groupby('Trip count').mean()
print(grounped_data3)

