_______ __
____ p.. _______ P..
____ u__.r.. _______ u..
____ bs4 _______ BeautifulSoup
____ c.. _______ d..

# import the countries xml file
tmp  P..(__.g..("TMP", "/tmp"
countries tmp / 'countries.xml'

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
    w__ o.. countries, _ __ f:
        contents f.r..

    soup BeautifulSoup(contents, features='html.parser')
    table soup.find_all('wb:country')
    d d.. l..

    ___ tr __ table:
        name tr.find('wb:name').text
        income tr.find('wb:incomelevel').text
        d[income].a..(name)

    r.. d..(s..(d.i.., k.._l.... item: item[1]