import googlemaps
import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

print "Latitude : " + str(lat)
print "Longitude : " + str(lon)

gmaps = googlemaps.Client(key='YOUR_API_KEY')
API_key = "your API Key"

# Request
url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lon) + "&key=" + str(API_key)
x = requests.get(url)
resp = json.loads(x.text)

l = len(resp["results"][0]["address_components"])

# print l

for i in range(0,l):
    if resp["results"][0]["address_components"][i]["types"][0] == "administrative_area_level_1":
        index = i
        break

print "Your location : " + resp["results"][0]["address_components"][index]["long_name"]





