# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 9
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# # Adopted from https://github.com/containernet/containernet/blob/master/examples/dockerhosts.py
#
# """
# This example shows how to create a simple network and
# how to create docker containers (based on existing images)
# to it.
# """
#
# ____ mininet.net ______ Containernet
# ____ mininet.node ______ Controller, Docker, OVSSwitch
# ____ mininet.cli ______ CLI
# ____ mininet.log ______ setLogLevel, info
# ____ mininet.link ______ TCLink, Link
#
#
# ___ emulate
#
#     "Create a network with some docker containers acting as hosts."
#
#     net _ Containernet(controller_Controller)
#
#     info('*** Adding controller\n')
#     net.addController('c0')
#
#     info('*** Adding hosts\n')
#     h1 _ net.addHost('h1')
#     h2 _ net.addHost('h2')
#
#     info('*** Adding docker containers\n')
#     d1 _ net.addDocker('d1', ip_'10.0.0.251', dimage_"ubuntu:trusty")
#
#     # A container with more specific params: cpu period and cpu quota
#     d2 _ net.addDocker('d2', ip_'10.0.0.252', dimage_"ubuntu:trusty", cpu_period_50000, cpu_quota_25000)
#
#     # Add a container as a host, using Docker class option.
#     d3 _ net.addHost('d3', ip_'11.0.0.253', cls_Docker, dimage_"ubuntu:trusty", cpu_shares_20)
#
#     Add a container with a specific volume.
#     d5 _ net.addDocker('d5', dimage_"ubuntu:trusty", volumes_["/:/mnt/vol1:rw"])
#
#     info('*** Adding switch\n')
#     s1 _ net.addSwitch('s1')
#     s2 _ net.addSwitch('s2', cls_OVSSwitch)
#     s3 _ net.addSwitch('s3')
#
#     info('*** Creating links\n')
#     net.addLink(h1, s1)
#     net.addLink(s1, d1)
#     net.addLink(h2, s2)
#     net.addLink(d2, s2)
#     net.addLink(s1, s2)
#
#     # try to add a second interface to a docker container
#     net.addLink(d2, s3, params1_{"ip": "11.0.0.254/8"})
#     net.addLink(d3, s3)
#
#     info('*** Starting network\n')
#     net.s..
#
#     # The typical ping example, with two docker instances in place of hosts.
#     net.ping([d1, d2])
#
#     # our extended ping functionality
#     net.ping([d1], manuald..ip_"10.0.0.252")
#     net.ping([d2, d3], manuald..ip_"11.0.0.254")
#
#     info('*** Dynamically add a container at runtime\n')
#     d4 _ net.addDocker('d4', dimage_"ubuntu:trusty")
#
#     # we have to specify a manual ip when we add a link at runtime
#     net.addLink(d4, s1, params1_{"ip": "10.0.0.254/8"})
#
#     # Ping docker instance d1.
#     net.ping([d1], manuald..ip_"10.0.0.254")
#
#     info('*** Running CLI\n')
#     CLI(net)
#
#     info('*** Stopping network')
#     net.stop()
#
# __ _______ __ ______
#     setLogLevel('info')
#     emulate()
