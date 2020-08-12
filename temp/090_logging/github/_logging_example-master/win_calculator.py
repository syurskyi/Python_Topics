# ______ math
# ____ collections ______ OD..
# ____ log_config ______ get_logger
#
# __metaclass__ _ type
#
# payouts _ OD..([
#     ((1, 2), 2.0),  # Sym1
#     ((1, 3), 5.0),
#     ((1, 4), 20.0),
#     ((1, 5), 100.0),
#     ((2, 3), 5.0),  # Sym2
#     ((2, 4), 20.0),
#     ((2, 5), 100.0),
#     ((3, 3), 5.0),  # Sym3
#     ((3, 4), 40.0),
#     ((3, 5), 120.0),
#     ((4, 3), 5.0),  # Sym4
#     ((4, 4), 40.0),
#     ((4, 5), 120.0),
#     ((5, 3), 10.0), # Sym5
#     ((5, 4), 50.0),
#     ((5, 5), 140.0),
#     ((6, 3), 10.0),  # Sym6
#     ((6, 4), 50.0),
#     ((6, 5), 140.0),
#     ((7, 2), 10.0),  # Sym7
#     ((7, 3), 40.0),
#     ((7, 4), 100.0),
#     ((7, 5), 150.0),
#     ((8, 2), 10.0),  # Sym8
#     ((8, 3), 40.0),
#     ((8, 4), 100.0),
#     ((8, 5), 150.0),
#     ((9, 2), 20.0),  # Sym9
#     ((9, 3), 80.0),
#     ((9, 4), 150.0),
#     ((9, 5), 200.0),
#     ((10, 2), 20.0),  # Sym10
#     ((10, 3), 80.0),
#     ((10, 4), 150.0),
#     ((10, 5), 200.0),
#     ((11, 2), 50.0),  # Sym11
#     ((11, 3), 150.0),
#     ((11, 4), 200.0),
#     ((11, 5), 250.0)
# ])
#
#
# c_ Shape
#     ___  -  side
#         ? _ ?
#
#     ___ process_reques caller
#         print g.. ? ?
#         r_ g..  ? "Invalid Caller" ?
#
#
#     ___ area caller
#         print("Parent")
#         r_ ?
#
#     ___ parameter caller
#         print("Parent")
#         r_ ?
#
#
#
# c_ Square Sh..
#
#     ___  -  side
#         ? _ ?
#         s___ ? ? . - ?
#
#     ___ area caller
#         r_ s..*s..
#
#     ___ parameter caller
#         r_ 4*s..
#
# #caller area/parameter
#
#
# #Result format : winning[{
# #                           'symbol': 1,
# #                           'offset': [[0,1],[1,0]],
# #                        }]
#
#
# ___ calculate_winning(symbol_grid, multiplier_1, wild_multiplier_||
#     #symbol_list = [1,2,3,4,5,6,7,8,9,10,11]
#     symbol_list _ set(symbol_grid[0])
#     win _  # list
#     ___ symbol __ ?
#         sym_data _ |'symbol' ? 'offset': # list
#         ___ col __ ra..(0 le. ?
#             col_offset _ # list
#             sym_found _ F..
#             ___ row __ ra.. le. s_g..|c..
#                 __ s_g.. c.. r.. __ s..
#                     c_o__.ap.. c.. r..
#                     sym_found _ T..
#
#             __ row __ le. s_g.. c..-1
#                 __ le. c_o.. > 0
#                     s_d.. 'offset' .ap.. c_o..
#
#             __ no. s_f..
#                 __ le. c_o.. > 0
#                     s_d.. 'offset' .ap.. c_o..
#                 b..
#
#         __ le. s_d.. 'offset'  > 1
#             w__.ap.. s_d..
#     r_ w_a.. w..
#
# ___ win_amount wins
#     gl.. pa..
#     amount _ 0
#     ___ win __ w..
#         symbol _ w.. 'symbol'
#         length _ le. w.. 'offset'
#         ways _ 1
#         ___ of.. __ w.. 'offset'
#             w.. *_ le. o..
#         a.. +_ p.. s.. l.. *w..
#     r_ a..
#
#
# __  -n__'__main__':
#     logger _ ? "win_calculator"
#     ?.d.. "a d.. m.."
#     ?.e.. "a d.. m.."
#     ?.i.. "a d.. m.."
#     ?.c.. "a d.. m.."
#
#     '''caller = 'parameter'
#     square = Square(10)
#     print(caller ," : ",square.process_request(caller))
#     caller = 'area'
#     print(caller ," : ",square.process_request(caller))
#     #print(__metaclass__)'''
#     #symbol_grid = [[2, 1, 11, 5], [7, 6, 7, 10], [2, 4, 3, 1], [11, 7, 8, 9], [3, 1, 5, 6]]
#     #symbol_grid = [[3, 9, 8, 11], [10, 11, 8, 7], [3, 1, 5, 2], [8, 9, 10, 11], [2, 4, 3, 1]]
#
#     symbol_grid _ [[3, 11, 8, 11], [10, 11, 8, 11], [3, 1, 5, 11], [8, 9, 10, 11], [2, 4, 3, 11]]
#
#     print c_w.. s_g..
#
#     '''for win in wins:
#         print(win['symbol'])
#         for offset  in win['offset']:
#             print(offset)'''
#
#
#
