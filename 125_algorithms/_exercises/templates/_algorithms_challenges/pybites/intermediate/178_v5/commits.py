_______ __
_______ __
____ c.. _______ Counter
____ urllib.request _______ urlretrieve
____ dateutil.parser _______ p..

commits = __.p...j..('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

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
    ##
    # Example log line:
    # Date:   Tue Mar 5 22:34:33 2019 +0100 | 2 files changed, 4 insertions(+), 4 deletions(-)
    # Groups:    (                         )                  ( )              ( )
    log_regex = __.c..(
        r'^Date: +\w+ (\w+ \d+ \d+:\d+:\d+ \d{4} [+-]\d{4}) .+ged(?:, (\d+) ins.*?)?(?:, (\d+) del.*?)?$',
        flags=__.MULTILINE)

    log = Counter()
    c = 0
    w__ o.. commit_log) __ cl:
        ___ x __ log_regex.f..(cl.read:
            c += 1
            dt = p..(x[0])
            __ year __ N.. o. year __ dt.year:
                log += Counter({(YEAR_MONTH.f..(y=dt.year, m=dt.month)): i..('0' + x[1]) - i..('0' + x[2])})
    lst = s..([(k, v) ___ k, v __ log.i..], key=l.... x: x[1])
    r.. lst[0][0], lst[-1][0]
