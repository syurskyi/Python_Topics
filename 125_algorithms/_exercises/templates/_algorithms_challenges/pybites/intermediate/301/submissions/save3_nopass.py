_______ os
____ datetime _______ date, timedelta
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
    r.. [start_date+timedelta(days=x) ___ x __ r..(delta.days+1)]


___ match_daily_rates(start: date, end: date, daily_rates: d..) -> Dict[date, date]:
    pass


___ exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, d..]:
    pass