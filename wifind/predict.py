from wifind.utils import get_model, split_x
from wifind.scan import scan

def predict():
    model = get_model()
    sample = scan(room="pred")
    X = split_x(sample)
    y = model.predict(X)
    y_prob = model.predict_proba(X)[0][0]
    print(f'{y[0]}: {y_prob:.2f}')