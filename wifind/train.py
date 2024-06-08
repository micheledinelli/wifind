from wifind.utils import get_data, save_model, get_model


def train():
    data = get_data()
    model = get_model()

    X = data.drop("room", axis=1)
    y = data["room"]

    model.fit(X, y)

    save_model(model)