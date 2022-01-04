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

w__ open(holidays_page) __ f:
    content = f.read()

holidays = defaultdict(l..)


___ get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")
    holiday_table = soup.find(class_="list-table")
    holiday_dates = [h_date.get_text() ___ h_date __ holiday_table.select("time")]
    holiday_names = [h_name.get_text() ___ h_name __ holiday_table.select("a")]
    holiday_zip = z..(holiday_dates, holiday_names)
    ___ h_date, h_name __ holiday_zip:
        month = h_date.s..("-")[1]
        holidays[month].a..(h_name.strip())
    r.. holidays


# if __name__ == "__main__":
#     print(get_us_bank_holidays())