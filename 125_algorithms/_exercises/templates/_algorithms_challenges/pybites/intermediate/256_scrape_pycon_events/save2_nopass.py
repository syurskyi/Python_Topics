_______ j__
____ c.. _______ n..
____ t___ _______ L..

_______ r__
____ ___ _______ B.. __ S..
____ dateutil.parser _______ p..

PYCON_DATA "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"

PyCon n..("PyCon", "name city country start_date end_date url")

country_lookup {
    "Africa": [
        "Algeria", "Angola", "Benin", "Botswana",
        "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
        "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
        "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
        "Ivory Coast", "Kenya", "Lesotho", "Liberia",
        "Libya", "Madagascar", "Malawi", "Mali",
        "Mauritania", "Mauritius", "Morocco", "Mozambique",
        "Namibia", "Niger", "Nigeria", "Republic of the Congo",
        "Rwanda", "São Tome and Principe", "Senegal", "Seychelles",
        "Sierra Leone", "Somalia", "South Africa", "South Sudan",
        "Sudan", "Swaziland", "Tanzania", "The Gambia",
        "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
        "Bangladesh", "Bhutan", "Brunei", "Cambodia",
        "China", "East Timor", "Georgia", "India",
        "Indonesia", "Iran", "Iraq", "Israel",
        "Japan", "Jordan", "Kazakhstan", "Kuwait",
        "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
        "Maldives", "Mongolia", "Myanmar", "Nepal",
        "North Korea", "Oman", "Pakistan", "Palestinian territories",
        "Philippines", "Qatar", "Saudi Arabia", "Singapore",
        "South Korea", "Sri Lanka", "Syria", "Taiwan",
        "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
        "United Arab Emirates", "Uzbekistan", "Vietnam",
        "Yemen",
    ],
    "Australia and Oceania": [
        "Australia", "Federated States of Micronesia", "Fiji",
        "Kiribati", "Marshall Islands", "Nauru", "New Zealand",
        "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
        "Tonga", "Tuvalu", "Vanuatu",
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belarus", "Belgium",
        "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
        "Czech Republic", "Denmark", "Estonia", "Finland",
        "France", "Germany", "Greece", "Hungary", "Iceland",
        "Italy", "Latvia", "Liechtenstein", "Lithuania",
        "Luxembourg", "Malta", "Moldova", "Monaco",
        "Montenegro", "Netherlands", "Norway", "Poland",
        "Portugal", "Republic of Ireland", "Republic of Macedonia",
        "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
        "Slovenia", "Spain", "Sweden", "Switzerland",
        "Ukraine", "United Kingdom", "U.K.", "Vatican City",
    ],
    "North America": [
        "Antigua and Barbuda", "Barbados", "Belize",
        "Canada", "Costa Rica", "Cuba", "Dominica",
        "Dominican Republic", "El Salvador", "Grenada",
        "Guatemala", "Haiti", "Honduras", "Jamaica",
        "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
        "Saint Lucia", "Saint Vincent and the Grenadines",
        "The Bahamas", "Trinidad and Tobago",
        "United States of America", "U.S.A.",
    ],
    "South America": [
        "Argentina", "Bolivia", "Brazil", "Chile",
        "Colombia", "Ecuador", "Guyana", "Paraguay",
        "Peru", "Suriname", "Uruguay", "Venezuela",
    ],
}


___ get_continent(country: s..) __ s..
    """
    Given a country name returns the associated continent of the country.

    :param country: The name of the country
    :type country: str
    :returns: The continent of the country
    :rtype: str
    """
    ___ continent, countries __ country_lookup.i..
        ___ c __ countries:
            __ country.l.. __ c.l..:
                r.. continent


___ _get_pycon_data
    """Helper function that retrieves the required PyCon data"""
    w__ r__.S.. __ session:
        r.. ?.g.. PYCON_DATA).content.d.. "utf-8")


___ get_pycon_events(data=_get_pycon_data __ L..[PyCon]:
    """
    Scrape the PyCon events from the given website data and
    return a list of PyCon namedtuples. Pay attention to the
    application/ld+json data structure website data.
    """
    soup S.. ? features='html.parser')
    data ?.f.. 'script', t..='application/ld+json')
    event_list    # list
    ___ x __ data:
        name j__.l.. (x.s__)["name"]
        __ name.s.. 'PyCon'
            event_list.a..(PyCon(name=name,
                                    city=j__.l.. (x.s__)["location"]["address"]["addressLocality"],
                                    country=j__.l.. (x.s__)["location"]["address"]["addressCountry"],
                                    start_date=j__.l.. (x.s__)["startDate"],
                                    end_date=j__.l.. (x.s__)["endDate"],
                                    url=j__.l.. (x.s__)["url"]
    r.. event_list


___ filter_pycons(pycons: L..[PyCon],
                  year: i.. 2019,
                  continent: s.. "Europe") __ L..[PyCon]:
    """
    Given a list of PyCons a year and a continent return
    a list of PyCons that take place in that year and on
    that continent.
    """
    filtered_list    # list
    ___ event __ pycons:
        event_year p..(event.start_date).year
        event_continent get_continent(event.country)
        __ event_year __ year a.. event_continent __ continent:
            filtered_list.a..(event)
    r.. filtered_list
