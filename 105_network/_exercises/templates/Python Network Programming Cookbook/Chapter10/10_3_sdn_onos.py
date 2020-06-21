# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 10
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ____ mininet.net ______ Mininet
# ____ mininet.node ______ Controller, RemoteController, OVSController
# ____ mininet.node ______ CPULimitedHost, Host, Node
# ____ mininet.node ______ OVSKernelSwitch, UserSwitch
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
#                       controller_RemoteController,
#                       ip_'127.0.0.1',
#                       protocol_'tcp',
#                       port_6653)
#
#     info( '*** Add switches\n')
#     s2 _ net.addSwitch('s2', cls_OVSKernelSwitch)
#     s1 _ net.addSwitch('s1', cls_OVSKernelSwitch)
#     s5 _ net.addSwitch('s5', cls_OVSKernelSwitch, failMode_'standalone')
#
#     info( '*** Add hosts\n')
#     h2 _ net.addHost('h2', cls_Host, ip_'10.0.0.2', d..Route_None)
#     h1 _ net.addHost('h1', cls_Host, ip_'10.0.0.1', d..Route_None)
#     h4 _ net.addHost('h4', cls_Host, ip_'10.0.0.4', d..Route_None)
#     h3 _ net.addHost('h3', cls_Host, ip_'10.0.0.3', d..Route_None)
#
#     info( '*** Add links\n')
#     s1s2 _ {'bw':400,'loss':0}
#     net.addLink(s1, s2, cls_TCLink , **s1s2)
#     s2h1 _ {'bw':1000,'loss':10,'max_queue_size':10,'speedup':40}
#     net.addLink(s2, h1, cls_TCLink , **s2h1)
#     s2h2 _ {'bw':120,'loss':0}
#     net.addLink(s2, h2, cls_TCLink , **s2h2)
#     s2h3 _ {'bw':400,'loss':20}
#     net.addLink(s2, h3, cls_TCLink , **s2h3)
#     s1s5 _ {'bw':200,'delay':'12','loss':10}
#     net.addLink(s1, s5, cls_TCLink , **s1s5)
#     s5h4 _ {'bw':100,'loss':50}
#     net.addLink(s5, h4, cls_TCLink , **s5h4)
#
#     info( '*** Starting network\n')
#     net.build()
#     info( '*** Starting controllers\n')
#     ___ controller __ net.controllers:
#         controller.s..
#
#     info( '*** Starting switches\n')
#     net.get('s2').start([c0])
#     net.get('s1').start([c0])
#     net.get('s5').start([])
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
