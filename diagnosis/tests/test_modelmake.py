from diagnosis.modelmake import decision_tree, random_forest
import numpy as np
import pandas as pd

train_data = pd.read_csv('data/train.csv')
val_data = pd.read_csv('data/val.csv')
X_train = train_data.drop(labels = ['diagnosis','id'],axis = 1) 
y_train = train_data['diagnosis']
X_val = val_data.drop(labels = ['diagnosis','id'],axis = 1) 

def test_decision_tree():
	model, y_pred_train, y_pred_val = decision_tree(X_train, y_train, X_val, seed_value = 10)
	assert np.mean(y_pred_val) == 0.36082474226804123
	
def test_random_forest():
	model, y_pred_train, y_pred_val = random_forest(X_train, y_train, X_val, 5, seed_value = 10)
	assert np.mean(y_pred_val) == 0.3402061855670103