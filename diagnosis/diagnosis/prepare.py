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
    Read, clean, and split the breast cancer data.
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
    
    return train, val, test