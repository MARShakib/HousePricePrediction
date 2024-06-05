import pickle
import json
import numpy as np


def load_model():
    with open("hpp/essentials/banglore_home_prices_model.pickle", "rb") as file:
        model = pickle.load(file)
    return model


def get_data_columns():
    with open("hpp/essentials/columns.json", "rb") as file:
        data_columns = json.load(file)["data_columns"]
    return data_columns


def get_predicted_price(location, sqft, bhk, bath):
    data_columns = get_data_columns()
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    model = load_model()

    return round(model.predict([x])[0], 2)
