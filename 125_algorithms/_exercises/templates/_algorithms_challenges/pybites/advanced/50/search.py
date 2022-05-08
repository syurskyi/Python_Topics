# ____ c.. _______ n..
# ____ d__ _______ d__
# _______ d__
# ____ t__ _______ mktime
#
# _______ feedparser
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
#
#     dt d__.d__.f.. m.. ?
#
#     r.. ?.d..
#
#
#
# ___ get_feed_entries feed_?
#     """Use feedparser to parse PyBites RSS feed.
#        Return a list of Entry namedtuples (date = date, drop time part)
#     """
#     d f__.p.. ?
#     entries ?.e..
#
#     all_entries =   # list
#     ___ entry __ ?
#         title ?.?
#         link ?.?
#         date ?.p..
#         tags ?.t..
#         tags t.g.. 'term' .l.. ___ ? __ ?
#
#         date _? d..
#
#
#         entry ? d.. t.. l.. t..
#         ?.a.. ?
#
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
#
#     entry_tags entry.tags
#     __ '&' __ s..
#         splits s...s.. '&'
#
#         r.. a.. s...l.. __ e.. ___ s.. __ ?
#     ____ '|' __ s..
#         splits s...s.. '|'
#         r.. a__ s...l.. __ e.. ___ s.. __ ?
#     ____
#         r.. s...l.. __ e..
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
#
#     ?.s.. k.._l.... x ?.d..
#     w... T...
#         term i.. "Search Term? "
#         __ ? __ ''
#             print('Please provide a search term')
#             _____
#         __ ? __ 'q'
#             print('Bye')
#             _____
#
#
#         matches 0
#         ___ entry __ ?
#             found f.. t.. e..
#             __ ?
#                 print ?.t..
#                 m.. +_ 1
#
#
#         __ m.. __ 1
#             print('1 entry matched')
#         ____
#             print _*m.. entries matched
#
# __ _____ __ _____
#     m..
