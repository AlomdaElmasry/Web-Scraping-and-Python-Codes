import requests

# constants
RUN_URL_compile = u'http://api.hackerearth.com/code/compile/'  # for code compilation
RUN_URL_run = u'http://api.hackerearth.com/code/run/'  # for code execution

CLIENT_SECRET = 'your client secret key'

source = "print 2+5"

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0, # Aysnchronous mode
    'source': source, # Source Code
    'lang': "PYTHON",
    'time_limit': 5,
    'memory_limit': 262144,
}

r1 = requests.post(RUN_URL_compile, data=data)
r2 = requests.post(RUN_URL_run, data=data)

# Print responses
print r1.json()
print "\n"
print r2.json()