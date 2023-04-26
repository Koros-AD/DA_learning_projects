#a)	Используя pandas, напишите сценарий, который из DataFrame файла sales.csv выбирает только те строки,
# в которых Status = presented, и сортирует их по цене от меньшего к большему.
import pandas as pd
df=pd.read_csv('D:/Media/sales.csv')
pres_df = df[df['Status'] == 'presented']
sorted_df = pres_df.sort_values('Price')
print(sorted_df)
