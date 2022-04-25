# _______ i___
# _______ r__
#
# _______ p__
#
# ____ ? _______ ? ? ?
#
#
# ___ test_should_not_instantiate_abc
#     w__ p__.r.. T..
#         ch ? 0 'Should not instantiate ABC'
#         ?.n..
#
#
# ___ test_baseclass_methods_are_abstract
#     lines line.s.. ___ ? __
#              i___.g.. ? 0
#     verify_method i l.. ___ ? ? __
#                      e.. ?
#                      __ 'def verify' __ ?
#     ... verify_method "Cannot find a method called verify"
#     verify_index v.. 0 0
#     ... l.. ? - 1 __ "@abstractmethod"
#     pretty_title_index ?.i.. 'def pretty_title(self):'
#     ... l.. ? - 1 __ "@abstractmethod"
#
#
# ___ test_super_and_abst_method_implementation
#     merged_prs [41, 42, 44]
#     ___
#         blog ? 1, 'Wordvalues' ?
#     ______ T..
#         p__.f.. "Unexpected TypeError, missing methods/properties?"
#
#     ... ?.v.. r__.c.. ?
#     ... n.. ?.v.. 43
#     ... ?.p.. __ 'PCC1 - Wordvalues'
#
#
# ___ test_super_and_abst_property_implementation
#     ___
#         bite ? 24, 'ABC and class inheritance', 'my result'
#     ______ T..
#         p__.f.. "Unexpected TypeError, missing methods/properties?"
#
#     ... ?.v.. 'my result'
#     ... n.. ?.v.. 'other result'
#     ... ?.p.. __ 'Bite 24. ABC and class inheritance'