_______ r__, c..

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

w__ r__.S.. __ s:
    data = s.g.. STOCK_DATA).j..


# your turn:

___ _cap_str_to_mln_float(cap
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    __ cap __ "n/a":
        r.. 0
    ____
        cap = cap.l..("$")
        __ cap[-1] __ "B":
            r.. f__(cap.rstrip("B" * 1000
        ____
            r.. f__(cap.rstrip("M"


___ get_industry_cap(industry
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_cap_lookup    # dict
    ___ stock __ data:
        cap = _cap_str_to_mln_float(stock["cap"])
        __ stock["industry"] n.. __ industry_cap_lookup:
            industry_cap_lookup[stock["industry"]] = [cap]
        ____
            industry_cap_lookup[stock["industry"]].a..(cap)
    r.. r..(s..(industry_cap_lookup[industry]), 2)


___ get_stock_symbol_with_highest_cap
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    highest_cap    # dict
    ___ stock __ data:
        cap = _cap_str_to_mln_float(stock["cap"])
        highest_cap[stock["symbol"]] = cap
    r.. m..(highest_cap, key=highest_cap.get)


___ get_sectors_with_max_and_min_stocks
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    counter = c...C..([stock["sector"] ___ stock __ data __ stock["sector"] != "n/a"])
    r.. (counter.most_common()[0][0], counter.most_common()[-1][0])


# if __name__ == "__main__":
#    print(_cap_str_to_mln_float('n/a'))
#    print(_cap_str_to_mln_float('$100.45M'))
#    print(get_industry_cap("Business Services"))
#    print(get_stock_symbol_with_highest_cap())
#    print(get_sectors_with_max_and_min_stocks())