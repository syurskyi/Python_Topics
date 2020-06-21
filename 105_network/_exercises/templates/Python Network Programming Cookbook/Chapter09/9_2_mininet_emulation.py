# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 9
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ______ ?
# ____ mininet.net ______ Mininet
# ____ mininet.topolib ______ TreeTopo
#
# # Emulate a network with depth of depth_ and fanout of fanout_
# ___ emulate(depth_, fanout_):
#
#     # Create a network with tree topology
#     tree_ _ TreeTopo(depth_depth_,fanout_fanout_)
#
#     # Initiating the Mininet instance
#     net _ Mininet(topo_tree_)
#
#     # Start Execution of the Emulated System.
#     net.s..
#
#     # Name two of the instances as h1 and h2.
#     h1, h2  _ net.hosts[0], net.hosts[depth_]
#
#     # Ping from an instance to another, and print the output.
#     print (h1.cmd('ping -c1 @'  h2.IP()))
#
#     # Stop the Mininet Emulation.
#     net.stop()
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Mininet Simple Emulation')
#     ?.a_a..('--depth', a.._"store", d.._"depth", ty.._in., r.._T..)
#     ?.a_a..('--fanout', a.._"store", d.._"fanout", ty.._in., r.._T..)
#     given_args _ ?.p_a..
#     emulate(given_args.depth, given_args.fanout)
#
