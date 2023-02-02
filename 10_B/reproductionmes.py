import pandas as pd
import matplotlib.pyplot as plt4

def repromes():
    #Intent de fer el A
    #Llegim el csv seleccionant les columnes que indica el pais, la data i els reproduction_rates
    df = pd.read_csv('df_covid19_countries.csv', usecols = ['location', 'date', "reproduction_rate"])
    #Passem les dates a format datetime, i transformem els valors en nomes el mes
    df['date'] = pd.to_datetime(df.date).dt.month
    #Agrupem per date i location, i fem suma dels valors de reproduction_rates segons aquests parametres. Unstack no se que fa, pero
    #sense unstack no funciona
    a = df.groupby(by=['date', 'location']).sum().unstack()
    #Seleccionem les primeres 20 columnes (si agafo 10 les dades no son gaire significatives al grafic)
    b = a.iloc[:, : 20]
    #Fem plot de les dades seleccionades a b
    b.plot()
    plt4.show()
