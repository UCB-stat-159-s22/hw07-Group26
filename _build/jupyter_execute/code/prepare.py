#!/usr/bin/env python
# coding: utf-8

# # Data Preparation
# 
# In this notebook, we prepare the dataset for Exploratory Data Analysis (EDA), model consturction and selection, and model evaluation. 

# ## Import the packages

# Import all the necessary packages for the following analysis. 

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


# ## Load the data

# In[2]:


raw = pd.read_csv('../data/raw_data.csv')
raw.head()


# ## Clean the data

# Drop the empty column.

# In[3]:


# drop the last column
clean = raw.iloc[:, :-1]
clean.head()


# Check and fix the missing values

# In[4]:


# count the missing values in each column
clean.isna().sum()


# Check and drop the duplicate observations/rows

# In[5]:


# count the duplicated observations/rows
clean.duplicated().sum()


# Check and fix the data type of columns 

# In[6]:


# print out the type of each column
clean.dtypes


# Since `diagnosis` is a categorical variable, we need to one-hot encode it. 

# In[7]:


# fit a one hot encoder and use it to transform the data
encoder = OneHotEncoder(drop='first') # drop one category to avoid potential singularity
diagnosis_enc = encoder.fit_transform(clean[['diagnosis']]).toarray()
enc_clean = clean.copy()
enc_clean['diagnosis'] = diagnosis_enc
enc_clean.head()


# After the transformation, `diagnosis = 1.0` stands for `malignant` and `diagnosis = 0.0` stands for `benign`.

# ## Train-val-test Split 

# First split the dataset into training+validation and testing sets. 

# In[9]:


train_val, test = train_test_split(enc_clean, test_size=0.15, random_state=159)


# In[10]:


train, val = train_test_split(train_val, test_size=0.2, random_state=159)


# In[11]:


train.shape[0], val.shape[0], test.shape[0]


# ## Save the dataset 

# In[15]:


enc_clean.to_csv('../data/clean.csv', index=False)
train.to_csv('../data/train.csv', index=False)
val.to_csv('../data/val.csv', index=False)
test.to_csv('../data/test.csv', index=False)


# ## Combine the pipeline
# We can combine the pipeline above into helper functions.

# In[23]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def clean_data(data, enc_columns=[]):
    """
    Clean the data and one-hot encode the columns/features
    ---
    Arguments:
    data (pandas.DataFrame): the data to clean
    enc_columns (list[str]): the names of the columns to be one-hot encoded 
    
    Returns:
    clean_data (pandas.DataFrame): the cleaned data
    """
    
    # drop the last column
    clean_data = data.iloc[:, :-1]
    
    # drop the observations with missing values
    clean_data = clean_data.dropna()
    
    # drop the duplicated observations
    clean_data = clean_data.drop_duplicates()
    
    # one-hot encode the columns
    enc_clean = clean_data.copy()
    for col in enc_columns:
        encoder = OneHotEncoder(drop='first') # drop the first category to avoid singularity
        diagnosis_enc = encoder.fit_transform(clean_data[[col]]).toarray()
        enc_clean = clean_data.copy()
        enc_clean[col] = diagnosis_enc
    
    clean_data = enc_clean.reset_index().drop('index', axis=1)
    
    return clean_data

def load_data(file_path, enc_columns=[], val_size=0.2, test_size=0.15, random_state=159):
    """
    Read, clean, and split the breast cancer data. Then save the edited datasets.
    ---
    Arguments:
    file_path (str): the path to the data we want to load
    enc_columns (list[str]): the names of the columns to be one-hot encoded 
    val_size (float): the percentage of the validation set among train+val sets
    test_size (float): the percentage of the validation set among test
    
    Returns:
    (train, val, test) (tuple(pandas.DataFrame * 3)): the training, validation, and testing sets
    """
    assert (val_size <= 1) and (val_size >= 0), "Invalid validation set size" 
    assert (test_size <= 1) and (test_size >= 0), "Invalid testing set size"
    
    raw = pd.read_csv(file_path)
    clean = clean_data(raw, enc_columns)
    
    # train-val-test split of the data
    train_val, test = train_test_split(clean, test_size=test_size, random_state=random_state)
    train, val = train_test_split(train_val, test_size=val_size, random_state=random_state)
    
    clean.to_csv('../data/clean.csv', index=False)
    train.to_csv('../data/train.csv', index=False)
    val.to_csv('../data/val.csv', index=False)
    test.to_csv('../data/test.csv', index=False)
    
    return train, val, test


# Testing functions for the helper functions above. 

# In[25]:


def test_clean():
    test_input = pd.DataFrame(data={"a":[1.0, np.nan, 3.0, 1.0],
                                    "b":[1.0, 3.0, 3.0, 1.0],
                                    "c":[2.0, 4, 1, 4]})
    test_output = pd.DataFrame(data={"a":[1.0, 3.0],
                                     "b":[1.0, 3.0]})
    out = clean_data(test_input)
    assert test_output.equals(out)
    
def test_load():
    return

test_clean()


# In[ ]:




