# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 9
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ ns.app..
# ______ ns.co..
# ______ ns.in..
# ______ ns.ne..
# ______ ns.po..
# ______ ?
#
#
# ___ simulate ipv4add ipv4mask
#     # Enabling logs at INFO level for both the server and the client.
#     __.co__.LCE.. "UdpEchoClientApplication"  __.co__.L_L_I..
#     __.co__.LCE.. "UdpEchoServerApplication"  __.co__.L_L_I..
#
#     # Create the 2 nodes.
#     nodes _ __.n__.NC..
#     ?.C.. 2
#
#     pointToPoint _ __.p_t_p_.PTPH..
#
#     devices _ pTP__.I.. n..
#
#     stack _ __.i__.ISH..
#     ?.I.. n..
#
#     # Set addresses based on the input args.
#     address _ __.i__.I4AH..
#     ?.SB.. __.n__.I4A.. i4a..   __.n__.Ipv4Mask i4m..
#
#     interfaces _ ?.A.. d..
#
#     # Running the echo server
#     echoServer _ __.ap.. __.UESH.. 9
#     serverApps _ ?.I.. n__.G.. 1
#
#     # Running the echo client
#     echoClient _ __.a__.UECH.. i__.GA.. 1 3
#     clientApps _ eC__.I.. n__.G.. 0
#
#     # Running the simulator
#     __.co__.S__.R..
#     __.co__.S__.D..
#
#
# __ _______ __ ______
#     ? _ ?.AP.. d.._'NS-3 Simple Simulation'
#     ?.a_a.. '--ipv4add'  a.._"store"  d.._"ipv4add"  ty.._str  r.._T..
#     ?.a_a.. '--ipv4mask'  a.._"store"  d.._"ipv4mask"  ty.._str  r.._T..
#     given_args _ ?.p_a..
#     s.. ?.i4a.. ?.i4m..
#
