import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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
