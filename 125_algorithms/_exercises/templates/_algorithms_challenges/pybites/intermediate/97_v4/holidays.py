____ collections _______ defaultdict
_______ os
____ urllib.request _______ urlretrieve
____ d__ _______ d__
____ bs4 _______ BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.j..(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(l..)


___ _parse_date(date: s..):
    """returns a datetime from parsing dates as formatted in table"""
    r.. d__.strptime(date.s.. [0], '%Y-%m-%d%B')


___ _get_table(content=content) -> l..:
    """returns the cleaned table with datetimes for the dates"""
    soup = BeautifulSoup(content, 'html.parser')
    raw_table = soup.find('table', {'class': 'list-table'})
    table = [[c.get_text().s.. ___ c __ r.find_all('td')]
             ___ r __ raw_table.find_all('tr')]
    table.pop(0)                # remove header
    ___ row __ table:
        row[1] = _parse_date(row[1])
    r.. table


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    table = _get_table()

    ___ row __ table:
        holidays[f'{row[1].month:02d}'].a..(row[3].strip())

    r.. holidays
