#2) Преобразование данных (pivot):
#а)создать сводную таблицу
import pandas as pd
import numpy as np

data = {'Rep': ['Craig', 'Sally', 'John', 'Sally', 'Martyn', 'John'],
        'Manager': ['Alex', 'Bert', 'Joseph', 'Steve', 'Bert', 'Alex'],
        'Product': ['Chevrolet','Pegeot','Volvo','Skoda','Renault','Opel'],
        'Price': [20, 18, 12, 10, 16, 18],
        'Quantity': [100, 150, 20, 50, 80, 120]}

df = pd.DataFrame(data)

pivot_table = pd.pivot_table(df,
                             index=['Rep', 'Manager', 'Product'],
                             values=['Price', 'Quantity'],
                             aggfunc=[np.sum], fill_value=0)

sorted_pivot_table = pivot_table.sort_index(level=['Manager', 'Rep'])

print(sorted_pivot_table)

