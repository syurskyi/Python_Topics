# _______ __
# ____ pp__ _______ pp__
#
# COURSE ('Introduction 1 Lecture 01:47'
#           'The Basics 4 Lectures 32:03'
#           'Getting Technical!  4 Lectures 41:51'
#           'Challenge 2 Lectures 27:48'
#           'Afterword 1 Lecture 05:02')
# TWEET ('New PyBites article: Module of the Week - Requests-cache '
#          'for Repeated API Calls - http://pybit.es/requests-cache.html '
#          '#python #APIs')
# HTML ('<p>pybites != greedy</p>'
#         '<p>not the same can be said REgarding ...</p>')
#
#
# ___ extract_course_times course_?
#     """Return the course timings from the passed in
#        course string. Timings are in mm:ss (minutes:seconds)
#        format, so taking COURSE above you would extract:
#        ['01:47', '32:03', '41:51', '27:48', '05:02']
#        Return this list.
#     """
#     r.. __.f.. _ (\d\d:\d\d) ?
#
#
# ___ get_all_hashtags_and_links tweet_?
#     """Get all hashtags and links from the tweet text
#        that is passed into this function. So for TWEET
#        above you need to extract the following list:
#        ['http://pybit.es/requests-cache.html',
#         '#python',
#         '#APIs']
#        Return this list.
#     """
#     r.. __.f.. _ (#\w+|https?://[^\s]*)' ?
#
#
# ___ match_first_paragraph html_?
#     """Extract the first paragraph of the passed in
#        html, so for HTML above this would be:
#        'pybites != greedy' (= content of first paragraph).
#        Return this string.
#     """
#     result __.s.. _ <p>(.+?)</p> ?
#     r.. ?.g.. 1 __ ? ____ ''
#
# __ _______ __ _______
#     pp__ ?
#     pp__ ?
#     pp__ ?
