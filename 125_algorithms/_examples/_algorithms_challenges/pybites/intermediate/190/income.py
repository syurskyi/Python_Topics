import os
import xml.etree.ElementTree as ET
from pathlib import Path
from u__.r.. import u..
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
    country_incomes = defaultdict(list)
    tree = ET.parse(xml)
    root = tree.getroot()
    for child in root:
        level = ""
        country = ""
        for ele in child:
            element = ele.tag[ele.tag.rfind("}") +1:].lower()

            if element == "incomelevel":
                level = ele.text
            if element == "name":
                country = ele.text

        country_incomes[level].append(country)

    return country_incomes

# if __name__ == "__main__":
#     print(get_income_distribution())