import tushare as ts
import types

df=ts.get_sina_dd('601318',date="2017-07-14",vol=3000)
print (df)
print (type(df))
