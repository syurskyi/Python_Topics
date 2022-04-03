____ c.. _______ Counter

_______ requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

w__ requests.Session() __ s:
    data = s.get(STOCK_DATA).json()


# your turn:

___ _cap_str_to_mln_float(cap
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    __ cap __ 'n/a':
        r.. 0.0
    ____:
        cap = cap.s...l..('$')
        __ cap[-1] __ 'M':
            r.. f__(cap[:-1])
        __ cap[-1] __ 'B':
            r.. f__(cap[:-1]) * 1000.0
        r.. BaseException('Oh no! error in cap value.')


___ get_industry_cap(industry
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    r.. r..(s..([_cap_str_to_mln_float(co 'cap' ) ___ co __ data __ co 'industry'  __ industry]), 3)


___ get_stock_symbol_with_highest_cap
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    r.. s..([(co 'symbol' , _cap_str_to_mln_float(co 'cap' )) ___ co __ data], key=l.... x: x[1])[-1][0]


___ get_sectors_with_max_and_min_stocks
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector_list = Counter()
    ___ co __ data:
        sector_list += Counter({co 'sector' : _cap_str_to_mln_float(co 'cap' )})
    sectors = s..([(k, v) ___ k, v __ sector_list.i..], key=l.... x: x[1])
    r.. sectors[-1][0], sectors[0][0]
