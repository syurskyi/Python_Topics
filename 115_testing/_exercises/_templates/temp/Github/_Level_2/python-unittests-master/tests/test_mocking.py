______ unittest
______ requests_mock

____ app.mocking ______ convert_currency, CURRENCY_CONVERSION_API_URL


c_ TestCurrency(unittest.TestCase):
    ___ test_convert_currency__without_mocking
        result _ convert_currency('EUR', 'CZK', 100)
        assertIsInstance(result, float)

    ___ test_convert_currency__mocking
        mocked_response _ """
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
            m.get('{CURRENCY_CONVERSION_API_URL}/latest?base=EUR'.f..(
                CURRENCY_CONVERSION_API_URL_CURRENCY_CONVERSION_API_URL), text_mocked_response)
            result _ convert_currency('EUR', 'CZK', 100)
        assertIsInstance(result, float)
        assertAlmostEqual(result, 2577.7)
