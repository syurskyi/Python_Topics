# ____ a.. _____ A.. a..
# _____ fu...
#
#
# ___ invariant predicate
#     """Create a c_ decorator which checks a c_ invariant.
#
#     Args:
#         predicate: A callable to which, after every method invocation,
#             the object on which the method was called will be passed.
#             The predicate should evaluate to True if the c_ invariant
#             has been maintained, or False if it has been violated.
#
#     Returns:
#         A c_ decorator for checking the c_ invariant tested by
#         the supplied predicate function.
#     """
#     ___ invariant_checking_class_decorator ___
#         """A c_ decorator for checking invariants."""
#
#         method_names _ |name ___ ?, attr __ v..(___).it.. __ ca..(at..
#         ___ name __ method_names:
#             _wrap_method_with_invariant_checking_proxy ___ name, pr..
#
#         property_names _ |name ___ ?, attr __ v..(___).it.. __ isi.. at.. PDD..
#         ___ name __ ?
#             _wrap_property_with_invariant_checking_proxy ___ n.. pr..
#
#         r_ ___
#
#     r_ i_c_c_d...
#
#
# ___ _wrap_method_with_invariant_checking_proxy ___ name predicate
#     method _ ge.. ___ n...
#     ass.. ca.. ?
#
#     ?f__.w.. m..
#     ___ invariant_checking_method_decorator $ $$
#         result _ m... $ $$
#         __ no. pr..
#             r_ R..("Class invariant {!r} violated for {!r}".f.. pr... -d, ____
#         r_ ?
#
#     se.. ___ n.. i_c_m_d..
#     p..
#
#
# c_ PropertyDataDescriptor A..
#
#     ??
#     ___ __get__ instance owner
#         r_ N...
#
#     ??
#     ___ -sinstance value
#         r_ N...
#
#     ??
#     ___ -d instance
#         r_ N...
#
#     ??
#     ??
#     ___ __isabstractmethod__
#         r_ N...
#
#
# PDD__.r.. pr..
#
#
# c_ InvariantCheckingPropertyProxy P..
#
#     ___ - referent predicate
#         _? ?
#         _? ?
#
#     ___ -g instance owner
#         __ ? __ N..
#             r_ ____
#         result _ _r___. -g ?  ?
#         __ no. _p... ?
#             r_ R..("Class invariant {!r} violated for {!r}".f.. _p___. -d i..
#         r_ ?
#
#     ___ -s instance value
#         result _ _r___. -s ? ?
#         __ no. _p... ?
#             r_ R..("Class invariant {!r} violated for {!r}".f.. _p___. -d i..
#         r_ ?
#
#     ___ -d instance
#         result _ _r___. -d?
#         __ no. _p... ?
#             r_ R..("Class invariant {!r} violated for {!r}".f..(_p___. -d, i..
#         r_ ?
#
#     ___ __isabstractmethod__
#         r_ _r___.?
#
#
# ___ _wrap_property_with_invariant_checking_proxy ___ name predicate
#     prop _ ge.. ___  n..
#     invariant_checking_proxy _ ICPP.. pro. pr..
#     se.. ___ n.. i_c_p..
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
#
# ?i.. b_a_h
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
#         _k... _ (? + 459.67) * 5/9
