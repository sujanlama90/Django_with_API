// Optional: Fetch actual data using OpenWeather API
const apiKey = "546aa424c7307f3e3c5ebae20a7db814";

async function fetchWeather(city) {
  if (!apiKey || apiKey === "Y546aa424c7307f3e3c5ebae20a7db814") return;
  try {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`);
    const data = await response.json();

    if (data.cod === 200) {
      document.getElementById("city-name").innerText = data.name;
      document.getElementById("temp").innerText = `${Math.round(data.main.temp)}°C`;
      document.getElementById("feels-like").innerText = `${Math.round(data.main.feels_like)}°C`;
      document.getElementById("humidity").innerText = `${data.main.humidity}%`;
      document.getElementById("wind-speed").innerText = `${data.wind.speed} m/s`;
      document.getElementById("pressure").innerText = `${data.main.pressure} hPa`;
      document.getElementById("weather-desc").innerText = data.weather[0].description;
    }
  } catch (error) {
    console.error("Error fetching weather data:", error);
  }
}

document.getElementById("search-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const city = document.getElementById("city-input").value;
  fetchWeather(city);
});
