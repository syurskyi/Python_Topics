import unittest
import requests_mock

from app.mocking import convert_currency, CURRENCY_CONVERSION_API_URL


class TestCurrency(unittest.TestCase):
    def test_convert_currency__without_mocking(self):
        result = convert_currency('EUR', 'CZK', 100)
        self.assertIsInstance(result, float)

    def test_convert_currency__mocking(self):
        mocked_response = """
        {
            "base":"EUR",
            "date":"2018-06-27",
            "rates":{
                "AUD":1.5725,
                "BGN":1.9558,
                "BRL":4.4152,
                "CAD":1.5443,
                "CHF":1.1536,
                "CNY":7.6649,
                "CZK":25.777
            }
        }
        """

        with requests_mock.mock() as m:
            m.get('{CURRENCY_CONVERSION_API_URL}/latest?base=EUR'.format(
                CURRENCY_CONVERSION_API_URL=CURRENCY_CONVERSION_API_URL), text=mocked_response)
            result = convert_currency('EUR', 'CZK', 100)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 2577.7)
