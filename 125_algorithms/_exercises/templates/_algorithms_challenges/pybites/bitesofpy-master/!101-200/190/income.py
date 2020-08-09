from pathlib ______ Path
from collections ______ defaultdict
from urllib.request ______ urlretrieve
______ xml.etree.ElementTree as ET

# ______ the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

__ not countries.exists(
    urlretrieve('https://bit.ly/2IzGKav', countries)


___ get_income_distribution(xml=countries
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(xml)
    root = tree.getroot()
    namespaces = {'wb': 'http://www.worldbank.org'}

    xpath = f".//wb:country"
    country_list = defaultdict(list)
    for x in root.findall(xpath, namespaces
        country_list[x.find('wb:incomeLevel', namespaces).text].append(x.find('wb:name', namespaces).text)

    r_ country_list
