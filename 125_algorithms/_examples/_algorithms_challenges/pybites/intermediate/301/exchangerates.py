import os
import json
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Dict, List
from u__.r.. import u..

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    u..(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    
    dates = []
    date_diff = (end_date - start_date).days
    current_date = start_date

    for _ in range(date_diff +1):
        dates.append(current_date)
        current_date = current_date + timedelta(days=1)

    return dates


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:

    dates_open_lookup = sorted(map(lambda x: datetime.strptime(x, "%Y-%m-%d").date(), daily_rates))

    dates = {}
    date_diff = (end - start).days
    current_date = start
    for i in range(date_diff +1):
        previous_date = current_date
        if current_date not in dates_open_lookup:
            while previous_date not in dates_open_lookup:
                previous_date = previous_date - timedelta(days=1)
            dates[current_date] = previous_date
            current_date = current_date + timedelta(days=1)
        else:
            dates[current_date] = current_date
            current_date = current_date + timedelta(days=1)

    return dates


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    
    with open(RATES_FILE) as file:
        data = json.load(file)

    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    if start < datetime.strptime(data["start_at"], "%Y-%m-%d").date() or end > datetime.strptime(data["end_at"], "%Y-%m-%d").date():
        raise ValueError("Invalid start date or end date")

    dates = match_daily_rates(start, end, data["rates"])

    result = {}
    for key, value in dates.items():
        temp_dict = {}
        date_string = value.strftime("%Y-%m-%d")
        temp_dict["Base Date"] = value
        temp_dict.update(data["rates"][date_string])
        result[key] = temp_dict #data["rates"][date_string]

    return result


# if __name__ == "__main__":
#     start_date = date(2020, 4, 9)
#     end_date = date(2020, 4, 14)
#     get_all_days(start_date, end_date)
#     print(exchange_rates("2020-04-09", "2020-04-14"))