_______ os
____ pathlib _______ Path
____ urllib.request _______ urlretrieve
____ bs4 _______ BeautifulSoup
____ collections _______ defaultdict

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

__ n.. countries.exists
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


___ get_income_distribution(___=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    w__ open(countries, 'r') __ f:
        contents = f.read()

    soup = BeautifulSoup(contents, features='html.parser')
    table = soup.find_all('wb:country')
    d = defaultdict(l..)

    ___ tr __ table:
        name = tr.find('wb:name').text
        income = tr.find('wb:incomelevel').text
        d[income].a..(name)

    r.. d..(s..(d.i.., key=l.... item: item[1]))