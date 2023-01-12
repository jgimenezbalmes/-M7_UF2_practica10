import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ciutats.csv', usecols = ['City', 'Population'], nrows=11)

df2 = df.dropna()
df2['Population'] = df2['Population'].apply(lambda x : x.replace(',',''))
df2['Population'] = df2['Population'].astype(int)
plt.pie(df2["Population"], labels=df2['City'], autopct='%1.1f%%')
def graf1():
    plt.show()

