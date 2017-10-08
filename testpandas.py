import pandas as pd
import tushare as ts
import os
df=pd.read_csv('industry.csv')
df=df['industry']

print (df)
for x in df:
    print(x) 
print (type(x))
print (type(df))
