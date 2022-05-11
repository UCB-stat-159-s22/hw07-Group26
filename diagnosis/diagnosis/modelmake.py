import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,ConfusionMatrixDisplay, RocCurveDisplay,PrecisionRecallDisplay

def preprocessing(train_data,val_data):
    '''
    Does some preprocessing of the data before performing logistic regression.
    ---
    Arguments: 
    train_data (DataFrame): training data 
    val_data (DataFrame): validation data
    
    Returns: 
    X_train (DataFrame): preprocessed training feature matrix
    X_val (DataFrame): preprocessed validation feature matrix
    y_train (Series): training labels
    y_val (Series): validation labels
    
    '''
    X_train = train_data.drop(labels = ['diagnosis','id'],axis = 1) # drop labels and less predictive features for feature matrix
    y_train = train_data['diagnosis']
    X_val = val_data.drop(labels = ['diagnosis','id'],axis = 1)
    y_val = val_data['diagnosis']
    return X_train,X_val,y_train,y_val

def logistic_regression(X,y):
    '''
    Fits a logistic regression model to a feature matrix and labels.
    ---
    Arguments: 
    X (DataFrame): feature matrix
    y (Series): feature labels
    
    Returns: 
    fitted logistic regression model to X and y
    
    '''
    model = LogisticRegression(max_iter = 5000)
    return model.fit(X,y)

def logistic_regression_predict(model, X):
    '''
    Outputs logistic regression labels given a feature matrix X.
    ---
    Arguments: 
    X (DataFrame): feature matrix
    
    Returns:
    y_preds (array): predicted labels for the feature matrix
    
    '''
    return model.predict(X)

def get_metrics(y_preds,y_val):
    '''
    Gets all the measured metrics including accuracy, precision, recall and F1 score.
    ---
    Arguments:
    y_preds (array): predictions labels
    y_vals (Series): validation labels
    
    Returns: 
    Accuracy (float):Accuracy of the classifier
    Precision (float): Precision of the classifier
    Recall (float): Recall of the classifier
    F1 score (float): F1 score of the classifier

    '''
    print('Accuracy is:', accuracy_score(y_preds,y_val))
    print('Precision is:', precision_score(y_preds,y_val))
    print('Recall is:', recall_score(y_preds,y_val))
    print('F1 score is:' , f1_score(y_preds,y_val))  
  
# function to fit Decision Tree model
def decision_tree(X_train, y_train, X_val, seed_value = 10):
    """
    Fit a decision tree model and predict y values on train and validation data
    ---
    Arguments:
    X_train (pandas.DataFrame): the training data containing features used to predict Y
    y_train (pandas.Series): the training data containing result of diagnosis
	X_val (pandas.DataFrame): the validation data containing features used to predict Y
    seed_value (int): the random seed set to control stochastic results
    
    Returns:
    model (sklearn.DecisionTreeClassifier): the decision tree model trained by training set
    y_pred_train (array): the prediction of y using training data
    y_pred_val (array): the prediction of y using validation data
    """
    # set random seed
    np.random.seed(seed_value)
    # set the model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    # predict the values for the training and validation sets
    y_pred_train = model.predict(X_train)
    y_pred_val = model.predict(X_val)
    return model, y_pred_train, y_pred_val


# function to fit Random Forest model
def random_forest(X_train, y_train, X_val, max_feature, seed_value = 10):
    """
    Fit a random forest model and predict y values on train and validation data
    ---
    Arguments:
    X_train (pandas.DataFrame): the training data containing features used to predict Y
    y_train (pandas.Series): the training data containing result of diagnosis
	X_val (pandas.DataFrame): the validation data containing features used to predict Y
    max_feature (int): the maximum number of features Random Forest is allowed to try in individual tree
    seed_value (int): the random seed set to control stochastic results
    
    Returns:
    model (sklearn.RandomForestClassifier): the random forest model trained by training set
    y_pred_train (array): the prediction of y using training data
    y_pred_val (array): the prediction of y using validation data
    """
    # set random seed
    np.random.seed(seed_value)
    # set the model
    model = RandomForestClassifier(max_features = max_feature)
    model.fit(X_train, y_train)
    # predict the values for the training and validation sets
    y_pred_train = model.predict(X_train)
    y_pred_val = model.predict(X_val)
    return model, y_pred_train, y_pred_val
