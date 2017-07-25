# -*- coding: UTF-8 -*-
import tushare as ts
import abc
def testfun(x,y,z):
    print (x,y,z)
stock = '601318'
df = ts.get_hist_data(stock,start='2017-07-24',end='2017-07-25')
#ds = df.loc[:,['close','volume','p_change','price_change','turnover']]
#print (df)

df = ts.get_sina_dd(stock,'2017-07-24',vol=2000)
ds= df[df.type=='买盘']

do=df.groupby("type").size()
print (do)
print (type(do))
print(do.index)
print (do.values)
#print (type(do.values))
print(do.values[1])



df.to_csv('tmp6005161.csv')
