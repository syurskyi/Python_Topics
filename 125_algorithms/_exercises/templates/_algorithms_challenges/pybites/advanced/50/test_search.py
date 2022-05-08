# ____ d__ _______ d__, date
# ____ ?.m.. _______ p..
#
# _______ p__
#
# ____ s.. _______ ? ?
#                     ? ? ?
#
#
# c_ AttrDict d..
#     """feedparser lets you access dict keys as attributes, hence a bit of
#        mocking, got this from https://stackoverflow.com/a/14620633"""
#     ___ - , $  $$
#         s.. ? - - $ $$
#         -d -
#
#
# dt1 d__(2018, 2, 18, 19, 52, 0).t..
# dt2 d__(2017, 1, 6, 11, 0, 0).t..
#
# MOCK_ENTRIES ? 'entries':
#                 [?({'author': 'PyBites',
#                            'link':
#                            'https://pybit.es/twitter_digest_201808.html',  # noqa E501
#                            'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
#                            'published_parsed': dt1,
#                            'summary': 'Every weekend we share ...',
#                            'tags': [?({'term': 'twitter'}),
#                                     ?({'term': 'Flask'}),
#                                     ?({'term': 'Python'}),
#                                     ?({'term': 'Regex'})],
#                            'title': 'Twitter Digest 2018 Week 08'}),
#                  ?({'author': 'Julian',
#                            'link': 'https://pybit.es/pyperclip.html',
#                            'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
#                            'published_parsed': dt2,
#                            'summary': 'Use the Pyperclip module to ...',
#                            'tags': [?({'term': 'python'}),
#                                     ?({'term': 'tips'}),
#                                     ?({'term': 'tricks'}),
#                                     ?({'term': 'code'}),
#                                     ?({'term': 'pybites'})],
#                            'title': 'Copy and Paste with Pyperclip'})]})
#
#
# ?p__.m__.p. "arg, ret", [
#     (d__(2017, 9, 12, 8, 50, 0).t.. ,
#      date y.._2017,  m.._9,  d.._12,
#     (d__(2017, 9, 8, 14, 30, 0).t.. ,
#      date y.._2017,  m.._9,  d.._8,
#     (d__(2016, 12, 19, 9, 26, 0).t.. ,
#      date y.._2016,  m.._12,  d.._19,
#
# ___ test_convert_struct_time_to_dt(arg, ret
#     ... _convert_struct_time_to_dt(arg) __ ret
#
#
# $p.. ("feedparser.parse", s.._ M..
# ___ test_get_feed_entries inp
#     first, last t.. ?
#
#     ... ?.d.. __ date y.._2018,  m.._2,  d.._18
#     ... ?.t.. __ 'Twitter Digest 2018 Week 08'
#     ... ?.l.. __ 'https://pybit.es/twitter_digest_201808.html'
#     e.. =  'flask', 'python', 'regex', 'twitter'
#     # allow list or set
#     ... s.. l.. f__.t.. __ e..
#
#     ... ?.d.. __ date y.._2017  m.._1  d.._6
#     ... ?.t.. __ 'Copy and Paste with Pyperclip'
#     ... ?.l.. __ 'https://pybit.es/pyperclip.html'
#     e.. =  'code', 'pybites', 'python', 'tips', 'tricks'
#     ... s.. l.. ?.t.. __ e..
#
#
# ?p__.m__.p. "arg, ret", [
#     ('blabla', F..),
#     ('tricks', T..),
#     ('TRICKS', T..),  # case should not matter
#     ('TriCkS', T..),
#     ('python', F..),  # whole term only so python != pythonic
#     ('matplotlib&pandas', T..),
#     ('matplotlib&pandas&collections', T..),
#     ('matplotlib&pandas&flask', F..),
#     ('matplotlib|flask', T..),
#     ('matplotlib|django|flask', T..),
#     ('pyramid|django|flask', F..),
#
# ___ test_filter_entries_by_tag arg ret
#     entry ? d.._?(2016, 12, 22),
#                   t.._'2016 py articles and useful books',
#                   l.._'https://pybit.es/py-articles-books2016.html',
#                   t.._{'pythonic', 'data science',
#                         'tips', 'tricks', 'matplotlib',
#                         'pandas', 'books', 'collections'})
#     ... ? ? ? __ ?
#
#
# $p.. "feedparser.parse", s.._ M..
# $p.. "builtins.input", side_effect= 'pycon', 'twitter', 'python', 'nonsense',
#                                       'python|regex', 'python&regex', 'REGeX',
#                                       '', 'q'
# ___ test_main entries inp capfd
#     m..
#     out, _ ?.r..
#
#     output line ___ ? __ o__.s.. \n __ l__.s..
#
#     e.. =  '0 entries matched', 'Twitter Digest 2018 Week 08',
#                 '1 entry matched', 'Copy and Paste with Pyperclip',
#                 'Twitter Digest 2018 Week 08', '2 entries matched',
#                 '0 entries matched', 'Copy and Paste with Pyperclip',
#                 'Twitter Digest 2018 Week 08', '2 entries matched',
#                 'Twitter Digest 2018 Week 08', '1 entry matched',
#                 'Twitter Digest 2018 Week 08', '1 entry matched',
#                 'Please provide a search term', 'Bye'
#
#     ... l.. ?  __ l.. e..
#
#     ___ line exp __ z.. ? , e..
#         ... e.. __ l.
