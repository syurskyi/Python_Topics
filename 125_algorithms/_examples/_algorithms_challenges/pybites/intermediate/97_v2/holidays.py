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


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    soup = BeautifulSoup(content,'html.parser')

    table = soup.find('table',class_="list-table")

    for i,row in enumerate(table.find_all('tr')):
        if i == 0:
            continue
        date = row.select_one('td:nth-child(2)').getText(strip=True)
        hyphen = date.index('-')
        date = date[hyphen+1:hyphen+ 3]

        holiday = row.select_one('td:nth-child(4)').getText(strip=True)
        holidays[date].append(holiday)
    

    return holidays


if __name__ == "__main__":


    get_us_bank_holidays()
