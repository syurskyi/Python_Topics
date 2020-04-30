# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 10
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ____ mininet.net ______ Mininet
# ____ mininet.node ______ Controller, RemoteController, OVSController
# ____ mininet.node ______ CPULimitedHost, Host, Node
# ____ mininet.node ______ OVSKernelSwitch, UserSwitch
# ____ mininet.node ______ IVSSwitch
# ____ mininet.cli ______ CLI
# ____ mininet.log ______ setLogLevel, info
# ____ mininet.link ______ TCLink, Intf
# ____ subprocess ______ call
#
# ___ myNetwork
#
#     net _ Mininet( topo_None,
#                    build_False,
#                    ipBase_'10.0.0.0/8')
#
#     info( '*** Adding controller\n' )
#     c0_net.addController(name_'c0',
#                       controller_Controller,
#                       protocol_'tcp',
#                       port_6633)
#
#     info( '*** Add switches\n')
#     s9 _ net.addSwitch('s9', cls_OVSKernelSwitch)
#     s8 _ net.addSwitch('s8', cls_OVSKernelSwitch)
#     s4 _ net.addSwitch('s4', cls_OVSKernelSwitch)
#     s5 _ net.addSwitch('s5', cls_OVSKernelSwitch)
#     s7 _ net.addSwitch('s7', cls_OVSKernelSwitch)
#     s6 _ net.addSwitch('s6', cls_OVSKernelSwitch)
#     s10 _ net.addSwitch('s10', cls_OVSKernelSwitch)
#     s1 _ net.addSwitch('s1', cls_OVSKernelSwitch)
#     s3 _ net.addSwitch('s3', cls_OVSKernelSwitch)
#     s2 _ net.addSwitch('s2', cls_OVSKernelSwitch)
#
#     info( '*** Add hosts\n')
#     h3 _ net.addHost('h3', cls_Host, ip_'10.0.0.3', d..Route_None)
#     h9 _ net.addHost('h9', cls_Host, ip_'10.0.0.9', d..Route_None)
#     h1 _ net.addHost('h1', cls_Host, ip_'10.0.0.1', d..Route_None)
#     h7 _ net.addHost('h7', cls_Host, ip_'10.0.0.7', d..Route_None)
#     h10 _ net.addHost('h10', cls_Host, ip_'10.0.0.10', d..Route_None)
#     h2 _ net.addHost('h2', cls_Host, ip_'10.0.0.2', d..Route_None)
#     h6 _ net.addHost('h6', cls_Host, ip_'10.0.0.6', d..Route_None)
#     h4 _ net.addHost('h4', cls_Host, ip_'10.0.0.4', d..Route_None)
#     h11 _ net.addHost('h11', cls_Host, ip_'10.0.0.11', d..Route_None)
#     h8 _ net.addHost('h8', cls_Host, ip_'10.0.0.8', d..Route_None)
#     h5 _ net.addHost('h5', cls_Host, ip_'10.0.0.5', d..Route_None)
#
#     info( '*** Add links\n')
#     s7s1 _ {'bw':250,'loss':0}
#     net.addLink(s7, s1, cls_TCLink , **s7s1)
#     s7s8 _ {'bw':250,'loss':0}
#     net.addLink(s7, s8, cls_TCLink , **s7s8)
#     s8s2 _ {'bw':250,'loss':0}
#     net.addLink(s8, s2, cls_TCLink , **s8s2)
#     net.addLink(s1, s3)
#     net.addLink(s1, s4)
#     net.addLink(s1, s9)
#     net.addLink(s1, s10)
#     net.addLink(s1, s5)
#     net.addLink(s1, s6)
#     net.addLink(s2, s3)
#     net.addLink(s2, s4)
#     net.addLink(s2, s9)
#     net.addLink(s2, s10)
#     net.addLink(s2, s5)
#     net.addLink(s2, s6)
#     net.addLink(s3, h1)
#     net.addLink(s3, h2)
#     net.addLink(s4, h3)
#     net.addLink(s4, h4)
#     net.addLink(s9, h5)
#     net.addLink(s9, h6)
#     net.addLink(s10, h7)
#     net.addLink(s10, h8)
#     net.addLink(s5, h9)
#     net.addLink(s6, h10)
#     net.addLink(s6, h11)
#
#     info( '*** Starting network\n')
#     net.build()
#     info( '*** Starting controllers\n')
#     ___ controller __ net.controllers:
#         controller.s..
#
#     info( '*** Starting switches\n')
#     net.get('s9').start([])
#     net.get('s8').start([c0])
#     net.get('s4').start([])
#     net.get('s5').start([])
#     net.get('s7').start([c0])
#     net.get('s6').start([])
#     net.get('s10').start([])
#     net.get('s1').start([])
#     net.get('s3').start([])
#     net.get('s2').start([])
#
#     info( '*** Post configure switches and hosts\n')
#
#     CLI(net)
#     net.stop()
#
# __ _______ __ ______
#     setLogLevel( 'info' )
#     myNetwork()
#
