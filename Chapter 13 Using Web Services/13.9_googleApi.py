# Google has an excellent web service that allows us to make use of their large
# database of geographic information. We can submit a geographical search string
# like “Ann Arbor, MI” to their geocoding API and have Google return its best
# guess as to where on a map we might find our search string and tell us about the
# landmarks nearby.

# The geocoding service is free but rate limited so you cannot make unlimited use of
# the API in a commercial application. But if you have some survey data where an
# end user has entered a location in a free-format input box, you can use this API
# to clean up your data quite nicely.

# This program takes user input string (i.e. “Ann Arbor, MI”) and constructs a URL 
# with the search string as a properly encoded parameter and then uses urllib to 
# retrieve the text from the Google geocoding API. Unlike a fixed web page, the 
# data we get depends on the parameters we send and the geographical data stored 
# in Google’s servers. Once we retrieve the JSON data, we parse it with the json library 
# and do a few checks to make sure that we received good data, then extract the 
# information that we are looking for.


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

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

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    location = js['results'][0]['formatted_address']

    print('lat', lat, 'lng', lng)
    print(location)