#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 


# In[2]:


df = pd.read_csv("C:\\Users\\hp\\Downloads\\Python_Diwali_Sales_Analysis-main\\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv",encoding='unicode_escape')
print(df)


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info


# In[6]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[7]:


df.info()


# In[8]:


pd.isnull(df)


# In[9]:


pd.isnull(df).sum()


# In[10]:


df.shape


# In[11]:


df.dropna(inplace=True)


# df.shape

# In[12]:


pd.isnull(df).sum()


# In[13]:


df['Amount'] = df['Amount'].astype('int')


# In[14]:


df.info()


# In[15]:


df['Amount'].dtypes


# In[16]:


df.columns


# In[17]:


df.describe()


# In[18]:


df[['Age','Orders','Amount']].describe()


# # Exploratory data analysis

# # Gender

# In[19]:


ax= sns.countplot(x='Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)



# In[20]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[21]:


sales_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)



# # Age

# In[22]:


ax= sns.countplot(x='Age Group',data = df,hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# total amount vs age group


# In[24]:


sales_age=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x = 'Age Group',y='Amount',data=sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# In[ ]:


# state


# total number of orders from top 10 states.

sales_states = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_states,x='State',y='Orders')


# In[26]:


# total amount /sales from top 10 states.

sales_states = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_states,x='State',y='Amount')


# In[27]:


ax= sns.countplot(x='Marital_Status',data = df)
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_states = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_states,x='Marital_Status',y='Amount',hue='Gender')


# # occupation

# In[30]:


sns.set(rc={'figure.figsize':(20,5)})
ax= sns.countplot(data = df,x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sales_states = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(,5)})
sns.barplot(data = sales_states,x='Marital_Status',y='Amount',hue='Gender')


# # product category

# # 

# In[37]:


sns.set(rc={'figure.figsize':(20,5)})
ax= sns.countplot(data = df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_states = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_states,x='Product_Category',y='Amount')


# In[41]:


sales_states = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_states,x='Product_ID',y='Orders')


# # conclusion:

# In[ ]:


Married women age group 26-35 yrs from up.maharasta and karnataka working IT,Healthcare and aviatin are more likely to buy product from food ,clothing and electronics category. 

