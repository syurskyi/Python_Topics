"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
____ c.. _______ Counter, n..
_______ os
_______ urllib.request

# prep

tempfile = os.path.j..('/tmp', 'dirnames')
__ n.. os.path.isfile(tempfile):
    urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.s..

users, popular_challenges = Counter(), Counter()

Stats = n..('Stats', 'user challenge')


# code

___ gen_files
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    w__ open(tempfile,'rt') __ f:
        ___ row __ f.read().splitlines
            fields = row.s..(',')
            __ fields[1] __ 'False':
                continue
            fields = fields[0].s..('/')
            y.. fields


___ diehard_pybites
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    ___ pr __ gen_files
        __ pr[1] n.. __ IGNORE:
            users[pr[1]] += 1
        popular_challenges[pr[0]] += 1
    r.. Stats(user=users.most_common(1)[0][0], challenge=popular_challenges.most_common(1)[0])
