from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")
    holiday_table = soup.find(class_="list-table")
    holiday_dates = [h_date.get_text() for h_date in holiday_table.select("time")]
    holiday_names = [h_name.get_text() for h_name in holiday_table.select("a")]
    holiday_zip = zip(holiday_dates, holiday_names)
    for h_date, h_name in holiday_zip:
        month = h_date.split("-")[1]
        holidays[month].append(h_name.strip())
    return holidays


# if __name__ == "__main__":
#     print(get_us_bank_holidays())