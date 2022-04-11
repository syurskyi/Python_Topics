_______ __
____ p.. _______ P..
____ u__.r.. _______ u..
____ c.. _______ d..
_______ ___.e__.E__ __ ET

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
    dist d..(l..)
    tree ET.p..(countries)
    root tree.getroot()

    ___ child __ root:
        dist[child[4].text].a..(child[1].text)

    r.. dist
