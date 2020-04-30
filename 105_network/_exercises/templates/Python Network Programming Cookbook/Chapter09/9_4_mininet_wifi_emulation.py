# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 9
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ____ mininet.net ______ Mininet
# ____ mininet.node ______ Controller, OVSKernelAP
# ____ mininet.link ______ TCLink
# ____ mininet.cli ______ CLI
# ____ mininet.log ______ setLogLevel
#
# ___ emulate
#     # Setting the position of nodes and providing mobility
#
#     # Create a network.
#     net _ Mininet(controller_Controller, link_TCLink, accessPoint_OVSKernelAP)
#
#     print ("*** Creating nodes")
#     # Add the host
#     h1 _ net.addHost('h1', mac_'00:00:00:00:00:01', ip_'10.0.0.1/8')
#
#     # Add 3 mobile stations, sta1, sta2, sta3.
#     sta1 _ net.addStation('sta1', mac_'00:00:00:00:00:02', ip_'10.0.0.2/8')
#     sta2 _ net.addStation('sta2', mac_'00:00:00:00:00:03', ip_'10.0.0.3/8')
#     sta3 _ net.addStation('sta3', mac_'00:00:00:00:00:04', ip_'10.0.0.4/8')
#
#     # Add an access point
#     ap1 _ net.addAccessPoint('ap1', ssid_'new-ssid', mode_'g', channel_'1', position_'45,40,30')
#
#     # Add a controller
#     c1 _ net.addController('c1', controller_Controller)
#
#     print ("*** Configuring wifi nodes")
#     net.configureWifiNodes()
#
#     print ("*** Associating and Creating links")
#     net.addLink(ap1, h1)
#     net.addLink(ap1, sta1)
#     net.addLink(ap1, sta2)
#     net.addLink(ap1, sta3)
#
#     print ("*** Starting network")
#     net.build()
#     c1.s..
#     ap1.start([c1])
#
#     # Plot a 3-dimensional graph.
#     net.plotGraph(max_x_100, max_y_100, max_z_200)
#
#     # Start the mobility at the start of the emulation.
#     net.startMobility(time_0)
#
#     # Start the mobile stations from their initial positions.
#     net.mobility(sta1, 'start', time_1, position_'40.0,30.0,20.0')
#     net.mobility(sta2, 'start', time_2, position_'40.0,40.0,90.0')
#     net.mobility(sta3, 'start', time_3, position_'50.0,50.0,160.0')
#
#     # Indicate the final destination of the mobile stations during the emulation.
#     net.mobility(sta1, 'stop', time_12, position_'31.0,10.0,50.0')
#     net.mobility(sta2, 'stop', time_22, position_'55.0,31.0,30.0')
#     net.mobility(sta3, 'stop', time_32, position_'75.0,99.0,120.0')
#
#     # Stop the mobility at certain time.
#     net.stopMobility(time_33)
#
#     print ("*** Running CLI")
#     CLI(net)
#
#     print ("*** Stopping network")
#     net.stop()
#
# __ _______ __ ______
#     setLogLevel('info')
#     emulate()
