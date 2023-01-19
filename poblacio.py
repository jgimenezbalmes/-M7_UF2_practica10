import pandas as pd
import matplotlib.pyplot as plt

#LLegim el csv ciutats, fem servir les columnes City i Population, i agafem 11 files (incloem la de valors buits)
df = pd.read_csv('ciutats.csv', usecols = ['City', 'Population'], nrows=11)
#Borrem la fila de valors buits i guardem la taula resultant en una altra variable
df2 = df.dropna()
#A la columna Population, treiem les comes dels valors que tenen coma (ja que no es de decimals)
df2['Population'] = df2['Population'].apply(lambda x : x.replace(',',''))
#A la columna Population, canviem els valors que hi hagi a integer (per si son strings)
df2['Population'] = df2['Population'].astype(int)
#Fem un plot de sectors, agafant els valors de Population, segons les cities (que seran la llegenda)
plt.pie(df2["Population"], labels=df2['City'], autopct='%1.1f%%')


