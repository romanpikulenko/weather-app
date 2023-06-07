import requests
from django.conf import settings
from django.shortcuts import render

from weather.forms import CityForm

from .models import City


# Create your views here.
def index(request):
    openweather_url = r"https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=%s" % (
        settings.OPENWEATHER_API_KEY,
    )

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all().order_by("name")
    weather_data = []

    for city in cities:
        r = requests.get(openweather_url.format(city)).json()

        city_weather = {
            "city": city.name,
            "temperature": r["main"]["temp"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"],
        }
        weather_data.append(city_weather)

    context = {
        "weather_data": weather_data,
        "form": form,
    }

    return render(request, "weather/weather.html", context)
