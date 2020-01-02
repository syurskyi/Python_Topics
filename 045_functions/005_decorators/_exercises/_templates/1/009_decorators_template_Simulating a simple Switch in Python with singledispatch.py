# ######################################################################################################################
# Simulating a simple Switch in Python
# recall our own implementation of the @singledispatch decorator:
#
# ___ switcher fn
#     registry _ d_
#     registry|_default_| _ fn
#
#     ___ register case
#         ___ inner fn
#             registry|c..| _ fn
#             r_ fn  # we do this so we can stack register decorators!
#
#         r_ i..
#
#     ___ decorator case
#         fn _ registry.g_ c... registry|_default_|
#         r_ fn()
#
#     decorator.register _ register
#     r_ d..
#
# _s...
# ___ dow
#     print Invalid day of week
#
# _d__.register 1
# ___ dow_1(
#     print Monday
#
# dow.r_(2)(l_| print Tuesday
# dow.r_(3)(l_| print Wednesday
# dow.r_(4)(l_| print Thursday
# dow.r_(5)(l_| print Friday
# dow.r_(6)(l_| print Saturday
# dow.r_(7)(l_| print Sunday
#
# dow(1)
# dow(2)
# dow(100)
#
# print()