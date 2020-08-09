#!python3
#exchante_rates.py is a script to list out current exchange rates for all currencies

______ requests
______ json

API_URL = "https://openexchangerates.org/api/latest.json?app_id="
API_KEY = "<INSERT YOUR APP ID KEY HERE>"

___ get_json(
    r_ requests.get(API_URL + API_KEY).json()

___ exchange_rates(data
    rates = data['rates']
    print("US$1.00 currently buys:")
    ___ k, v in rates.items(
        print("{}: {}".format(k, v))

__ __name__ __ "__main__":
    data = get_json()
    exchange_rates(data)
