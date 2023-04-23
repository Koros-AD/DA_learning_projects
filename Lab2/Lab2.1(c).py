#c)	Слияние и объединение данных (соединить два DataFrames в определенном столбце)
import pandas as pd
df1=pd.read_csv('D:/Media/email.csv')
df2=pd.read_csv('D:/Media/username.csv')
merged=pd.merge(df1,df2,on='Trip count')
print((merged))