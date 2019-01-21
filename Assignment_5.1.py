#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# 1) How-to-count-distance-to-the-previous-zero
# For each value, count the difference of the distance from the previous zero (or the start
# of the Series, whichever is closer) and if there are no previous zeros,print the position

# In[34]:


df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})


# In[38]:


x = (df['X'] != 0).cumsum()
y = x != x.shift()
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()
df['Y']


# 2.Create a DatetimeIndex that contains each business day of 2015 and use it to index a
# Series of random numbers.

# In[29]:


dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dti)), index=dti)


# In[30]:


s


# 3.Find the sum of the values in s for every Wednesday.

# In[31]:


s[dti.weekday == 2].sum() 


# 4) Average For each calendar month

# In[32]:


s.resample('M', how='mean')


# 5.For each group of four consecutive calendar months in s, find the date on which the
# highest value occurred.

# In[33]:


s.groupby(pd.TimeGrouper('4M')).idxmax()


# In[ ]:





# In[ ]:





# In[ ]:




