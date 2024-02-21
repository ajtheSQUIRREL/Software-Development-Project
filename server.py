# Weather Application

from geopy.geocoders import Nominatim
import requests
import json


def weather_data(lat, long):
    # loc = Nominatim(user_agent="GetLoc")
    # print("Enter Your Location : ", end=" ")
    # location = input()

    # getLoc = loc.geocode(location)

    try:

        # Latitude = getLoc.latitude
        # Longitude = getLoc.longitude

        # print(f"Latitude : {Latitude},Longitude : {Longitude}")

        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=313c138faa75abd252dd9aefcd356d9c"

        response = requests.get(api_url)
        content = response.content.decode("utf-8")
        dict_content = json.loads(content)
        temperature = dict_content["main"]["temp"] - 273.16
        # print("Weather Update :")
        # print(f'Country        : {dict_content["sys"]["country"]}')
        # print(f"Place          : {location.capitalize()}")
        # print(f"Temperature    : {round(temperature,2)} Degree Celsius")
        # print(
        #     f'Condition      : {dict_content["weather"][0]["description"].capitalize()}'
        # )
        # print(f'Humidity       : {dict_content["main"]["humidity"]}%')
        return temperature
    except:
        print("Sorry,You Entered Wrong Location.")


# weather_data()
