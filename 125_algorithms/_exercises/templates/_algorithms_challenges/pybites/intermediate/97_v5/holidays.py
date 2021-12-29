____ collections _______ defaultdict
_______ os
____ urllib.request _______ urlretrieve

____ bs4 _______ BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(l..)


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, features='html.parser')
    hol_list = soup.find(class_='list-table').tbody
    ___ hol __ hol_list('tr'):
        _,month,_ = hol.time.string.split('-')
        holidays[month].a..(hol.a.string.strip())
    r.. holidays
