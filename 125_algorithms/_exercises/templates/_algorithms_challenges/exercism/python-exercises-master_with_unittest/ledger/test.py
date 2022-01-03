# -*- coding: utf-8 -*-
_______ unittest

____ ledger _______ format_entries, create_entry


c_ LedgerTest(unittest.TestCase):
    maxDiff = 5000

    ___ test_empty_ledger
        currency = 'USD'
        locale = 'en_US'
        entries    # list
        expected = 'Date       | Description               | Change       '
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_one_entry
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_credit_and_debit
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-02', 'Get present', 1000),
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
            '01/02/2015 | Get present               |       $10.00 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_multiple_entries_on_same_date_ordered_by_description
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-02', 'Get present', 1000),
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '01/01/2015 | Buy present               |      ($10.00)',
            '01/02/2015 | Get present               |       $10.00 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_final_order_tie_breaker_is_change
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Something', 0),
            create_entry('2015-01-01', 'Something', -1),
            create_entry('2015-01-01', 'Something', 1),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '01/01/2015 | Something                 |       ($0.01)',
            '01/01/2015 | Something                 |        $0.00 ',
            '01/01/2015 | Something                 |        $0.01 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_overlong_description
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Freude schoner Gotterfunken', -123456),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '01/01/2015 | Freude schoner Gotterf... |   ($1,234.56)',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_euros
        currency = 'EUR'
        locale = 'en_US'
        entries = [
            create_entry('2015-01-01', 'Buy present', -1000),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            u'01/01/2015 | Buy present               |      (€10.00)',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_dutch_locale
        currency = 'USD'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', 123456),
        ]
        expected = '\n'.j..([
            'Datum      | Omschrijving              | Verandering  ',
            '12-03-2015 | Buy present               |   $ 1.234,56 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_dutch_locale_and_euros
        currency = 'EUR'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', 123456),
        ]
        expected = '\n'.j..([
            'Datum      | Omschrijving              | Verandering  ',
            u'12-03-2015 | Buy present               |   € 1.234,56 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_dutch_negative_number_with_3_digits_before_decimal_point
        currency = 'USD'
        locale = 'nl_NL'
        entries = [
            create_entry('2015-03-12', 'Buy present', -12345),
        ]
        expected = '\n'.j..([
            'Datum      | Omschrijving              | Verandering  ',
            '12-03-2015 | Buy present               |    $ -123,45 ',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)

    ___ test_american_negative_number_with_3_digits_before_decimal_point
        currency = 'USD'
        locale = 'en_US'
        entries = [
            create_entry('2015-03-12', 'Buy present', -12345),
        ]
        expected = '\n'.j..([
            'Date       | Description               | Change       ',
            '03/12/2015 | Buy present               |     ($123.45)',
        ])
        assertEqual(format_entries(currency, locale, entries), expected)


__ __name__ __ '__main__':
    unittest.main()
