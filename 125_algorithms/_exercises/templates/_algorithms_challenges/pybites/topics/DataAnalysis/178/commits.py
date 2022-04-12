____ c.. _______ C..
_______ __
____ u__.r.. _______ u..
____ c.. _______ d..
____ d__ _______ d__


____ dateutil.parser _______ p..

commits __.p...j..(__.g.. TMP  /tmp, 'commits')
u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH '{y}-{m:02d}'


___ get_min_max_amount_of_commits(commit_log: s.. commits,
                                  year: i.. N..) __ (s.., s..
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    print _*year argument is {year}')
    commit_log d..(i..)
    w__ o.. commits) __ f:
        ___ line __ f:
            date, commit  = line.s..(' | ')
            date_time_obj d__.s..(date[12:], '_b _d _H|_M:_S _Y _z')
            dt_yr date_time_obj.s..("_Y")
            year_month date_time_obj.s.. _Y-_m
            commit_list commit.s..
            __ year __ N.. o. year __ i..(dt_yr
                __ l..(commit_list) __ 7:
                    total_commit i..(commit_list[3])+i..(commit_list[5])
                ____
                    total_commit i..(commit_list[3])
                commit_log[year_month] += total_commit
    newlist s..(commit_log.i.., k.._l.... item: item[1], r.._T..
    r.. (newlist[-1][0], newlist 0 0 )

print(get_min_max_amount_of_commits y.._2017