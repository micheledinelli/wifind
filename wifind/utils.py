import os
import pickle
import pandas as pd
import sys
from wifind.errors import NoDataException

from sklearn.ensemble import RandomForestClassifier

DATA_PATH = "data.csv"
MODEL_PATH = "model.pkl"

def get_data():
    """
    This function is used to load the data from the file system.

    Returns: Dataframe: A dataframe.

    Raises: NoDataException: An exception is raised if no data is available.
    """
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH, index_col=0)
    else:
        raise NoDataException()

def save_data(online_data):
    """
    This function is used to save the data to the file system.
    """
    try:
        data = get_data()
        df = pd.concat([data, pd.DataFrame([online_data])], ignore_index=True)
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)
    except NoDataException:
        # If there is no data, create a new file
        df = pd.DataFrame(online_data, index=[0])
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)

def get_model():
    """
    This function is used to load the model from the file system.
    """
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as file:  
            model = pickle.load(file)
            return model
    else:
        return get_pipeline()
    
def save_model(model):
    """
    This function is used to save the model to the file system.
    """
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

def get_pipeline():
    return RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")

def preprocess_sample(sample: dict):
    """
    This function is used to preprocess the sample data. It fills in the missing values and removes the extra columns.
    Args: sample (dict): A dictionary.
    Returns: Dataframe: A dataframe.
    """

    # Load the data
    data = None
    try:
        data = get_data()
    except NoDataException as e:
        print(e)
        sys.exit(1)

    # Some APs may not be in the model, so we need to fill in the missing values
    X = pd.DataFrame([sample])

    # X has to contain all the columns in data, if X miss some columns it has to be added with the median value of the column
    missing_columns = set(data.drop(columns=["room"]).columns) - set(X.columns)
    for col in missing_columns:
        # Fill missing columns with the median value from the training data
        median_value = data[col].median()
        X[col] = median_value
        
    # X has to contain all the columns in data, if X has more columns than data, it has to be removed
    X = X[data.drop(columns=["room"]).columns]
    return X

def clear():
    """
    Clears data 
    """
    if os.path.exists(DATA_PATH):
        os.remove(DATA_PATH)

    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)