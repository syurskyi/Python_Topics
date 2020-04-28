#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 7
# This program requires Python 2.7 or any later version
# SOAPpy has discontinued its support for Python 3.
# You may find more information and other potential libraries at https://stackoverflow.com/questions/7817303/what-soap-libraries-exist-for-python-3-x

______ SOAPpy

TEST_URL _ 'http://s3.amazonaws.com/ec2-downloads/2009-04-04.ec2.wsdl'


___ list_soap_methods(url):
    proxy _ SOAPpy.WSDL.Proxy(url)

    print ('d methods in WSDL:'  le.(proxy.methods) + '\n')
    ___ key __ proxy.methods.keys
        print ("Key Name: @" key)
        print ("Key Details:")
        ___ k,v __ proxy.methods[key].__dict__.iteritems
            print ("@ ==> @" (k,v))
        b..

__ _______ __ ______
    list_soap_methods(TEST_URL)
