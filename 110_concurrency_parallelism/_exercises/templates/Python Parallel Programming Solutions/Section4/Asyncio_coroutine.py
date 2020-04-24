# #Asyncio Finite State Machine
#
# ______ a..
# ______ ti..
# ____ ra__ ______ r_i..
#
#
# ??.?
# ___ StartState
#     print ("Start State called \n")
#     input_value _ r_i.. 0,1
#     t__.s.. 1
#     __ ? __ 0
#         result _ ? ? _2 ?
#     ____
#         result _ ? ? _1 ?
#     print("Resume of the Transition : \nStart State calling "\
#           + r..
#
#
# ??.?
# ___ State1 transition_value
#     outputValue _  st.(("State 1 with transition value = @ \n"\
#                         ?
#     input_value _ r_i.. 0 1
#     t__.s.. 1
#     print("...Evaluating...")
#     __ ? __ 0
#         result _  ? ? _3 ?
#     ____ :
#         result _ ? ? _2 ?
#     result _ "State 1 calling " + r..
#     r_  o.. + st. r..
#
#
# ??.?
# ___ State2 transition_value
#     outputValue _  st.(("State 2 with transition value = @ \n" \
#                         ?
#     input_value _ r_i.. 0 1
#     t__.s.. 1
#     print("...Evaluating...")
#     __ ? __ 0
#         result _ ? ? _1 ?
#     ____
#         result _ ? ? _3 ?
#     result _ "State 2 calling " + result
#     r_ (o.. + st. r..
#
#
# ??.?
# ___ State3 transition_value
#     outputValue _  st.(("State 3 with transition value = @ \n" \
#                         ?
#     input_value _ r_i.. 0 1
#     t__.s.. 1
#     print("...Evaluating...")
#     __ ? __ 0
#         result _ ? ? _1 ?
#     ____
#         result _ ? ? E.. ?
#     result _ "State 3 calling " + r..
#     r_  o.. + st. r..
#
#
# ??.?
# ___ EndState transition_value
#     outputValue _  st.(("End State with transition value = @ \n"\
#                         ?
#     print("...Stop Computation...")
#     r_ ?
#
# __ _______ __ _______
#     print("Finite State Machine simulation with Asyncio Coroutine")
#     loop _ ?.g_e_l..
#     ?.r_u_c.. S..
