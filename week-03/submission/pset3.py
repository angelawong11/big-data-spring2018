import pandas as pd
import numpy as np

#import os
#os.chdir('week-03')

df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

df.columns
type(df.columns)
df_multipleColumns = df[['hour', 'cat', 'count']]
df.head
df['hour'] == 158
time = df[df['hour'] == 158]
time.head
time.shape

#2
for i in range(0, 168, 24):
    j = range(0,168,1)[i-5]
    if (j>i):
        df['hour'].replace(range(i,i+19,1), range(5,24,1), inplace=True)
        df['hour'].replace()
    else:
        df['hour'].replace(range(j,i+19,1), range(0,24,1), inplace=True)
