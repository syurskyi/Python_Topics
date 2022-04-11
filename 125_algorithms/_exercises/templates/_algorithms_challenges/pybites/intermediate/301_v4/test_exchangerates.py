_______ j__
____ d__ _______ date

_______ p__

____ exchangerates _______ RATES_FILE, exchange_rates, get_all_days, match_daily_rates


?p__.f..(scope="session")
___ exchange_rates_result
    r.. exchange_rates()


?p__.f..(scope="session")
___ matching_result
    start date(2020, 1, 1)
    end date(2020, 9, 1)
    daily_rates j__.l.. (RATES_FILE.read_text["rates"]
    r.. match_daily_rates(start, end, daily_rates)


?p__.m__.p.(
    "start, end, expected",
    [
        (date(2020, 1, 1), date(2020, 1, 31), 31),
        (date(2020, 1, 14), date(2020, 1, 29), 16),
        (date(2020, 4, 12), date(2020, 4, 14), 3),
    ],
)
___ test_get_all_days(start, end, e..
    a.. get_all_days(start, end)
    ... l..(a..) __ e..

    ... isi..(a..[0], date)
    ... isi..(a..[-1], date)

    ... a..[0] __ start
    ... a..[-1] __ end


?p__.m__.p.(
    "date, expected",
    [
        (date(2020, 1, 18), date(2020, 1, 17,
        (date(2020, 2, 2), date(2020, 1, 31,
        (date(2020, 5, 3), date(2020, 4, 30,
        (date(2020, 8, 15), date(2020, 8, 14,
    ],
)
___ test_match_daily_rates(date, e.., matching_result
    a.. matching_result
    ... a..[date] __ e..


?p__.m__.p.(
    "testdate, expected",
    [
        (
            date(2020, 7, 16),
            {"Base Date": date(2020, 7, 16), "GBP": 0.90875, "USD": 1.1414},
        ),
        (
            date(2020, 7, 17),
            {"Base Date": date(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
        ),
        (
            date(2020, 7, 18),
            {"Base Date": date(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
        ),
    ],
)
___ test_exchange_rates_sample(testdate, e.., exchange_rates_result
    a.. exchange_rates_result

    ... a..[testdate]["Base Date"] __ e..["Base Date"]
    ... a..[testdate]["GBP"] __ e..["GBP"]
    ... a..[testdate]["USD"] __ e..["USD"]


___ test_exchange_rates_all_dates(exchange_rates_result
    ... l..(exchange_rates_result) __ 245


___ test_exchange_rates_order(exchange_rates_result
    a.. l..(exchange_rates_result.keys
    e.. s..(exchange_rates_result.keys

    ... a.. __ e..


___ test_exchange_rates_validate_start
    w__ p__.r..(V...
        exchange_rates(start_date="1950-01-01")


___ test_exchange_rates_validate_end
    w__ p__.r..(V...
        exchange_rates(end_date="2050-01-01")