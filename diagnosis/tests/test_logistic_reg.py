import numpy 
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

train_data = pd.read_csv('../data/train.csv')
val_data = pd.read_csv('../data/val.csv')

X_train = train_data.drop(['diagnosis','id'], 1)
X_val = val_data.drop(['diagnosis','id'],1)
y_train = train_data['diagnosis']
y_val = val_data['diagnosis']

model = LogisticRegression(max_iter = 5000)

def test_preprocessing():
    '''
    Asserts that the preprocessing has been done correctly
    '''
    assert X_train.shape[1] == 30

def test_logistic_regression():
    '''
    Asserts that the model has been fitted correctly
    ''' 
    assert type(model.fit(X_val,y_val)) == sklearn.linear_model._logistic.LogisticRegression

def test_logistic_regression_predict():
    '''
    Asserts that the predictions have been generated correctly
    '''
    assert type(model.predict(X_val)) == numpy.ndarray

def test_get_metrics():
    '''
    Asserts that the metrics have been generated correctly
    '''
    y_preds = model.predict(X_val)
    assert type(accuracy_score(y_preds,y_val)) == numpy.float64