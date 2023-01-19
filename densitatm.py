import pandas as pd
import matplotlib.pyplot as plt3

#LLegim el csv ciutats, fem servir les columnes City i Density  M2, i agafem 11 files (incloem la de valors buits)
df5 = pd.read_csv('ciutats.csv', usecols = ['City', 'Density  M2'], nrows=11)
#Borrem la fila de valors buits i guardem la taula resultant en una altra variable
df6 = df5.dropna()
#A la columna Density  M2, treiem les comes dels valors que tenen coma (ja que no es de decimals)
df6['Density  M2'] = df6['Density  M2'].apply(lambda x : x.replace(',',''))
#A la columna Density  M2, canviem els valors que hi hagi a integer (per si son strings)
df6['Density  M2'] = df6['Density  M2'].astype(int)
#Fem un plot de sectors, agafant els valors de Density  M2, segons les cities (que seran la llegenda)
plt3.pie(df6['Density  M2'], labels=df6['City'], autopct='%1.1f%%')
