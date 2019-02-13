from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from weather.models import City
from weather.forms import CityForm
import requests
# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=006c89cde1c1914e319a96dc02446ab9'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('weather:home'))
    else:
        form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {
        'weather_data': weather_data, 'form': form
    }
    return render(request, 'weather/index.html', context)
