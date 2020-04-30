# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 9
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ______ ___
# ______ maxinet
# ____ mininet.topolib ______ TreeTopo
#
# # Emulate a network with depth of depth_ and fanout of fanout_
# ___ emulate(depth_, fanout_):
#     # Start the MaxiNet as a Mininet cluster.
#     cluster _ maxinet.MininetCluster("pc1","pc2","pc3")
#     cluster.s..
#
#     # Emulate the network topology.
#     emu _ maxinet.Emulation(cluster, TreeTopo(depth_,fanout_))
#
#     # Start Execution of the Emulated System.
#     emu.setup()
#
#     # Name two of the instances as h1 and h2.
#     h1, h2  _ net.hosts[0], net.hosts[depth_]
#
#     # Ping from an instance to another, and print the output.
#     print (h1.cmd('ping -c1 @'  h2.IP()))
#
#     # Stop the MaxiNet Emulation.
#     emu.stop()
#     cluster.stop()
#
# __ _______ __ ______
#     parser _ ?.AP..(d.._'Maxinet Simple Emulation')
#     ?.a_a..('--depth', a.._"store", d.._"depth", ty.._in., r.._T..)
#     ?.a_a..('--fanout', a.._"store", d.._"fanout", ty.._in., r.._T..)
#     given_args _ ?.p_a..
#     emulate(?.depth, ?.fanout)
#
