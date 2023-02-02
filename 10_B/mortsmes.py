import pandas as pd
import matplotlib.pyplot as plt4

def mortsmes():
    #Intent de fer el A
    #Llegim el csv seleccionant les columnes que indica el pais, la data i morts totals
    df = pd.read_csv('df_covid19_countries.csv', usecols = ['location', 'date', "total_deaths"])
    #Passem les dates a format datetime, i transformem els valors en nomes el mes
    df['date'] = pd.to_datetime(df.date).dt.month
    #Agrupem per date i location, i fem suma dels valors de total_deaths segons aquests parametres. Unstack no se que fa, pero
    #sense unstack no funciona
    a = df.groupby(by=['date', 'location']).sum().unstack()
    #Seleccionem les primeres 20 columnes (si agafo 10 les dades no son gaire significatives al grafic)
    b = a.iloc[:, : 20]
    #Fem plot de les dades seleccionades a b
    b.plot()
    #Ensenyem el grafic
    plt4.show()
