_______ p__

____ pybytes _______ Duration, PythonBytes

REAL_PYTHON "realpython.com"
PYBITES 'pybit.es'


?p__.f.. s.._"module"
___ pb
    r.. PythonBytes()


___ test_get_episodes_pybites_was_mentioned(pb
    a.. pb.get_episode_numbers_for_mentioned_domain(PYBITES)
    e.. =  '106', '98', '34', '26', '14'
    ... s..(a..) __ s..(e..)


___ test_get_episodes_realpython_was_mentioned(pb
    a.. pb.get_episode_numbers_for_mentioned_domain(REAL_PYTHON)
    e.. =  '143', '134', '123', '119', '118', '114', '110', '102',
                '100', '97', '88', '86', '85', '84', '83', '82', '80', '76',
                '75', '71', '66', '56', '37', '20', '7'
    ... s..(a..) __ s..(e..)


___ test_number_episodes_with_special_guests(pb
    a.. pb.number_episodes_with_special_guest()
    e.. 17
    ... a.. __ e..


___ test_number_episodes_with_special_guests_half_feed(pb
    """To prevent hardcoding the answer"""
    org_entries pb.entries
    pb.entries pb.entries[:20]
    a.. pb.number_episodes_with_special_guest()
    e.. 7
    pb.entries org_entries  # pb is module scope so restore entries
    ... a.. __ e..


___ test_get_most_mentioned_domain_names_default_top_15(pb
    a.. pb.get_most_mentioned_domain_names()
    e.. [('https://github.com', 120),
                ('https://www.youtube.com', 50),
                ('https://medium.com', 38),
                ('https://www.python.org', 26),
                ('https://www.reddit.com', 26),
                ('https://docs.python.org', 25),
                ('https://realpython.com', 24),
                ('https://hackernoon.com', 22),
                ('https://pypi.python.org', 20),
                ('https://pypi.org', 16),
                ('https://en.wikipedia.org', 14),
                ('https://pragprog.com', 13),
                ('https://docs.pytest.org', 11),
                ('http://rollbar.com', 11),
                ('https://dbader.org', 9)]
    ... a.. __ e..


___ test_get_most_mentioned_domain_names_top_5(pb
    a.. pb.get_most_mentioned_domain_names(n=5)
    e.. [('https://github.com', 120),
                ('https://www.youtube.com', 50),
                ('https://medium.com', 38),
                ('https://www.python.org', 26),
                ('https://www.reddit.com', 26)]
    ... a.. __ e..


___ test_average_episode_duration_full_feed(pb
    a.. pb.get_average_duration_episode_in_seconds()
    max_, min_ '00:56:54', '00:15:27'
    e.. Duration(avg=1439, max_=max_, min_=min_)
    # depending the way mean is calculated, results might differ
    expected_alt Duration(avg=1442, max_=max_, min_=min_)
    ... a.. __ (e.., expected_alt)


___ test_average_episode_duration_half_feed(pb
    """To prevent hardcoding the answer"""
    num_half_episodes i..(l..(pb.entries)/2)
    org_entries pb.entries
    pb.entries pb.entries[:num_half_episodes]
    a.. pb.get_average_duration_episode_in_seconds()
    max_, min_ '00:56:54', '00:16:40'
    e.. Duration(avg=1606, max_=max_, min_=min_)
    # depending the way mean is calculated, results might differ
    expected_alt Duration(avg=1607, max_=max_, min_=min_)
    pb.entries org_entries  # pb is module scope so restore entries
    ... a.. __ (e.., expected_alt)
