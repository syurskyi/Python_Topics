# ____ c.. _______ C..
#
# _______ ___
# _______ r__
#
# COMMON_DOMAINS ("https://bites-data.s3.us-east-2.amazonaws.com/"
#                   "common-domains.html")
# TARGET_DIV {"class": "middle_info_noborder"}
#
#
# ___ get_common_domains url_?
#     """Scrape the url return the 100 most common domain names"""
#     response r__.g.. ?
#     soup ___.B.. ?.c.. "html.parser"
#     soup_content ?.f.. c.._"content"
#     soup_table ?.f.. c.._"middle_info_noborder"
#     soup_row ?.f.. "tr"
#     r.. row.s.. "td td td" 2 .g..  ___ ? __ ?
#
#
# ___ get_most_common_domains emails common_domains_ N..
#     """Given a list of emails return the most common domain names,
#        ignoring the list (or set) of common_domains"""
#     __ ? __ N..
#         ? ?
#
#     most_common_prep    # list
#     ___ email __ ?
#         domain ?.s.. "@" 1
#         __ ? __ c..
#             _____
#         ____
#             m__.a.. ?
#
#     most_common C.. ?
#     r.. ?.M.. 2
#
#
# __ _______ __ _______
#     #get_common_domains()
#     ? ? "a@gmail.es", "b@googlemail.com", "c@somedomain.com", "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"