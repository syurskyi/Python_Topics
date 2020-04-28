#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ ?

______ urllib.r__
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib2

REMOTE_SERVER_HOST _ 'http://www.cnn.com'

c_ HTTPClient:

    ___ -  host):
        host _ host

    ___ fetch
        response _ urllib.r__.urlopen(host)
        # Comment out the above line and uncomment the below for Python 2.7.x.
        #response = urllib2.urlopen(self.host)

        data _ response.read()
        text _ data.d..('utf-8')
        r_ text

__ _____ __ ______
    parser _ ?.AP..(d.._'HTTP Client Example')
    parser.a_a..('--host', a.._"store", d.._"host",  default_REMOTE_SERVER_HOST)

    given_args _ parser.p_a..
    host _ given_args.host
    client _ HTTPClient(host)
    print (client.fetch())

