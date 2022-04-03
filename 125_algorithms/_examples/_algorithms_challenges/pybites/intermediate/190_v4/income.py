import os
from pathlib import Path
from u__.r.. import u..
from collections import defaultdict
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    u..(
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
    dist = defaultdict(list)
    tree = ET.parse(countries)
    root = tree.getroot()

    for child in root:
        dist[child[4].text].append(child[1].text)

    return dist
