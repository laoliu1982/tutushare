import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import tushare as ts
def normalization(x):
    return(x-x.min())/(x.max()-x.min())
def xplot(code):
    df=ts.get_k_data(code,ktype='D',autype='qfq')
    df=df.tail(300)
    data=df.close.values
    data_normal=normalization(data)
    c=pd.to_datetime(df.date.values)
    plt.plot(c,data_normal)

xplot('000001')
xplot('601166')
#xplot('601998')
#xplot('601398')
xplot('600036')
plt.show()


