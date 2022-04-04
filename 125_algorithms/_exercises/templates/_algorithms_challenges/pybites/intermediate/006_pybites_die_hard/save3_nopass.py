____ c.. _______ C.., n..
_______ __
_______ u__.r..


tmp = __.g..("TMP", "/tmp")
tempfile = __.p...j..(tmp, 'dirnames')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.s..

Stats = n..('Stats', 'user challenge')


___ gen_files(tempfile=tempfile
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
    file = o.. tempfile).r...l...s.. 

    names    # list
    ___ line __ file:
        line = line.s..(',')[0]
        names.a..(line)

    filtered1 = [x ___ x __ names __ "." n.. __ x]
    exclude = [item ___ item __ filtered1 ___ name __ IGNORE __ name __ item]

    output = [item ___ item __ filtered1 __ item n.. __ exclude]

    r.. output


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

    files = [entry ___ entry __ files __ entry.s..('/')[1] n.. __ IGNORE]
    
    stats_list    # list
    challenge_list    # list
    user_list    # list

    ___ entry __ files:
        entry = entry.s..('/')
        challenge_list.a..(entry[0])
        user_list.a..(entry[1])

    users = C..(user_list)
    popular_challenges = C..(challenge_list)

    ___ entry __ files:
        entry = entry.s..('/')
        ___ challenge, number __ popular_challenges.i..:
            __ entry[0] __ challenge:
                stats_list.a..(Stats(user=entry[1], challenge=(entry[0], number)))

    top_user = users.most_common(1)[0][0]
    top_challenge = popular_challenges.most_common(1)[0]
    r.. [stat ___ stat __ stats_list
            __ stat.user __ top_user a.. stat.challenge __ top_challenge][0]