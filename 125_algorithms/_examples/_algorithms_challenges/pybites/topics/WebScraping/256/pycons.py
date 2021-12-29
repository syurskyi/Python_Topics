import json
from collections import namedtuple
from typing import List

import requests
from bs4 import BeautifulSoup as Soup
from dateutil.parser import parse

PYCON_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"

PyCon = namedtuple("PyCon", "name city country start_date end_date url")

country_lookup = {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana",
        "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
        "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
        "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
        "Ivory Coast", "Kenya", "Lesotho", "Liberia",
        "Libya", "Madagascar", "Malawi", "Mali",
        "Mauritania", "Mauritius", "Morocco", "Mozambique",
        "Namibia", "Niger", "Nigeria", "Republic of the Congo",
        "Rwanda", "São Tome and Principe", "Senegal", "Seychelles",
        "Sierra Leone", "Somalia", "South Africa", "South Sudan",
        "Sudan", "Swaziland", "Tanzania", "The Gambia",
        "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
        "Bangladesh", "Bhutan", "Brunei", "Cambodia",
        "China", "East Timor", "Georgia", "India",
        "Indonesia", "Iran", "Iraq", "Israel",
        "Japan", "Jordan", "Kazakhstan", "Kuwait",
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
        "Maldives", "Mongolia", "Myanmar", "Nepal",
        "North Korea", "Oman", "Pakistan", "Palestinian territories",
        "Philippines", "Qatar", "Saudi Arabia", "Singapore",
        "South Korea", "Sri Lanka", "Syria", "Taiwan",
        "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
        "United Arab Emirates", "Uzbekistan", "Vietnam",
        "Yemen",
    ],
    "Australia and Oceania": [
        "Australia", "Federated States of Micronesia", "Fiji",
        "Kiribati", "Marshall Islands", "Nauru", "New Zealand",
        "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
        "Tonga", "Tuvalu", "Vanuatu",
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland",
        "France", "Germany", "Greece", "Hungary", "Iceland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland",
        "Portugal", "Republic of Ireland", "Republic of Macedonia",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
        "Slovenia", "Spain", "Sweden", "Switzerland",
        "Ukraine", "United Kingdom", "U.K.", "Vatican City",
    ],
    "North America": [
        "Antigua and Barbuda", "Barbados", "Belize",
        "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada",
        "Guatemala", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
        "Saint Lucia", "Saint Vincent and the Grenadines",
        "The Bahamas", "Trinidad and Tobago",
        "United States of America", "U.S.A.",
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile",
        "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela",
    ],
}


def get_continent(country: str) -> str:
    """
    Given a country name returns the associated continent of the country.

    :param country: The name of the country
    :type country: str
    :returns: The continent of the country
    :rtype: str
    """
    for continent, countries in country_lookup.items():
        for c in countries:
            if country.lower() in c.lower():
                return continent


def _get_pycon_data():
    """Helper function that retrieves the required PyCon data"""
    with requests.Session() as session:
        return session.get(PYCON_DATA).content.decode("utf-8")


def get_pycon_events(data=_get_pycon_data()) -> List[PyCon]:
    """
    Scrape the PyCon events from the given website data and
    return a list of PyCon namedtuples. Pay attention to the
    application/ld+json data structure website data.
    """
    whole_text = Soup(data, "html.parser")
    events = whole_text.find_all("script", {"type":"application/ld+json"})
    #print(events[0].text.strip())
    pycon_events = []
    for event in events:
        event_json = json.loads(event.text.strip())
        if 'pycon' in event_json["name"].lower():
            # { "@context": "http://schema.org", "@type": "Event", 
            # "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Trento", "addressCountry": "Italy" }, 
            # "name": "Trento, Italy" }, "name": "EuroSciPy", "startDate": "2018-08-28", "url": "https://www.euroscipy.org/2018/", "endDate": "2018-09-01" }
            # PyCon = namedtuple("PyCon", "name city country start_date end_date url")
            event_name = event_json['name']
            event_city = event_json["location"]["address"]["addressLocality"]
            event_country = event_json["location"]["address"]["addressCountry"]
            event_startDate = parse(event_json['startDate'])
            event_endDate = parse(event_json['endDate'])
            event_url = event_json['url']
            pycon_tuple = PyCon(name=event_name,
                                city=event_city,
                                country=event_country,
                                start_date=event_startDate,
                                end_date=event_endDate,
                                url=event_url
                                )
            pycon_events.append(pycon_tuple)
    return sorted(pycon_events, key=lambda x: x.city)



def filter_pycons(pycons: List[PyCon],
                  year: int = 2019,
                  continent: str = "Europe") -> List[PyCon]:
    """
    Given a list of PyCons a year and a continent return
    a list of PyCons that take place in that year and on
    that continent.
    """
    filtered_event = []
    for pycon in pycons:
        event_year = pycon.start_date.year
        event_continent = get_continent(pycon.country)
        print(event_year, event_continent)
        if int(event_year) == year and event_continent == continent:
            filtered_event.append(pycon)
    return sorted(filtered_event, key=lambda x: x.city)

#print(len(get_pycon_events()))
#print(get_pycon_events())

#print(filter_pycons(get_pycon_events()))