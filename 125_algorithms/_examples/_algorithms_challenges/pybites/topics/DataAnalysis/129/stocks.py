import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:
mkdi
def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    elif cap[0] == '$' and cap[-1] == 'M':
        return float(cap[1:-1])
    elif cap[0] == '$' and cap[-1] == 'B':
         return float(cap[1:-1])*1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    locallist = [counter['cap'] for counter in data if counter['industry'] == industry]
    return round(sum([_cap_str_to_mln_float(cap) for cap in locallist]),2)

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    #highest_cap = 0
    highest_cap_stock = max(data, key=lambda counter: _cap_str_to_mln_float(counter['cap']))
    #for counter in data:
    #    if _cap_str_to_mln_float(counter['cap']) > highest_cap:
    #        highest_cap_stock = counter['symbol']
    #        highest_cap = _cap_str_to_mln_float(counter['cap'])
    return highest_cap_stock['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    stock_by_sector = Counter(counter['sector'] for counter in data if counter['sector'] != 'n/a')
    return stock_by_sector.most_common()[0][0], stock_by_sector.most_common()[-1][0]



#stock_by_sector = Counter(counter['sector'] for counter in data if counter['sector'] != 'n/a')
#print(stock_by_sector.most_common()[-1][0])

print(get_stock_symbol_with_highest_cap())