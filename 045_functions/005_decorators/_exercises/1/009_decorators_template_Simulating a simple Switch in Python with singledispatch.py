# ######################################################################################################################
# Simulating a simple Switch in Python
# recall our own implementation of the @singledispatch decorator:
#
# ___ switcher fn
#     registry _ di..
#     ? _default_| _ fn
#
#     ___ register case
#         ___ inner fn
#             registry|c..| _ ?
#             r_ ?  # we do this so we can stack register decorators!
#
#         r_ ?
#
#     ___ decorator case
#         fn _ re__.g_ c... re__|_default_|
#         r_ f..
#
#     decorator.reg.. _ register
#     r_ d..
#
# ??
# ___ dow
#     print Invalid day of week
#
# _d__.reg.. 1
# ___ dow_1(
#     print Monday
#
# ? 2  l____ print Tuesday
# ? 3  l____ print Wednesday
# ? 4  l____ print Thursday
# ? 5  l____ print Friday
# ? 6  l____ print Saturday
# ? 7  l____ print Sunday
#
# d.. 1
# d.. 2
# d.. 100
#
# print()
