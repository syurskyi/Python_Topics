import os
from datetime import date, timedelta
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


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    pass


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    pass