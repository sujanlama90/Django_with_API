from django.shortcuts import render
from django.contrib import messages
from decouple import  config #pip install python-decouple
import requests

# Create your views here.
def home(request):
    API_KEY = config('API_KEY')
    ACCESS_KEY = config('ACCESS_KEY')
    if 'city' in request.POST:
        city = request.POST.get('city','kathmandu')
    else:
        city = 'kathmandu'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    param = {'units':'metric'}
    data = requests.get(url,param).json()
    
    image_url = f'https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id={ACCESS_KEY}'
    response = requests.get(image_url).json()
    img = response['results'][0]['urls']['regular']
    try:
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        weather = data["weather"][0]["description"]
        weather_icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        country = data["sys"]["country"]
        return render(request,'index.html',{'temp':temp,'city':city,
                                            'wind':wind,"description":weather,'humidity':humidity,
                                            'weather_icon':weather_icon,'feels_like':feels_like,
                                            'pressure':pressure,"country":country,'img':img})
    except:
        messages.error(request,"no such  city ")
        temp = 0
        wind = 0
        weather = 0
        weather_icon = ''
        humidity = 0
        feels_like = 0
        pressure = 0
        country = "NP"
        return render(request,'index.html',{'temp':temp,'city':city,
                                            'wind':wind,"description":weather,'humidity':humidity,
                                            'weather_icon':weather_icon,'feels_like':feels_like,
                                            'pressure':pressure,"country":country})