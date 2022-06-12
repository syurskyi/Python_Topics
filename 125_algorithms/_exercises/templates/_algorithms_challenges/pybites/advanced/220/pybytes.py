# ____ c.. _______ n.., C..
# _______ __
# ____ t___ _______ N..
#
# _______ f..
#
# SPECIAL_GUEST 'Special guest'
#
# # using _ as min/max are builtins
# Duration n..('Duration', 'avg max_ min_')
#
# # static copy, original: https://pythonbytes.fm/episodes/rss
# URL 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
# IGNORE_DOMAINS {'https://pythonbytes.fm', 'http://pythonbytes.fm',
#                   'https://twitter.com', 'https://training.talkpython.fm',
#                   'https://talkpython.fm', 'http://testandcode.com'}
#
#
# c_ PythonBytes
#
#     ___ -  url_URL
#         """Load the feed url into self.entries using the feedparser module."""
#         entries f__.p.. ? entries
#
#
#     ___ get_episode_numbers_for_mentioned_domain  domain s.. __ l..
#         """Return a list of episode IDs (itunes_episode attribute) of the
#            episodes the pass in domain was mentioned in.
#         """
#
#         episode_ids    # list
#
#
#         ___ entry __ ?
#             #summary = entry['summary']
#             summary ? ?
#             __ d.. __ ?
#                 e.. ? i..
#                 e__.a.. ?
#
#
#         r.. ?
#
#
#
#     ___ get_most_mentioned_domain_names  n i.. 15 __ l..
#         """Get the most mentioned domain domains. We match a domain using
#            regex: "https?://[^/]+" - make sure you only count a domain once per
#            episode and ignore domains in IGNORE_DOMAINS.
#            Return a list of (domain, count) tuples (use Counter).
#         """
#         counts C..
#         ___ entry __ ?
#             summary ? 'summary'
#             domains s..__.f.. _ https?://[^/] ?
#             ___ domain __ ?
#                 __ ? n.. __ I..
#                     c.. ? +_ 1
#
#
#
#         r.. ?.m.. n
#
#
#     ___ number_episodes_with_special_guest ____ __ i..
#         """Return the number of episodes that had one of more special guests
#            featured (use SPECIAL_GUEST).
#         """
#
#         r.. s.. S.__ entry 'summary'  ___ ? __ ?
#
#     ___ get_average_duration_episode_in_seconds ____ __ N..
#         """Return the average duration in seconds of a Python Bytes episode, as
#            well as the shortest and longest episode in hh:mm:ss notation.
#            Return the results using the Duration namedtuple.
#         """
#
#
#         min_duration_seconds f__ inf
#         max_duration_seconds f__ -inf
#         min_duration ? N..
#         duration_sums 0
#
#
#         ___ entry __ ?
#             duration= ? 'itunes_duration'
#             hours minutes seconds m.. i.. ?.s.. ':'
#             total_seconds 3600 * ? + 60 * ? + ?
#             duration_sums +_ ?
#             __ ? < m..
#                 m.. t..
#                 m.. d..
#             __ t.. > m..
#                 m.. t..
#                 m.. d..
#
#         average_duration i.. d..s/ l.. e..
#         r.. ? ? ? ?
#
#
#
#
#
# __ _______ __ _______
#
#
#     python_bites ?
#     ?.g..
#
