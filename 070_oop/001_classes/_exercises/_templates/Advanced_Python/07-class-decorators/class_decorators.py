# ______ fun..
#
#
# ___ invariant predicate
#     """Create a c_ decorator which checks a c_ invariant.
#
#     Args:
#         predicate: A callable to which, after every method invocation,
#             the object on which the method was called will be passed.
#             The predicate should evaluate to True __ the c_ invariant
#             has been maintained, or False __ it has been violated.
#
#     Returns:
#         A c_ decorator for checking the c_ invariant tested by
#         the supplied predicate function.
#     """
#     ___ invariant_checking_class_decorator ___
#         """A c_ decorator for checking invariants."""
#
#         method_names _ |name ___ ?, attr __ v..(___).it.. __ c... at..
#         ___ name __ ?
#             _w... ___ name predicate
#
#         property_names _ |name ___ ?, attr __ v..(___).it.. __ isi.. at.. pr...
#         ___ name __ ?
#             _w_p_w_i_c_p.. ___ n.. p..
#
#
#         r_ ___
#
#     r_ i..
#
#
# ___ _wrap_method_with_invariant_checking_proxy ___ name predicate
#     method _ ge.. ___ n..
#     ass.. c... ?
#
#     ?f__.w.. m..
#     ___ invariant_checking_method_decorator $ $$
#         result _ m... $ $$
#         __ no pr.. ?
#             r_ R..("Class invariant {!r} violated for {!r}".f... pr___. -d ____
#         r_ r..
#
#     s..a.. ___ n.. i_c_m_d..
#
#
# ___ _wrap_property_with_invariant_checking_proxy ___ name predicate
#     prop _ g__a.. ___ n..
#     ass.. isi.. ? pr..
#
#     invariant_checking_proxy _ ICPP... pro. pre..
#
#     s_a.. ___ name invariant_checking_proxy
#
#
# c_ InvariantCheckingPropertyProxy
#
#     ___ - referent predicate
#         _?  ?
#         _?  ?
#
#     ___ -g instance owner
#         __ instance __ N..
#             r_ _r..
#         result _ _r__. -g i.. o..
#         __ no. _pr...  i...
#             r_ R..("Class invariant {!r} violated for {!r}".f...|
#                 _p___. -d i...
#         r_ ?
#
#     ___ -s instance value
#         result _ _r___. -s i.. v..
#         __ not _pr.. i..
#             r_ R..("Class invariant {!r} violated for {!r}".f...|
#                 _p__. -d i...
#         r_ ?
#
#     ___ -d instance
#         result _ _r___. -d ?
#         __ not _p___ ?
#             r_ R..("Class invariant {!r} violated for {!r}".f...(
#                 _p___. -d ?
#         r_ ?
#
#
# ___ not_below_absolute_zero temperature
#     """Temperature not below absolute zero"""
#     r_ ?._k.. >_ 0
#
#
# ___ below_absolute_hot temperature
#     """Temperature below absolute hot"""
#     # See http://en.wikipedia.org/wiki/Absolute_hot
#     r_ ?._k.. <_ 1.416785e32
#
# ?i.. (_a_h..
# ?i.. n_b_a_z..
# c_ Temperature
#
#     ___ - kelvin
#         _?  ?
#
#     ___ get_kelvin
#         r_ _?
#
#     ___ set_kelvin value
#         _k.. _ ?
#
#     ??
#     ___ celsius
#         r_ _k.. - 273.15
#
#     ??.?
#     ___ celsius value
#         _k.. _ ? + 273.15
#
#     ??
#     ___ fahrenheit
#         r_ _k.. * 9/5 - 459.67
#
#     ??.?
#     ___ fahrenheit value
#         _k.. _ (? + 459.67) * 5/9