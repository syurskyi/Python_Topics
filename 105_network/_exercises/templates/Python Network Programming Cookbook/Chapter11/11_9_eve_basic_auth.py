#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

____ eve ______ Eve
____ eve.auth ______ BasicAuth

c_ MyBasicAuth(BasicAuth):
    ___ check_auth username, password, allowed_roles, resource,
                   method):
        r_ username __ 'admin' and password __ 'secret'

___ run_server
    app _ Eve(auth_MyBasicAuth)
    app.r..
       
__ _______ __ ______
    run_server()


