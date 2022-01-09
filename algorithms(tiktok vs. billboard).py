#!/usr/bin/env python
# coding: utf-8

# # Finding the relationship between Tiktok popularity score and Billboard rank

# ### Step 1. Filter the data of tracks that are in both Tiktok and Billboard dataset

# In[180]:


# Make a separate data array of Tiktok trending tracks and Billboard Hot 100 Tracks
import pandas as pd

tiktok = pd.read_csv('./tiktok_newdataset.csv')
billboard = pd.read_csv('./billboard.csv')


# In[181]:


tiktok


# In[182]:


billboard


# In[183]:


tiktok_pop = pd.DataFrame(columns=tiktok.columns)
billboard_pop = pd.DataFrame(columns=billboard.columns)

tiktok = tiktok.drop_duplicates()
for index, row in tiktok.iterrows():
    current_song = billboard.loc[billboard['song']==row['track_name']]
    if (not current_song.empty):
        current_song_bilboard = current_song.head(1)
        tiktok_pop = tiktok_pop.append(row, ignore_index=True)
        billboard_pop = billboard_pop.append(current_song_bilboard, ignore_index=True)


# In[184]:


tiktok_pop


# In[185]:


billboard_pop


# ### Step 2. Create machine learning algorithms for the models
# 
# #### Linear Models
# ##### Insight 1. Tiktok popularity score vs. Peak-rank at Billboard Hot 100

# In[186]:


from sklearn.model_selection import train_test_split

# Combine the billboard data and tiktok data
song_data = pd.DataFrame(columns=['tiktok_pop', 'billboard_pop'])
song_data['tiktok_pop'] = tiktok_pop['popularity']
song_data['billboard_pop'] = billboard_pop['peak-rank']

X = song_data.iloc[:, :-1].values
y = song_data.iloc[:, 1].values

# Get the training and testing dataset
tiktok_train, tiktok_test, billboard_train, billboard_test = train_test_split(X, y, test_size=0.25, random_state=0)


# In[187]:


from sklearn.linear_model import LinearRegression, Ridge, Lasso

# build Linear Regression model
linear_regression = LinearRegression().fit(tiktok_train, billboard_train)
print("lr.coef_: {}".format(linear_regression.coef_))
print("lr.intercept_: {}".format(linear_regression.intercept_))


# In[188]:


print("Training set score: {:.2f}".format(linear_regression.score(tiktok_train, billboard_train)))
print("Test set score: {:.2f}".format(linear_regression.score(tiktok_test, billboard_test)))


# In[189]:


# build Ridge model

ridge = Ridge(alpha=0.00001).fit(tiktok_train, billboard_train)
print("Training set score: {:.2f}".format(ridge.score(tiktok_train, billboard_train)))
print("Test set score: {:.2f}".format(ridge.score(tiktok_test, billboard_test)))


# In[190]:


# build Lasso model

lasso = Lasso(alpha=10).fit(tiktok_train, billboard_train)
print("Training set score: {:.2f}".format(lasso.score(tiktok_train, billboard_train)))
print("Test set score: {:.2f}".format(lasso.score(tiktok_test, billboard_test)))


# In[193]:


import matplotlib.pyplot as plt

# Visualizing the graph between billboard peak rank and tiktok population score
song_data.plot(x='billboard_pop', y='tiktok_pop', style='o')
plt.title('Relationship between Tiktok population score and Billboard peak-rank')
plt.ylabel('Tiktok population score')
plt.xlabel('Billboard peak-rank')
plt.show()


# ##### Insight 2. Tiktok Tracks Danceability vs. Billboard Hot 100 Peak-Rank

# In[194]:

# Combine the billboard data and tiktok data
song_data2 = pd.DataFrame(columns=['tiktok_pop', 'billboard_pop'])
song_data2['tiktok_pop'] = tiktok_pop['danceability']
song_data2['billboard_pop'] = billboard_pop['peak-rank']

X2 = song_data2.iloc[:, :-1].values
y2 = song_data2.iloc[:, 1].values

# Get the training and testing dataset
tiktok_train2, tiktok_test2, billboard_train2, billboard_test2 = train_test_split(X2, y2, test_size=0.25, random_state=0)


# In[195]:

# build Linear Regression model
linear_regression2 = LinearRegression().fit(tiktok_train2, billboard_train2)
print("lr.coef_: {}".format(linear_regression2.coef_))
print("lr.intercept_: {}".format(linear_regression2.intercept_))


# In[196]:

# Visualizing the graph between billboard peak rank and tiktok danceability score for the tracks
song_data2.plot(x='billboard_pop', y='tiktok_pop', style='o')
plt.title('Relationship between Tiktok danceability score and Peak-rank of the track at Billboard Hot 100')
plt.ylabel('Tiktok danceability score')
plt.xlabel('Billboard peak-rank')
plt.show()


# #### Classification - Decision Tree Model
# 
# ##### Insight 3. Make a decision tree model of the rank classifier in Billboard by the track's danceability score

# In[154]:


pip install graphviz


# In[197]:


from sklearn import tree
import graphviz

# create a separate data frame that combines danceability score and classifiers for the popularity (Based on the number of weeks)
song_data3 = pd.DataFrame(columns=['tiktok_pop', 'billboard_pop'])
song_data3['tiktok_pop'] = tiktok_pop['danceability']
song_data3['billboard_pop'] = billboard_pop['popularity-weeks']

X3 = song_data3.iloc[:, :-1].values
y3 = song_data3.iloc[:, 1].values

# build the decision tree model
tree_classifier = tree.DecisionTreeClassifier(max_depth=10, random_state=0)
tree_classifier = tree_classifier.fit(X3, y3)


plt.figure(figsize=(30, 30))
tree.plot_tree(tree_classifier, feature_names=['dance'], class_names=billboard_pop['popularity-weeks'].unique(), rounded=True, fontsize=8)
plt.show()


# In[198]:


from sklearn.tree import DecisionTreeClassifier

# build the decision tree model (separating from training set and testing set)
tiktok_train3, tiktok_test3, billboard_train3, billboard_test3 = train_test_split(X3, y3, test_size=0.25, random_state=0)

tree_classifier = tree_classifier.fit(tiktok_train3, billboard_train3)
print("Accuracy on training set: {:.3f}".format(tree_classifier.score(tiktok_train3, billboard_train3)))
print("Accuracy on test set: {:.3f}".format(tree_classifier.score(tiktok_test3, billboard_test3)))





