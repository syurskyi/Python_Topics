#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

______ a_p..

______ http.client
# Comment out the above line and uncomment the below for Python 2.7.x.
#import httplib

______ urllib.parse
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urlparse

______ re
______ urllib.r__, urllib.e..
# Comment out the above line and uncomment the below for Python 2.7.x.
#import urllib

DEFAULT_URL _ 'http://www.python.org'

HTTP_GOOD_CODES _  [http.client.OK, http.client.FOUND, http.client.MOVED_PERMANENTLY]
# Comment out the above line and uncomment the below for Python 2.7.x.
#HTTP_GOOD_CODES =  [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]

___ get_server_status_code(url):
    """
    Download just the header of a URL and
    return the server's status code.
    """
    host, pa__ _ urllib.parse.urlparse(url)[1:3]
    # Comment out the above line and uncomment the below for Python 2.7.x.
    #host, path = urlparse.urlparse(url)[1:3] 
    ___
        conn _ http.client.HTTPConnection(host)       
        # Comment out the above line and uncomment the below for Python 2.7.x.
        #conn = httplib.HTTPConnection(host)

        conn.r__('HEAD', pa__)
        r_ conn.getresponse().status

    ______ E.. __ e:
        print ("Server: @ status is: @ " (url, e))
        # Comment out the above line and uncomment the below for Python 2.7.x.
        #except StandardError:
        r_ None

__ _______ __ ______
    parser _ ?.AP..(d.._'Example HEAD Request')
    ?.a_a..('--url', a.._"store", d.._"url", default_DEFAULT_URL)
    given_args _ ?.p_a..
    url _ ?.url
    __ get_server_status_code(url) __ HTTP_GOOD_CODES:
        print ("Server: @ status is OK: @ " (url, get_server_status_code(url)))
    ____
        print ("Server: @ status is NOT OK: @" (url, get_server_status_code(url)))
