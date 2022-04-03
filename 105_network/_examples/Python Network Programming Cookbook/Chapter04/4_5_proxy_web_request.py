#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

import u__.r.., urllib.parse, urllib.error
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib

URL = 'https://www.github.com'
PROXY_ADDRESS = "165.24.10.8:8080" # By Googling free proxy server


if __name__ == '__main__':

    proxy = u__.r...ProxyHandler({"http" : PROXY_ADDRESS})
    opener = u__.r...build_opener(proxy)
    u__.r...install_opener(opener)
    resp = u__.r...urlopen(URL)
    # Comment out the above 4 lines and uncomment the below for Python 2.7.x.
    #resp = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})

    print ("Proxy server returns response headers: %s " %resp.headers)

