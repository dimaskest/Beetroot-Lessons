import requests
import datetime as dt
from tabulate import tabulate


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6a3d1390b4a1a53a20e298ab662b7102"
CITY = "Kyiv"


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return str(round(celsius)) + "°C"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_celsius = kelvin_to_celsius(response["main"]["temp"])
feels_like_celsius = kelvin_to_celsius(response["main"]["feels_like"])
weather = response["weather"][0]["main"]
wind_speed = response["wind"]["speed"]
sunrise_time = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunset_time = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])

data = [[CITY, temp_celsius, feels_like_celsius, weather, f"{wind_speed} m/s", sunrise_time, sunset_time]]
print(tabulate(data, headers=["City", "Tempareature", "Feels like", "Weather", "Wind speed", "Sunrise", "Sunset"]))