#-*- coding: UTF-8 -*-
import traceback
import tushare as ts
import pandas as pd
from datetime import datetime
import time
from sqlalchemy import create_engine
import logging 

engine=create_engine('mysql://laoliu1982:Lewei50_MYSQL@lwkits.com/tusharetest?charset=utf8')
df=pd.read_csv('day2017-06-15.csv',encoding='utf8')
dx=df[['name','price']]
print (dx)

x=dx.to_sql('utf',engine,if_exists='append')
print (x)
#df.to_csv('tmp.csv',encoding='utf8')

#df.to_sql('utf',engine,if_exists='append')

    
    
