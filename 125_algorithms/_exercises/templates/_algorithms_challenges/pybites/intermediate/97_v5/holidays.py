____ c.. _______ defaultdict
_______ __
____ urllib.request _______ urlretrieve

____ bs4 _______ BeautifulSoup


# prep data
holidays_page = __.p...j..('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

w__ o.. holidays_page) __ f:
    content = f.r..

holidays = defaultdict(l..)


___ get_us_bank_holidays(content=content
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, features='html.parser')
    hol_list = soup.find(class_='list-table').tbody
    ___ hol __ hol_list('tr'
        _,month,_ = hol.time.s__.s..('-')
        holidays[month].a..(hol.a.s__.strip
    r.. holidays
