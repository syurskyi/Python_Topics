_______ os
____ pathlib _______ Path
____ urllib.request _______ urlretrieve
____ c.. _______ defaultdict
_______ ___.e__.E__ __ ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

__ n.. countries.exists
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


___ get_income_distribution(___=countries
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    dist = defaultdict(l..)
    tree = ET.p..(countries)
    root = tree.getroot()

    ___ child __ root:
        dist[child[4].text].a..(child[1].text)

    r.. dist
