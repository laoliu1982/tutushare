# -*- coding: UTF-8 -*-
import tushare as ts
import types
import time
import pandas as pd
import numpy as np
from numpy import array

from datetime import datetime
print (time.strftime("%Y-%m-%d %H:%M:%S"))
#df=ts.get_sina_dd('601318',date="2017-07-18",vol=3000)
'''
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
'''
def datelist(beginDate, endDate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_l=[datetime.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

#dates = pd.date_range('20170701',periods =6)
#print(dates)
dayrange = datelist("2017-07-03", "2017-07-5")
print (dayrange)
print (type(dayrange))
#print (list('abcd'))
df = pd.DataFrame(np.random.randn(3,2), index=dayrange, columns=['in','out'])
print (df)
print (type(np.random.randn(3,2)))
print (np.random.randn(3,2))
print ("--------------------------------------------")
dayinstock=[]
volin=[]
volout=[]

test =[[]]

for x in dayrange:

    df=ts.get_sina_dd('601318',x,vol=2000)
    if not df is None:
        print (x)
        dayinstock.append(x)
        volin.append(df[df.type=='买盘']['volume'].sum())
        volout.append(df[df.type == '卖盘']['volume'].sum())
        time.sleep(2)


print(volin)
print (test)
print(type(test))
print(np.array(volin))
test.append(volin)
test.append(volout)
print(np.array(test))


'''
        print (df.groupby('type').size())
        print (df[df.type=='买盘']['volume'].sum())
        print (df[df.type=='卖盘']['volume'].sum())
        print ("--------------------------------------------")



df=ts.get_sina_dd('601318','2017-07-18',vol=2000)
print(df.values)
'''

'''
df=ts.get_sina_dd('601318',dayrange[0],vol=2000)
#din=df[df['type'] == '买盘']
#dout = df[df['type'] == '卖盘']
do=df.loc[:,['time','price','volume','preprice','type']]
#print (do)
print ("--------------------------------------------")
print (do.groupby('type').size())
print ("--------------------------------------------")
#do=df.sort_values(by='volume')
print(do)

do=df.loc[:,['time','type','volume']]
#print (do)
#print (df['volume'])
#print (df[df.type=='买盘']['volume'])
print (df[df.type=='买盘']['volume'].sum())
print ("--------------------------------------------")
#print (df[df.type=='卖盘']['volume'])
do=df[df.type=='卖盘']['volume'].sum()
print(do)
#print (type(do))
#print (df.dtypes)

#print((ts.get_hist_data('601318',start='2017-07-01')).loc[:,['turnover','close']])
'''

