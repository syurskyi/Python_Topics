import os
import re
import u__.r..
from collections import defaultdict
from datetime import datetime

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

u__.r...u..(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def _parse_book_line(line):
    """returns a dict representing the line"""
    out_dict = dict()
    date = re.findall(r'^([0-9]{2}-[0-9]{2})', line)[0]
    out_dict['date'] = datetime.strptime(date, '%m-%d')
    out_dict['title'] = re.findall(r'DEBUG.*- (.*)', line)[0]
    return out_dict


def create_chart():

    chart = defaultdict(str)
    with open(SAFARI_LOGS, 'r') as f:
        prev = f.readline()
        for line in f:
            if 'sending to slack channel' in line:
                detail = _parse_book_line(prev)
                char = PY_BOOK if 'python' in detail['title'].lower() else '.'
                chart[detail['date']] += char

            prev = line

    for key in sorted(chart.keys()):
        print('{} {}'.format(key.strftime('%m-%d'), chart[key]))
