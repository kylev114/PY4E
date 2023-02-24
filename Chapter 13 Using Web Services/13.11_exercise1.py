# Exercise 1: Change either geojson.py (13.9) to print out the two character 
# country code from the retrieved data. Add error checking so
# your program does not traceback if the country code is not there. Once
# you have it working, search for “Atlantic Ocean” and make sure it can
# handle locations that are not in any country

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4)) # returns the JSON file 

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    location = js['results'][0]['formatted_address']
    
    # ***Actual Code Edit***
    try: shortName = js['results'][0]['address_components'][2]['short_name']
    except: 
        shortName = js['results'][0]['address_components'][0]['short_name']
        if len(shortName) >2 : shortName = 'Location not in a country'
    # ***

    print('Short Name:', shortName)
    print('lat', lat, 'lng', lng)
    print(location)
