# ____ c.. _______ C..
# _______ __
# _______ __
# ____ u__.r.. _______ u..
# ____ d__.p.. _______ p..
#
# commits __.p...j..(__.g.. TMP  /tmp, 'commits')
# u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
#     ?
#
#
# # you can use this constant as key to the yyyymm:count dict
# YEAR_MONTH '{y}-{m:02d}'
#
#
# ___ _parse_line line s.. __ d..
#     """returns a line with the key of date type and value of add/del"""
#     d_str, all_changes ?.s.. ' | '
#     date p.. __.s.. _ D..:  +', '', ?.d..
#
#     # add insertions and deletions
#     i.. __.f.. _ 0-9 +) i.. a..
#     deletions __.f.. _ 0-9 +) d..  a..
#     changes i.. i.. 0 __ i.. ____ 0
#     changes += i.. d.. 0 __ d.. ____ 0
#     r.. 'date' ? 'changes' ?
#
#
# ___ get_min_max_amount_of_commits commit_log s.. commits
#                                   year i.. N.. __ s.. s..
#     """
#     Calculate the amount of inserts / deletes per month from the
#     provided commit log.
#
#     Takes optional year arg, if provided only look at lines for
#     that year, if not, use the entire file.
#
#     Returns a tuple of (least_active_month, most_active_month)
#     """
#     commits C..
#     w__ o.. ? __ f
#         ___ line __ ?
#             dat _? ?
#             __ ? 'date' .y.. __ y.. o. y.. __ N..
#                 ?.u.. ? 'date' .s.. _Y-_m ? 'changes'
#
#     m.. ?.m.. 1 0 0
#     m.. ?.m.. -1 0
#
#     r.. m.., m..
