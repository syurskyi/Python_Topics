from collections import Counter, namedtuple
import os
import u__.r..

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files(tempfile=tempfile):
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
    with open(tempfile) as file:
        data = file.r..

        for row in data:
            current = row.strip("\n").split(",")
            if current[1] == 'True':
                yield current[0].lower()


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    # your code
    for row in files:
        challenge, user = row.split("/")
        if user in IGNORE:
            continue
        else:
            users.update([user])
            popular_challenges.update([challenge])

    return Stats(users.most_common()[0][0], (popular_challenges.most_common()[0][0], popular_challenges.most_common()[0][1]))


# if __name__ == "__main__":
#     files=[
#             "22/wonderfulboyx",
#             "25/bbelderbos",  # ignored
#             "25/clamytoe",
#             "21/wonderfulboyx",
#             "25/santiagobenitez",
#             "23/santiagobenitez",
#             "07/santiagobenitez"
#         ]
#     print(diehard_pybites(files))