____ c.. _______ Counter
_______ os
_______ __
____ urllib.request _______ urlretrieve

____ dateutil.parser _______ p..

commits = os.path.j..(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


___ get_min_max_amount_of_commits(commit_log: s.. = commits,
                                  year: i.. = N..) __ (s.., s..):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """


    month_changes = Counter()


    w__ open(commit_log,'r') __ f:
        ___ line __ f:
            date_section, change_section = line.s..('|')
            date = p..(date_section,fuzzy=T..)
            
            __ year:
                __ date.year < year:
                    _____
                __ date.year > year:
                    _____

            numbers = __.f..(r'(\d+) (?:insertions|deletions)',change_section)

            changes= s..(map(i..,numbers))


            month_changes[date.strftime('%Y-%m')] += changes




    values = month_changes.most_common()


    r.. values[-1][0],values[0][0]

__ _______ __ _______
    get_min_max_amount_of_commits()



