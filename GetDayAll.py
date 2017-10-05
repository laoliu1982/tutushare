# -*- coding: UTF-8 -*-
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
def getConfig(ConfigFile):
    CurrentDir=os.getcwd()
    ParentDir=os.path.dirname(CurrentDir)
    FilePath=os.path.join(ParentDir,ConfigFile)
    with open(FilePath,'r') as f:
        x=f.read()
    return(x)


today=time.strftime('%Y-%m-%d',time.localtime())
daterange_l=datelist('2017-09-29',today)
engine=create_engine(getConfig('config.txt'))
for x in daterange_l:
    try:
        df=ts.get_day_all(date=x)
        if not df is None:
            df['date']=x
            print(df)
            df.to_sql('test',engine,if_exists='append',index=False)
            time.sleep(0.2)
    except Exception as e:
        print(str(e))


    
