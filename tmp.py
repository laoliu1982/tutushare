# -*- coding: UTF-8 -*-
import tushare as ts
import abc
import time
def testfun(x,y,z):
    print (x,y,z)
stock = '601318'
date='2017-08-01'
#df = ts.get_hist_data(stock,start='2017-06-01',end='2017-07-25')
#ds = df.loc[:,['close','volume','p_change','price_change','turnover']]
#print (ds)
now = time.time()
now=time.localtime()
strtime=time.strftime("%Y-%m-%d",now)

print (strtime)

'''
df = ts.get_sina_dd(stock,strtime,vol=2000)

do=df.groupby("type").size()
print (do)
df.to_csv(stock+'-'+strtime+'.csv')
'''
df =ts.get_today_all()
print (df)
df.to_csv('all-'+strtime+'.csv')
df =ts.get_day_all()
print (df)
df.to_csv('all2-'+strtime+'.csv')
