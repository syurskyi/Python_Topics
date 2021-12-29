import json
import time
import requests
from dataclasses import dataclass
from datetime import datetime
from math import acos, cos, radians, sin
import os
from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"



tmp = Path(os.getenv("TMP", "/tmp"))
pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"



response = requests.get(RESPONSES)

data = response.json()

pycons = requests.get(URL).json()
print(pycons)




if not pycons_file.exists() or not nominatim_responses.exists():
    urlretrieve(URL, pycons_file)
    urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


    def __lt__(self,other):
        if isinstance(other,PyCon):
            return self.start_date < other.start_date


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            )
            for pycon in json.load(f)
        ]


def _km_distance(origin, destination):
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat]
    )
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


def _extract_city_country_to_lat_lon():
        
    
    with open(nominatim_responses,'r') as f:
        places = json.load(f)
    
    mapping = {}
    for key,places in places.items():
        for r in places:
            if r['type'] == 'city':
                city,*temp,country = r['display_name'].split(',')
                city = city.strip()
                country = country.strip()
                mapping[(city,country)] = (r['lat'],r['lon'])
    
    return mapping
        

# Your code #
def update_pycons_lat_lon(pycons):
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """
    mapping = _extract_city_country_to_lat_lon()

    for pycon in pycons:
        city = pycon.city
        country = pycon.country

        for response in data:
            lat,lon = mapping[(city,country)]
            pycon.lat = lat
            pycon.lon = long
    














def create_travel_plan(pycons):
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """

    sorted_pycons = sorted(pycons)



    return [Trip(sorted_pycons[i],sorted_pycons[i +1],_get_pycons(sorted_pycons[i],sorted_pycons[i +1])) for i in range(len(sorted_pycons) - 1)]











def total_travel_distance(journey):
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """


    return round(sum(leg.distance for leg in journey),2)
