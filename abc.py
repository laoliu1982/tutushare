import tushare as ts
import types
import time
print (time.time())
#df=ts.get_sina_dd('601318',date="2017-07-14",vol=3000)
df=ts.get_hist_data('601318','2017-07-01')
#df=ts.get_sina_dd('601318','2017-07-17',vol=2000)
print (df)
print (df.dtypes)
print ('index \r\n')
print (df.index)
print ('column \r\n')
print (df.columns)
print (df.values)
print ("test select")
#do=df.iloc[:,4]
do=df.loc[:,['close','volume','price_change','p_change','turnover']]
print (do)

