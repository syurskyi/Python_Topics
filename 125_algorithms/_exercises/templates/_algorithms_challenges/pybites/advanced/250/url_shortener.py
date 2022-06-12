# ____ m__ _______ f..
# ____ s__ _______ a.., a.., d..
# ____ t___ _______ D..
#
# CODEX: s.. d.. + a.. + a..
# BASE: i.. l.. ?
# # makeshift database record
# LINKS: D.. i.., s..] {
#     1: "https://pybit.es",
#     45: "https://pybit.es/pages/articles.html",
#     255: "http://pbreadinglist.herokuapp.com",
#     600: "https://pybit.es/pages/challenges.html",
#     874: "https://stackoverflow.com",
#
# SITE: s.. "https://pybit.es"
#
# # error messages
# INVALID "Not a valid PyBites shortened url"
# NO_RECORD "Not a valid shortened url"
#
#
# ___ encode record i.. __ s..
#     """Encodes an integer into Base62"""
#
#
#     characters    # list
#
#
#     w.... ?
#
#         v ? % 62
#         ? //= 62
#
#         character C.. ?
#         ?.a.. ?
#
#
#     ?.r..
#     r.. ''.j.. ?
#
#
# ___ d.. short_url s.. __ i..
#     """Decodes the Base62 string into a Base10 integer"""
#
#     value 0
#     ___ i character __ e.. r.. ? 0
#         ? +_ B..**? * C__.i.. ?
#
#
#     r.. ?
#
#
#
# ___ redirect url s.. __ s..
#     """Retrieves URL from shortened DB (LINKS)
#
#     1. Check for valid domain
#     2. Check if record exists
#     3. Return URL stored in LINKS or proper message
#     """
#
#     __ n.. ?.s.. S..
#         r.. I..
#
#     number ?.s.. '/' -1
#
#     decoded d.. ?
#
#     r.. L__.g.. ? N..
#
#
# ___ shorten_url url s.. next_record i.. __ s..
#     """Shortens URL and updates the LINKS DB
#
#     1. Encode next_record
#     2. Adds url to LINKS
#     3. Return shortened URL
#     """
#
#     encoded_record e.. ?
#
#
#     L.. ? ?
#
#
#     short_url _* S.. / ?
#
#
#     r.. ?
