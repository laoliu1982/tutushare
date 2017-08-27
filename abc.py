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
stock ='600516'
#df=ts.get_sina_dd('601318',date="2017-07-18",vol=3000)
#iovol=np.arange(1500).reshape(150,10)

#print (iovol)

def datelist(beginDate, endDate):
    # beginDate, endDate是形如‘20160601’的字符串或datetime格式
    date_l=[datetime.strftime(x,'%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

dayrange = datelist("2017-06-03", "2017-08-20")
print (dayrange)
print ("--------------------------------------------")
dayinstock=[]
#print (ts.get_sina_dd(stock,date='2017-06-28'))


def oneinmonth(days,stock):
    now =time.localtime()
    strtime=time.strftime("%Y-%m-%d",now)
    iovol=np.zeros((50,14))
    row=0
    inoutspan=0
    dayinstock=[]
    for x in dayrange:
        print (x)
        df=ts.get_sina_dd(stock,x,vol=100)
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

            df=ts.get_sina_dd(stock,x,vol=400)
            if not df is None:
                iovol[row][0]=df[df.type=='买盘']['volume'].sum()

                iovol[row][1]=df[df.type == '卖盘']['volume'].sum()
                iovol[row][10]=inoutspan+iovol[row][0]-iovol[row][1]
                inoutspan=iovol[row][10]
                # for in out count
                do=df.groupby("type").size()
                print (do)
                buy=do.ix['买盘']
                sold=do.ix['卖盘']
                buysold= do.ix['中性盘']
                if not buy is None:
                    iovol[row][11]=buy
                if not sold is None:
                    iovol[row][12]=sold
                if not buysold is None:
                    iovol[row][13]=buysold

            time.sleep(0.1)
            df=ts.get_sina_dd(stock,x,vol=1000)
            if not df is None:
                iovol[row][2]=df[df.type=='买盘']['volume'].sum()
                iovol[row][3]=df[df.type == '卖盘']['volume'].sum()

            time.sleep(0.1)
            df=ts.get_sina_dd(stock,x,vol=2000)
            if not df is None:
                iovol[row][4]=df[df.type=='买盘']['volume'].sum()
                iovol[row][5]=df[df.type == '卖盘']['volume'].sum()
                do=df.groupby("type").size()
                print (do)

            row=row+1
    finalArray=iovol[0:row,:]
    #print (finalArray)
    #print (dayinstock)
   # print (iovol)
    dates=pd.DataFrame(finalArray,index=dayinstock,columns=['in400','out40','in1000','out1000','in2000','out2000','volume','p_change','turnover','close','inoutspan','in400count','out400count','inout400cout'])
   # dates=pd.DataFrame(iovol,index=dayinstock,columns=['in400','out40','in1000','out1000','in2000','out2000','volume','p_change','turnover','close','inoutspan'])

    print ('googluck')
    print (dates)
    csvname=stock+strtime+'.csv'
    dates.to_csv(csvname)

#oneinmonth(dayrange,'600516')
#oneinmonth(dayrange,'600036')
oneinmonth(dayrange,'601318')
#oneinmonth(dayrange,'000651')
#oneinmonth(dayrange,'002415')
#oneinmonth(dayrange,'000001')
#oneinmonth(dayrange,'000333')


#oneinmonth(dayrange,'600519')
'''
oneinmonth(dayrange,'601001')
oneinmonth(dayrange,'600862')
oneinmonth(dayrange,'600516')
oneinmonth(dayrange,'600020')
oneinmonth(dayrange,'600240')
oneinmonth(dayrange,'600458')
oneinmonth(dayrange,'600596')
oneinmonth(dayrange,'600503')
oneinmonth(dayrange,'600755')
oneinmonth(dayrange,'600269')
'''
#
