#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ u__.request, u__.e.., u__.parse
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib2

BROWSER _ 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0'
URL _ 'http://www.python.org'

___ spoof_firefox

    opener _ ?.r__.build_opener()
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #opener = urllib2.build_opener()

    opener.addheaders _ [('User-agent', BROWSER)]
    result _ opener.open(URL)
    print ("Response headers:")

    ___ header __  result.headers:
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #for header in  result.headers.headers:
        print ("@: @" (header, result.headers.get(header)))
        # Comment out the above line and uncomment the below for Python 2.7.x.
        #print (header)
__ _______ __ ______
    spoof_firefox()

