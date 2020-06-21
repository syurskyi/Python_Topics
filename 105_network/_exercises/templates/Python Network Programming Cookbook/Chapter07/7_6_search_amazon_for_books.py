# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 7
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
# # Supply the Amazon Access and Secret Keys via local_settings.py
#
# ______ a_p..
# ______ bottlenose
# ____ xml.dom ______ minidom __ xml
#
# ___
#     ____ l_s.. ______ a_a..
# ______ I..
#     p..
#
# ACCESS_KEY _ a_a.. 'access_key'
# SECRET_KEY _ a_a.. 'secret_key'
# AFFILIATE_ID _ a_a.. 'affiliate_id']
#
#
# ___ search_for_books tag index
#     """Search Amazon for Books """
#     amazon _ ?.A.. A.. S.. A..
#     results _ ?.IS..
#                 SI.. _ i..
#                 Sort _ "relevancerank",
#                 Keywords _ tag
#
#     parsed_result _ ___.pS.. ?
#
#     all_items _ # list
#     attrs _ 'Title','Author', 'URL'
#
#     ___ item __ p_r_.gEBTN.. 'Item'
#         parse_item _  # dict
#
#         ___ attr __ a..
#             ?|? _ ""
#             ___
#                 p_i.. ? _ i__.gEBTN.. ? 0 .cN.. 0 .d..
#             ______
#                 p..
#         all_i__.ap.. ?
#     r_ all_items
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Search info from Amazon'
#     ?.a_a.. '--tag', a.._"store", d.._"tag", d.._'Python'
#     ?.a_a.. '--index', a.._"store", d.._"index", d.._'Books'
#     # parse arguments
#     given_args _ ?.p_a..
#     books _ ? ?.t.. ?.i..
#
#     ___ book __ ?
#         ___ k v __ ?.i_i..
#             print ("@: @"  ? ?
#         print ("-" * 80)
