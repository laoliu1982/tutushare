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

today=time.strftime('%Y-%m-%d',time.localtime())
daterange_l=datelist('2017-06-11',today)
engine=create_engine('mysql://u:p@x.com/dealperday?charset=utf8')
for x in daterange_l:
    try:
        print (x)
        df=ts.get_day_all(x)
        if not df is None:
          df['date']=x
          df.to_csv('day'+x+'.csv')
          df.to_sql('dealperday',engine,if_exists='append',index=False)
          time.sleep(0.2)
          print ('to csv succeed')
          
    except Exception as e:
        print (x+'is not workday'+' error is'+str(e) )
        continue
    
    
