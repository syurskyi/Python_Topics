# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 10
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ____ mininet.net ______ Mininet
# ____ mininet.node ______ OVSSwitch, Controller, RemoteController
# ____ mininet.cli ______ CLI
# ____ mininet.log ______ setLogLevel
#
# ___ execute
#
#     # Create Mininet instance.
#     net _ Mininet()
#
#     # Add the SDN controller to the network.
#     c1 _ net.addController(name_'c1', controller_RemoteController,
#                                        ip_'127.0.0.1')
#
#     # Add hosts to the network.
#     h0_net.addHost('h0')
#     h1_net.addHost('h1')
#
#     # Add switches to the network.
#     s0_net.addSwitch('s0')
#     s1_net.addSwitch('s1')
#     s2_net.addSwitch('s2')
#
#     # Creating links between the switches in the network
#     net.addLink(s0, s1)
#     net.addLink(s1, s2)
#     net.addLink(s0, s2)
#
#     # Connect hosts to the relevant switches in the network.
#     net.addLink(h0, s0)
#     net.addLink(h1, s1)
#
#     # Start execution.
#     net.s..
#
#     CLI( net )
#
# __ _______ __ ______
#     setLogLevel( 'info' )  # for CLI output
#     execute()
