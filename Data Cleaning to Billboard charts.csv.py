#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[27]:


bilboard = pd.read_csv('./charts.csv')


# In[28]:


bilboard_filtered = bilboard.loc[bilboard['date'] >= '1960-01-01']
bilboard_filtered['popularity-weeks'] = 'NA'

bilboard_filtered.loc[bilboard_filtered['weeks-on-board'] <= 30, 'popularity-weeks'] = 'low'
bilboard_filtered.loc[(31 <= bilboard_filtered['weeks-on-board']) & (bilboard_filtered['weeks-on-board'] <= 60), 'popularity-weeks'] = 'medium'
bilboard_filtered.loc[(61 <= bilboard_filtered['weeks-on-board']), 'popularity-weeks'] = 'high'

bilboard_filtered = bilboard_filtered[['date', 'rank', 'song', 'artist', 'peak-rank', 'weeks-on-board', 'popularity-weeks']]


# In[29]:


bilboard_filtered

