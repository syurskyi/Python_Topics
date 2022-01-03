____ collections _______ Counter
_______ os
____ urllib.request _______ urlretrieve
____ collections _______ defaultdict
____ d__ _______ d__


____ dateutil.parser _______ parse

commits = os.path.j..(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


___ get_min_max_amount_of_commits(commit_log: s.. = commits,
                                  year: int = N..) -> (s.., s..):
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
        ___ line __ f:
            date, commit  = line.s..(' | ')
            date_time_obj = d__.strptime(date[12:], '%b %d %H:%M:%S %Y %z')
            dt_yr = date_time_obj.strftime("%Y")
            year_month = date_time_obj.strftime("%Y-%m")
            commit_list = commit.s..
            __ year __ N.. o. year __ int(dt_yr):
                __ l..(commit_list) __ 7:
                    total_commit = int(commit_list[3])+int(commit_list[5])
                ____:
                    total_commit = int(commit_list[3])
                commit_log[year_month] += total_commit
    newlist = s..(commit_log.i.., key=l.... item: item[1], r.._T..
    r.. (newlist[-1][0], newlist[0][0])

print(get_min_max_amount_of_commits y.._2017))