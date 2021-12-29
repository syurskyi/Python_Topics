_______ os
____ d__ _______ date, t..
____ pathlib _______ Path
____ typing _______ Dict, List
____ urllib.request _______ urlretrieve

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

__ n.. RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


___ get_all_days(start_date: date, end_date: date) -> List[date]:
    delta = end_date - start_date
    r.. [start_date+t..(days=x) ___ x __ r..(delta.days+1)]

___ _parse_date(date_string: s..) -> date:
    y,m,d = date_string.s.. 
    r.. date(days=d,  m.._m, year=y)

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

___ match_daily_rates(start: date, end: date, daily_rates: d..) -> Dict[date, date]:
    
    r_start = _parse_date(daily_rates['start_at'])
    r_end = _parse_date(daily_rates['end_at'])
    
    __ start < r_start o. end < r_end:
        raise ValueError('Date out of range')
    
    


___ exchange_rates(
    start_date: s.. = "2020-01-01", end_date: s.. = "2020-09-01"
) -> Dict[date, d..]:
    pass