_______ os
_______ __
_______ urllib.request

LOG = os.path.j..('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


___ create_chart
    line_check = __.c..(r'^(\d\d-\d\d) \d\d:\d\d \w+\s+DEBUG\s+(\w*) - (.*)$')
    book = ''
    last_date = ''
    w__ open(LOG) __ log:
        ___ line __ log:
            (d,i,t) = line_check.m..(line).groups()
            __ d != last_date:
                print _*\n{d} ',end='')
                last_date = d
            __ i != '':
                book = t
            ____:
                __ t __ 'sending to slack channel':
                    print(PY_BOOK __ 'python' __ book.l.. ____ OTHER_BOOK, end='')
        print()
