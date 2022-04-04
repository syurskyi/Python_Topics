____ c.. _______ d..
_______ __
____ u__.r.. _______ u..
____ d__ _______ d__
____ bs4 _______ BeautifulSoup


# prep data
tmp = __.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = __.p...j..(tmp, page)
u..(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

w__ o.. holidays_page) __ f:
    content = f.r..

holidays = d..(l..)


___ _parse_date(date: s..
    """returns a datetime from parsing dates as formatted in table"""
    r.. d__.s..(date.s.. [0], '%Y-%m-%d%B')


___ _get_table(content=content) __ l..:
    """returns the cleaned table with datetimes for the dates"""
    soup = BeautifulSoup(content, 'html.parser')
    raw_table = soup.find('table', {'class': 'list-table'})
    table = [[c.get_text().s.. ___ c __ r.find_all('td')]
             ___ r __ raw_table.find_all('tr')]
    table.pop(0)                # remove header
    ___ row __ table:
        row[1] = _parse_date(row[1])
    r.. table


___ get_us_bank_holidays(content=content
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    table = _get_table()

    ___ row __ table:
        holidays[f'{row[1].month:02d}' .a..(row[3].strip

    r.. holidays
