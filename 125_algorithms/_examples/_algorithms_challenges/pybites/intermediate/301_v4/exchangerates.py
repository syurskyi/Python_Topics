import os
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, OrderedDict
from urllib.request import urlretrieve
import json
from collections import OrderedDict

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    delta = end_date - start_date
    return [start_date+timedelta(days=x) for x in range(delta.days+1)]


def _parse_date(date_string: str) -> date:
    return date(*map(int, date_string.split('-')))


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


def _date_conv(data: dict):
    return {_parse_date(k): v for k, v in data.items()}


def match_daily_rates(start: date,
                      end: date, daily_rates: dict) -> Dict[date, date]:
    keys = list(daily_rates.keys())
    if isinstance(keys[0], str):
        data_days = sorted(list(map(_parse_date, keys)))
    else:
        data_days = sorted(keys)

    r_start = min(data_days)
    r_end = max(data_days)

    if start < r_start or end < r_end:
        raise ValueError('Date out of range')

    days = get_all_days(start, end)
    result = {}
    for day in days:
        if day in data_days:
            match = day
        else:
            closest = min(data_days, key=lambda x: abs((x-day).days))
            if closest > day:
                match = data_days[data_days.index(closest) - 1]
            else:
                match = closest
        result[day] = match

    return result


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> OrderedDict:
    daily_rates = _date_conv(json.loads(RATES_FILE.read_text())['rates'])
    start_date, end_date = map(_parse_date, [start_date, end_date])
    if start_date < min(daily_rates.keys()) or end_date > max(daily_rates.keys()):
        raise ValueError('Date out of range for data')
    matches = match_daily_rates(start_date, end_date, daily_rates)
    result = {}
    for day, match in matches.items():
        result[day] = {"Base Date": match, **daily_rates[match]}

    return result
