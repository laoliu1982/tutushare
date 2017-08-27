import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,4,np.nan,6,8])
print (s)
print (type (s))
dates=pd.date_range('20170801',periods=10)
print (dates)
print (type(dates))
'''
df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))

print (df)
df1=df.sort_values(by='A')
print(df1)
'''
x=pd.Timestamp('20130314')
print(x)
print(type(x))
y=pd.Categorical(['aaa','bbb','ccc'])
print (y)
print (type(y))
z=np.array([3]*5)
print(z)

df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
print (df)
print (df[df.A>0])
df2=df.copy()
print (df2)
df2['e']=pd.Timestamp('20130314')
print(df2)
print (df2.describe())
print (df2.mean())
s=pd.Series(np.random.randint(0,10,size=100000))
print(s.value_counts())
df3=df2['A']
df3=df2.loc[:,['A','B']]
print (df3)
df3.plot()
plt.show()

