import requests
import json

API_KEY = "AIzaSyC8Ny7X4cuCOd_9SE21raopnTC-KswEs0Y"

li = {"origins" : "Delhi", "destinations" : "Mumbai", "mode" : "driving", "key" : API_KEY}

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&mode={mode}&key={key}"
final_url = url.format(**li)


r = requests.post(final_url)
j = json.loads(r.text)

print j['rows']

