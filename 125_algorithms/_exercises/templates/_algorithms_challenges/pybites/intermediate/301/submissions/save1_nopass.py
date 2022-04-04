_______ __
____ d__ _______ date, t..
____ pathlib _______ Path
____ t___ _______ Dict, L..
____ u__.r.. _______ u..

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(__.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

__ n.. RATES_FILE.exists
    u..(URL, RATES_FILE)


___ get_all_days(start_date: date, end_date: date) __ L..[date]:
    delta = end_date - start_date
    r.. [start_date()+t..(d.._x) ___ x __ r..(delta.days)]


___ match_daily_rates(start: date, end: date, daily_rates: d..) __ Dict[date, date]:
    p..


___ exchange_rates(
    start_date: s.. = "2020-01-01", end_date: s.. = "2020-09-01"
) __ Dict[date, d..]:
    p..