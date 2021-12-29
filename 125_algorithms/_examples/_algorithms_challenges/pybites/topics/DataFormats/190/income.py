import os
from pathlib import Path
from typing import DefaultDict
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET


# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    new_list = DefaultDict(list)
    tree = ET.parse(countries)
    root = tree.getroot()
    for country in root:
        country_name = country.findtext('{http://www.worldbank.org}name')
        incomeLevel = country.findtext('{http://www.worldbank.org}incomeLevel')
        new_list[incomeLevel].append(country_name)
    return new_list

print(get_income_distribution())