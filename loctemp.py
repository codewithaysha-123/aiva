from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
import speak as sp
import webbrowser as web
import requests

def temperature():
    api_key = "34aa2e75f01e573ba281169e4bd7f508"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    sp.speak("Which city's temperature do you want to find")
    city_name = input("Enter city name : ")

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()
    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        sp.speak(f" Temperature (in kelvin unit) = {current_temperature}  ")
        sp.speak(f"atmospheric pressure (in hPa unit) = {current_pressure}  ")
        sp.speak(f"humidity (in percentage) = {current_humidity}")
        sp.speak(f"description = {weather_description}")

    else:
        sp.speak("Sorry ma'am we are unable to find the City...")


def myloc():
    sp.speak("Wait ma'am, let me check")
    loc = Nominatim(user_agent="GetLoc")

    getLoc = loc.geocode("bhatkal")

    sp.speak("We are here in")
    sp.speak(getLoc.address)

    sp.speak(f"Latitude = {getLoc.latitude}")
    sp.speak(f"Longitude = { getLoc.longitude}")

def loc():
    op = "https://www.google.com/maps/place/Anjuman+Institute+of+Management+and+Computer+Application/@13.9990795,74.5548662,215m/data=!3m1!1e3!4m12!1m6!3m5!1s0x3bbc436a527b3203:0xa7603312ddf8bb1!2sAnjuman+Pre+University+college!8m2!3d13.9953604!4d74.5552229!3m4!1s0x0:0x90956de6d72d34e6!8m2!3d13.9991418!4d74.5555674"
    web.open(op)

    sp.speak("Wait Ma'am, Checking..")
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo' + ip_add + '.json'

    geo_q = requests.get(url)
    geo_d = geo_q.json()

    state = geo_d['city']
    country = geo_d['country']

    sp.speak(f"Ma'am, You are now in {state,country}.")

def GoogleMaps(place):
    url_place = "https://www.google.com/maps/place/" + str(place)

    sp.speak("Ma'am, fetching the location!!")

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails= True)

    web.open(url = url_place)

    target_latlon = location.latitude, location.longitude
    location = location.raw['address']

    target = {'city': location.get('city',''),
              'state': location.get('state',''),
              'country': location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    sp.speak(target)
    sp.speak(f"Ma'am, {place} is {distance} kilometer away from your Location")

if __name__ == "__main__":
    GoogleMaps("bhatkal")