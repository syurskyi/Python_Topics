# ____ d__ _______ d__, d__
#
# MAC1 """
# reboot    ~                         Wed Apr 10 22:39
# reboot    ~                         Wed Mar 27 16:24
# reboot    ~                         Wed Mar 27 15:01
# reboot    ~                         Sun Mar  3 14:51
# reboot    ~                         Sun Feb 17 11:36
# reboot    ~                         Thu Jan 17 21:54
# reboot    ~                         Mon Jan 14 09:25
# """
#
#
# ___ extract_date reboots
#     months {
#         'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
#         'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
#     }
#     lines reboots.s..k.._F..
#     ___ line __ ?
#         __ l.. ?.s.. __ 0:
#             _____
#         line_parts ?.s...s..
#         time_part ? -1 .s.. ':'
#         y.. d__ y.._2019
#                         m.._? ? -3
#                         d.._i.. ? -2
#                        hour_i.. ? 0
#                        minute_i.. ? 1
#
#
# ___ calc_max_uptime reboots
#     """Parse the passed in reboots output,
#        extracting the datetimes.
#
#        Calculate the highest uptime between reboots =
#        highest diff between extracted reboot datetimes.
#
#        Return a tuple of this max uptime in days (int) and the
#        date (str) this record was hit.
#
#        For the output above it would be (30, '2019-02-17'),
#        but we use different outputs in the tests as well ...
#     """
#     previous N..
#     records    # list
#     ___ this_date __ ? ?
#         __ p.. __ N..
#             p.. ?
#             _____
#         r__.a.. p.. - ? .d.. s.. p__.d..
#         p.. ?
#     r.. s.. ? -1
