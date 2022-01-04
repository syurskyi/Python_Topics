"""
Given a listing of files of our community branch determine who PR'd (= submitted pull request)
the most (excluding PyBites) and what challenge is the most popular (PR'd) as per snapshot of
today (8th of Dec 2017).

See preparation done in the code template below. Replace pass with your code to make the test pass.
Good luck and have fun!
"""

"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
____ c.. _______ Counter, n..
_______ os
_______ urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.j..(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

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
    w__ open(tempfile) __ infile:
        ___ line __ infile:
            chunks = line.s..(',')
            __ chunks[1].s.. __ "True":
                s = chunks[0].s..('/')
                y.. s[1]

___ diehard_pybites
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    ___ i __ gen_files
        __ i n.. __ IGNORE:
            users[i] += 1
    w__ open(tempfile) __ infile:
        ___ line __ infile:
            chunks = line.s..(',')
            __ chunks[1].s.. __ "True":
                s = chunks[0].s..('/')
                popular_challenges[s[0]] += 1
    s = Stats(users.most_common(1)[0][0], popular_challenges.most_common(1)[0])
    r.. s

diehard_pybites()