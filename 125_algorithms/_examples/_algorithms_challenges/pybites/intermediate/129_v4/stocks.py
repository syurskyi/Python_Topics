import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""

    if 'n/a' in cap:
        value = 0
    else:
        unit = cap[-1]
        cap = cap[1:-1]
        value = float(cap)
        value = value * 1000 if unit == 'B' else value

    return value


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total = sum(map(lambda x: _cap_str_to_mln_float(x['cap']),
                    filter(lambda x: x['industry'] == industry, data)
                    )
                )

    return round(total, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return max(data, key=lambda x: _cap_str_to_mln_float(x['cap']))['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    min_max = Counter(map(lambda x: x['sector'],
                          filter(lambda x: x['sector'] != 'n/a', data)
                          )
                      )
    most = min_max.most_common(1)[0][0]
    least = min_max.most_common()[-1][0]
    return most, least
