import pandas as pd
import numpy as np

df = pd.read_csv('week-03/data/skyhook_2017-07.csv', sep=',')

import matplotlib
# This line allows the results of plots to be displayed inline with our code.
%matplotlib inline

df['date']
df.groupby(['date', 'hour'])['count'].describe()
test = df.groupby(['date', 'hour'])['count']
test.plot()
day_hours = df[df['date'] == '2017-07-02'].groupby('hour')['count'].sum()
day_hours
day_hours.plot()

df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)
df['weekday'].replace(7, 0, inplace = True)
df[df['date'] == '2017-07-10'].groupby('hour')['count'].sum()
for i in range(0, 168, 24):
  j = range(0,168,1)[i - 5]
  if (j > i):
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    ( (df['hour'] < j) & (df['hour'] > i + 18) ) |
    ( (df['hour'] > i + 18 ) & (df['hour'] < j) )
    )
    ].index, inplace = True)
  else:
    df.drop(df[
    (df['weekday'] == (i/24)) &
    (
    (df['hour'] < j) | (df['hour'] > i + 18 )
    )
    ].index, inplace = True)

for i in range(0, 168, 24):
    j = range(0,168,1)[i - 5]
    print(j)
