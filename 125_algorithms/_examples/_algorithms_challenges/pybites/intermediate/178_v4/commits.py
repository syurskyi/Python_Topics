from collections import Counter
import re
import os
from u__.r.. import u..
from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def _parse_line(line: str) -> dict:
    """returns a line with the key of date type and value of add/del"""
    d_str, all_changes = line.split(' | ')
    date = parse(re.sub(r'Date:[ ]+', '', d_str)).date()

    # add insertions and deletions
    insertions = re.findall(r'([0-9]+) insertions', all_changes)
    deletions = re.findall(r'([0-9]+) deletions', all_changes)
    changes = int(insertions[0]) if insertions else 0
    changes += int(deletions[0]) if deletions else 0
    return {'date': date, 'changes': changes}


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    commits = Counter()
    with open(commit_log) as f:
        for line in f:
            dat = _parse_line(line)
            if dat['date'].year == year or year is None:
                commits.update({dat['date'].strftime('%Y-%m'): dat['changes']})

    max = commits.most_common(1)[0][0]
    min = commits.most_common()[-1][0]

    return min, max
