_______ __
____ p.. _______ P..
____ t___ _______ DefaultDict
____ u__.r.. _______ u..
_______ ___.e__.E__ __ ET


# import the countries xml file
tmp  P.. __.g.. "TMP", "/tmp"
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
    new_list DefaultDict(l..)
    tree ET.p..(countries)
    root tree.getroot()
    ___ country __ root:
        country_name country.findtext('{http://www.worldbank.org}name')
        incomeLevel country.findtext('{http://www.worldbank.org}incomeLevel')
        new_list[incomeLevel].a..(country_name)
    r.. new_list

print(get_income_distribution