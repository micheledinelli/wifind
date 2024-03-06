import os
import pickle
import json
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline

DATA_PATH = "data.csv"
MODEL_PATH = "model.pkl"

def get_data():
    """
    This function is used to load the data from the file system.

    Returns:
        Dataframe: A dataframe.
    """
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH, index_col=0)
    else:
        return pd.DataFrame()

def save_data(online_data):
    """
    This function is used to save the data to the file system.
    """
    # check file exists
    data = get_data()
    
    if data.empty:
        df = pd.DataFrame(online_data, index=[0])

        # Nan becomes 0
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)
    else:
        df = pd.concat([data, pd.DataFrame([online_data])], ignore_index=True)
        
        # Nan becomes 0
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)

def get_model():
    """
    This function is used to load the model from the file system.
    """
    with open(MODEL_PATH, 'rb') as file:  
        model = pickle.load(file)
        return model
    
def save_model(model):
    """
    This function is used to save the model to the file system.
    """
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

def get_pipeline(clf=RandomForestClassifier(n_estimators=100, class_weight="balanced")):
    return make_pipeline(DictVectorizer(sparse=False), clf)

def split_x(data: dict):
    return list(data.values())

def clear():
    """
    Clears data 
    """
    if os.path.exists(DATA_PATH):
        os.remove(DATA_PATH)