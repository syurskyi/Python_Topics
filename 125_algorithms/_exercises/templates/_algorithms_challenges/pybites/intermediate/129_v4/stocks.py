_______ requests
____ collections _______ Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

___ _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""

    __ 'n/a' __ cap:
        value = 0
    ____:
        unit = cap[-1]
        cap = cap[1:-1]
        value = float(cap)
        value = value * 1000 __ unit __ 'B' ____ value

    r.. value


___ get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total = s..(map(l.... x: _cap_str_to_mln_float(x['cap']),
                    filter(l.... x: x['industry'] __ industry, data)
                    )
                )

    r.. round(total, 2)


___ get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    r.. max(data, key=l.... x: _cap_str_to_mln_float(x['cap']))['symbol']


___ get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    min_max = Counter(map(l.... x: x['sector'],
                          filter(l.... x: x['sector'] != 'n/a', data)
                          )
                      )
    most = min_max.most_common(1)[0][0]
    least = min_max.most_common()[-1][0]
    r.. most, least
