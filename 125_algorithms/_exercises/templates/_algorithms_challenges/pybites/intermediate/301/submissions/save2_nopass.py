_______ __
____ d__ _______ date, t..
____ p.. _______ P..
____ t___ _______ Dict, L..
____ u__.r.. _______ u..

URL "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP P.. __.g.. "TMP", "/tmp"
RATES_FILE TMP / "exchangerates.json"

__ n.. ?.e..
    u.. ? ?


___ get_all_days start_date ? end_date ? __ L.. ?
    delta ? - ?
    r.. [start_date+t..(d.._x) ___ x __ r..(delta.days)]


___ match_daily_rates start d.. end d.. daily_rates d.. __ D.. ? ?
    p..


___ exchange_rates(
    start_date: s.. "2020-01-01", end_date: s.. "2020-09-01"
) __ Dict[date, d..]:
    p..