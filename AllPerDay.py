# -*- coding: UTF-8 -*-
import logging
import traceback
import tushare as ts
import pandas as pd
from datetime import datetime
import time
from sqlalchemy import create_engine
def datelist(begin,end):
    date_l=[datetime.strftime(x,'%Y-%m-%d')for x in list(pd.date_range(start=begin,end=end))]
    return date_l

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d)] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='mylog.log',filemode='w')
today=time.strftime('%Y-%m-%d',time.localtime())
daterange_l=datelist('2017-10-13','2017-10-13')
engine=create_engine('mysql://root:Lewei50_MYSQL@localhost/test?charset=utf8')

for x in daterange_l:
    try:
        print (x)
        df=ts.get_day_all(x)
        if not df is None:
          df['date']=x
          #df.to_csv('day'+x+'.csv')d
          df.to_sql('gettodayall',engine,if_exists='append',index=False)
          time.sleep(0.2)
          logging.info ('to sql succeed')
          
    except Exception as e:
        logging.info(str(e))
        continue

    
    
