# Weather Application

from geopy.geocoders import Nominatim
import requests
import json


def weather_data(location=None):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(location)
    try:
        Latitude = getLoc.latitude
        Longitude = getLoc.longitude

        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid=313c138faa75abd252dd9aefcd356d9c"
        response = requests.get(api_url)
        dict_content = response.content.decode("utf-8")
        temperature = dict_content["main"]["temp"] - 273.16
        detail = {}
        detail["Temperature "] = round(temperature, 2)
        detail["Condition"] = dict_content["weather"][0]["description"].capitalize()
        detail["Humidity"] = dict_content["main"]["humidity"]
        detail["pressure"] = dict_content["main"]["pressure"]
        detail["wind"] = dict_content["wind"]["speed"]
        return detail
    except:
        print("Sorry,You Entered Wrong Location.")
        return None
