import pandas as pd
import matplotlib.pyplot as plt5

#Llegim el csv seleccionant les columnes que volem
df = pd.read_csv('test.csv', usecols=['id', 'clock_speed'])
#Indiquem els valors que volem restant 1, ja que les posicions a un array comencen pel numero 0
valors = [2, 12, 33, 55, 69, 84, 109, 119, 209, 399]
#Localitzem aquelles files en les posicions indicades
a = df.loc[valors]
#Fem un grafic de barres seleccionant el id per a l'eix x i el clock_speed per al y. De color seleccionem el marró
plt5.bar(a.id, a.clock_speed, color ='maroon', width=6)

#LA RESTA D'EXERCICIS SEGUEIXEN LES MATEIXES COMANDES