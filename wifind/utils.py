import os
import pickle
import pandas as pd
from wifind.errors import NoDataException
from sklearn.ensemble import RandomForestClassifier


DATA_DIR = os.path.expanduser("~/.wifind")
DATA_PATH = os.path.join(DATA_DIR, "data.csv")
MODEL_PATH = os.path.join(DATA_DIR, "model.pkl")


def get_data() -> pd.DataFrame:
    if os.path.exists(get_data_path()):
        return pd.read_csv(DATA_PATH, index_col=0)
    else:
        raise NoDataException("No data found")


def save_data(online_data):
    try:
        data = get_data()
        df = pd.concat([data, pd.DataFrame([online_data])], ignore_index=True)
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)
    except NoDataException:
        df = pd.DataFrame(online_data, index=[0])
        df.fillna(0, inplace=True)
        df.to_csv(DATA_PATH)


def get_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as file:  
            model = pickle.load(file)
            return model
    else:
        return get_pipeline()
    
    
def save_model(model):
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)


def get_pipeline():
    return RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")


def preprocess_sample(sample: dict):
    data = get_data()

    # Some APs may not be in the model, so we need to fill in the missing values
    X = pd.DataFrame([sample])

     # X has to contain all the columns in data, if X miss some columns it has to be added with the median value of the column
    missing_columns = set(data.drop(columns=["room"]).columns) - set(X.columns)
    
    for col in missing_columns:
        X[col] = 0
        
    # X has to contain all the columns in data, if X has more columns than data, it has to be removed
    X = X[data.drop(columns=["room"]).columns]
    return X


def clear():
    if os.path.exists(DATA_PATH):
        os.remove(DATA_PATH)

    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)

    if os.path.exists(DATA_DIR):
        os.rmdir(DATA_DIR)


def get_data_path():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    return DATA_PATH


def get_model_path():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    return MODEL_PATH