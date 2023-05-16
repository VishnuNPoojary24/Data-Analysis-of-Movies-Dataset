#!/usr/bin/env python
# coding: utf-8

# In[141]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[142]:


d=pd.read_csv("D:\\archive (2)\\IMDB-Movie-Data.csv")


# In[143]:


df=pd.DataFrame(d)


# In[144]:


df


# # 1. Display top 10 rows of the Dataset

# In[145]:


df.head(10)


# # 2. Check last 10 rows of the Dataset

# In[146]:


df.tail(10)


# # 3. Find the shape of the Dataset (Number of Rows, Number of Columns) 

# In[147]:


df.shape


# In[148]:


print("Number of Rows",df.shape[0])
print("Number of Columns",df.shape[1])


# # 4. Getting information about our Dataset like total numbers of rows, total number of columns, datatypes of each column and memory requirement

# In[149]:


df.info()


# # 5. Checking missing values

# In[150]:


print("Any missing value?",df.isnull().values.any())


# In[151]:


df.isnull().sum()


# In[152]:


sns.heatmap(df.isnull())


# In[153]:


per_missing=df.isnull().sum()*100/len(df)


# In[154]:


per_missing


# # 6. Drop all missing values

# In[155]:


df.dropna(axis=0,inplace=True)


# In[156]:


df


# # 7. Check for duplicate data

# In[157]:


dup_data=df.duplicated().values.any()


# In[158]:


print("Are there any duplicate values?",dup_data)


# In[159]:


df.drop_duplicates(inplace=True)
df


# # 8. Overall Statistics about the DataFrame

# In[160]:


df.describe()


# # 9. Display title of the movie having Runtime>=180 Minutes

# In[161]:


df.columns


# In[162]:


df[df['Runtime (Minutes)']>=180]['Title']


# # 10. In which year there was the highest average voting?

# In[163]:


df.columns


# In[164]:


df.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[165]:


sns.barplot(x='Year',y='Votes',data=df)
plt.title('Votes by Year')
plt.show()


# # 11. In which year there was the Highest Average Revenue

# In[166]:


df.columns


# In[167]:


df.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[168]:


sns.barplot(x='Year',y='Revenue (Millions)',data=df)


# # 12. Find the average rating for the each Director

# In[169]:


df.columns


# In[170]:


df.groupby('Director')['Rating'].mean().sort_values(ascending=False)


# # 13. Display Top 10 Lengthy Movies and Title

# In[171]:


df.columns


# In[172]:


top10_len=df.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']].set_index('Title')


# In[173]:


top10_len


# In[174]:


sns.barplot(x='Runtime (Minutes)',y=top10_len.index,data=top10_len)
plt.show()


# # 14. Number of movies per year

# In[177]:


df.columns


# In[178]:


df['Year'].value_counts()


# In[180]:


sns.countplot(x='Year',data=df)
plt.title("Number of Movies per Year")


# # 15. Most popular Movie Title (Highest Revenue)

# In[181]:


df.columns


# In[193]:


df[df['Revenue (Millions)'].max()==df['Revenue (Millions)']]['Title']


# In[194]:


df.columns


# # 16. Display top 10 Highest Rated Movies Titles and its Directors

# In[200]:


top10_len=df.nlargest(10,'Rating')[['Title','Rating','Director']].set_index('Title')


# In[201]:


top10_len


# In[212]:


sns.barplot(x='Rating',y=top10_len.index,data=top10_len,hue='Director',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# # 17. Display top 10 Highest Revenue Movie Titles

# In[214]:


df.columns


# In[219]:


df.nlargest(10,'Revenue (Millions)')['Title']


# In[224]:


top_10=df.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')


# In[225]:


top_10


# In[229]:


sns.barplot(x='Revenue (Millions)',y=top_10.index,data=top_10)
plt.title("Top 10 Highest Revenue Movie Titles")
plt.show()


# # 18. Find the Average Rating of Movies Year Wise

# In[230]:


df.columns


# In[232]:


df.groupby('Year')['Rating'].mean().sort_values(ascending=False)


# # 19. Does Rating affect the Revenue

# In[233]:


df.columns


# In[235]:


sns.scatterplot(x='Rating',y='Revenue (Millions)',data=df)


# # 20. Classify movies based on Ratings(Excellent, Good and Average

# In[237]:


df.columns


# In[238]:


def rating(rating):
    if rating>=7.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    else:
        return "Average"


# In[241]:


df['Rating_Category']=df['Rating'].apply(rating)


# In[242]:


df.head()


# # 21. Count number of Action Movies

# In[250]:


df.columns


# In[251]:


df['Genre'].dtype


# In[252]:


len(df[df['Genre'].str.contains('Action',case=False)])


# # 22. Find Unique values from Genre

# In[254]:


df.columns


# In[255]:


df['Genre']


# In[259]:


list1=[]
for i in df['Genre']:
    list1.append(i.split(','))


# In[261]:


list2=[]
for j in list1:
    for k in j:
        list2.append(k)   


# In[262]:


list3=[]
for l in list2:
    if l not in list3:
        list3.append(l)


# In[263]:


list3


# In[264]:


len(list3)


# In[266]:


list4=[]
for i in list1:
    for j in i:
        list4.append(j)        


# In[267]:


list4


# In[272]:


from collections import Counter


# In[273]:


Counter(list4)


# In[ ]:




