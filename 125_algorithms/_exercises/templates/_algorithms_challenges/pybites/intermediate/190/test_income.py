_______ p__

____ income _______ get_income_distribution

EXPECTED = {'High income': ['Aruba',
                            'Argentina',
                            'Antigua and Barbuda',
                            'Bahamas, The',
                            'Barbados',
                            'Chile',
                            'Curacao',
                            'Cayman Islands',
                            'St. Kitts and Nevis',
                            'St. Martin (French part)',
                            'Panama',
                            'Puerto Rico',
                            'Sint Maarten (Dutch part)',
                            'Turks and Caicos Islands',
                            'Trinidad and Tobago',
                            'Uruguay',
                            'British Virgin Islands',
                            'Virgin Islands (U.S.)'],
            'Low income': ['Haiti'],
            'Lower middle income': ['Bolivia',
                                    'Honduras',
                                    'Nicaragua',
                                    'El Salvador'],
            'Upper middle income': ['Belize',
                                    'Brazil',
                                    'Colombia',
                                    'Costa Rica',
                                    'Cuba',
                                    'Dominica',
                                    'Dominican Republic',
                                    'Ecuador',
                                    'Grenada',
                                    'Guatemala',
                                    'Guyana',
                                    'Jamaica',
                                    'St. Lucia',
                                    'Mexico',
                                    'Peru',
                                    'Paraguay',
                                    'Suriname',
                                    'St. Vincent and the Grenadines',
                                    'Venezuela, RB']}


@p__.f..(scope="module")
___ actual
    r.. get_income_distribution()


@p__.m__.p..("income, countries", EXPECTED.i..
___ test_return_function(actual, income, countries):
    ... income __ actual
    ... s..(actual[income]) __ s..(countries)