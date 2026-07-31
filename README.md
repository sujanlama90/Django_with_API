# 🌤️ Django Weather Dashboard

A modern weather dashboard built with
**Django** that fetches live weather data from the
**OpenWeatherMap API** and displays a beautiful city image from the **Unsplash API**.

---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Live temperature in Celsius
- 🌤️ Weather condition with official weather icon
- 💨 Wind speed
- 💧 Humidity
- 🌡️ Feels like temperature
- 📊 Atmospheric pressure
- 🌍 Country code display
- 🖼️ Dynamic city image from Unsplash
- 🚨 Beautiful error notifications using Alertify.js
- 🎨 Responsive Bootstrap 5 interface
- 🔐 Secure API keys using `.env`
- 📱 Mobile-friendly design

---

## 🛠️ Built With

- Python
- Django
- Bootstrap 5
- Bootstrap Icons
- HTML5
- CSS3
- Requests
- Python Decouple
- Alertify.js
- OpenWeatherMap API
- Unsplash API

---

## 📁 Folder Structure

```text
fetchApi/
│
├── fetchApi/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── weather/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── index.css
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   └── apps.py
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## 🚀 Installation

```bash
git clone https://github.com/sujanlama90/fetchApi.git

cd fetchApi

python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a **.env** file:

```env
API_KEY=your_openweathermap_api_key
ACCESS_KEY=your_unsplash_access_key
```

Run the server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🌐 APIs Used

### OpenWeatherMap

Provides:

- Temperature
- Weather Description
- Weather Icon
- Wind Speed
- Humidity
- Pressure
- Feels Like Temperature
- Country Code

### Unsplash

Provides a high-quality background image for the searched city.

---

## 📸 UI Highlights

- 🌙 Modern Glassmorphism Weather Card
- 🔍 Interactive Search Bar
- 🌤️ Live Weather Icon
- 📷 Dynamic City Image
- 📊 Weather Statistics Cards
- 🚨 Alertify Notifications
- 📱 Fully Responsive Layout

---

## 📸 Screenshots

> 

```
screenshots/
├── weather.png
```

---

## 👨‍💻 Author

**Sujan Lama**

- 🐍 Python Developer
- 🌐 Django Developer
- 🚀 Backend Enthusiast

GitHub: **https://github.com/sujanlama90**

---

## ⭐ Show Your Support

If you like this project, don't forget to ⭐ star the repository!
