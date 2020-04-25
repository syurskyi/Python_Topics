# # Application #1 - Part #1
#
# ______ ra__
# ______ ___
#
#
# ___ subnet_calc
#     ___
#         print("\n")
#
#         # Checking IP address validity
#         w__ T..
#             ip_address _ in__("Enter an IP address: ")
#
#             # Checking octets
#             ip_octets _ ?.sp.. '.'
#
#             __ (le. ? __ 4| an. |1 <_ in. ? 0 <_ 223| an. in. ? 0 | !_ 127 an.
#                     in. ? 0 | !_ 169 o. in. ? 1| !_ 254 an.
#                     0 <_ in. ? 1| <_ 255 an. 0 <_ in. ? 2 <_ 255 an. 0 <_ in. ? 3 <_ 255
#                 b..
#
#             ____
#                 print("\nThe IP address is INVALID! Please retry!\n")
#                 c..
#
#         masks _ 255, 254, 252, 248, 240, 224, 192, 128, 0
#
#         # Checking Subnet Mask validity
#         w__ T..
#             subnet_mask _ in__("Enter a subnet mask: ")
#
#             # Checking octets
#             mask_octets _ ?.sp.. '.'
#
#             __ le. ? __ 4| an. in. ? 0  __ 255| an. in. ? 1 __ masks an.
#                     in. ? 2 __ masks| an. in. ? 3 __ masks an.
#                     in. ? 0 >_ in. ? 1 >_ in. ? 2 >_ in. ? 3
#                 b..
#
#             ____
#                 print("\nThe subnet mask is INVALID! Please retry!\n")
#                 c..
#
#         # Application #1 - Part #2
#
#         # Algorithm for subnet identification, based on IP and Subnet Mask
#
#         # Convert mask to binary string
#         mask_octets_binary _   # list
#
#         ___ octet __ mask_octets
#             binary_octet _ bi. in. ? .ls.. '0b'
#             # print(binary_octet)
#
#             ?.ap.. ?.zf.. 8
#
#         # print(mask_octets_binary)
#
#         binary_mask _ "".j.. ?
#         # print(decimal_mask)
#         # Example: for 255.255.255.0 => 11111111111111111111111100000000
#
#         # Counting host bits in the mask and calculating number of hosts/subnet
#         no_of_zeros _ ?.c..("0")
#         no_of_ones _ 32 - ?
#         no_of_hosts _ abs(2 ** n_o_z.. - 2)  # return a positive value for the /32 mask (all 255s)
#
#         # print(no_of_zeros)
#         # print(no_of_ones)
#         # print(no_of_hosts)
#
#         # Obtaining wildcard mask
#         wildcard_octets _   # list
#
#         ___ octet __ m_o..
#             wild_octet _ 255 - in. oc..
#             ?.ap.. st. ?
#
#         # print(wildcard_octets)
#
#         wildcard_mask _ ".".j.. ?
#         # print(wildcard_mask)
#
#         # Application #1 - Part #3
#
#         # Convert IP to binary string
#         ip_octets_binary _   # list
#
#         ___ octet __ i_o..
#             binary_octet _ bi. in. o.. .ls.. '0b'
#             # print(binary_octet)
#
#             ?.ap.. b_o_.zf.. 8
#
#         # print(ip_octets_binary)
#         # Example: for 192.168.10.1 =>
#
#         binary_ip _ "".j.. ?
#
#         # print(binary_ip)
#         # Example: for 192.168.2.100 => 11000000101010000000101000000001
#
#         # Getting the network address and broadcast address from the binary strings obtained above
#
#         network_address_binary _ b_i.|; n_o_o.. + "0" * n_o_z..
#         # print(network_address_binary)
#
#         broadcast_address_binary _ ?|; n_o_o.. + "1" * n_o_z..
#         # print(broadcast_address_binary)
#
#         # Converting everything back to decimal (readable format)
#         net_ip_octets _   # list
#
#         # range(0, 32, 8) means 0, 8, 16, 24
#         ___ bit __ ra.. 0, 32, 8
#             net_ip_octet _ n_a_b..|?; ? + 8
#             ?.ap.. ?
#
#         # We will end up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24:31]; remember that each slice goes up to, but not including, the index on the right side of the colon!
#
#         # print(net_ip_octets)
#
#         net_ip_address _   # list
#
#         ___ each_octet __ ?
#             ?.ap.. st. in. ? 2
#
#         # print(net_ip_address)
#
#         network_address _ ".".j.. ?
#         # print(network_address)
#
#         bst_ip_octets _   # list
#
#         # range(0, 32, 8) means 0, 8, 16, 24
#         ___ bit __ ra.. 0, 32, 8
#             ? _ b_a_b..|?; ? + 8
#             ?.ap.. ?
#
#         # print(bst_ip_octets)
#
#         bst_ip_address _   # list
#
#         ___ each_octet __ ?
#             ?.ap.. st. in. ? 2
#
#         # print(bst_ip_address)
#
#         broadc__t_address _ ".".j.. ?
#         # print(broadcast_address)
#
#         # Results for selected IP/mask
#         print("\n")
#         print("Network address is: @"  n_a..
#         print("Broadcast address is: @"  b_a..
#         print("Number of valid hosts per subnet: @"  n_o_h..
#         print("Wildcard mask: @"  w_m..
#         print("Mask bits: @"  n_o_o..
#         print("\n")
#
#         # Application #1 - Part #4
#
#         # Generation of random IP addresses in the subnet
#         w__ T..
#             generate _ in__("Generate random IP address from this subnet? (y/n)")
#
#             __ generate __ "y":
#                 generated_ip _   # list
#
#                 # Obtain available IP address in range, based on the difference between octets in broadcast address and network address
#                 ___ indexb, oct_bst __ en.. b_i_a..
#                     # print(indexb, oct_bst)
#                     ___ indexn, oct_net __ en.. n_i_a..
#                         # print(indexn, oct_net)
#                         __ indexb __ indexn
#                             __ oct_bst __ o_n..
#                                 # Add identical octets to the generated_ip list
#                                 g_i_.ap.. o_b..
#                             ____
#                                 # Generate random number(s) from within octet intervals and append to the list
#                                 g_i_.ap.. st. ra__.r_i.. in. o_n.. in. o_b..
#
#                 # IP address generated from the subnet pool
#                 # print(generated_ip)
#                 y_iaddr _ ".".j.. ?
#                 # print(y_iaddr)
#
#                 print("Random IP address is: @"  y__
#                 print("\n")
#                 c..
#
#             ____
#                 print("Ok, bye!\n")
#                 b..
#
#     ______ K..
#         print("\n\nProgram aborted by user. Exiting...\n")
#         ___.e..
#
#
# # Calling the function
# ?
#
# # End of program