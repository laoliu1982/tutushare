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
df=ts.get_stock_basics()
print(df)
print (df.dtypes)
dx=df[['name','industry']]

print (dx)
today=time.strftime('%Y-%m-%d',time.localtime())
daterange_l=datelist('2017-09-22','2017-09-22')
engine=create_engine('mysql://u:p@localhost/gettodayall?charset=utf8')
try:
    dy=ts.get_today_all()
    if not df is None:
      dy['date']='2017-09-22'
      dz=pd.merge(dy,dx,on='name')
      print (dz)
      dz.to_sql('gettodayall',engine,if_exists='append',index=False)
      time.sleep(0.2)
      print ('to csv succeed')
      
except Exception as e:
    print (str(e))

    
