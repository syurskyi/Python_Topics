# # Restore IP Addresses
# # Question: Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# # For example: Given "25525511135",
# # Return ["255.255.11.135", "255.255.111.35"]. (Order does not matter).
# # Solutions:
#
#
# c_ Solution
#     # @param s, a string
#     # @return a list of strings
#     ___ restoreIpAddresses  s
#         solution _   # list
#         restoreIpAddressesRec s 0 0  # list,solution)
#         r_ ?
#
#     ___ restoreIpAddressesRec  s index octets tempSolution solution
#         __ le. ? - ? < 4 - ?
#             r_
#         __ le. ? - ? > 3* 4 - ?
#             r_
#         __ o.. __ 4
#             __ i..__ le. ?
#                 t__.p..
#                 s__.ap.. "".j.. t__
#                 t__.ap.. '.'
#             r_
#         ___ size __ ra.. 1,4
#             __ ? ? __ '0' an. ? > 1
#                 b..
#             __ in. ? ?|? + ? > 255
#                 b..
#             t__.ap.. ? ?|? + ?
#             t__.ap.. '.'
#             ? ? ? + s.. o.. + 1 ? ?
#             t__.p..
#             t__.p..
#
#
# ? .? "25525511135"