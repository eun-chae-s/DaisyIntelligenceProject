#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning for tiktok.csv

# In[4]:


import pandas as pd

data = pd.read_csv('./tiktok.csv')
data


# In[5]:


data.columns


# In[6]:


#  Data wrangling for only necessary source from the original file

filtered_dataset = data[['track_name', 'artist_name', 'release_date', 'popularity', 'danceability',
       'acousticness','tempo', 'genre']]
filtered_dataset


# In[7]:


# Adding new column (popularity_rate) to indicate popularity rate corresponding to its popularity

filtered_dataset['popularity_rate'] = 'NA'
filtered_dataset


# In[8]:


# Categorizing popularity_rate

filtered_dataset.loc[filtered_dataset['popularity'] <= 33, 'popularity_rate'] = 'low'
filtered_dataset.loc[(33 < filtered_dataset['popularity']) & (filtered_dataset['popularity'] <= 66), 'popularity_rate'] = 'medium'
filtered_dataset.loc[filtered_dataset['popularity'] > 66, 'popularity_rate']  = 'high'
filtered_dataset


# In[9]:


# Sending new csv files

filtered_dataset.to_csv('./tiktok_newdataset.csv', index=False)
file = pd.read_csv('./tiktok_newdataset.csv')
file
