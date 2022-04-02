____ c.. _______ defaultdict
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

w__ o.. holidays_page) __ f:
    content = f.r..

holidays = defaultdict(l..)


___ get_us_bank_holidays(content=content
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    soup = BeautifulSoup(content,'html.parser')

    table = soup.find('table',class_="list-table")

    ___ i,row __ e..(table.find_all('tr')):
        __ i __ 0:
            _____
        date = row.select_one('td:nth-child(2)').getText(strip=T..)
        hyphen = date.index('-')
        date = date[hyphen+1:hyphen+ 3]

        holiday = row.select_one('td:nth-child(4)').getText(strip=T..)
        holidays[date].a..(holiday)
    

    r.. holidays


__ _______ __ _______


    get_us_bank_holidays()
