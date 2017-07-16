import tushare as ts
import types
import time
print (time.time())
#df=ts.get_sina_dd('601318',date="2017-07-14",vol=3000)
df=ts.get_hist_data('601318','2017-07-01')
print (df)
print (type(df))
