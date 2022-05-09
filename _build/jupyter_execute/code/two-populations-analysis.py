#!/usr/bin/env python
# coding: utf-8

# ### Two Populations Comparative Statistical Analysis

# This notebook explores the differences between two populations: patients with breast cancer and those without. We have a sample of 357 patients with malignant cancer and 212 patients with benign cancer consisting of 30 key variables that may help distinguish key features between these two populations which may help to better identify cancer in patients. We will utilize hypothesis testing to see whether the two groups do indeed differ in some key features which is not due to chance. 

# In[1]:


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from diagnosis.twosample import plt_by_diagnosis, two_sample_t_test


# In[2]:


dat = pd.read_csv('../data/clean.csv')
dat_ = dat.iloc[:, 1:]
dat.head()


# Below we see all of the features that are included in the data in regards to each patient. While we may conduct a hypothesis test for each of the features, instead we will choose a few so that we do not run into the issue of multiple testing which though may be corrected by using certain techniques. I specifically want to conduct a two sample t test on the feature that differs the most in the patients that are diagnosed vs. those that are not, and the feature that differs the least. We are using the average oberved value in the two samples as the measurement of difference in the two populations. Additionally, we have also computed the standard deviation for each feature in the two populations, as the two sample t test differs for whether the two populations are assumed to have the same variance or not.

# In[3]:


dat.columns


# In[4]:


dat__diagnosis_mean = dat_.groupby("diagnosis").mean()
dat__diagnosis_mean


# In[5]:


dat__diagnosis_std = dat_.groupby("diagnosis").std()
dat__diagnosis_std


# In the below table, we see that the 'area worst' feature has the minimum difference and the 'texture_se' has the maximum difference. More so, it appears that 'area worst' has a different variance in the population while 'texture se' has thee same population variance.

# In[6]:


dat__diagnosis_mean.loc["diff"] = dat__diagnosis_mean.loc[0] - dat__diagnosis_mean.loc[1] 
dat__diagnosis_mean


# In[7]:


min_diff, max_diff = dat__diagnosis_mean.loc["diff"].min(), dat__diagnosis_mean.loc["diff"].max()


# In[8]:


dat__diagnosis_mean.columns[dat__diagnosis_mean.loc["diff"] == min_diff][0]


# In[9]:


dat__diagnosis_mean.columns[dat__diagnosis_mean.loc["diff"] == max_diff][0]


# In[10]:


dat__diagnosis_mean["area_worst"]


# In[11]:


dat__diagnosis_std["area_worst"]


# In[12]:


dat__diagnosis_mean["texture_se"]


# In[13]:


dat__diagnosis_std["texture_se"]


# The below plot depicts the count distribution of 'Worst Area' for patients with malignant cancer and for those with benign cancer. We see that the patients with malignant cancer have a distribution with a higher variance, while those with benign cancer have a lower variance. We see that patients with benign cancer have a lower mean than those with malignant cancer.

# In[14]:


plt_by_diagnosis(dat, "area_worst", "Worst Area")


# The below plot depicts the count distribution of 'Texture SE for patients with malignant cancer and for those with benign cancer. We see that the patients with malignant cancer have a very similar to those with benign cancer We see that patients with benign cancer have a slighlty longer right tail than those with malignant cancer.

# In[15]:


plt_by_diagnosis(dat, "texture_se", "Texture SE")


# We see that the two sample t test for 'area worst' is statistically highly significant at alpha = 0.05 with a p-value very close to zero. This means that we reject the null hypothesis that the two populations have a different area worst mean, which means that doctors may utilize this variable as an indicator of benign vs malignant cancer. 

# In[16]:


two_sample_t_test(dat, "diagnosis", "area_worst", False)


# We see that the two sample t test for 'texture se' is not statistically  significant at alpha = 0.05 with a p-value of approximately 0.84. This means that we fail to reject the null hypothesis that the two populations have the same area worst mean, which means that doctors may not find utilizing this variable as an indicator of benign vs malignant cancer too helpful. 

# In[17]:


two_sample_t_test(dat, "diagnosis", "texture_se", True)

