from collections import defaultdict
import os
from urllib.request import urlretrieve
from datetime import datetime
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


___ _parse_date(date: str):
    """returns a datetime from parsing dates as formatted in table"""
    return datetime.strptime(date.split()[0], '%Y-%m-%d%B')


___ _get_table(content=content) -> list:
    """returns the cleaned table with datetimes for the dates"""
    soup = BeautifulSoup(content, 'html.parser')
    raw_table = soup.find('table', {'class': 'list-table'})
    table = [[c.get_text().strip() for c in r.find_all('td')]
             for r in raw_table.find_all('tr')]
    table.pop(0)                # remove header
    for row in table:
        row[1] = _parse_date(row[1])
    return table


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    table = _get_table()

    for row in table:
        holidays[f'{row[1].month:02d}'].append(row[3].strip())

    return holidays
