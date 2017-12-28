
# coding: utf-8

# In[1]:


import pandas as pd

locations = pd.read_csv('dsst-locations-geocoded.csv')


# In[18]:


required_columns = ['id', 'Address', 'City', 'State', 'Zip', 'link', 'name', 'Latitude', 'Longitude', 'FeatureMatchingResultType']
smaller_locations = locations[required_columns]


# In[19]:


smaller_locations.to_csv('dsst-locatons-plotly.csv')


# In[17]:


smaller_locations.FeatureMatchingResultType.describe()

