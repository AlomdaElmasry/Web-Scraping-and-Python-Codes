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

q = raw_input("What do you want to search for : ")
r = raw_input("Enter radius for search : ")

API_KEY = 'AIzaSyC8Ny7X4cuCOd_9SE21raopnTC-KswEs0Y'

places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lon)+ \
             "&radius=" + str(r) + "&keyword=" + str(q) + "&key=" + str(API_KEY)

x = requests.post(places_url)
resp = json.loads(x.text)

l = len(resp["results"])
# print l

for i in range(0,l):
    if resp["results"][i]["name"]:
        print resp["results"][i]["name"] + "  -  " + resp["results"][i]["vicinity"]
    else:
        print "Name not found"







