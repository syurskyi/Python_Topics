from collections import Counter
import os
from urllib.request import urlretrieve
from collections import defaultdict
from datetime import datetime


from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    print(f'year argument is {year}')
    commit_log = defaultdict(int)
    with open(commits) as f:
        for line in f:
            date, commit  = line.split(' | ')
            date_time_obj = datetime.strptime(date[12:], '%b %d %H:%M:%S %Y %z')
            dt_yr = date_time_obj.strftime("%Y")
            year_month = date_time_obj.strftime("%Y-%m")
            commit_list = commit.split()
            if year == None or year == int(dt_yr):
                if len(commit_list) == 7:
                    total_commit = int(commit_list[3])+int(commit_list[5])
                else:
                    total_commit = int(commit_list[3])
                commit_log[year_month] += total_commit
    newlist = sorted(commit_log.items(), key=lambda item: item[1], reverse=True)
    return (newlist[-1][0], newlist[0][0])

print(get_min_max_amount_of_commits(year=2017))