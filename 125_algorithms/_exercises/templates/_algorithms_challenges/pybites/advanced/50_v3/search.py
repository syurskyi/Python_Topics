# ____ c.. _______ n..
# ____ d__ _______ d__
#
# _______ f..
#
# FEED 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'
#
# Entry n.. 'Entry', 'date title link tags'
#
#
# ___ _convert_struct_time_to_dt stime
#     """Convert a time.struct_time as returned by feedparser into a
#     datetime.date object, so:
#     time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
#     -> date(2016, 12, 28)
#     """
#     r.. date y.._?.t..  m.._?.t..  d.._?.t..
#
#
# ___ get_feed_entries feed_?
#     """Use feedparser to parse PyBites RSS feed.
#        Return a list of Entry namedtuples (date = date, drop time part)
#     """
#     f f__.p.. ?
#     result    # list
#     ___ item __ ?.e..
#         result.a.. E.. ? i__.p..
#                             i__.t..
#                             i__.l..
#                             t.t__.l.. ___ ? __ i__.t..
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
#     __ '&' __ s..
#         r.. a.. tag.l.. __ ?.t.. ___ ? __ s...s.. '&'
#     __ '|' __ s..
#         r.. a__ tag.l.. __ ?.t.. ___ ? __ s...s.. '|'
#     r.. s...l.. __ ?.t..
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
#     entries g..
#     w... T...
#         term i.. 'Search for (q for exit): ')
#         __ ? __ ''
#             print('Please provide a search term')
#             _____
#         __ ? __ 'q'
#             print('Bye')
#             _____
#         matches s.. entry ___ ? __ ? __ f.. t.. ?
#         ___ m.. __ ?
#             print _* m...date:10 | m...title:50 | m...link
#         print _*\n l.. ? entr{"y" __ l.. ? __ 1 ____ "ies"} ?
#
# __ _____ __ _____
#     main()
