import pandas as pd
import matplotlib.pyplot as plt5

df = pd.read_csv('test.csv', usecols=['id', 'px_height'])
valors = [2, 12, 33, 55, 69, 84, 109, 119, 209, 399]
a = df.loc[valors]
plt5.bar(a.id, a.px_height, color ='maroon', width=6)
plt5.show()