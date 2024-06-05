from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_data_columns, get_predicted_price


def predict(request):

    data_columns = get_data_columns()
    locations = data_columns[3:]

    location = None
    bath = 1
    bhk = 1
    sqft = 1000
    price = None

    if request.method == "POST":
        location = request.POST.get("location")
        sqft = request.POST.get("sqft", 1000)
        bhk = request.POST.get("bhk", 1)
        bath = request.POST.get("bath", 1)
        price = get_predicted_price(location, sqft, bhk, bath)

    content = {
        "locations": locations,
        "location": location,
        "sqft": sqft,
        "bhk": bhk,
        "bath": bath,
        "price": price,
    }

    return render(request, "hpp/hpp.html", content)
