#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import talib as ta
from pandas_datareader import data
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.simplefilter('ignore')


# In[3]:


start = '2020-05-23'
end = '2021-05-22'

df = data.DataReader('^N225', 'yahoo', start, end)


# In[4]:


df.head(10)


# In[5]:


date=df.index
close=df['Adj Close']


# In[6]:


span01=5
span02=25
span03=50

df['sma01'] = close.rolling(window=span01).mean()
df['sma02'] = close.rolling(window=span02).mean()
df['sma03'] = close.rolling(window=span03).mean()


# In[7]:


plt.figure(figsize=(30, 15))
plt.subplot(2,1,1)

plt.plot(date,close,label='Close',color='#99b898')
plt.plot(date,df['sma01'],label='sma01',color='#e84a5f')
plt.plot(date,df['sma02'],label='sma02',color='#ff847c')
plt.plot(date,df['sma03'],label='sma03',color='#feceab')
plt.legend()

plt.subplot(2,1,2)
plt.bar(date,df['Volume'],label='Volume',color='grey')
plt.legend()


# In[9]:


df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)


# In[10]:


df.tail()


# In[11]:


plt.figure(figsize=(30, 15))
plt.subplot(2,1,1)

plt.plot(date,close,label='Close',color='#99b898')
plt.plot(date,df['sma01'],label='sma01',color='#e84a5f')
plt.plot(date,df['sma02'],label='sma02',color='#ff847c')
plt.plot(date,df['sma03'],label='sma03',color='#feceab')
plt.legend()

plt.subplot(2,1,2)
plt.fill_between(date, df['macdhist'], color= 'grey', alpha=0.5, label='MACD_hist')
plt.hlines(0,start,end,"gray",linestyles='dashed')
plt.legend()


# In[ ]:




