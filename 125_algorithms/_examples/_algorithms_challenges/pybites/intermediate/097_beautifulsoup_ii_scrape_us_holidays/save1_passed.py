from collections import defaultdict
import os
from u__.r.. import u..

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
u..(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    
    soup = BeautifulSoup(content, 'html.parser')
    right_table = soup.find('table', {'class': 'list-table'})

    dates = []
    for row in right_table.findAll('time'):
        dates.append(row.text[5:7])

    holiday = []
    for row in right_table.findAll('a'):
        holiday.append(row.text.strip())

    l = zip(dates, holiday)

    for k, v in l:
        holidays[k].append(v)

    return holidays