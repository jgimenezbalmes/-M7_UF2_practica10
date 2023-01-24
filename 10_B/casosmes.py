import pandas as pd
import matplotlib.pyplot as plt4

#Intent de fer el A
#Llegim el csv seleccionant les columnes que indica el pais, la data i els cassos totals
df = pd.read_csv('df_covid19_countries.csv', usecols = ['location', 'date', "total_cases"])
#Passem les dates a format datetime, i transformem els valors en nomes el mes
df['date'] = pd.to_datetime(df.date).dt.month
#La variable a sera un dataframe, on s'agrupen els cassos totals per mes i pais
a = df.groupby(by=['date', 'location']).sum()

a.to_csv(r'C:\Users\Joan\Desktop\M7_UF2_practica10\10_B\casospermes.csv')
b = pd.read_csv(r'C:\Users\Joan\Desktop\M7_UF2_practica10\10_B\casospermes.csv')
plt4.axline(b.date, b.total_cases)
plt4.show()
