_______ os
_______ re
_______ urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


___ create_chart():
    line_check = re.compile(r'^(\d\d-\d\d) \d\d:\d\d \w+\s+DEBUG\s+(\w*) - (.*)$')
    book = ''
    last_date = ''
    with open(LOG) as log:
        ___ line __ log:
            (d,i,t) = line_check.match(line).groups()
            __ d != last_date:
                print(f'\n{d} ',end='')
                last_date = d
            __ i != '':
                book = t
            ____:
                __ t __ 'sending to slack channel':
                    print(PY_BOOK __ 'python' __ book.lower() ____ OTHER_BOOK, end='')
        print()
