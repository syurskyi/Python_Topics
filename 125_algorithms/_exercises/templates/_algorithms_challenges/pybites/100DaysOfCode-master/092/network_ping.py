#!python3
#network_ping.py is a script to ping all IPs on a given network.

______ ipaddress
______ os

network = input("Please enter a network to ping (format: xxx.xxx.xxx.0/xx ")
netobj = ipaddress.ip_network(network)

___ ip in netobj.hosts(
    os.system("ping " + str(ip))