import tushare as ts
#df = ts.get_hist_data('601318',start='2017-06-01',end='2017-07-20')
#ds = df.loc[:,['close','volume','p_change','price_change','turnover']]
ds = ts.get_sina_dd('601318',date='2017-06-28',vol=100)
print (ds)

