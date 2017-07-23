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
stock ='601318'
#df=ts.get_sina_dd('601318',date="2017-07-18",vol=3000)
#iovol=np.arange(1500).reshape(150,10)

#print (iovol)

def datelist(beginDate, endDate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_l=[datetime.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

dayrange = datelist("2017-06-03", "2017-07-21")
print (dayrange)
print ("--------------------------------------------")
dayinstock=[]
print (ts.get_sina_dd(stock,date='2017-06-28'))

iovol=np.zeros((50,11))

def oneinmonth(days,stock):
    row=0
    inoutspan=0
    dayinstock=[]
    for x in dayrange:
        print (x)
        df=ts.get_sina_dd(stock,x,vol=400)
        if not df is None:
            dt=ts.get_hist_data(stock,start=x,end=x)
            dtt=dt.loc[x,['volume','p_change','turnover','close']]
            print (type(dtt))
            print (dtt)
            print (x)
            iovol[row][6]=dtt.iloc[0]
            iovol[row][7]=dtt.iloc[1]
            iovol[row][8]=dtt.iloc[2]
            iovol[row][9]=dtt.iloc[3]

            dayinstock.append(x)
            iovol[row][0]=df[df.type=='买盘']['volume'].sum()

            iovol[row][1]=df[df.type == '卖盘']['volume'].sum()
            iovol[row][10]=inoutspan+iovol[row][0]-iovol[row][1]
            inoutspan=iovol[row][10]

            time.sleep(0.1)
            df=ts.get_sina_dd(stock,x,vol=1000)
            iovol[row][2]=df[df.type=='买盘']['volume'].sum()
            iovol[row][3]=df[df.type == '卖盘']['volume'].sum()
            time.sleep(0.1)
            df=ts.get_sina_dd(stock,x,vol=2000)
            iovol[row][4]=df[df.type=='买盘']['volume'].sum()
            iovol[row][5]=df[df.type == '卖盘']['volume'].sum()
            row=row+1
    finalArray=iovol[0:row,:]
    print (finalArray)
    print (dayinstock)
    print (iovol)
    dates=pd.DataFrame(finalArray,index=dayinstock,columns=['in400','out40','in1000','out1000','in2000','out2000','volume','p_change','turnover','close','inoutspan'])
   # dates=pd.DataFrame(iovol,index=dayinstock,columns=['in400','out40','in1000','out1000','in2000','out2000','volume','p_change','turnover','close','inoutspan'])
    
    print ('googluck')
    print (dates)
    csvname=stock+'.csv'
    dates.to_csv(csvname)

oneinmonth(dayrange,'600036')
oneinmonth(dayrange,'601318')
