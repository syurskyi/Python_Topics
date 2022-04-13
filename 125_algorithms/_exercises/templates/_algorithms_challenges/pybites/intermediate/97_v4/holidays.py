____ c.. _______ d..
_______ __
____ u__.r.. _______ u..
____ d__ _______ d__
____ ___ _______ B..


# prep data
tmp  __.g.. TMP  /tmp
page 'us_holidays.html'
holidays_page __.p...j.. ? page)
u..(
    _*https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

w__ o.. holidays_page) __ f:
    content f.r..

holidays d.. l..


___ _parse_date(date: s..
    """returns a datetime from parsing dates as formatted in table"""
    r.. d__.s..(date.s.. [0], '_Y-%m-_d%B')


___ _get_table(content=content) __ l..:
    """returns the cleaned table with datetimes for the dates"""
    soup B..(content, 'html.parser')
    raw_table ?.f.. 'table', {'class': 'list-table'})
    table [[c.g.. .s.. ___ c __ r.f.. 'td')]
             ___ r __ raw_table.f.. 'tr')]
    table.p.. 0)                # remove header
    ___ row __ table:
        row[1] _parse_date(row[1])
    r.. table


___ get_us_bank_holidays(content=content
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    table _get_table()

    ___ row __ table:
        holidays_* {row[1].month:02d}' .a..(row[3].strip

    r.. holidays
