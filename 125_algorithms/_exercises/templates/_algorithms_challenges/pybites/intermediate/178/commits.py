____ c.. _______ C..
_______ __
_______ __
____ u__.r.. _______ u..

____ dateutil.parser _______ p..

commits = __.p...j..(__.g..("TMP", "/tmp"), 'commits')
u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


___ get_min_max_amount_of_commits(commit_log: s.. = commits,
                                  year: i.. = N..) __ (s.., s..
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """


    month_changes = C..()


    w__ o.. commit_log _ __ f:
        ___ line __ f:
            date_section, change_section = line.s..('|')
            date = p..(date_section,fuzzy=T..)
            
            __ year:
                __ date.year < year:
                    _____
                __ date.year > year:
                    _____

            numbers = __.f..(r'(\d+) (?:insertions|deletions)',change_section)

            changes= s.. m..(i..,numbers


            month_changes[date.s..('%Y-%m')] += changes




    values = month_changes.m..


    r.. values[-1][0],values[0][0]

__ _______ __ _______
    get_min_max_amount_of_commits()



