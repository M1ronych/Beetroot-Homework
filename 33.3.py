import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "apid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    response = requests.get(BASE_URL,params=params)

    if response.status_code != 200:
        print("Місто не знайдене фбо помилка запиту")
        return

    data = response.json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"Місто: {city}")
    print(f"Погода: {weather}")
    print(f"Температура: {temp}°C")
    print(f"Відчувається як: {feels_like}°C")
    print(f"ВологістьЄ {humidity}%")
    print(f"Вітер: {wind} м/с")

if __name__ == "__main__":
    city_name = input("Введіть назву міста:")
    get_weather(city_name)


