from wifind.utils import get_model
from wifind.utils import preprocess_sample
from wifind.scan import scan

def predict():
    # Load the model
    model = get_model()

    # Get online data
    sample = scan(room=None)

    X = preprocess_sample(sample)
    y = model.predict(X)

    print(y)

def predict_proba():
    # Load the model
    model = get_model()

    # Get online data
    sample = scan(room=None)

    X = preprocess_sample(sample)
    y_prob = model.predict_proba(X)

    # Print classes with respective probabilities
    out = dict()
    for class_label, prob in zip(model.classes_, y_prob[0]):
        out[class_label] = prob

    print(out)
