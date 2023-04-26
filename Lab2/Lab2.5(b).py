#b)	 Из файла climate.csv отображает в виде двух столбцов названия и коды (rw_country_code) тех стран,
# у которых cri_score больше 100, а fatalities_total не более 10.
import pandas as pd
df=pd.read_csv('D:/Media/climate.csv')
mask = (df['cri_score'] > 100) & (df['fatalities_total'] <= 10)
sorted= df.loc[mask, ['country', 'rw_country_code']]

print(sorted)
