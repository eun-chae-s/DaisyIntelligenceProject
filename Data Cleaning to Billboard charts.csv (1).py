#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[31]:


billboard = pd.read_csv('./charts.csv')


# In[32]:


billboard_filtered = bilboard.loc[bilboard['date'] >= '1960-01-01']
billboard_filtered['popularity-weeks'] = 'NA'

billboard_filtered.loc[bilboard_filtered['weeks-on-board'] <= 30, 'popularity-weeks'] = 'low'
billboard_filtered.loc[(31 <= bilboard_filtered['weeks-on-board']) & (bilboard_filtered['weeks-on-board'] <= 60), 'popularity-weeks'] = 'medium'
billboard_filtered.loc[(61 <= bilboard_filtered['weeks-on-board']), 'popularity-weeks'] = 'high'

billboard_filtered = bilboard_filtered[['date', 'rank', 'song', 'artist', 'peak-rank', 'weeks-on-board', 'popularity-weeks']]


# In[33]:


billboard_filtered


# In[38]:


billboard_filtered.to_csv('billboard.csv', index=False)  


# In[39]:


pd.read_csv('./billboard.csv')


# In[ ]:




