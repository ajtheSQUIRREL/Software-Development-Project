# Weather Application

from geopy.geocoders import Nominatim
import requests
import json


def weather_data(location=None):
    loc = Nominatim(user_agent="GetLoc")
    # print("Enter Your Location : ", end=" ")
    # location = input()

    getLoc = loc.geocode(location)
    try:
        Latitude = getLoc.latitude
        Longitude = getLoc.longitude

        # print(f"Latitude : {Latitude},Longitude : {Longitude}")
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid=313c138faa75abd252dd9aefcd356d9c"
        response = requests.get(api_url)
        dict_content = response.content.decode("utf-8")
        # print(dict_content)
        temperature = dict_content["main"]["temp"] - 273.16

        # print(f'Country        : {dict_content["sys"]["country"]
        # print(f"Place          : {location.capitalize()}")
        Temperature = round(temperature, 2)
        Condition = dict_content["weather"][0]["description"].capitalize()
        Humidity = dict_content["main"]["humidity"]
        pressure = dict_content["main"]["pressure"]
        wind = dict_content["wind"]["speed"]
        return Temperature, Condition, Humidity, pressure, wind
    except:
        print("Sorry,You Entered Wrong Location.")


# weather_data()
