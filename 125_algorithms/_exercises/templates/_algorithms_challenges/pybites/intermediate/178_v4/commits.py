____ collections _______ Counter
_______ __
_______ os
____ urllib.request _______ urlretrieve
____ dateutil.parser _______ parse

commits = os.path.j..(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


___ _parse_line(line: s..) __ d..:
    """returns a line with the key of date type and value of add/del"""
    d_str, all_changes = line.s..(' | ')
    date = parse(__.sub(r'Date:[ ]+', '', d_str)).date()

    # add insertions and deletions
    insertions = __.f..(r'([0-9]+) insertions', all_changes)
    deletions = __.f..(r'([0-9]+) deletions', all_changes)
    changes = i..(insertions[0]) __ insertions ____ 0
    changes += i..(deletions[0]) __ deletions ____ 0
    r.. {'date': date, 'changes': changes}


___ get_min_max_amount_of_commits(commit_log: s.. = commits,
                                  year: i.. = N..) __ (s.., s..):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    commits = Counter()
    with open(commit_log) __ f:
        ___ line __ f:
            dat = _parse_line(line)
            __ dat['date'].year __ year o. year __ N..
                commits.update({dat['date'].strftime('%Y-%m'): dat['changes']})

    max = commits.most_common(1)[0][0]
    m.. = commits.most_common()[-1][0]

    r.. m.., max
