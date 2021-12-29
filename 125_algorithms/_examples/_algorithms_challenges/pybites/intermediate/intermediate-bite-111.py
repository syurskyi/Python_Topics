"""
In this Bite you will use the requests library to make a GET request to the ipinfo service.

Use IPINFO_URL and parse the (2 char) country code from the obtained json response.

Note how we mocked out the requests.get call in the tests, you can see another example of
this in our Parsing Twitter Geo Data and Mocking API Calls by Example article.

Querying APIs is a common need so this should become second nature :) - enjoy!
"""
import requests
import json as j

# https://stackoverflow.com/questions/58048879/what-is-the-difference-between-json-method-and-json-loads

IPINFO_URL = 'http://ipinfo.io/{ip}/json'

def get_ip_country_2(ip_address):
    response = requests.get(IPINFO_URL.format(ip=ip_address))
    print(type(response.text))
    print(response.text)
    jso = j.loads(response.text)
    print(type(jso))
    print(jso['country'])


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""

    # Execute HTTP GET request, this method returns requests.models.Response object
    response = requests.get(IPINFO_URL.format(ip=ip_address))
    # Returns json-encoded value of the response object, throws ValueError if the response body does not contain a valid json
    # So dzejson is a dict
    try:
        dzejson = response.json()
    except ValueError:
        print("Response did not contain a valid JSON")

    return(dzejson['country'])

print(get_ip_country_2(ip_address="8.8.8.8"))


