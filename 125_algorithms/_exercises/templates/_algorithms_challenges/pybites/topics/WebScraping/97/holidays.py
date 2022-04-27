____ c.. _______ d..
_______ __
____ u__.r.. _______ u..

#from bs4 import BeautifulSoup
____ ___ _______ B.. __ S..


# prep data
tmp  __.g.. TMP  /tmp
page 'us_holidays.html'
holidays_page __.p...j.. ? ?
u..(
    _*https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

w__ o.. ? __ f
    content f.r..

holidays d.. l..


___ get_us_bank_holidays(content_?
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup S.. ? html.parser
    table ?.f.. 'table', c.._'list-table')
    table_rows table.f.. 'tr')
    ___ tr __ table_rows:
        td tr.f.. 'td')
        row [i.text ___ i __ td]
        __ l..(row
            #print(row[1][6:8], row[3].strip())
            holidays[row[1][6:8]].a..(row[3].s..
    r.. holidays
    
#day = get_us_bank_holidays()

#print('>{}<'.format({day['02'][0]}))