______ requests

CURRENCY_CONVERSION_API_URL _ 'https://api.exchangeratesapi.io'


c_ CurrencyConvertor:
    """
    Why class? Because methods are easier to mock than functions. You mock it only for one object, not for whole class
    """

    ___ get_exchange_rate  base_currency, target_currency
        """
        :param base_currency: ISO 4217 code of base currency
        :param target_currency: ISO 4217 code of target currency
        :return how many units of target currency is one unit of base currency
        """
        resp _ requests.get('{currency_conversion_api_url}/latest?base={base}'.f..(
            base_base_currency, currency_conversion_api_url_CURRENCY_CONVERSION_API_URL))
        resp.raise_for_status()
        resp_parsed _ resp.j__()
        r_ resp_parsed['rates'][target_currency]

    ___ convert_currency  base_currency, target_currency, base_amount
        """

        :param base_currency: ISO 4217 code of base currency
        :param target_currency: ISO 4217 code of target currency
        :param base_amount: amount of target currency
        :return: amount o equivalent target currency
        """
        rate _ get_exchange_rate(base_currency, target_currency)
        r_ rate * base_amount
