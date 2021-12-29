_______ os
_______ re
_______ urllib.request
____ collections _______ defaultdict
____ d__ _______ d__

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


___ _parse_book_line(line):
    """returns a dict representing the line"""
    out_dict = d..()
    date = re.findall(r'^([0-9]{2}-[0-9]{2})', line)[0]
    out_dict['date'] = d__.strptime(date, '%m-%d')
    out_dict['title'] = re.findall(r'DEBUG.*- (.*)', line)[0]
    r.. out_dict


___ create_chart():

    chart = defaultdict(s..)
    with open(SAFARI_LOGS, 'r') as f:
        prev = f.readline()
        ___ line __ f:
            __ 'sending to slack channel' __ line:
                detail = _parse_book_line(prev)
                char = PY_BOOK __ 'python' __ detail['title'].lower() ____ '.'
                chart[detail['date']] += char

            prev = line

    ___ key __ s..(chart.keys()):
        print('{} {}'.f..(key.strftime('%m-%d'), chart[key]))
