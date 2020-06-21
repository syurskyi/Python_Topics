# ____ xml.dom ______ minidom
# ______ urllib2
#
# c_ AbstractNewsParser o..
#     ___ -
#         # Prohibit creating class instance
#         __  -c __ Ab..
#             r_ T... 'abstract class cannot be instantiated'
#
#     ___ print_top_news
#         """A Template method. Returns 3 latest news for every news website."""
#         url _ g_u..
#         raw_content _ g_r_c.. ?
#         content _ p_c.. ?
#
#         cropped _ c.. ?
#
#         ___ item __ cropped
#             print 'Title: ' ? t..
#             print 'Content: ' ? c..
#             print 'Link: ' ? l...
#             print 'Published: ' ? p..
#             print 'Id: ' ? i..
#
#     ___ get_url
#         r_ N..
#
#     ___ get_raw_content url
#         r_ u_2.u_o. ?.r..
#
#     ___ parse_content content
#         r_ N..
#
#     ___ crop parsed_content max_items_3
#         r_ p_c.. m_i..
#
# c_ YahooParser Ab..
#     ___ get_url
#         r_ 'http://news.yahoo.com/rss/'
#
#     ___ parse_content raw_content
#         parsed_content _     # list
#         dom _ m__.pS.. ?
#
#         ___ node __ ?.gEBTN.. *i..
#             parsed_item _     # dict
#             ___
#                 ? *t..  _ ?.g_EBTN.. *t.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *t..  _ N..
#
#             ___
#                 ? *c..  _ ?.g_EBTN.. *d.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *c..  _ N..
#
#             ___
#                 ? *l..  _ ?.g_EBTN.. *l.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *l...  _ N..
#
#             ___
#                 ? *i.  _ ?.g_EBTN.. *g.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *i.  _ N..
#
#             ___
#                 ? *p..  _ ?.g_EBTN.. *pD.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *p..  _ N..
#
#             p_c_.ap.. ?
#
#         r_ p_c..
#
#
# c_ GoogleParser Ab..
#     ___ get_url
#         r_ 'https://news.google.com/news/feeds?output_atom'
#
#     ___ parse_content raw_content
#         parsed_content _
#         dom _ mini__.pS.. ?
#
#         ___ node __ ?.gEBTN.. *e..
#
#             parsed_item _     # dict
#
#             ___
#                 ? *t..  _ ?.g_EBTN.. *t.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *t...  _ N..
#
#             ___
#                 ? *c...  _ ?.g_EBTN.. *c.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *c..  _ N..
#
#             ___
#                 ? *l..  _ ?.g_EBTN.. *l.. 0 .gA.. *href
#             ______ I....
#                 ? *l..  _ N..
#
#             ___
#                 ? *i.  _ ?.g_EBTN.. *i. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *i.  _ N..
#
#             ___
#                 ? *p...  _ ?.g_EBTN.. *u.. 0 .cN.. 0 .nV..
#             ______ I....
#                 ? *p...  _ N..
#
#             p_c_.ap.. ?
#
#         r_ p_c..
#
#
# __ ________ __ _________
#     google _ G..
#     yahoo _ Y..
#
#     print 'Google: \n', ?.p...
#     print 'Yahoo: \n', ?.p...
