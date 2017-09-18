# -*- coding: UTF-8 -*-
import traceback
import tushare as ts
import pandas as pd
from datetime import datetime
import time
from sqlalchemy import create_engine
def datelist(begin,end):
    date_l=[datetime.strftime(x,'%Y-%m-%d')for x in list(pd.date_range(start=begin,end=end))]
    return date_l
stocks=['601318','000001','000333','600036','000858','600900','000651','600104','600887','002415']
today=time.strftime('%Y-%m-%d',time.localtime())
daterange_l=datelist('2017-08-14',today)
engine=create_engine('mysql://u:p@x.com/dealdetail?charset=utf8')
for x in daterange_l:
    try:
        print (x)
        for stock in stocks:
            print (stock)
            df=ts.get_sina_dd(stock,x)
            if not df is None:
              df['date']=x
              print(df)
              df.to_csv('day'+x+'-'+stock+'.csv')
              df.to_sql('sinadd'+stock,engine,if_exists='append',index=False)
              time.sleep(1)
              print ('to csv succeed')
         
    except Exception as e:
        print (x+'is not workday'+' error is'+str(e) )
        continue
    
    
