import pandas as pd
import matplotlib.pyplot as plt2

df3 = pd.read_csv('ciutats.csv', usecols = ['City', 'Density KM2'], nrows=11)

df4 = df3.dropna()
df4['Density KM2'] = df4['Density KM2'].apply(lambda x : x.replace(',',''))
df4['Density KM2'] = df4['Density KM2'].astype(int)
plt2.pie(df4['Density KM2'], labels=df4['City'], autopct='%1.1f%%')

#def graf2():
    #plt2.show()