import logging
'''
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='mylog.log',filemode='w')

logging.debug('log debug')
logging.info('this is info')
logging.warning('warging')
'''
import tushare as ts
import time
from datetime import datetime
import pandas as pd

df=ts.get_day_all('2017-09-04')
print (df)
