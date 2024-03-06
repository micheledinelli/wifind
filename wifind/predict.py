from wifind.utils import get_model
from wifind.utils import save_data, get_data
from wifind.scan import scan
import pandas as pd

def predict():
    # Load the model
    model = get_model()
    
    # Load the data
    data = get_data()
    
    # Get online data
    sample = scan(room=None)

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

    y = model.predict(X)
    y_prob = model.predict_proba(X)
    print(f'{y[0]}: {y_prob.max() * 100:.2f}%')