_______ __
_______ ___.e__.E__ __ ET
____ pathlib _______ Path
____ u__.r.. _______ u..
____ c.. _______ defaultdict

# import the countries xml file
tmp = Path(__.getenv("TMP", "/tmp"))
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
    country_incomes = defaultdict(l..)
    tree = ET.p..(___)
    root = tree.getroot()
    ___ child __ root:
        level = ""
        country = ""
        ___ ele __ child:
            element = ele.tag[ele.tag.rfind("}") +1:].l..

            __ element __ "incomelevel":
                level = ele.text
            __ element __ "name":
                country = ele.text

        country_incomes[level].a..(country)

    r.. country_incomes

# if __name__ == "__main__":
#     print(get_income_distribution())