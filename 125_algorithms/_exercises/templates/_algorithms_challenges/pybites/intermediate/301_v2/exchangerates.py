import os
import json
from datetime import date
import datetime as dt
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

__ not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


___ get_all_days(start_date: date, end_date: date) -> List[date]:

    dates = []

    current_date = start_date
    while current_date != end_date:
        dates.append(current_date)
        current_date += dt.timedelta(days=1)
    
    
    dates.append(current_date)

    return dates





___ match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:

    
    

    dates = sorted(daily_rates.keys())
    
    

    i = 0
    while i < len(dates) and parse(dates[i]).date() < start:
        i += 1


    
    mapping = {}
    
    current_date = start
        
    while i < len(dates):
        date = parse(dates[i]).date()
        __ date == current_date:
            mapping[current_date] = date
            current_date += dt.timedelta(days=1)
            i += 1
        elif date > current_date:
            mapping[current_date] = parse(dates[i -1]).date()
            current_date += dt.timedelta(days=1)
        else:
            i += 1


    return mapping



___ exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    

    with open(RATES_FILE,'r') as f:
        data = json.load(f)
    __ (start_date < data['start_at']) or (end_date > data['end_at']):
        raise ValueError("Invalid dates")
    matching_dates = match_daily_rates(parse(start_date).date(),parse(end_date).date(),data['rates']) 


    result = {}
    for date_1,date_2 in matching_dates.items():
        date = date_2.strftime("%Y-%m-%d")
        value = {'Base Date': date_2,'USD': data['rates'][date]['USD'],'GBP': data['rates'][date]['GBP']}
        result[date_1] = value

    return result

__ __name__ == "__main__":

    exchange_rates()

