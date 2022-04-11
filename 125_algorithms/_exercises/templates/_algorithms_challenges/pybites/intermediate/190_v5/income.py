____ p.. _______ P..
____ c.. _______ d..
____ u__.r.. _______ u..
_______ ___.e__.E__ __ ET

# import the countries xml file
tmp  P..('/tmp')
countries tmp / 'countries.xml'

__ n.. countries.exists
    u..('https://bit.ly/2IzGKav', countries)


___ get_income_distribution(___=countries
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree ET.p..(___)
    root tree.getroot()
    namespaces {__: 'http://www.worldbank.org'}

    xpath f".//wb:country"
    country_list d..(l..)
    ___ x __ root.f..(xpath, namespaces
        country_list[x.find('wb:incomeLevel', namespaces).text].a..(x.find('wb:name', namespaces).text)

    r.. country_list
