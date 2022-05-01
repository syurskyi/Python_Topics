# _______ __
# _______ __
# ____ c.. _______ C..
# ____ u__.r.. _______ u..
# ____ d__.p.. _______ p..
#
# commits __.p...j..('/tmp', 'commits')
# u..('https://bit.ly/2H1EuZQ' ?
#
# # you can use this constant as key to the yyyymm:count dict
# YEAR_MONTH '{y}-{m:02d}'
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
#     ##
#     # Example log line:
#     # Date:   Tue Mar 5 22:34:33 2019 +0100 | 2 files changed, 4 insertions(+), 4 deletions(-)
#     # Groups:    (                         )                  ( )              ( )
#     log_regex __.c..
#         r'^Date: +\w+ (\w+ \d+ \d+:\d+:\d+ \d{4} [+-]\d{4}) .+ged(?:, (\d+) ins.*?)?(?:, (\d+) del.*?)?$',
#         f..___.M..
#
#     log C..
#     c 0
#     w__ o.. ? __ cl
#         ___ x __ l__.f.. ?.r..
#             ? +_ 1
#             dt p.. x 0
#             __ year __ N.. o. ? __ ?.y..
#                 log += C.. Y__.f.. y_?.y.. m_?.m..| i.. '0' + x 1 - i.. '0' + ? 2
#     lst s.. k v ___ ? ? __ l__.i.. k.._l.... x ?1
#     r.. ? 0 0  ? -1 0
