____ c.. _______ C..
_______ __
____ u__.r.. _______ u..
____ c.. _______ d..
____ d__ _______ d__


____ dateutil.parser _______ p..

commits = __.p...j..(__.getenv("TMP", "/tmp"), 'commits')
u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

year_argument = 'None'

w__ o.. commits) __ f:
    commit_log = d..(i..)
    ___ line __ f:
        #print(line)
        date, commit  = line.s..(' | ')
        date_time_obj = d__. s..(date[12:], '%b %d %H:%M:%S %Y %z')
        dt_yr = date_time_obj.s..("%Y")
        year_month = date_time_obj.s..("%Y-%m")
        __ year_argument __ 'None' o. dt_yr __ year_argument:
            commit_list = commit.s..
            __ l..(commit_list) __ 7:
                total_commit = i..(commit_list[3])+i..(commit_list[5])
            ____:
                total_commit = i..(commit_list[3])
            #print(f'{year_month} {total_commit}')
            commit_log[year_month] += total_commit
    newlist = s..(commit_log.i.., key=l.... item: item[1], r.._T..
    print(newlist[-1][0], newlist[0][0])