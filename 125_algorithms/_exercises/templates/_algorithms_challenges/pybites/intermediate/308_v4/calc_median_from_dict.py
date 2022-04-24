# ____ i.. _______ a...
#
#
# ___ calc_median_from_dict d d.. __ f__
#     """
#     :param d: dict of numbers and their occurrences
#     :return: float: median
#     Example:
#     {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
#     """
#     __ n.. isi.. ? d.. o. ? __ N..
#         r.. T..
#
#     __ n.. a.. isi.. k i.. f__ a.. ? ___ ? __ ?.v..
#         r.. T..
#
#     items k ? ? ___ ? __ s.. ?  # handle unordered dicts
#     values item 1 ___ ?__ ?
#     length s.. ?.v..
#     cumsums t.. a.. v..
#
#     # determine intervals: gotta be a way to do this with itertools
#     intervals    # list
#     lower 0
#     # determine intervals
#     ___ k __ c..
#         print _* ?_
#         i__.a.. l.. + 1 ?
#         lower k
#     cums i.. item) ___ ? ? __ z.. ? ?
#
#     # two cases, even length and odd length, next is same for both
#     b n.. f.. l.... x| ? 0 0  <_ l.. // 2 + 1 <_ x 0 1
#                     cums 1 0
#
#     __ l.. % 2 __ 1
#         r.. ?
#     ____
#         a n.. f.. l.... x| ? 0 0  <_ l.. // 2 <_ ? 0 1
#                         ? 1 0
#         r.. ? + ? / 2
