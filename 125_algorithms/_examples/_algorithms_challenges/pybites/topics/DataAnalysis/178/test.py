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

year_argument = 'None'

with open(commits) as f:
    commit_log = defaultdict(int)
    for line in f:
        #print(line)
        date, commit  = line.split(' | ')
        date_time_obj = datetime. strptime(date[12:], '%b %d %H:%M:%S %Y %z')
        dt_yr = date_time_obj.strftime("%Y")
        year_month = date_time_obj.strftime("%Y-%m")
        if year_argument == 'None' or dt_yr == year_argument:
            commit_list = commit.split()
            if len(commit_list) == 7:
                total_commit = int(commit_list[3])+int(commit_list[5])
            else:
                total_commit = int(commit_list[3])
            #print(f'{year_month} {total_commit}')
            commit_log[year_month] += total_commit
    newlist = sorted(commit_log.items(), key=lambda item: item[1], reverse=True)
    print(newlist[-1][0], newlist[0][0])