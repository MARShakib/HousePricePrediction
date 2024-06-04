from django.shortcuts import render
from django.http import HttpResponse
from .utils import load_model, get_data_columns, get_predicted_price


def predict(request):
    model = load_model()
    data_columns = get_data_columns()
    locations = data_columns[3:]
    features = [["Indira Nagar", 1000, 2, 2]]
    print(get_predicted_price("Indira Nagar", 1000, 2, 2))
    return HttpResponse("ok")
