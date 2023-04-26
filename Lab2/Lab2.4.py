#4)  Используя pandas, напишите скрипт, который загружает CSV-файл в DataFrame и отображает первые 5 строк df.
import pandas as pd
df=pd.read_csv("D:/Media/email.csv")
print(df.head())