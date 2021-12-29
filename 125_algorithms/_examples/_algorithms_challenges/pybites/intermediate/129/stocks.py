import requests, collections

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
    if cap == "n/a":
        return 0
    else:
        cap = cap.lstrip("$")
        if cap[-1] == "B":
            return float(cap.rstrip("B")) * 1000
        else:
            return float(cap.rstrip("M"))


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_cap_lookup = {}
    for stock in data:
        cap = _cap_str_to_mln_float(stock["cap"])
        if stock["industry"] not in industry_cap_lookup:
            industry_cap_lookup[stock["industry"]] = [cap]
        else:
            industry_cap_lookup[stock["industry"]].append(cap)
    return round(sum(industry_cap_lookup[industry]), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    highest_cap = {}
    for stock in data:
        cap = _cap_str_to_mln_float(stock["cap"])
        highest_cap[stock["symbol"]] = cap
    return max(highest_cap, key=highest_cap.get)


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    counter = collections.Counter([stock["sector"] for stock in data if stock["sector"] != "n/a"])
    return (counter.most_common()[0][0], counter.most_common()[-1][0])


# if __name__ == "__main__":
#    print(_cap_str_to_mln_float('n/a'))
#    print(_cap_str_to_mln_float('$100.45M'))
#    print(get_industry_cap("Business Services"))
#    print(get_stock_symbol_with_highest_cap())
#    print(get_sectors_with_max_and_min_stocks())