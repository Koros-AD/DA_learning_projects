#c)	Из файла cars.csv отображает названия 50 первых американских машин,
# у которых расход топлива MPG не менее 25, а частное внутреннего объема (Displacement) и количества цилиндров не более 40.
# Названия машин нужно вывести в алфавитном порядке.
import pandas as pd
df=pd.read_csv('D:/Media/cars.csv')
df_filtered = df[(df['Origin'] == 'US') & (df['MPG'] >= 25) & ((df['Displacement'] / df['Cylinders']) <= 40)]
uscars = df_filtered['Car'].sort_values().head(50)
print(uscars)