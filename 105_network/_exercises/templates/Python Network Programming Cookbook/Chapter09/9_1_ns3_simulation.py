#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 9
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ ns.applications
______ ns.core
______ ns.internet
______ ns.network
______ ns.point_to_point
______ ?


___ simulate(ipv4add, ipv4mask):
    # Enabling logs at INFO level for both the server and the client.
    ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
    ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)
    
    # Create the 2 nodes.
    nodes _ ns.network.NodeContainer()
    nodes.Create(2)

    pointToPoint _ ns.point_to_point.PointToPointHelper()

    devices _ pointToPoint.Install(nodes)

    stack _ ns.internet.InternetStackHelper()
    stack.Install(nodes)

    # Set addresses based on the input args.
    address _ ns.internet.Ipv4AddressHelper()
    address.SetBase(ns.network.Ipv4Address(ipv4add), ns.network.Ipv4Mask(ipv4mask))

    interfaces _ address.Assign(devices)

    # Running the echo server
    echoServer _ ns.applications.UdpEchoServerHelper(9)
    serverApps _ echoServer.Install(nodes.Get(1))

    # Running the echo client
    echoClient _ ns.applications.UdpEchoClientHelper(interfaces.GetAddress(1), 3)
    clientApps _ echoClient.Install(nodes.Get(0))

    # Running the simulator
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()


__ _______ __ ______
    parser _ ?.AP..(d.._'NS-3 Simple Simulation')
    parser.a_a..('--ipv4add', a.._"store", d.._"ipv4add", type_str, r.._T..)
    parser.a_a..('--ipv4mask', a.._"store", d.._"ipv4mask", type_str, r.._T..)
    given_args _ parser.parse_args()
    simulate(given_args.ipv4add, given_args.ipv4mask)

