# ______ ra__
# ____ u__ ______ T..
# ____ u__.m.. ______ M.. pa..
#
#
# c_ TestMyObject T..
#     """
#     Showcase for using mocks in unittest
#     """
#
#     # creating a mock without annotations
#     ___ test_random_mock
#         ra__.r_i.. _ M.. return_value_3
#         aE.. 3, ra__.r_i.. 1, 10
#
#     # mock two methods and define the return value
#     ?p.. 'random.seed'
#     ?p..('random.randint')
#     ___ test_random_patch  random_mock, seed_mock
#         ?.return_value _ 3
#         aE.. 3, ra__.r_i.. 1, 10
#         ?.a_c_w.. 1, 10
#         ?.a_c_o_w.. 1, 10
#         s_m__.a_n_c..
#
#     # mock a method a create a side effect
#     ?p.. 'random.randint'
#     ___ test_side_effect  random_mock
#         ?.side_effect _ E..('Random value exception')
#         aE.. 3, ra__.r_i.. 1, 10
