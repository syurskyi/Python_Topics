import os
from pathlib import Path
from collections import defaultdict
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

__ not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


___ get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    with open(xml,'r') as f:
        soup = BeautifulSoup(f.read())

    
    income_to_countries = defaultdict(list)

    for country in soup.find_all("wb:country"):
        country_name = country.find('wb:name').getText()
        income = country.find('wb:incomelevel').getText()
        income_to_countries[income].append(country_name)

    return income_to_countries

__ __name__ == "__main__":

    get_income_distribution()


