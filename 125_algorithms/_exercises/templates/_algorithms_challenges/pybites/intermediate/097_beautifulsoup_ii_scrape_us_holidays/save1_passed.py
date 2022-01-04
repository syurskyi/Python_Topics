____ collections _______ defaultdict
_______ os
____ urllib.request _______ urlretrieve

____ bs4 _______ BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.j..(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) __ f:
    content = f.read()

holidays = defaultdict(l..)


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    
    soup = BeautifulSoup(content, 'html.parser')
    right_table = soup.find('table', {'class': 'list-table'})

    dates    # list
    ___ row __ right_table.findAll('time'):
        dates.a..(row.text[5:7])

    holiday    # list
    ___ row __ right_table.findAll('a'):
        holiday.a..(row.text.strip())

    l = z..(dates, holiday)

    ___ k, v __ l:
        holidays[k].a..(v)

    r.. holidays