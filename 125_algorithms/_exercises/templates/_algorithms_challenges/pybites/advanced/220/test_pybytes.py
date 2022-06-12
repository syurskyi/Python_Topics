# _______ p__
#
# ____ ? _______ ? ?
#
# REAL_PYTHON "realpython.com"
# PYBITES 'pybit.es'
#
#
# ?p__.f.. s.._"module"
# ___ pb
#     r.. P..
#
#
# ___ test_get_episodes_pybites_was_mentioned pb
#     a.. ?.? P..
#     e.. =  '106', '98', '34', '26', '14'
#     ... s.. a.. __ s.. e..
#
#
# ___ test_get_episodes_realpython_was_mentioned pb
#     a.. ?.? R..
#     e.. =  '143', '134', '123', '119', '118', '114', '110', '102',
#                 '100', '97', '88', '86', '85', '84', '83', '82', '80', '76',
#                 '75', '71', '66', '56', '37', '20', '7'
#     ... s.. a.. __ s.. e..
#
#
# ___ test_number_episodes_with_special_guests pb
#     a.. ?.n..
#     e.. 17
#     ... a.. __ e..
#
#
# ___ test_number_episodes_with_special_guests_half_feed ?
#     """To prevent hardcoding the answer"""
#     org_entries ?..e..
#     ?..e.. ?..e.. |20
#     a.. ?.n..
#     e.. 7
#     ?..e.. ?  # pb is module scope so restore entries
#     ... a.. __ e..
#
#
# ___ test_get_most_mentioned_domain_names_default_top_15 pb
#     a.. ?.g..
#     e.. 'https://github.com', 120),
#                 ('https://www.youtube.com', 50),
#                 ('https://medium.com', 38),
#                 ('https://www.python.org', 26),
#                 ('https://www.reddit.com', 26),
#                 ('https://docs.python.org', 25),
#                 ('https://realpython.com', 24),
#                 ('https://hackernoon.com', 22),
#                 ('https://pypi.python.org', 20),
#                 ('https://pypi.org', 16),
#                 ('https://en.wikipedia.org', 14),
#                 ('https://pragprog.com', 13),
#                 ('https://docs.pytest.org', 11),
#                 ('http://rollbar.com', 11),
#                 ('https://dbader.org', 9
#     ... a.. __ e..
#
#
# ___ test_get_most_mentioned_domain_names_top_5 pb
#     a.. ?.g..n_5
#     e.. 'https://github.com', 120),
#                 ('https://www.youtube.com', 50),
#                 ('https://medium.com', 38),
#                 ('https://www.python.org', 26),
#                 ('https://www.reddit.com', 26
#     ... a.. __ e..
#
#
# ___ test_average_episode_duration_full_feed pb
#     a.. ?.g..
#     max_, min_ '00:56:54', '00:15:27'
#     e.. ? a.._1439 m.__? m..__?
#     # depending the way mean is calculated, results might differ
#     expected_alt ? a.._1442 m..__? m..__?
#     ... a.. __ e.. ?
#
#
# ___ test_average_episode_duration_half_feed pb
#     """To prevent hardcoding the answer"""
#     num_half_episodes i..(l..(?..e..)/2)
#     org_entries ?..e..
#     ?..e.. ?..e.. |?
#     a.. ?.g..
#     max_, min_ '00:56:54', '00:16:40'
#     e.. ? a.._1606 m.._? m.._?
#     # depending the way mean is calculated, results might differ
#     expected_alt ? a.._1607 m.._? m.._?
#     ?..e.. org_entries  # pb is module scope so restore entries
#     ... a.. __ e.. ?
