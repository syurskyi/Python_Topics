______ requests

CURRENCY_CONVERSION_API_URL _ 'https://api.exchangeratesapi.io'


___ convert_currency(base_currency, target_currency, base_amount
    """

    :param base_currency: ISO 4217 code of base currency
    :param target_currency: ISO 4217 code of target currency
    :param base_amount: amount of target currency
    :return: amount o equivalent target currency
    """
    resp _ requests.get('{CURRENCY_CONVERSION_API_URL}/latest?base={base}'.f..(
        base_base_currency, CURRENCY_CONVERSION_API_URL_CURRENCY_CONVERSION_API_URL))
    resp.raise_for_status()
    resp_parsed _ resp.j__()
    rate _ resp_parsed['rates'][target_currency]
    r_ rate * base_amount
