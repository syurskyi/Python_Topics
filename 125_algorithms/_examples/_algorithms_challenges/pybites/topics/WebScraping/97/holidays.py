from collections import defaultdict
import os
from urllib.request import urlretrieve

#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as Soup


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
    soup = Soup(content, 'html.parser')
    table = soup.find('table', class_='list-table')
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if len(row):
            #print(row[1][6:8], row[3].strip())
            holidays[row[1][6:8]].append(row[3].strip())
    return holidays
    
#day = get_us_bank_holidays()

#print('>{}<'.format({day['02'][0]}))