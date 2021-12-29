____ collections _______ Counter
_______ os
____ urllib.request _______ urlretrieve
____ collections _______ defaultdict
____ d__ _______ d__


____ dateutil.parser _______ parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

year_argument = 'None'

with open(commits) as f:
    commit_log = defaultdict(int)
    ___ line __ f:
        #print(line)
        date, commit  = line.s..(' | ')
        date_time_obj = d__. strptime(date[12:], '%b %d %H:%M:%S %Y %z')
        dt_yr = date_time_obj.strftime("%Y")
        year_month = date_time_obj.strftime("%Y-%m")
        __ year_argument __ 'None' o. dt_yr __ year_argument:
            commit_list = commit.s..
            __ l..(commit_list) __ 7:
                total_commit = int(commit_list[3])+int(commit_list[5])
            ____:
                total_commit = int(commit_list[3])
            #print(f'{year_month} {total_commit}')
            commit_log[year_month] += total_commit
    newlist = s..(commit_log.items(), key=l.... item: item[1], r.._T..
    print(newlist[-1][0], newlist[0][0])