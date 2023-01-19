import pandas as pd
import matplotlib.pyplot as plt2

#LLegim el csv ciutats, fem servir les columnes City i Density KM2, i agafem 11 files (incloem la de valors buits)
df3 = pd.read_csv('ciutats.csv', usecols = ['City', 'Density KM2'], nrows=11)
#Borrem la fila de valors buits i guardem la taula resultant en una altra variable
df4 = df3.dropna()
#A la columna Density KM2, treiem les comes dels valors que tenen coma (ja que no es de decimals)
df4['Density KM2'] = df4['Density KM2'].apply(lambda x : x.replace(',',''))
#A la columna Density KM2, canviem els valors que hi hagi a integer (per si son strings)
df4['Density KM2'] = df4['Density KM2'].astype(int)
#Fem un plot de sectors, agafant els valors de Density KM2, segons les cities (que seran la llegenda)
plt2.pie(df4['Density KM2'], labels=df4['City'], autopct='%1.1f%%')
