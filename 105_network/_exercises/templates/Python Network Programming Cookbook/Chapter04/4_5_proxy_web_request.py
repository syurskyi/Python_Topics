#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ u__.r__, u__.parse, u__.e..
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib

URL _ 'https://www.github.com'
PROXY_ADDRESS _ "165.24.10.8:8080" # By Googling free proxy server


__ _______ __ ______

    proxy _ ?.r__.ProxyHandler({"http" : PROXY_ADDRESS})
    opener _ ?.r__.build_opener(proxy)
    ?.r__.install_opener(opener)
    resp _ ?.r__.u_o..(URL)
    # Comment out the above 4 lines and uncomment the below for Python 2.7.x.
    #resp = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})

    print ("Proxy server returns response headers: @ " resp.headers)

