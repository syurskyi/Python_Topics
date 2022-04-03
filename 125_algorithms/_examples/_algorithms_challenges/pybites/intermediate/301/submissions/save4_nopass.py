import os
from datetime import date, timedelta, strptime
from pathlib import Path
from typing import Dict, List
from u__.r.. import u..

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    u..(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    delta = end_date - start_date
    return [start_date+timedelta(days=x) for x in range(delta.days+1)]

def _parse_date(date_string: str) -> date:
    y,m,d = date_string.split()
    return date(days=d, month=m, year=y)

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

def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    
    r_start = _parse_date(daily_rates['start_at'])
    r_end = _parse_date(daily_rates['end_at'])
    
    if start < r_start or end < r_end:
        raise ValueError('Date out of range')
    
    


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    pass