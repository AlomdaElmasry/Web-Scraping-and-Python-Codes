import requests
import json

API_KEY = "YOUR_API_KEY"

li = {"origins" : "Delhi", "destinations" : "Mumbai", "mode" : "driving", "key" : API_KEY}

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&mode={mode}&key={key}"
final_url = url.format(**li)


r = requests.post(final_url)
j = json.loads(r.text)

print j['rows']

