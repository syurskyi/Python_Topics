____ c.. _______ d..
_______ __
____ u__.r.. _______ u..

____ ___ _______ B..


# prep data
holidays_page __.p...j..('/tmp', 'us_holidays.php')
u..('https://bit.ly/2LG098I', holidays_page)

w__ o.. holidays_page) __ f:
    content f.r..

holidays d.. l..


___ get_us_bank_holidays(content=content
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup B..(content, features='html.parser')
    hol_list ?.f.. c.._'list-table').tbody
    ___ hol __ hol_list('tr'
        _,month,_ hol.t__.s__.s..('-')
        holidays[month].a..(hol.a.s__.s..
    r.. holidays
