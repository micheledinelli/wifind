from wifind.utils import get_train_data, get_pipeline, save_model

def train():
    """
    This function is used to train the model using the data in data.csv.
    """    
    X, y = get_train_data()
    # model = get_model()

    # Train the model
    lp = get_pipeline()
    lp.fit(X, y)

    save_model(lp)