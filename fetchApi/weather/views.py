from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST.get('city','kathmandu')
    else:
        city = 'kathmandu'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=546aa424c7307f3e3c5ebae20a7db814'
    param = {'units':'metric'}
    data = requests.get(url,param).json()
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    weather = data["weather"][0]["description"]
    weather_icon = data["weather"][0]["icon"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    return render(request,'index.html',{'temp':temp,'city':city,'wind':wind,"description":weather,'humidity':humidity,'weather_icon':weather_icon,'feels_like':feels_like,'pressure':pressure})