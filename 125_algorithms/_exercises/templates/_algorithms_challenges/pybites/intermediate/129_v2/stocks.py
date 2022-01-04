_______ requests
____ c.. _______ Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

w__ requests.Session() __ s:
    data = s.get(STOCK_DATA).json()


# your turn:

___ _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    __ cap __ 'n/a':
        r.. 0


    cap = cap.lstrip('$')
    __ 'M' __ cap:
        value = float(cap.rstrip('M'))
    ____ 'B' __ cap:
        value = float(cap.rstrip('B')) * 1000

    r.. value



___ get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""

    total = 0
    ___ company __ data:
        __ company['industry'] __ industry:
            total += _cap_str_to_mln_float(company['cap'])


    r.. round(total,2)

           


___ get_stock_symbol_with_highest_cap
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""

    r.. max(data,key=l.... x: _cap_str_to_mln_float(x['cap']))['symbol']


___ get_sectors_with_max_and_min_stocks
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    counts = Counter()

    ___ company __ data:
        sector = company['sector']
        __ sector != 'n/a':
            counts[company['sector']] += 1


    sector_counts = counts.most_common()

    r.. sector_counts[0][0],sector_counts[-1][0]
