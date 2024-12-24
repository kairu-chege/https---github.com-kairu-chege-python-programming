from django.shortcuts import render
from .models import City
import requests

# Create your views here.

def weather_data(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        api_key = '523146928c6f4093a89f74857a70c737'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json
        context = {
            'city': city_name,
            'temperature': response['main']['temp'],
            'humidity': response['main']['humidity'],
            'wind_speed': response['wind']['speed'],
            'pressure': response['main']['pressure'],
            'description': response['weather'][0]['description'],
        }
        return render(request, 'weather/index.html', context)
    return render(request, 'weather/index.html')