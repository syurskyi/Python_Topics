____ pathlib _______ Path
____ collections _______ defaultdict
____ urllib.request _______ urlretrieve
_______ ___.e__.E__ as ET

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

__ n.. countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


___ get_income_distribution(___=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(___)
    root = tree.getroot()
    namespaces = {'wb': 'http://www.worldbank.org'}

    xpath = f".//wb:country"
    country_list = defaultdict(l..)
    ___ x __ root.findall(xpath, namespaces):
        country_list[x.find('wb:incomeLevel', namespaces).text].a..(x.find('wb:name', namespaces).text)

    r.. country_list
