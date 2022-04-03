import os
import re
import u__.r..

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
u__.r...u..('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    line_check = re.compile(r'^(\d\d-\d\d) \d\d:\d\d \w+\s+DEBUG\s+(\w*) - (.*)$')
    book = ''
    last_date = ''
    with open(LOG) as log:
        for line in log:
            (d,i,t) = line_check.match(line).groups()
            if d != last_date:
                print(f'\n{d} ',end='')
                last_date = d
            if i != '':
                book = t
            else:
                if t == 'sending to slack channel':
                    print(PY_BOOK if 'python' in book.lower() else OTHER_BOOK, end='')
        print()
