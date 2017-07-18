# -*- coding: UTF-8 -*-
import tushare as ts
import types
import time
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from datetime import datetime
print (time.strftime("%Y-%m-%d %H:%M:%S"))
#df=ts.get_sina_dd('601318',date="2017-07-18",vol=3000)
iovol=np.zeros((12,6))
print (iovol)

def datelist(beginDate, endDate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_l=[datetime.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

#dates = pd.date_range('20170701',periods =6)
#print(dates)
dayrange = datelist("2017-07-03", "2017-07-18")
print (dayrange)

print ("--------------------------------------------")
dayinstock=[]

row=0
for x in dayrange:
    df=ts.get_sina_dd('601318',x,vol=400)
    if not df is None:

        print (x)
        dayinstock.append(x)
        iovol[row][0]=df[df.type=='买盘']['volume'].sum()

        iovol[row][1]=df[df.type == '卖盘']['volume'].sum()
        time.sleep(0.1)
        df=ts.get_sina_dd('601318',x,vol=1000)
        iovol[row][2]=df[df.type=='买盘']['volume'].sum()
        iovol[row][3]=df[df.type == '卖盘']['volume'].sum()
        time.sleep(0.1)
        df=ts.get_sina_dd('601318',x,vol=2000)
        iovol[row][4]=df[df.type=='买盘']['volume'].sum()
        iovol[row][5]=df[df.type == '卖盘']['volume'].sum()
        row=row+1
print (iovol)

dates=pd.DataFrame(iovol,index=dayinstock,columns=['in400','out40','in1000','out1000','in2000','out2000'])
print (dates)
dates.to_csv('abc.csv')
dates=dates.cumsum()
plt.figure()
dates.plot()
plt.legend(loc= 'best')


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

