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
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0


    cap = cap.lstrip('$')
    if 'M' in cap:
        value = float(cap.rstrip('M'))
    elif 'B' in cap:
        value = float(cap.rstrip('B')) * 1000

    return value



def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""

    total = 0
    for company in data:
        if company['industry'] == industry:
            total += _cap_str_to_mln_float(company['cap'])


    return round(total,2)

           


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""

    return max(data,key=lambda x: _cap_str_to_mln_float(x['cap']))['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    counts = Counter()

    for company in data:
        sector = company['sector']
        if sector != 'n/a':
            counts[company['sector']] += 1


    sector_counts = counts.most_common()

    return sector_counts[0][0],sector_counts[-1][0]
