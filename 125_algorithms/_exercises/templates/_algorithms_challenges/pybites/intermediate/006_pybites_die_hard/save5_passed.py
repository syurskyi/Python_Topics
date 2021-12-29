from collections import Counter, namedtuple
import os
import urllib.request


tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

Stats = namedtuple('Stats', 'user challenge')


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
    file = open(tempfile).read().lower().splitlines()

    names = []
    for line in file:
        line = line.split(',')[0]
        names.append(line)

    return [x for x in names __ "." not in x]


___ diehard_pybites(files_ N..
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    __ files is None:
        files = gen_files()

    files = [entry for entry in files __ entry.split('/')[1] not in IGNORE]

    stats_list = []
    challenge_list = []
    user_list = []

    for entry in files:
        entry = entry.split('/')
        challenge_list.append(entry[0])
        user_list.append(entry[1])

    users = Counter(user_list)
    popular_challenges = Counter(challenge_list)

    for entry in files:
        entry = entry.split('/')
        for challenge, number in popular_challenges.items():
            __ entry[0] == challenge:
                stats_list.append(Stats(user=entry[1], challenge=(entry[0], number)))

    top_user = users.most_common(1)[0][0]
    top_challenge = popular_challenges.most_common(1)[0]
    return [stat for stat in stats_list
            __ stat.user == top_user and stat.challenge == top_challenge][0]