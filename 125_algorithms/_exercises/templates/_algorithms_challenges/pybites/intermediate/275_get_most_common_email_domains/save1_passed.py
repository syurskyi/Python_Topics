# ____ c.. _______ C..
# ____ ___ _______ B..
# _______ r__
# _______ __
#
# COMMON_DOMAINS ("https://bites-data.s3.us-east-2.amazonaws.com/"
#                   "common-domains.html")
# TARGET_DIV {"class": "middle_info_noborder"}
#
#
# ___ get_common_domains url_?
#     """Scrape the url return the 100 most common domain names"""
#
#     response r__.g.. C..
#     soup B..(?.t.., 'html.parser')
#     right_table ?.f.. 'div' T..
#
#     domains    # list
#     ___ row __ ?.f.. 'tr'
#         cells ?.f.. 'td'
#         ?.a.. ?2 .f.. text_T..
#
#     r.. ?
#
#
# ___ get_most_common_domains emails common_domains_ N..
#     """Given a list of emails return the most common domain names,
#        ignoring the list (or set) of common_domains"""
#     __ ? __ N..
#         ? ?
#
#     l    # list
#     ___ email __ ?
#         m.. __.f.. _ @(\w+.\w+) ? 0
#         __ m.. n.. __ ?
#             l.a.. m..
#
#     r.. s.. l.. C.. ? .i.. r.._T..