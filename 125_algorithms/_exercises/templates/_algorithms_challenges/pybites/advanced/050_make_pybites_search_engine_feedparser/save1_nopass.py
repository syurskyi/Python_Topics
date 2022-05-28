# ____ c.. _______ n..
# ____ t__ _______ mktime
# ____ f.. _______ p..
# ____ d__ _______ d__
# _______ __
#
#
# FEED 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'
#
# Entry n..('Entry', 'date title link tags')
#
#
# ___ _convert_struct_time_to_dt stime
#     """Convert a time.struct_time as returned by feedparser into a
#     datetime.date object, so:
#     time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
#     -> date(2016, 12, 28)
#     """
#     __ t.. ? __ s..
#         f..  _a, _d _b _Y _H|_M:_S _z'
#         dt_object d__.s.. ? f..
#         r.. ?.d..
#     ____
#         r.. d__.f.. m.. ?.d..
#
#
# ___ get_feed_entries feed_?
#     """Use feedparser to parse PyBites RSS feed.
#        Return a list of Entry namedtuples (date = date, drop time part)
#     """
#     file p.. ?
#     output    # list
#     ___ entry __ ?.e..
#         date ? ?.p..
#         tag_list tag 'term'  ___ ? __ ?.t..
#         ?.a.. ? d.. ?.t.. ?.l.. t..
#     r.. ?
#
#
# ___ filter_entries_by_tag s.. entry
#     """Check if search matches any tags as stored in the Entry namedtuple
#        (case insensitive, only whole, not partial string matches).
#        Returns bool: True if match, False if not.
#        Supported searches:
#        1. If & in search do AND match,
#           e.g. flask&api should match entries with both tags
#        2. Elif | in search do an OR match,
#           e.g. flask|django should match entries with either tag
#        3. Else: match if search is in tags
#     """
#     s.. s...l..
#     tag_list tag ___ ? __ ?.t..
#     __ n.. __.s.. _ \|', s..) a.. n.. __.s.. _ \&', s..
#         r.. s.. __ ?
#     __ __.s.. _ \|', s..
#         s.. __.s.. _ \|', s..)
#         r.. a__ item __ ? ___ ? __ s..
#     __ __.s.. _ \&', s..
#         s.. __.s.. _ \&', s..)
#         r.. a.. item __ ? ___ ? __ s..
#     r.. s..
#
#
# ___ main
#     """Entry point to the program
#        1. Call get_feed_entries and store them in entries
#        2. Initiate an infinite loop
#        3. Ask user for a search term:
#           - if enter was hit (empty string), print 'Please provide a search term'
#           - if 'q' was entered, print 'Bye' and exit/break the infinite loop
#        4. Filter/match the entries (see filter_entries_by_tag docstring)
#        5. Print the title of each match ordered by date ascending
#        6. Secondly, print the number of matches: 'n entries matched'
#           (use entry if only 1 match)
#     """
#     entries ?
#     w... T...
#         ___
#             search_term i.. 'Search for (q for exit): ')
#         ______ E..
#             _____
#
#         __ ? __ '':
#             print('Please provide a search term')
#
#         __ ? !_ '' a.. ? !_ 'q'
#             output_list    # list
#             ___ entry __ ?
#                 __ f.. s.. ?
#                     ?.a.. ?
#             output_list s.. ? k.._l.... x ?.d..
#
#             titles ''.j.. ?.t.. ___ ? __ ?
#
#             output_number l.. ?
#             __ ? < 1
#                 print _* ? entries matched
#             __ ? __ 1
#                 print t..
#                 print _* ? entry matched
#             __ ? > 1
#                 print t..
#                 print _* ? entries matched
#
#         __ s.. __ 'q':
#             print('Bye')
#             _____
#
#
# __ _____ __ _____
#     ?
#
#
#
