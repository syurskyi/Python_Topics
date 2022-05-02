_______ __
____ d__ _______ d__, t..
____ p.. _______ P..
____ t___ _______ D.., L..
____ u__.r.. _______ u..

URL "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP P.. __.g.. "TMP", "/tmp"
RATES_FILE TMP / "exchangerates.json"

__ n.. ?.e..
    u.. ? ?


___ get_all_days start_date ? end_date ? __ L.. ?
    delta ? - ?
    r..  ?+t.. d.._x ___ ? __ r.. ?.d.. +1

___ _parse_date date_string s.. __ d..
    y,m,d date_string.s..
    r.. date(d.._d,  m.._m, year=y)

"""{
    "start_at": "2019-01-01",
    "end_at": "2020-09-01",
    "base": "EUR",
    "rates": {
        "2019-06-28": {
            "USD": 1.138,
            "GBP": 0.89655
        },
        "2020-05-19": {
            "USD": 1.095,
            "GBP": 0.89535
        },
        "...": {}
    }
}"""

___ match_daily_rates start d.. end d.. daily_rates d.. __ D.. ? ?
    
    r_start _parse_date(daily_rates 'start_at' )
    r_end _parse_date(daily_rates 'end_at' )
    
    __ start < r_start o. end < r_end:
        r.. V...('Date out of range')
    
    


___ exchange_rates(
    start_date: s.. "2020-01-01", end_date: s.. "2020-09-01"
) __ Dict[date, d..]:
    p..