#b) Учебный файл (data.csv) + практика Dataframe.pivot. Поворот фрейма данных и суммирование повторяющихся значений.
import pandas as pd
df=pd.read_csv('D:/Media/data.csv')
pivoted=pd.pivot_table(df,index='Date',
                       columns='Product',
                       values='Sales',aggfunc='sum')
pivoted.to_csv('D:/Media/Dataframepivot.csv', index=False)
print(pivoted)
df_sum=df.groupby(["Date","Sales",'Product']).sum()
print(f'Сумма повторяющихся значений{df_sum}')
