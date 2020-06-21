# ______ u__
# ____ n__.tools ______ _
# ____ words ______ numwords, wordcounts, addcounts
# ___ test_numwords
#     a_e.. 0 n.. ""
#     a_e.. 1 n.. "hey"
#     a_e.. 3 n.. "blue moon is blue"
#     a_e.. 3 n.. "Blue moon is blue"
#     a_e.. 3 n.. "Blue moon, is blue."
#     a_e.. 3 n.. "Blue moon, ... is blue."
#     a_e.. 3 n.. "Blue moon, ...is blue."
#     a_e.. 3 n.. "Blue moon, is ...blue."
#     a_e.. 3 n.. "Truth is beauty; beauty, truth."
#     a_e.. 15 n..("A bidarka, is it not so? Look! a bidarka, and one man who drives clumsily with a paddle!"
#
# ___ test_wordcounts
#     a_d_e.. || nw..(""
#     a_d_e.. 'foo': 1|, nw.. "foo"
#     a_d_e.. 'truth': 2, 'is': 1, 'beauty': 2
#             nw.. "Truth is beauty; beauty, truth."
#     a_d_e.. 'truth': 2, 'is': 1, 'beauty': 2
#             nw.. "Truth is beauty; beauty ... truth."
#
# # The nose way of checking that a function raises and exception.
# ?r.. V..
# ___ test_addcounts_badarg_existing
#     a..(N.. ||
#
# ?r.. V..
# ___ test_addcounts_badarg_new
#     a.. || N..
#
# ?r.. V..
# ___ test_addcounts_badargs
#     a.. N.. N..
#
# # For setup fixtures, we sometimes need to use unittest.TestCase.
# # nose's @with_setup doesn't let us do the following.
# # However, nose can find and run these tests just fine.
# c_ TestWords_addcounts?.?
#     ___ setUp
#         existing _  'truth': 2, 'is': 1, 'beauty': 2
#
#     ___ test_addcounts_empty
#         a.. existing ||
#         aE.. 'truth': 2, 'is': 1, 'beauty': 2| ?
#
#     ___ test_addcounts_double
#         new _ di.. ?
#         a.. ? ?
#         aE.. 'truth': 4, 'is': 2, 'beauty': 4| ?
#
#     ___ test_addcounts_newword
#         a.. ? |'love': 1
#         aE.. 'truth': 2, 'is': 1, 'beauty': 2, 'love': 1|, ?
#
#     ___ test_addcounts_errors
#         '''
#         Alternate way to check that ValueError is raised.
#         '''
#         w__ aR.. V..
#             a.. N.. ||
#         w__ aR.. V..
#             a.. || N..
#         w__ aR.. V..
#             a.. N.. N..
