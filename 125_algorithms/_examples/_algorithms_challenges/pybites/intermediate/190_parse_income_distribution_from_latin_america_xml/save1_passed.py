import os
from pathlib import Path
from u__.r.. import u..
from bs4 import BeautifulSoup
from collections import defaultdict

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
    with open(countries, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, features='html.parser')
    table = soup.find_all('wb:country')
    d = defaultdict(list)

    for tr in table:
        name = tr.find('wb:name').text
        income = tr.find('wb:incomelevel').text
        d[income].append(name)

    return dict(sorted(d.items(), key=lambda item: item[1]))