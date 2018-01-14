# -*- coding: UTF-8 -*-
import sys 
import traceback
import tushare as ts
import pandas as pd
from datetime import datetime
import time
import os
from sqlalchemy import create_engine

def datelist(begin,end):
    date_l=[datetime.strftime(x,'%Y-%m-%d')for x in list(pd.date_range(start=begin,end=end))]
    return date_l

today=time.strftime('%Y-%m-%d',time.localtime())

daterange_l=datelist('2018-01-01',today)
print (daterange_l)
amount=[]
day=[]

for x in daterange_l:
    try:
        df=ts.get_day_all(date=x)
        if not df is None:
            df['date']=x
            a=df[df.industry=='保险'].amount.sum()
            b=df[df.industry=='银行'].amount.sum()
            c=df[df.code=='000001'].amount.values[0]
            d=100*c/b
            e=df[df.code=='000001'].p_change.values[0]
            amount.append([a,b,c,d,e])
            day.append(x)
            print (x,a,b,c,d,e)
            time.sleep(0.2)
    except Exception as e:
        print(str(e))
print (amount)
print (day)
dx=pd.DataFrame(amount,index=day,columns=['bx','yh','payh','ratio','p_change'])

print (dx)

