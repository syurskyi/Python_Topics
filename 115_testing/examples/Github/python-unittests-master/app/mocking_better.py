import requests

CURRENCY_CONVERSION_API_URL = 'https://api.exchangeratesapi.io'


class CurrencyConvertor:
    """
    Why class? Because methods are easier to mock than functions. You mock it only for one object, not for whole class
    """

    def get_exchange_rate(self, base_currency, target_currency):
        """
        :param base_currency: ISO 4217 code of base currency
        :param target_currency: ISO 4217 code of target currency
        :return how many units of target currency is one unit of base currency
        """
        resp = requests.get('{currency_conversion_api_url}/latest?base={base}'.format(
            base=base_currency, currency_conversion_api_url=CURRENCY_CONVERSION_API_URL))
        resp.raise_for_status()
        resp_parsed = resp.json()
        return resp_parsed['rates'][target_currency]

    def convert_currency(self, base_currency, target_currency, base_amount):
        """

        :param base_currency: ISO 4217 code of base currency
        :param target_currency: ISO 4217 code of target currency
        :param base_amount: amount of target currency
        :return: amount o equivalent target currency
        """
        rate = self.get_exchange_rate(base_currency, target_currency)
        return rate * base_amount
