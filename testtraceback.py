import traceback
import tushare as ts
import pandas as pd
from datetime import datetime
import time
def datelist(begin,end):
    date_l=[datetime.strftime(x,'%Y-%m-%d')for x in list(pd.date_range(start=begin,end=end))]
    return date_l

    
daterange_l=datelist('2017-09-01','2017-09-06')
for x in daterange_l:
    try:
        print (x)
        df=ts.get_day_all(x)
        df.to_csv('day'+x+'.csv')
        time.sleep(0.2)
    except Exception as e:
        print (e)    
        print (x+'is not workday')
        continue
    
