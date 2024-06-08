from wifind.utils import get_model
from wifind.utils import preprocess_sample
from wifind.scan import scan


def predict():
    model = get_model()
    sample = scan(room=None)

    X = preprocess_sample(sample)
    y = model.predict(X)

    print("".join(y))


def predict_proba():
    model = get_model()

    sample = scan(room=None)

    X = preprocess_sample(sample)
    y_prob = model.predict_proba(X)

    out = dict()
    for class_label, prob in zip(model.classes_, y_prob[0]):
        out[class_label] = prob

    print(out)
