import datetime as date
import pandas as pd
import matplotlib.pyplot as plt4

#Intent de fer el A
df = pd.read_csv('df_covid19_countries.csv', usecols = ['location', 'date'])
df['date'] = pd.to_datetime(df.date)
a = df.groupby(by=['date', 'location']).count(df.date.month)

print(a)