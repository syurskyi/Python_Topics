# c_ Journal
#     ___ -
#         ?entries _    # list
#         ?count _ 0
#
#     ___ add_entry text
#         ?e__.ap.. _*|?c.. : |? "
#         ?c.. += 1
#
#     ___ remove_entry pos
#         del ?e.. |?
#
#     ___ -s
#         r_ "\n".jo.. ?e..
#
#     # break SRP
#     ___ save filename
#         file _ o.. ? _
#         ?.w.. st. ____
#         ?.cl..
#
#     ___ load  filename
#         p..
#
#     ___ load_from_web uri
#         p..
#
#
# c_ PersistenceManager
#     ___ save_to_file journal filename
#         file _ o.. ? _
#         ?.w.. st. j..
#         ?.cl..
#
#
# j = J..
# ?.a.. "I cried today.")
# ?.a.. ("I ate a bug.")
# print _*Journal entries:\n|? \n")
#
# p = P..
# file = r'C:\Users\syurskyi\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\060_Design_Patterns\Video' \
#        r'\Design Patterns in Python\Section 1 The SOLID Design Principles\journal.txt'
# # p.save_to_file(j, file)
# #
# # # verify!
# w____ o.. ? __ fh
#     print ?.r..
