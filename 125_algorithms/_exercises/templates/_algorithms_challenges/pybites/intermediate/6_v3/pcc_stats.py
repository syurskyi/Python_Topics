____ collections _______ Counter, namedtuple
____ itertools _______ filterfalse
_______ os
_______ urllib.request
_______ sys
# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.s..

Stats = namedtuple('Stats', 'user challenge')


# code

___ gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile) as f: lines = f.read().splitlines()

    filtered = filter(l.... x: x.split(',')[-1]__'True', lines)
    ___ line __ filtered:
        yield line.split(',')[0].lower()



___ diehard_pybites(files_ N..
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    __ files __ N..
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()
    files = l..(filterfalse(l.... x: x.split('/')[-1] __ IGNORE, files))
    users.update([f.split('/')[-1] ___ f __ files])
    popular_challenges.update([f.split('/')[0] ___ f __ files])
    print(l..(files), file=sys.stderr, flush=True)
    r.. Stats(user=users.most_common(1)[0][0],
                 challenge=(popular_challenges.most_common(1)[0][0],
                            popular_challenges.most_common(1)[0][1])
                 )
