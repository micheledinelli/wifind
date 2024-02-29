import os
import pickle
import json

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline

DATA_PATH = "data.json"
MODEL_PATH = "model.pkl"

def get_data():
    """
    This function is used to load the data from the file system.

    Returns:
        list: A list object containing the loaded data.
    """
    try:
        return list(json.load(open(DATA_PATH)))
    except (FileNotFoundError, json.JSONDecodeError):
        raise Exception("No data found")
    
def get_train_data():
    """
    This function is used to load the data from the file system.

    Returns:
        tuple: A tuple object containing the loaded data.
    """
    
    data = get_data()

    # Extract 'y' and 'x' for each key
    X, y = [], []
    for d in data:
        for key, value in d.items():
            X.append(value)
            y.append(key)
    return X, y

def save_data(online_data):
    """
    This function is used to save the data to the file system.
    """
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(online_data)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f)
    
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