#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv('./tiktok.csv')
data


# In[2]:


data.columns


# In[3]:


filtered_dataset = data[['track_name', 'artist_name', 'release_date', 'popularity', 'danceability',
       'acousticness','tempo', 'genre']]
filtered_dataset


# In[4]:


filtered_dataset['popularity_rate'] = 'NA'
filtered_dataset


# In[5]:


filtered_dataset.loc[filtered_dataset['popularity'] <= 33, 'popularity_rate'] = 'low'
filtered_dataset.loc[(33 < filtered_dataset['popularity']) & (filtered_dataset['popularity'] <= 66), 'popularity_rate'] = 'medium'
filtered_dataset.loc[filtered_dataset['popularity'] > 66, 'popularity_rate']  = 'high'
filtered_dataset


# In[7]:


filtered_dataset.to_csv('./tiktok_newdataset.csv', index=False)
file = pd.read_csv('./tiktok_newdataset.csv')
file


# In[ ]:




