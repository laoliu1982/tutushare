import tushare as ts
df = ts.get_hist_data('601318',start='2017-07-01',end='2017-07-20')
ds = df.loc[:,['close','volume','p_change','price_change','turnover']]
print (ds)
