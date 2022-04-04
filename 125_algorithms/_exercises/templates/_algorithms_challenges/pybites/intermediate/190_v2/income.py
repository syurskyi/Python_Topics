_______ __
____ p.. _______ P..
____ c.. _______ d..
____ u__.r.. _______ u..
____ bs4 _______ BeautifulSoup

# import the countries xml file
tmp = P..(__.g..("TMP", "/tmp"
countries = tmp / 'countries.xml'

__ n.. countries.exists
    u..(
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
    w__ o.. ___ _ __ f:
        soup = BeautifulSoup(f.read

    
    income_to_countries = d..(l..)

    ___ country __ soup.find_all("wb:country"
        country_name = country.find('wb:name').getText()
        income = country.find('wb:incomelevel').getText()
        income_to_countries[income].a..(country_name)

    r.. income_to_countries

__ _______ __ _______

    get_income_distribution()


