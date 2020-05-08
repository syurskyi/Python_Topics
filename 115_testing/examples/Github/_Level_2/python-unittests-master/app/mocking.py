import requests

CURRENCY_CONVERSION_API_URL = 'https://api.exchangeratesapi.io'


def convert_currency(base_currency, target_currency, base_amount):
    """

    :param base_currency: ISO 4217 code of base currency
    :param target_currency: ISO 4217 code of target currency
    :param base_amount: amount of target currency
    :return: amount o equivalent target currency
    """
    resp = requests.get('{CURRENCY_CONVERSION_API_URL}/latest?base={base}'.format(
        base=base_currency, CURRENCY_CONVERSION_API_URL=CURRENCY_CONVERSION_API_URL))
    resp.raise_for_status()
    resp_parsed = resp.json()
    rate = resp_parsed['rates'][target_currency]
    return rate * base_amount
