from django.shortcuts import render
from django.contrib import messages
from decouple import config  # Import environment variables from .env
import requests  # Library for making API requests


# Create your views here.
def home(request):
    # Get API keys from .env file
    API_KEY = config('API_KEY')
    ACCESS_KEY = config('ACCESS_KEY')

    # Get city name from form submission, otherwise use Kathmandu
    if 'city' in request.POST:
        city = request.POST.get('city', 'kathmandu')
    else:
        city = 'kathmandu'

    # OpenWeatherMap API URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    # Request parameters
    param = {'units': 'metric'}

    # Fetch weather data
    data = requests.get(url, param).json()

    # Unsplash API URL for city image
    image_url = f'https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id={ACCESS_KEY}'

    # Fetch city image
    response = requests.get(image_url).json()

    try:
        # Extract weather information
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        weather = data["weather"][0]["description"]
        weather_icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        country = data["sys"]["country"]

        # Get city image URL
        img = response['results'][0]['urls']['regular']

        # Render template with weather data
        return render(request, 'index.html', {
            'temp': temp,
            'city': city,
            'wind': wind,
            'description': weather,
            'humidity': humidity,
            'weather_icon': weather_icon,
            'feels_like': feels_like,
            'pressure': pressure,
            'country': country,
            'img': img
        })

    except:
        # Show error message if city is invalid or API fails
        messages.error(request, "no such city")

        # Default values
        temp = 0
        wind = 0
        weather = 0
        weather_icon = ''
        humidity = 0
        feels_like = 0
        pressure = 0
        country = "NP"
        img = ""

        # Render template with default values
        return render(request, 'index.html', {
            'temp': temp,
            'city': city,
            'wind': wind,
            'description': weather,
            'humidity': humidity,
            'weather_icon': weather_icon,
            'feels_like': feels_like,
            'pressure': pressure,
            'country': country,
            'img': img
        })