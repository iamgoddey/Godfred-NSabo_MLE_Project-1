#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling
import seaborn as sns


# In[85]:


# Loading the ProvincePopulation and SouthAfricaCrimeStats datasets

ProvinPop = pd.read_csv('ProvincePopulation.csv').sort_values('Province')
SA_Crime = pd.read_csv('SouthAfricaCrimeStats_v2.csv')


# In[86]:


# Printing the SA_Crime dataset
SA_Crime.head()


# In[87]:


# Printing the Popluation dataset
ProvinPop


# In[ ]:





# In[ ]:





# # Q_1a 
# * Joining Population data with crime statistics table

# In[89]:


# Combining the two datasets

#combine_datasets = pd.concat([SA_Crime, ProvinPop], sort=True)
######################################################################

combine_datasets = pd.merge(ProvinPop, SA_Crime, on = 'Province')

########################################################################
#combine_datasets = combine_datasets.set_index('Province') 

combine_datasets.head()


# In[ ]:





# # Q_1b
# * Grouping combine_datasets by: Province and sum crimes over each year

# In[113]:


# Grouping the data set and summing the crimes over each year

Group_datasets_Prov = combine_datasets.pivot_table(index='Province', aggfunc=np.sum)

Group_datasets_Prov.reset_index(inplace = True)
Group_datasets_Prov


# In[ ]:





# # Q1_c
# * What is the most dangerous province overall

# In[67]:


# Dropping some columns to make the datasets 

New_datasets_Prov = Group_datasets_Prov.drop(columns=['Population','Density', 'Area'])
#New_datasets_Prov

# Finding and Returning index of first occurrence of maximum over requested axis (Province).

New_datasets_Prov.idxmax(axis=0,skipna=True)


# In[68]:


# Returning the maximum number along the Province.

Max = np.max(New_datasets_Prov, axis=1)
Max


# In[70]:


# Returning index of first occurrence of maximum
Dangerous_Prov = Max.idxmax()

# Printing the Dangerous Province using the maximum crime occured in all Provinces.
print(Dangerous_Prov, Max.max())


# In[ ]:





# # Q1_d
# * Ranking the average crimes per year for all crime types

# In[110]:


# Dropping some columns to make the dataset compact and easy viewing

New_combine = combine_datasets.drop(columns=['Area', 'Density','Population', 'Station'])

# Re-Grouping the dataset into Categories or type of Crimes
New_combine = New_combine.pivot_table(index="Category")

# Ranking the average crimes for all crimes

New_combine = New_combine.rank(method = 'average', ascending=True)

New_combine.head()


# In[ ]:





# In[ ]:





# # Q2_a
# * Contrasting the volume vs density of crimes

# In[98]:


#combine_datasets['Province']='Eastern Cape'
#combine_datasets.head()


# In[80]:


#sns.distplot(combine_datasets['Density'], kde = True, bins = 10, hist = False)
sns.jointplot(x = '2005-2006', y = 'Density', data = Alt_Group_Prov)


# In[74]:


#with sns.axes_style("white"):
#    sns.jointplot(x= ', y='Density', kind="kde",color="b");


# In[ ]:





# # Q2_b
# * Compare population density and crime rate - do places with higher
#   population density tend to have higher crime rates (correlation)?

# In[121]:


# Iterating over the years and convert it into string

columns = [str(year)+'-'+str(year+1) for year in range(2005, 2016)]
#columns

#Grouping by Province  
Combined_data_sum = combine_datasets.groupby(['Province'],sort=False)[columns].agg('sum').reset_index()


# In[127]:


Data_Province_Allcrimes = Combined_data_sum.sum(axis=1).reset_index()
Data_Province_Allcrimes


# In[124]:


# Re_assigning of the ProvincePopulation.csv

Data_withcrimes = ProvinPop


# In[130]:


# Creating a new Column called 'Crimes'  and appending the total crime rate
Data_withcrimes['Crimes'] = [int(i) for i in Data_Province_Allcrimes[0]]
Data_withcrimes


# In[132]:


# Finding the correlation between the Population Density and crime rate

Data_withcrimes['Density'].corr(Data_withcrimes['Crimes'])

# It turns out that places with high population density have high crime rate


# In[ ]:





# # Q_3a
# * Group by Crime type

# In[138]:


Data_Crimetype = combine_datasets.groupby('Category')
Data_Crimetype.first()


# In[ ]:





# # Q_3b
# * In which provinces does drug-related crime occur more than 1000
#     times a year (on average).

# In[140]:


# Drug Related crimes in the combined datasets
Data_Drugs_Related = combine_datasets.loc[combine_datasets['Category'] == 'Drug-related crime']
Data_Drugs_Related.head()


# In[144]:


# Printing all the Drug Related Crimes 

Data_Drugs_Related_Prov =Data_Drugs_Related.loc[(combine_datasets['2005-2006']>1000) | (combine_datasets['2006-2007']>1000) |(combine_datasets['2007-2008']>1000)|(combine_datasets['2008-2009']>1000)|(combine_datasets['2009-2010']>1000)|(combine_datasets['2010-2011']>1000) |(combine_datasets['2011-2012']>1000)|(combine_datasets['2012-2013']>1000)|(combine_datasets['2013-2014']>1000)|(combine_datasets['2014-2015']>1000)|(combine_datasets['2015-2016']>1000)]
Data_Drugs_Related_Prov.head()


# In[153]:


# Summing the Data Related Drugs
Data_Prov_Drugs_Related_sum = Data_Drugs_Related_Prov.groupby(['Province'],sort=False)[columns].agg('sum')

Data_Prov_Drugs_Related_sum.head()


# In[ ]:





# # Q3_c
# * Which Province has the highest number of stations?

# In[156]:


Data_stations = combine_datasets.groupby(['Station'],sort=False)
#Data_stations.tail()


# In[157]:


for i in Data_withcrimes['Province']:
    print((i,list(combine_datasets['Province']).count(i)))


# * The Province with the highest number of stations is the Eastern Cape

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q_5. Plots/Visualizations:
# * Boxplots and edf/Kernel density estimates of
#   some crime type distributions across time.

# In[146]:


Group_Prov = combine_datasets.groupby('Category')


# In[ ]:





# In[158]:


#sns.boxplot(x = 'Drug-related crime', y = '2015-2016', data = Group_Prov)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Q_6
# * Do any other exploration or analysis with the data apart from the questions mentioned above.

# In[92]:


# Alternative

columns = [str(year)+'-'+str(year+1) for year in range(2005, 2016)]
Combined_data_sum = combine_datasets.groupby(['Province'],sort=False)[columns].agg('sum').reset_index()
Combined_data_avg = combine_datasets.groupby(['Province'],sort=False)[columns].agg('mean').reset_index()


# In[94]:


Combined_data_sum


# In[95]:


Combined_data_avg


# In[93]:


# Alternative for Grouping the data set and summing the crimes over each year

Alt_Group_Prov = combine_datasets.groupby('Province').sum(axis=None, skipna=True)
Alt_Group_Prov


# In[96]:


# Alternative of ranking average crimes
New_combine = combine_datasets.drop(columns=['Area', 'Density','Population', 'Station'])

New_combine = New_combine.pivot_table(index="Category", margins=True)

New_combine['rank_2005&06'] = New_combine['2005-2006'].rank(method = 'average',ascending=False)
New_combine['rank_2006&07'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2007&08'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2008&09'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2010&11'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2011&12'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2012&13'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2013&14'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2014&15'] = New_combine['2006-2007'].rank(method = 'average',ascending=False)
New_combine['rank_2015&16'] = New_combine['2015-2016'].rank(method = 'average',ascending=False)

New_combine.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




