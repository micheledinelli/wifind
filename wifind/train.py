from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from wifind.utils import get_data, get_pipeline, save_model, get_model

def train():
    """
    This function is used to train the model using the data in data.csv.
    """    
    data = get_data()
    model = get_model()

    X = data.drop("room", axis=1)
    y = data["room"]

    model.fit(X, y)

    save_model(model)