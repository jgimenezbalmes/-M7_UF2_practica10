import pandas as pd
import matplotlib.pyplot as plt3

df5 = pd.read_csv('ciutats.csv', usecols = ['City', 'Density  M2'], nrows=11)

df6 = df5.dropna()
df6['Density  M2'] = df6['Density  M2'].apply(lambda x : x.replace(',',''))
df6['Density  M2'] = df6['Density  M2'].astype(int)
plt3.pie(df6['Density  M2'], labels=df6['City'], autopct='%1.1f%%')

#def graf3():
    #plt3.show()