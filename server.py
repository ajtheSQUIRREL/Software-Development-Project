# Weather Application

from geopy.geocoders import Nominatim


def weather_data():
    loc = Nominatim(user_agent="GetLoc")
    print("Enter Your Location : ", end=" ")
    location = input()

    getLoc = loc.geocode(location)

    try:

        Latitude = getLoc.latitude
        Longitude = getLoc.longitude

        print(f"Latitude : {Latitude},Longitude : {Longitude}")

    except:
        print("Sorry,You Entered Wrong Location.")


weather_data()
